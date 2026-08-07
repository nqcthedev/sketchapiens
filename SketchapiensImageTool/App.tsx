/**
 * Sketchapiens — Tool sinh ảnh hàng loạt (bản RIÊNG, code mới)
 * Chạy trong Google Flow (dùng flow-sdk). Dán cả file này vào trình sửa code của tool Flow.
 *
 * Tính năng: chọn refs (ingredients) + khoá Style, dán/upload danh sách prompt (mỗi dòng 1 ảnh),
 * SMART REF BINDING theo @tag, GRID từng ảnh (trạng thái + thumbnail + chip ref + sửa prompt +
 * tạo lại lẻ + tải), chạy hàng loạt có concurrency + tự chạy tiếp + bỏ qua ảnh đã xong + Dừng,
 * tự retry khi lỗi, tự lưu (IndexedDB) reload không mất, tải tất cả.
 *
 * LƯU Ý: mình không test được flow-sdk ở môi trường build, nên nếu Flow báo lỗi tên hàm/tham số,
 * chụp lỗi gửi lại, mình chỉnh đúng API. Các lệnh flow-sdk dùng ở đây: Flow.media.selectMultiple,
 * Flow.generate.image, Flow.download.
 */
import React, { useState, useRef, useEffect, useCallback } from 'react';
import { Flow } from 'flow-sdk';

/* ----------------------------- Helpers ----------------------------- */
const REF_TAG_REGEX = /@([A-Za-z0-9_-]+)/g;

function normalizeRefKey(value: string): string {
  return (value || '')
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '')
    .replace(/[^a-zA-Z0-9_-]/g, '_')
    .replace(/_+/g, '_')
    .replace(/^_+|_+$/g, '');
}
function extractRefTags(text: string): string[] {
  if (!text) return [];
  return Array.from(text.matchAll(REF_TAG_REGEX)).map((m) => m[1].toLowerCase());
}
function sanitizePrefix(v: string): string {
  return (v || '').trim().replace(/[^a-zA-Z0-9_-]/g, '_').replace(/_+/g, '_').replace(/^_+|_+$/g, '');
}
const pad3 = (n: number) => String(n).padStart(3, '0');
function extFromMime(mime?: string): string {
  if (!mime) return 'png';
  const e = mime.split('/').pop() || 'png';
  return e === 'jpeg' ? 'jpg' : e;
}
const parseLines = (v: string) => v.split(/\r?\n/).map((l) => l.trim()).filter(Boolean);
const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));

/* --------------------------- IndexedDB (lưu state) --------------------------- */
const IDB_NAME = 'sketchapiens_image_tool';
const IDB_STORE = 'kv';
function idbOpen(): Promise<IDBDatabase> {
  return new Promise((res, rej) => {
    const r = indexedDB.open(IDB_NAME, 1);
    r.onupgradeneeded = () => r.result.createObjectStore(IDB_STORE);
    r.onsuccess = () => res(r.result);
    r.onerror = () => rej(r.error);
  });
}
async function idbSet(key: string, val: any) {
  const db = await idbOpen();
  return new Promise<void>((res, rej) => {
    const tx = db.transaction(IDB_STORE, 'readwrite');
    tx.objectStore(IDB_STORE).put(val, key);
    tx.oncomplete = () => res();
    tx.onerror = () => rej(tx.error);
  });
}
async function idbGet(key: string): Promise<any> {
  const db = await idbOpen();
  return new Promise((res, rej) => {
    const tx = db.transaction(IDB_STORE, 'readonly');
    const rq = tx.objectStore(IDB_STORE).get(key);
    rq.onsuccess = () => res(rq.result);
    rq.onerror = () => rej(rq.error);
  });
}

/* ------------------------------ Types ------------------------------ */
interface RefItem { mediaId: string; base64: string; mimeType: string; name: string; refKey: string; }
type JobStatus = 'pending' | 'running' | 'done' | 'error';
interface JobResult { status: JobStatus; url?: string; mediaId?: string; error?: string; prompt: string; }

