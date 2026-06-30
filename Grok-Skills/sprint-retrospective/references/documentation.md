# Sprint Retrospective

## Level
Level 2 - Business Skill

## Purpose
Hỗ trợ Scrum Master / Đội ngũ đánh giá lại quá trình làm việc trong Sprint vừa qua, nhận diện những điểm tốt, điểm chưa tốt và đề xuất Action Items cụ thể để cải tiến cho Sprint tiếp theo (Continuous Improvement).

## When to Use
Sử dụng vào ngày cuối cùng của Sprint, sau khi kết thúc Sprint Review.

## Prerequisites
- Đã hoàn thành Sprint

## Inputs
### Kết quả Sprint (Sprint Metrics)
- **Mô tả:** Dữ liệu thực tế của Sprint.
- **Bắt buộc:** Có
- **Ví dụ:** Kế hoạch 40 Points, Thực tế hoàn thành 32 Points. Có 5 Bug phát sinh.

### Ý kiến của Team
- **Mô tả:** Feedback từ Dev, QA, PO.
- **Bắt buộc:** Không
- **Ví dụ:** Mọi người cảm thấy requirements thay đổi giữa chừng.

## Process
### Bước 1: Thu thập dữ liệu Sprint
Nhìn lại các chỉ số.

- Velocity (Tốc độ hoàn thành)
- Sprint Goal có đạt không?
- Số lượng Bug/Escalation phát sinh
- Chất lượng (Code coverage, Review comments)

### Bước 2: Tổ chức phiên Brainstorming
Khuyến khích mọi người chia sẻ.

- Sử dụng format chuẩn: What went well? (Điều gì tốt?)
- What didn't go well? (Điều gì chưa tốt?)
- What can we improve? (Cần cải thiện gì?)
- Đảm bảo nguyên tắc: Không đổ lỗi (No blame game), tập trung vào quy trình.

### Bước 3: Phân tích nguyên nhân (Root Cause)
Tìm hiểu tại sao điều chưa tốt lại xảy ra.

- Sử dụng 5 Whys. (VD: Tại sao chậm tiến độ? → Vì QA test chậm → Tại sao test chậm? → Vì môi trường test lỗi...)

### Bước 4: Thiết lập Action Items
Đưa ra hành động cải tiến.

- Hành động phải cụ thể, đo lường được (SMART)
- Chỉ chọn tối đa 2-3 Action Items quan trọng nhất để làm trong Sprint tiếp theo
- Phân công người chịu trách nhiệm (Owner) cho từng Action Item

### Bước 5: Review Action Items cũ
Kiểm tra xem cải tiến của Sprint trước có hiệu quả không.

- Nếu Action cũ hiệu quả → Giữ thành Process mới
- Nếu không hiệu quả → Bỏ hoặc thử cách khác

## Outputs
### Retrospective Minutes
- **Định dạng:** Markdown Document
- **Mẫu:**

```
# Sprint [N] Retrospective

## 1. Metrics Review
- Goal: Thất bại
- Velocity: 32/40 Points

## 2. Feedback (Mad/Sad/Glad hoặc Start/Stop/Continue)
**What went well (Glad):**
- API tích hợp nhanh chóng, BE và FE phối hợp tốt.

**What didn't go well (Sad):**
- Requirement luồng Thanh toán bị đổi vào giữa Sprint.
- Môi trường Test chết 1 ngày.

## 3. Action Items cho Sprint tới
| # | Action Item | Phân loại | Owner | Deadline |
|---|---|---|---|---|
| 1 | Block mọi thay đổi requirement sau khi Sprint bắt đầu | Quy trình | PO | Ngay lập tức |
| 2 | Setup tool monitor cho Môi trường Test | Kỹ thuật | DevOps | Đầu Sprint [N+1] |
```

## Sub-Skills (Kỹ năng con)
- Root Cause Analysis
- Meeting Facilitation
- SMART Goal Setting

## Business Rules
- BR-RETRO-01: Không đổ lỗi cho cá nhân, mọi vấn đề là do hệ thống/quy trình.
- BR-RETRO-02: Action Item phải có Chủ sở hữu (Owner) cụ thể.
- BR-RETRO-03: Mỗi Sprint chỉ nên tập trung cải thiện 1-3 vấn đề lớn nhất.

## Edge Cases & Exceptions
- Team không ai chịu nói (Im lặng) → Dùng hình thức bỏ phiếu ẩn danh (Anonymous board)
- Xung đột cá nhân trong buổi Retro → Scrum Master can thiệp, đưa cuộc họp về chủ đề công việc

## Checklist
- [ ] Đã review lại Metrics của Sprint?
- [ ] Đã có mục 'What went well'?
- [ ] Đã có mục 'What didn't go well'?
- [ ] Đã dùng 5 Whys để tìm nguyên nhân chưa?
- [ ] Đã chốt được Action Items cụ thể (SMART)?
- [ ] Action Items đã có người phụ trách (Owner)?

## Example
Xem Retrospective Minutes template trong Outputs.

## Related Skills
- Sprint Planning
- Root Cause Analysis
