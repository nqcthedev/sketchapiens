# ENGLISH FINAL REWRITE — VIẾT LẠI BẢN ANH CUỐI

> **Status:** `ACTIVE CONDITIONAL WRITER REFERENCE`
>
> Chỉ load **sau khi bản tiếng Việt đã được owner duyệt/khóa**.
> Đây là semantic rewrite — viết lại theo ý, không phải line-by-line translation.

## 1. Entry gate — Cổng vào

Không chạy stage này nếu chưa có tín hiệu owner approval rõ cho bản VI.

Nếu caller yêu cầu English final nhưng VI chưa khóa:

- dừng;
- nói rõ gate chưa đạt;
- không tự suy ra “chắc là đã duyệt”.

## 2. Goal — Mục tiêu

Tạo narration tiếng Anh:

- tự nhiên khi nói;
- giữ đúng meaning;
- giữ structural intent;
- giữ evidence boundaries;
- giữ stakes/callback/logic đã duyệt;
- không mang cú pháp Việt sang tiếng Anh máy móc.

## 3. Meaning first — Ý trước câu

Không cố giữ:

- cùng số từ từng câu;
- cùng trật tự mệnh đề nếu English nghe gượng;
- cùng idiom;
- cùng punctuation pattern.

Phải giữ:

- proposition / claim;
- causal relation;
- uncertainty;
- referent;
- narrative function;
- approved tone/stakes.

Một câu Việt có thể cần tách thành hai câu Anh hoặc ngược lại, miễn không vi phạm artifact/hard constraints và không đổi logic.

## 4. Spoken English — Tiếng Anh để đọc thành tiếng

Ưu tiên:

- contractions khi tự nhiên;
- concrete verbs;
- pronoun referent rõ;
- syntax người nói có thể thở;
- idiom tự nhiên nhưng không slang quá tay;
- tránh literal calque từ tiếng Việt.

Không “nâng văn” chỉ vì đang chuyển sang English.
Nếu bản Việt bình tĩnh, bản Anh cũng bình tĩnh.

## 5. Three hard narration constraints — Ba ràng buộc cứng

Bản English final phải giữ:

1. `!` = 0;
2. không em dash/en dash/dash dùng như ngắt giữa câu;
3. mỗi câu narration một dòng.

`I ≈ 0` không phải constraint.

## 6. Evidence preservation — Giữ mức chắc

Nếu VI nói:

- “có thể” → không được thành “did” chắc chắn;
- “gợi ý” → không được thành “proves”;
- “một cách giải thích” → không được thành “the reason”.

Nếu English tự nhiên hơn cần thay cấu trúc hedge, vẫn phải giữ **epistemic strength** tương đương.

## 7. No factual expansion — Không tự thêm fact

Không thêm trong rewrite:

- số mới;
- year mới;
- researcher/site mới;
- mechanism detail mới;
- “helpful clarification” mang factual content chưa có trong VI locked/evidence packet.

Nếu cần factual addition để câu Anh hiểu được:

```text
STOP
→ mark factual addition
→ Evidence handoff
→ owner/flow resolves
→ then rewrite
```

## 8. Preserve causal logic — Không làm lệch quan hệ

Translation drift thường xảy ra khi một connector bị đổi:

- because → while;
- but → and;
- could → did;
- before → after;
- one of → the;
- some → all.

Sau rewrite, đọc lại theo **logic**, không chỉ grammar.

## 9. Preserve referents — Giữ chủ thể/chỗ bám

Kiểm từng đoạn:

- `it` là gì;
- `they` là ai;
- `this` trỏ vào claim nào;
- một callback còn trỏ đúng setup không;
- species/site/researcher có bị đổi chủ thể không.

Nếu câu Việt dựa vào subject omission tự nhiên, tiếng Anh thường cần subject rõ hơn.

## 10. Tone transfer — Chuyển tông, không chuyển chữ

Giữ chức năng của giọng:

- deadpan → deadpan tự nhiên bằng English;
- serious → không bơm trailer language;
- playful → không biến thành meme slang;
- restrained → không thêm intensifier.

Một joke không dịch được thì viết lại **cùng function**, không bám chữ.
Nếu joke chỉ sống nhờ pun tiếng Việt và không có equivalent tốt, ưu tiên clarity hơn ép joke.

## 11. Anti-AI pass — Chống dấu dịch máy / văn AI

Sau khi rewrite, đọc riêng bản English và hỏi:

- có câu nào nghe như literal translation không;
- có chỗ nào quá formal so với spoken register;
- có chiasmus/cách ngôn mới xuất hiện mà VI không có không;
- có “this is not X, it is Y” lặp quá nhiều không;
- có abstract noun stack không;
- contractions có bị tránh vô lý không;
- có pronoun bị mơ hồ sau khi reorder không.

Không rewrite chỉ để “de-AI” nếu câu đã tự nhiên.

## 12. Final comparison — So theo meaning, không side-by-side approval

Không tạo bảng EN+VI cho owner duyệt.

Writer có thể tự kiểm internally theo các câu hỏi:

```text
Mỗi claim còn cùng mức chắc?
Mỗi causal bridge còn cùng nghĩa?
Có fact mới nào lọt vào?
Có payoff/callback nào mất?
Có câu English nào đổi subject?
```

Output cho owner là **English narration final**, không phải bảng dịch.

## 13. Handoff after English rewrite

Nếu rewrite không phát sinh evidence debt:

- chạy hard-constraint QA theo workflow;
- chuyển sang review/approval artifact flow phù hợp;
- không tự làm packaging/production.

Nếu phát sinh factual change:

- return Evidence first.

## 14. Stop condition

Dừng khi English:

- nghe tự nhiên độc lập;
- giữ meaning/evidence/structure;
- sạch ba hard constraints;
- không có factual addition;
- không còn dấu literal translation đáng kể.

Không polish vô hạn để câu “đẹp hơn” nếu edit tiếp chỉ đổi gu mà không sửa weakness thật.