const IMAGE_MODELS = ['🍌 Nano Banana Pro', '🍌 Nano Banana 2'];
const ASPECTS = ['16:9', '9:16', '1:1'];
const MAX_REFS_PER_IMAGE = 10; // khớp với call đã chạy thật của bạn (referenceImageMediaIds.slice(0,10))
const STATE_KEY = 'workspace_v1';

/* ============================== Component ============================== */
export default function App() {
  const [refs, setRefs] = useState<RefItem[]>([]);
  const [promptText, setPromptText] = useState('');
  const [model, setModel] = useState(IMAGE_MODELS[0]);
  const [aspect, setAspect] = useState('16:9');
  const [prefix, setPrefix] = useState('EP-001');
  const [styleKey, setStyleKey] = useState('style');
  const [concurrency, setConcurrency] = useState(4);
  const [autoDownload, setAutoDownload] = useState(false);
  const [previewSrc, setPreviewSrc] = useState<string | null>(null);

  const resultsRef = useRef<Record<number, JobResult>>({});
  const [, forceRender] = useState(0);
  const rerender = useCallback(() => forceRender((x) => x + 1), []);

  const [running, setRunning] = useState(false);
  const [paused, setPaused] = useState(false);
  const stopRef = useRef(false);
  const pausedRef = useRef(false);
  const loadedRef = useRef(false);
  const [status, setStatus] = useState('');

  useEffect(() => { pausedRef.current = paused; }, [paused]);

  /* ----- Load persisted state ----- */
  useEffect(() => {
    (async () => {
      try {
        const s = await idbGet(STATE_KEY);
        if (s) {
          setRefs(s.refs || []);
          setPromptText(s.promptText || '');
          setModel(s.model || IMAGE_MODELS[0]);
          setAspect(s.aspect || '16:9');
          setPrefix(s.prefix || 'EP-001');
          setStyleKey(s.styleKey || 'style');
          setConcurrency(s.concurrency || 4);
          setAutoDownload(!!s.autoDownload);
          // dọn trạng thái 'running' kẹt khi reload
          const cleaned: Record<number, JobResult> = {};
          Object.entries(s.results || {}).forEach(([k, v]: any) => {
            cleaned[Number(k)] = v.status === 'running' ? { ...v, status: 'pending' } : v;
          });
          resultsRef.current = cleaned;
        }
      } catch (e) { console.warn('Load error', e); }
      finally { loadedRef.current = true; rerender(); }
    })();
  }, [rerender]);

  /* ----- Autosave (debounce) ----- */
  const saveTimer = useRef<any>(null);
  const scheduleSave = useCallback(() => {
    if (!loadedRef.current) return;
    clearTimeout(saveTimer.current);
    saveTimer.current = setTimeout(() => {
      idbSet(STATE_KEY, {
        refs, promptText, model, aspect, prefix, styleKey, concurrency, autoDownload,
        results: resultsRef.current,
      }).catch((e) => console.warn('Save error', e));
    }, 1200);
  }, [refs, promptText, model, aspect, prefix, styleKey, concurrency, autoDownload]);
  useEffect(() => { scheduleSave(); }, [refs, promptText, model, aspect, prefix, styleKey, concurrency, autoDownload, scheduleSave]);

  /* ----- Refs (ingredients) ----- */
  const selectRefs = async () => {
    try {
      const remaining = 20 - refs.length;
      if (remaining <= 0) return;
      const picked: any[] = await (Flow as any).media.selectMultiple({ filter: 'image', maxCount: remaining });
      if (picked && picked.length) {
        setRefs((prev) => {
          const mapped: RefItem[] = picked.map((p) => ({
            mediaId: p.mediaId, base64: p.base64, mimeType: p.mimeType, name: p.name,
            refKey: normalizeRefKey((p.name || '').split('.').slice(0, -1).join('.') || p.name),
          }));
          const combined = [...prev, ...mapped];
          return Array.from(new Map(combined.map((r) => [r.mediaId, r])).values()).slice(0, 20);
        });
      }
    } catch (e) { console.warn('selectRefs', e); }
  };
  const updateRefKey = (i: number, key: string) =>
    setRefs((prev) => prev.map((r, idx) => (idx === i ? { ...r, refKey: normalizeRefKey(key) } : r)));
  const removeRef = (i: number) => setRefs((prev) => prev.filter((_, idx) => idx !== i));

  const refKeysLower = refs.map((r) => (r.refKey || '').toLowerCase());
  const dupKeys = refKeysLower.filter((k, i) => k && refKeysLower.indexOf(k) !== i);

  /* ----- Jobs derived from promptText + results ----- */
  const lines = parseLines(promptText);
  const jobs: JobResult[] = lines.map((line, i) => {
    const r = resultsRef.current[i];
    if (r && r.prompt === line) return r;
    return { status: 'pending', prompt: line };
  });
  const doneCount = jobs.filter((j) => j.status === 'done').length;

  function refIdsForLine(line: string): string[] {
    const tags = extractRefTags(line);
    let ids = refs.filter((r) => tags.includes((r.refKey || '').toLowerCase())).map((r) => r.mediaId);
    const styleRef = refs.find((r) => (r.refKey || '').toLowerCase() === styleKey.toLowerCase());
    if (styleRef) ids = [styleRef.mediaId, ...ids.filter((x) => x !== styleRef.mediaId)];
    if (ids.length === 0) ids = refs.map((r) => r.mediaId); // fallback: gắn hết
    return ids.slice(0, MAX_REFS_PER_IMAGE);
  }
  function chipsForLine(line: string): string[] {
    const tags = extractRefTags(line);
    const chips = refs.filter((r) => tags.includes((r.refKey || '').toLowerCase())).map((r) => r.refKey);
    const styleRef = refs.find((r) => (r.refKey || '').toLowerCase() === styleKey.toLowerCase());
    if (styleRef && !chips.includes(styleRef.refKey)) chips.push(styleRef.refKey);
    return chips;
  }

  function setResult(i: number, val: JobResult) {
    resultsRef.current = { ...resultsRef.current, [i]: val };
    rerender();
    scheduleSave();
  }

  /* ----- Generate one ----- */
  async function genOne(i: number, line: string): Promise<void> {
    setResult(i, { status: 'running', prompt: line });
    const ids = refIdsForLine(line);
    let lastErr = '';
    for (let attempt = 0; attempt < 3; attempt++) {
      if (stopRef.current) { setResult(i, { status: 'pending', prompt: line }); return; }
      try {
        const res: any = await (Flow as any).generate.image({
          prompt: line,
          referenceImageMediaIds: ids.length ? ids : undefined,
          modelDisplayName: model,
          aspectRatio: aspect,
        });
        if (res && res.mediaId) {
          const url = `data:${res.mimeType};base64,${res.base64}`;
          setResult(i, { status: 'done', url, mediaId: res.mediaId, prompt: line });
          if (autoDownload) downloadOne(i).catch(() => {});
          return;
        }
        lastErr = 'Không nhận được mediaId';
      } catch (e: any) {
        lastErr = e?.message || 'Lỗi API';
        await sleep(800);
      }
    }
    setResult(i, { status: 'error', error: lastErr, prompt: line });
  }

  /* ----- Run all (pool) ----- */
  async function runAll() {
    if (running) return;
    if (dupKeys.length) { setStatus('Lỗi: trùng refKey — sửa trước khi chạy.'); return; }
    if (!refs.length) { setStatus('Chưa chọn ref (ingredients).'); return; }
    stopRef.current = false; setPaused(false); pausedRef.current = false;
    setRunning(true); setStatus('Đang chạy…');
    const allLines = parseLines(promptText);
    const pending = allLines.map((_, i) => i).filter((i) => resultsRef.current[i]?.status !== 'done');
    let cursor = 0;
    const worker = async () => {
      while (!stopRef.current) {
        const myPos = cursor++;
        if (myPos >= pending.length) break;
        while (pausedRef.current && !stopRef.current) await sleep(400);
        if (stopRef.current) break;
        const i = pending[myPos];
        await genOne(i, allLines[i]);
      }
    };
    await Promise.all(Array.from({ length: Math.max(1, concurrency) }, () => worker()));
    setRunning(false);
    setStatus(stopRef.current ? 'Đã dừng.' : 'Hoàn tất.');
  }
  function stopAll() { stopRef.current = true; setStatus('Đang dừng…'); }

  /* ----- Per-card actions ----- */
  function editLine(i: number, newText: string) {
    const arr = promptText.split(/\r?\n/);
    arr[i] = newText;
    setPromptText(arr.join('\n'));
    // prompt đổi → coi như cần tạo lại
    if (resultsRef.current[i]) { const copy = { ...resultsRef.current }; delete copy[i]; resultsRef.current = copy; rerender(); scheduleSave(); }
  }
  async function regenOne(i: number) {
    const ln = parseLines(promptText)[i];
    if (ln) await genOne(i, ln);
  }
  async function downloadOne(i: number) {
    const r = resultsRef.current[i];
    if (!r || !r.url) return;
    const base64 = r.url.split(',')[1];
    const fname = `${sanitizePrefix(prefix) || 'IMG'}-I.${pad3(i + 1)}.${extFromMime(r.url.split(';')[0].split(':')[1])}`;
    await (Flow as any).download({ base64, mimeType: r.url.split(';')[0].split(':')[1], filename: fname });
  }
  async function downloadAll() {
    const entries = Object.entries(resultsRef.current).filter(([, v]: any) => v.status === 'done');
    for (const [k] of entries) { await downloadOne(Number(k)); await sleep(120); }
    setStatus(`Đã tải ${entries.length} ảnh.`);
  }
  async function resetAll() {
    if (!confirm('Xoá toàn bộ tiến trình (prompt giữ nguyên)? Ảnh đã tải về máy không bị xoá.')) return;
    resultsRef.current = {}; rerender();
    await idbSet(STATE_KEY, { refs, promptText, model, aspect, prefix, styleKey, concurrency, autoDownload, results: {} });
    setStatus('Đã reset.');
  }

  function uploadTxt(e: React.ChangeEvent<HTMLInputElement>) {
    const f = e.target.files?.[0]; if (!f) return;
    const rd = new FileReader();
    rd.onload = (ev) => setPromptText(parseLines(ev.target?.result as string).join('\n'));
    rd.readAsText(f); e.target.value = '';
  }

  /* ------------------------------ UI ------------------------------ */
  return (
    <div className="sk-root">
      <style>{CSS}</style>

      <header className="sk-header">
        <div className="sk-title">🎬 Sketchapiens — Sinh ảnh hàng loạt</div>
        <div className="sk-sub">Smart ref binding · grid · tự chạy tiếp · tự lưu · Nano Banana Pro</div>
      </header>

      <div className="sk-grid2">
        {/* LEFT: refs + settings */}
        <section className="sk-card">
          <div className="sk-row sk-between">
            <b className="sk-label">① Refs (Ingredients)</b>
            {refs.length > 0 && <button className="sk-link" onClick={() => setRefs([])}>Xoá hết</button>}
          </div>
          <button className="sk-dashed" onClick={selectRefs} disabled={refs.length >= 20}>
            ＋ {refs.length ? 'Thêm ref' : 'Chọn refs'} ({refs.length}/20)
          </button>
          {dupKeys.length > 0 && <div className="sk-warn">Trùng refKey: {Array.from(new Set(dupKeys)).join(', ')}</div>}
          <div className="sk-reflist">
            {refs.map((r, i) => {
              const isStyle = (r.refKey || '').toLowerCase() === styleKey.toLowerCase();
              const dup = dupKeys.includes((r.refKey || '').toLowerCase());
              return (
                <div className={`sk-ref ${dup ? 'sk-ref-dup' : ''}`} key={r.mediaId || i}>
                  <img src={`data:${r.mimeType};base64,${r.base64}`} alt="" />
                  <div className="sk-ref-main">
                    <input value={r.refKey} onChange={(e) => updateRefKey(i, e.target.value)} placeholder="refKey" />
                    <span className="sk-tag">@{r.refKey || '?'}{isStyle ? ' · STYLE (gắn mọi ảnh)' : ''}</span>
                  </div>
                  <button className="sk-x" onClick={() => removeRef(i)}>✕</button>
                </div>
              );
            })}
          </div>

          <div className="sk-hr" />
          <b className="sk-label">② Cài đặt</b>
          <label className="sk-field">Model
            <select value={model} onChange={(e) => setModel(e.target.value)}>
              {IMAGE_MODELS.map((m) => <option key={m} value={m}>{m}</option>)}
            </select>
          </label>
          <label className="sk-field">Tỉ lệ
            <select value={aspect} onChange={(e) => setAspect(e.target.value)}>
              {ASPECTS.map((a) => <option key={a} value={a}>{a}</option>)}
            </select>
          </label>
          <label className="sk-field">Tên file (prefix)
            <input value={prefix} onChange={(e) => setPrefix(e.target.value)} placeholder="EP-001" />
          </label>
          <label className="sk-field">refKey khoá Style
            <input value={styleKey} onChange={(e) => setStyleKey(e.target.value)} placeholder="style" />
          </label>
          <label className="sk-field">Chạy song song: {concurrency}
            <input type="range" min={1} max={8} value={concurrency} onChange={(e) => setConcurrency(Number(e.target.value))} />
          </label>
          <label className="sk-check">
            <input type="checkbox" checked={autoDownload} onChange={(e) => setAutoDownload(e.target.checked)} /> Tự tải mỗi ảnh khi xong
          </label>
        </section>

        {/* RIGHT: prompts + controls */}
        <section className="sk-card">
          <div className="sk-row sk-between">
            <b className="sk-label">③ Danh sách prompt — {lines.length} dòng</b>
            <label className="sk-link">Upload .txt
              <input type="file" accept=".txt" onChange={uploadTxt} hidden />
            </label>
          </div>
          <textarea
            className="sk-textarea"
            value={promptText}
            onChange={(e) => setPromptText(e.target.value)}
            placeholder="@ANCESTOR a caveman ... (mỗi dòng = 1 ảnh, nhắc @refKey để gắn đúng nhân vật)"
          />
          <div className="sk-controls">
            {!running
              ? <button className="sk-primary" onClick={runAll}>▶ Tạo tất cả</button>
              : <>
                  <button className="sk-primary" onClick={() => setPaused((p) => !p)}>{paused ? '▶ Tiếp' : '⏸ Tạm dừng'}</button>
                  <button className="sk-ghost" onClick={stopAll}>■ Dừng</button>
                </>}
            <button className="sk-ghost" onClick={downloadAll}>⬇ Tải tất cả</button>
            <button className="sk-ghost" onClick={resetAll}>↺ Reset</button>
          </div>
          <div className="sk-progwrap">
            <div className="sk-prog"><i style={{ width: `${lines.length ? (doneCount / lines.length) * 100 : 0}%` }} /></div>
            <span className="sk-count">{doneCount}/{lines.length} xong</span>
          </div>
          {status && <div className="sk-status">{status}</div>}
        </section>
      </div>

      {/* GRID of images */}
      <div className="sk-gallery">
        {jobs.map((job, i) => (
          <div className={`sk-cell sk-${job.status}`} key={i}>
            <div className="sk-cell-top">
              <span className="sk-idx">{pad3(i + 1)}</span>
              <span className={`sk-badge sk-b-${job.status}`}>{
                job.status === 'done' ? '✓' : job.status === 'running' ? '…' : job.status === 'error' ? '⚠' : '○'
              }</span>
            </div>
            <div className="sk-thumb">
              {job.status === 'done' && job.url
                ? <img src={job.url} alt="" onClick={() => setPreviewSrc(job.url!)} />
                : <span className="sk-ph">{job.status === 'running' ? 'Đang tạo…' : job.status === 'error' ? (job.error || 'Lỗi') : ' '}</span>}
            </div>
            <div className="sk-chips">{chipsForLine(job.prompt).map((c) => <span className="sk-chip" key={c}>@{c}</span>)}</div>
            <textarea className="sk-cellprompt" value={job.prompt} onChange={(e) => editLine(i, e.target.value)} rows={2} />
            <div className="sk-cellbtns">
              <button onClick={() => regenOne(i)} title="Tạo lại ảnh này">↻</button>
              <button onClick={() => downloadOne(i)} disabled={job.status !== 'done'} title="Tải ảnh này">⬇</button>
            </div>
          </div>
        ))}
      </div>

      {previewSrc && (
        <div className="sk-modal" onClick={() => setPreviewSrc(null)}>
          <img src={previewSrc} alt="" />
        </div>
      )}
    </div>
  );
}

