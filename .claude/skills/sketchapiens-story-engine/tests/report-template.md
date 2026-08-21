# STORY ENGINE SMOKE REPORT — MẪU BÁO CÁO

SMOKE RUN: YYYY-MM-DD  
ENGINE COMMIT: `<sha>`  
PROFILE: `STRUCTURE_SMOKE` / `REVIEWER_SMOKE`  
SUITE STATUS: `PASS` / `FAIL` / `REVIEW`

---

FIXTURE: H-01
RESULT: REVIEW
SEVERITY: NONE
MUST DETECT: REVIEW
MUST NOT: REVIEW
EVIDENCE HANDOFF: N/A
CANDIDATE FIREWALL: PASS
OBSERVED DIAGNOSIS:
<ghi diagnosis thực tế ở đây>

---

> Copy block trên cho H-02 → H-05 và M-01 → M-10.
> Full suite phải có đủ 15 fixture ID để `check_smoke_report.py` pass mà không cần `--partial`.

## SUITE SUMMARY

PASS:  
FAIL:  
REVIEW:  
P0:  
P1:  
P2:  
P3:  

## REGRESSION NOTES — GHI CHÚ HỒI QUY

- First bad commit — commit đầu tiên gây lỗi:
- Fixture expectation có thể sai không:
- Engine/reference nào có khả năng gây regression:
- Case đối nghịch cần rerun:
- Quyết định: sửa engine / sửa fixture / giữ REVIEW:
