# Review Requirement

## Level
Level 4 - Thinking Skill

## Purpose
Rà soát và kiểm tra tính đầy đủ, chính xác, nhất quán của yêu cầu nghiệp vụ. Đây là kỹ năng kiểm duyệt cuối cùng trước khi chốt scope, đảm bảo không bỏ sót bất kỳ Business Rule, Exception, Validation, Permission, UI, API, Database, Workflow, Report hay Notification nào.

## When to Use
Sử dụng ở cuối giai đoạn phân tích, trước khi chốt scope với khách hàng hoặc bàn giao cho team Dev.

## Prerequisites
- Đã hoàn thành viết Requirement List / BRD / SRS

## Inputs
### Tài liệu yêu cầu (BRD/SRS/Requirement List)
- **Mô tả:** Bộ tài liệu cần review.
- **Bắt buộc:** Có
- **Ví dụ:** File SRS v1.0 với 45 Functional Requirements và 10 Non-Functional Requirements.

## Process
### Bước 1: Kiểm tra TÍNH ĐẦY ĐỦ (Completeness)
Rà soát xem có thiếu yêu cầu nào không.

- Missing Business Rule? Có quy tắc nghiệp vụ nào chưa được mô tả?
- Missing Exception? Các trường hợp ngoại lệ đã được xử lý hết chưa?
- Missing Validation? Các rule kiểm tra dữ liệu đầu vào đã đủ chưa?
- Missing Permission? Ai được làm gì trên mỗi chức năng?
- Missing UI? Có màn hình/form nào chưa được mô tả?
- Missing API? Có endpoint nào thiếu?
- Missing Database? Có trường dữ liệu nào chưa được định nghĩa?
- Missing Workflow? Luồng phê duyệt đã đủ chưa?
- Missing Report? Có báo cáo nào người dùng cần nhưng chưa liệt kê?
- Missing Notification? Có cảnh báo/email nào cần gửi nhưng chưa thiết kế?

### Bước 2: Kiểm tra TÍNH NHẤT QUÁN (Consistency)
Rà soát xem có requirement nào mâu thuẫn nhau không.

- Requirement A nói 'cho phép xóa' nhưng Requirement B nói 'không được xóa'?
- Thuật ngữ có được dùng nhất quán không? (VD: Customer vs Client vs Khách hàng)
- Business Rule có xung đột với nhau không?

### Bước 3: Kiểm tra TÍNH KHẢ THI (Feasibility)
Đánh giá xem requirement có khả thi về mặt kỹ thuật không.

- Yêu cầu 'realtime' có thực sự cần thiết không? (Nếu near-realtime 5 phút đã đủ thì rẻ hơn nhiều)
- Yêu cầu tích hợp bên thứ 3 có API không?
- Dữ liệu cần migrate có sẵn sàng không?

### Bước 4: Đưa ra câu hỏi cho khách hàng
Lập danh sách câu hỏi cần hỏi khách hàng để làm rõ.

- Mỗi câu hỏi phải liên kết với Requirement ID cụ thể
- Phân loại: Phải hỏi ngay (Blocker) vs Có thể hỏi sau (Nice to know)
- Đề xuất lựa chọn cho khách hàng (Option A / Option B) thay vì câu hỏi mở

### Bước 5: Đưa ra gợi ý bổ sung (Suggestions)
Dựa trên kinh nghiệm, đề xuất các yêu cầu mà khách hàng có thể chưa nghĩ tới.

- Gợi ý tính năng nâng cao (Nice-to-have)
- Gợi ý cải thiện UX
- Gợi ý về bảo mật, audit, logging

## Outputs
### Review Report
- **Định dạng:** Markdown Document
- **Mẫu:**

```
# Requirement Review Report

## 1. Tổng quan
- Số lượng Requirement đã review: [N]
- Số lượng Issue phát hiện: [N]
- Số lượng câu hỏi cần hỏi khách: [N]

## 2. Issues Found
| # | Requirement ID | Loại Issue | Mô tả | Severity |
|---|---|---|---|---|
| 1 | FR-015 | Missing Validation | Chưa validate email format | Medium |
| 2 | FR-022 | Missing Permission | Ai được xóa đơn hàng? | High |

## 3. Questions for Client
| # | Requirement ID | Câu hỏi | Gợi ý |
|---|---|---|---|
| 1 | BR-003 | Hàng hết HSD xử lý thế nào? | Option A: Tự động chặn xuất. Option B: Cảnh báo nhưng vẫn cho xuất. |

## 4. Suggestions
| # | Mô tả | Lý do |
|---|---|---|
| 1 | Thêm Audit Log cho mọi thao tác xóa | Truy vết khi có sự cố |
```

## Sub-Skills (Kỹ năng con)
- Completeness Check
- Consistency Check
- Feasibility Assessment
- Question Formulation

## Business Rules
- BR-REV-01: Mỗi Requirement phải được review ít nhất 1 lần trước khi chốt.
- BR-REV-02: Issue severity High phải được giải quyết trước khi bàn giao cho Dev.
- BR-REV-03: Mọi câu hỏi Blocker phải được trả lời trước khi bắt đầu Sprint.

## Edge Cases & Exceptions
- Khách hàng không trả lời câu hỏi → Ghi nhận assumption và tiến hành
- Requirement mâu thuẫn giữa 2 phòng ban → Escalate lên Sponsor

## Checklist
- [ ] Đã kiểm tra Missing Business Rule?
- [ ] Đã kiểm tra Missing Exception?
- [ ] Đã kiểm tra Missing Validation?
- [ ] Đã kiểm tra Missing Permission?
- [ ] Đã kiểm tra Missing UI?
- [ ] Đã kiểm tra Missing API?
- [ ] Đã kiểm tra Missing Database?
- [ ] Đã kiểm tra Missing Workflow?
- [ ] Đã kiểm tra Missing Report?
- [ ] Đã kiểm tra Missing Notification?
- [ ] Đã kiểm tra Consistency (không mâu thuẫn)?
- [ ] Đã đặt câu hỏi cho từng điểm chưa rõ?

## Example
Xem Review Report template trong Outputs.

## Related Skills
- Write BRD
- Write SRS
- Gap Analysis
- Impact Analysis