/* ------------------------------ CSS ------------------------------ */
const CSS = `
.sk-root{font-family:-apple-system,Segoe UI,Roboto,Arial,sans-serif;color:#e7ecf3;background:#0a0e17;min-height:100%;padding:18px;box-sizing:border-box}
.sk-header{margin-bottom:14px}
.sk-title{font-size:18px;font-weight:800}
.sk-sub{font-size:12px;color:#8a93a3}
.sk-grid2{display:grid;grid-template-columns:340px 1fr;gap:14px;margin-bottom:14px}
.sk-card{background:#0d1424;border:1px solid rgba(255,255,255,.07);border-radius:14px;padding:14px}
.sk-row{display:flex;align-items:center;gap:8px}.sk-between{justify-content:space-between}
.sk-label{font-size:12px;color:#00bcd4;text-transform:uppercase;letter-spacing:.5px}
.sk-link{background:none;border:none;color:#00bcd4;font-size:11px;cursor:pointer;font-weight:700}
.sk-dashed{width:100%;margin:8px 0;padding:9px;border:1px dashed rgba(255,255,255,.15);border-radius:10px;background:transparent;color:#00bcd4;font-weight:700;cursor:pointer;font-size:12px}
.sk-dashed:disabled{opacity:.3}
.sk-warn{background:rgba(229,57,53,.1);border:1px solid rgba(229,57,53,.3);color:#ff7a72;font-size:11px;padding:6px 8px;border-radius:8px;margin-bottom:6px}
.sk-reflist{max-height:230px;overflow:auto;display:flex;flex-direction:column;gap:6px}
.sk-ref{display:flex;align-items:center;gap:8px;background:#050a10;border:1px solid rgba(255,255,255,.06);border-radius:10px;padding:6px}
.sk-ref-dup{border-color:rgba(229,57,53,.5)}
.sk-ref img{width:42px;height:42px;border-radius:8px;object-fit:cover;flex:0 0 auto}
.sk-ref-main{flex:1;display:flex;flex-direction:column;gap:3px;min-width:0}
.sk-ref-main input{background:#0a0e17;border:1px solid rgba(255,255,255,.1);border-radius:6px;padding:4px 6px;color:#fff;font-size:11px;font-weight:700;text-transform:uppercase}
.sk-tag{font-size:9px;color:#00bcd4;font-weight:700}
.sk-x{background:none;border:none;color:#7a8392;cursor:pointer;font-size:13px}
.sk-hr{height:1px;background:rgba(255,255,255,.07);margin:12px 0}
.sk-field{display:flex;flex-direction:column;gap:4px;font-size:11px;color:#8a93a3;margin-bottom:8px}
.sk-field select,.sk-field input{background:#0a0e17;border:1px solid rgba(255,255,255,.1);border-radius:8px;padding:7px;color:#fff;font-size:13px}
.sk-check{display:flex;align-items:center;gap:8px;font-size:12px;color:#cdd5e0}
.sk-textarea{width:100%;height:200px;background:#050a10;border:1px solid rgba(255,255,255,.1);border-radius:10px;padding:10px;color:#fff;font-size:12px;resize:vertical;box-sizing:border-box}
.sk-controls{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px}
.sk-primary{background:#00bcd4;color:#001014;border:none;border-radius:10px;padding:10px 16px;font-weight:800;cursor:pointer;font-size:13px}
.sk-ghost{background:#1a2333;color:#e7ecf3;border:none;border-radius:10px;padding:10px 16px;font-weight:700;cursor:pointer;font-size:13px}
.sk-progwrap{display:flex;align-items:center;gap:10px;margin-top:10px}
.sk-prog{flex:1;height:8px;background:#1a2333;border-radius:6px;overflow:hidden}
.sk-prog>i{display:block;height:100%;background:#00bcd4;transition:width .2s}
.sk-count{font-size:11px;color:#8a93a3;white-space:nowrap}
.sk-status{font-size:12px;color:#cdd5e0;margin-top:8px}
.sk-gallery{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:12px}
.sk-cell{background:#0d1424;border:1px solid rgba(255,255,255,.07);border-radius:12px;padding:8px;display:flex;flex-direction:column;gap:6px}
.sk-done{border-color:rgba(46,125,50,.4)}.sk-error{border-color:rgba(229,57,53,.5)}.sk-running{border-color:rgba(0,188,212,.5)}
.sk-cell-top{display:flex;justify-content:space-between;align-items:center}
.sk-idx{font-size:11px;font-weight:800;color:#8a93a3}
.sk-badge{font-size:12px}.sk-b-done{color:#5fd47a}.sk-b-error{color:#ff7a72}.sk-b-running{color:#00bcd4}.sk-b-pending{color:#5a6473}
.sk-thumb{aspect-ratio:16/9;background:#050a10;border-radius:8px;display:flex;align-items:center;justify-content:center;overflow:hidden}
.sk-thumb img{width:100%;height:100%;object-fit:cover;cursor:zoom-in}
.sk-ph{font-size:10px;color:#5a6473;text-align:center;padding:6px}
.sk-chips{display:flex;flex-wrap:wrap;gap:4px;min-height:16px}
.sk-chip{font-size:9px;background:rgba(0,188,212,.12);color:#00bcd4;border-radius:6px;padding:1px 6px;font-weight:700}
.sk-cellprompt{width:100%;background:#050a10;border:1px solid rgba(255,255,255,.08);border-radius:8px;padding:6px;color:#cdd5e0;font-size:10px;resize:vertical;box-sizing:border-box}
.sk-cellbtns{display:flex;gap:6px}
.sk-cellbtns button{flex:1;background:#1a2333;border:none;color:#e7ecf3;border-radius:8px;padding:6px;cursor:pointer;font-size:13px}
.sk-cellbtns button:disabled{opacity:.3}
.sk-modal{position:fixed;inset:0;background:rgba(0,0,0,.9);display:flex;align-items:center;justify-content:center;padding:30px;z-index:9999;cursor:zoom-out}
.sk-modal img{max-width:100%;max-height:100%;border-radius:10px}
@media(max-width:820px){.sk-grid2{grid-template-columns:1fr}}
`;
