# Backlog Grooming

## Level
Level 2 - Business Skill

## Purpose
Hỗ trợ Product Owner (PO) và Team 'làm sạch' Product Backlog (Backlog Refinement). Bao gồm việc sắp xếp ưu tiên, làm rõ yêu cầu, thêm Acceptance Criteria, và chia nhỏ các User Stories quá lớn (Epics) để chuẩn bị sẵn sàng cho Sprint Planning.

## When to Use
Thường xuyên vào giữa Sprint (trước Planning) để đảm bảo Backlog luôn đủ việc cho 1-2 Sprints tiếp theo.

## Prerequisites
- Đã có Product Backlog sơ bộ

## Inputs
### Danh sách User Stories (Nháp)
- **Mô tả:** Các yêu cầu chưa rõ ràng.
- **Bắt buộc:** Có
- **Ví dụ:** User Story: 'Làm tính năng giỏ hàng' (chưa có chi tiết).

### Mục tiêu Product (Product Goal)
- **Mô tả:** Định hướng phát triển sản phẩm.
- **Bắt buộc:** Không
- **Ví dụ:** Tăng tỷ lệ chuyển đổi mua hàng lên 10%.

## Process
### Bước 1: Review và Xóa bỏ (Purge)
Loại bỏ những thứ không cần thiết.

- Xóa các User Stories đã quá cũ (ví dụ > 6 tháng không làm).
- Xóa các ý tưởng không còn phù hợp với Product Goal.

### Bước 2: Làm rõ yêu cầu (Detailing)
Bổ sung thông tin.

- Thêm Description rõ ràng (Ai, Làm gì, Để làm gì).
- Viết Acceptance Criteria (AC) theo chuẩn Given-When-Then.
- Đính kèm Mockup/UI nếu có.

### Bước 3: Chia nhỏ Story (Story Splitting)
Tách Epic thành Story nhỏ.

- Nếu Story quá lớn (VD: 'Thanh toán trực tuyến') -> Tách thành: 'Thanh toán VNPay', 'Thanh toán Momo'.
- Đảm bảo mỗi Story mới vẫn mang lại giá trị độc lập (INVEST).

### Bước 4: Sắp xếp thứ tự ưu tiên (Prioritization)
Kéo lên trên/xuống dưới.

- Sử dụng MoSCoW (Must, Should, Could, Won't) hoặc Giá trị mang lại vs Nỗ lực (Value vs Effort).

### Bước 5: Đánh giá Ready (Definition of Ready)
Chốt Story.

- Đảm bảo các Story nằm ở top Backlog thỏa mãn DoR (Có AC, Có Mockup, Đã được team review).

## Outputs
### Groomed Product Backlog
- **Định dạng:** Markdown Table
- **Mẫu:**

```
### Product Backlog (Sau Grooming)

| ID | User Story | Priority | Trạng thái (DoR) | Ghi chú (Action) |
|---|---|---|---|---|
| US-101 | As Khách, I want thanh toán VNPay... | High (Must) | Ready | Đã bổ sung 5 AC. |
| US-102 | As Khách, I want thanh toán Momo... | Medium (Should)| Not Ready | Chờ UI Mockup. |
| US-103 | (EPIC) Quản lý hồ sơ | Low | Splitted | Đã chia thành US-104, US-105. |
```

## Sub-Skills (Kỹ năng con)
- Story Splitting
- MoSCoW Prioritization
- DoR Assessment

## Business Rules
- BR-GROOM-01: Chỉ những Story nằm ở trên cùng của Backlog mới cần phân tích chi tiết (DoR).
- BR-GROOM-02: Epic không bao giờ được đưa vào Sprint, phải chia nhỏ thành Story.

## Edge Cases & Exceptions
- Story quá thiên về kỹ thuật (Technical Debt/Refactor) -> Đổi thành Technical Enabler, vẫn đưa vào backlog và gán điểm.

## Checklist
- [ ] Đã chia nhỏ các Story quá lớn (Epic)?
- [ ] Top Backlog đã có đủ Acceptance Criteria?
- [ ] Thứ tự ưu tiên đã rõ ràng chưa?
- [ ] Đã xóa các item rác?

## Example
Xem Groomed Product Backlog trong Outputs.

## Related Skills
- Write User Story
- Sprint Planning
