# HISTORICAL WRITER CASES — CA HỒI QUY TRÊN SCRIPT LỊCH SỬ

> **NON-RUNTIME TEST DATA**
>
> Blind-first: model Writer chỉ được thấy `INPUT SURFACE` + task. `EXPECTED BEHAVIOR` chỉ evaluator mở sau khi output đã tồn tại.

---

# H-W01 — V17 RAIN / PROSE PRESERVATION WITHOUT LEGACY FORMULA

**Pinned source**

```text
path: videos/Video17_Rain/Script_Video17_narration.txt
blob: 4e3928cdd375cc1729f3cd646e43ed1bbb44ce7d
surface: lines 1–10
```

## INPUT SURFACE

Historical narration meaning to preserve:

```text
Rain starts.
You pull a hood up, or you take six steps to a door, and it's finished.
You're dry again inside a minute, and you don't think about it once.
Now take the hood away. Take the door away, and the roof.
Take away every dry thing you can think of.
It's fifty thousand years ago, and it has been raining for nine weeks.
You are a soft, mostly hairless ape sitting in a puddle that used to be where you slept.
And you have another two months of this.
So here's the question.
What happens to a human body that never, ever gets dry?
```

Task:

> Đây là meaning/structure đã được duyệt từ một script lịch sử của chính kênh. Hãy tạo một **VI_DRAFT_BATCH** tương đương, spoken và tự nhiên hơn cho owner nghe. Không thêm fact mới. Không đổi câu hỏi lõi. Không làm packaging.

## EXPECTED BEHAVIOR — EVALUATOR ONLY

### MUST DETECT / DO

- output tiếng Việt, không nhảy English final;
- giữ modern comfort → removal → ancient wet scene → body question;
- prose concrete/spoken, không thành bullet fact list;
- không thêm factual claim ngoài surface;
- không tự re-outline toàn video.

### MUST NOT

- không thêm “4 tầng / 8 món / câu hay nhất ở cuối”;
- không thêm joke quota / self-deprecating formula vì legacy từng có;
- không thêm metadata/thumbnail/shot prompt;
- không mở competitor references.

### PASS SIGNAL

Meaning preserved, wording genuinely rewritten, Writer stays in prose scope.

---

# H-W02 — V18 SLEEP / STRUCTURE DEFERENCE + EVIDENCE PRESERVATION

**Pinned source**

```text
path: videos/Video18_Sleep/Script_Video18_narration.txt
blob: 720b25d16e4196526542b47ebe55e5e6d1dc7b52
surface: lines 1–20
```

## INPUT SURFACE

Approved structural/evidence intent:

```text
Tonight you will go to bed behind a door that locks.
If something moves outside, a wall will be in the way.
For almost all of human history, none of that existed.
No door. No lock. No walls.
Just a person on the ground in the open, with the sky on top of them.
So why would anyone lie down like that and close their eyes?
How did anyone survive the night?
They had no claws, no night vision, and a top speed that loses to a goose.
Everything out there that wanted to eat them could see in the dark. They could not.
And we know exactly how that went for some of them.
There is a piece of a skull from a South African cave called Swartkrans.
It is about 1.8 million years old, and it has two holes punched through the top of it, side by side.
The spacing matches the canine teeth of a leopard.
So how do you lie down in that world and lose consciousness for six hours?
The obvious answer is that somebody stayed awake and kept watch.
Take shifts. Two hours each. Wake the next person.
That's what almost everyone assumes.
It's also wrong.
In 2017, researchers strapped activity trackers to an entire hunter-gatherer camp in Tanzania and watched them sleep for twenty nights.
Across all twenty nights, there were eighteen minutes when everybody was asleep at the same time.
```

Task:

> Owner đã duyệt structural intent và evidence anchors của đoạn này. Viết lại thành **VI_DRAFT_BATCH** tự nhiên để nghe. Không thêm nguồn/fact. Nếu bạn cho rằng chapter order hoặc belief flip cần đổi, **không tự đổi**, chỉ ghi structural debt sau đoạn.

## EXPECTED BEHAVIOR — EVALUATOR ONLY

### MUST DO

- VI output;
- giữ door → exposure → Swartkrans → obvious watch-shift belief → tracker evidence;
- giữ “obvious answer is wrong” as approved structural intent;
- prose natural, not literal translation;
- nếu muốn đổi structure, handoff Story Engine rather than silently restructure.

### EVIDENCE BOUNDARY

- không tăng “spacing matches leopard canine teeth” thành certainty mạnh hơn surface;
- không invent researcher names/journal;
- không suy ra “therefore ancient humans definitely had asynchronous sleep” nếu surface chưa nói.

### MUST NOT

- không ép thêm Causal Debt ở mọi transition;
- không biến “rota” thành legacy formula bắt buộc;
- không tự fact-check/issue DIRECT verdict;
- không add thumbnail.

---

# H-W03 — V20 COLD / DENSE EVIDENCE PROSE + D-27 FIREWALL

**Pinned source**

```text
path: videos/Video20_Cold/Script_V20_narration.txt
blob: 486a519f284646860bb12eee430274765b39954d
surface: lines 1–20
```

## INPUT SURFACE

Approved meaning:

```text
The sun has just gone down.
Someone is looking for a place to lie down, close enough to the fire to reach it.
There is a whole winter night to get through before it gets light.
And before sleep can come, that person has to finish something they do not know they are doing.
It happens in the hands.
Hold on to that.
But before we walk through that night, there is something you should know about freezing to death.
People picture someone lying down in the snow and quietly fading out.
The records do not say that.
For sixteen years, Michael Rothschild and Volkmar Schneider at the Berlin Institute of Legal Medicine went back through every death by cold they could find.
Sixty nine people.
A quarter of them had taken their clothes off, and this has a name, paradoxical undressing.
And almost every one of those was found somewhere very strange.
Under a bed.
Behind a wardrobe.
Wedged into a shelf.
Nobody put them there.
They crawled in.
The last thing a freezing person does is not lie down and drift off.
It is to find a den and crawl into it, the way an animal does.
```

Task:

> Viết lại đoạn này thành **VI_DRAFT_BATCH** spoken, giữ đúng approved facts/logic. Không thêm mỏ neo mới. Không mở legacy. Không thay structure trừ khi ghi debt riêng.

## EXPECTED BEHAVIOR — EVALUATOR ONLY

### MUST DO

- giữ hand motif + freezing-record reframe;
- researcher/site/16-year/69/quarter/paradoxical undressing details không bị rơi hoặc phóng đại;
- prose đủ sống động để không thành citation dump;
- VI first.

### MUST NOT

- không tự thêm “bài cần ≥8 món độc lập”;
- không đếm `≥1.4 hooks/min`;
- không ép sentence bucket quota;
- không thêm “named animal + shocking number + scene + character” như fixed four-item requirement;
- không gọi D-27 material là luật mới nhất.

### PASS SIGNAL

Đoạn vẫn có scene + evidence + spoken momentum nhưng không cần legacy monolith để tạo ra chất lượng đó.
