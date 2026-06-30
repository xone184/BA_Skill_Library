# Phân tích Procurement

## Level
Level 2 - Business Skill

## Purpose
Phân tích toàn diện quy trình mua hàng (Procure-to-Pay / P2P), từ yêu cầu mua hàng (PR) đến thanh toán cho NCC, bao gồm luồng phê duyệt nhiều cấp, so sánh báo giá NCC, quản lý hợp đồng mua và đánh giá NCC.

## When to Use
Sử dụng khi xây dựng module Mua hàng cho ERP.

## Prerequisites
- Hiểu quy trình mua hàng doanh nghiệp

## Inputs
### Yêu cầu mua hàng (Purchase Requisition - PR)
- **Mô tả:** Phiếu đề xuất mua hàng từ các phòng ban.
- **Bắt buộc:** Có
- **Ví dụ:** PR-001: Phòng IT đề xuất mua 10 laptop Dell Latitude 5540, ngân sách 250 triệu.

### Danh sách NCC (Vendor List)
- **Mô tả:** Danh sách nhà cung cấp đã được phê duyệt.
- **Bắt buộc:** Có
- **Ví dụ:** NCC A (Phân phối Dell), NCC B (Tổng đại lý), NCC C (Amazon)

### Ma trận phê duyệt
- **Mô tả:** Ai duyệt PR/PO ở mức nào.
- **Bắt buộc:** Có
- **Ví dụ:** < 10tr: Trưởng phòng. 10-100tr: Giám đốc. > 100tr: CEO.

## Process
### Bước 1: Tạo & Duyệt PR
Nhân viên tạo yêu cầu mua hàng, gửi duyệt theo cấp.

- Nhân viên tạo PR với mô tả hàng, số lượng, ngân sách
- Hệ thống tự động xác định cấp duyệt dựa trên tổng tiền
- Người duyệt: Approve / Reject / Request More Info
- PR được duyệt → Chuyển sang Bộ phận Mua hàng

### Bước 2: Lấy báo giá & So sánh (RFQ)
Gửi yêu cầu báo giá cho nhiều NCC và so sánh.

- Gửi RFQ (Request for Quotation) cho ít nhất 3 NCC
- Nhận báo giá, nhập vào hệ thống
- So sánh trên: Giá, Thời gian giao, Điều kiện thanh toán, Bảo hành
- Chọn NCC tốt nhất

### Bước 3: Tạo & Duyệt PO
Tạo Purchase Order và gửi cho NCC.

- Tạo PO từ PR đã duyệt + Báo giá đã chọn
- PO qua luồng phê duyệt (tương tự PR nhưng có thể cấp cao hơn)
- PO được duyệt → Gửi cho NCC (Email/EDI)
- NCC xác nhận (PO Confirmation)

### Bước 4: Nhận hàng & Đối chiếu
Nhận hàng và đối chiếu 3 bên (3-Way Matching).

- Nhận hàng → Tạo GRN (liên kết với PO)
- 3-Way Matching: PO (đã đặt) vs GRN (đã nhận) vs Invoice (hóa đơn NCC)
- Nếu khớp → Duyệt thanh toán
- Nếu không khớp → Giữ lại (Hold) để điều tra

### Bước 5: Thanh toán (Payment)
Thanh toán cho NCC theo điều kiện hợp đồng.

- Kế toán duyệt Invoice
- Lên lịch thanh toán (Payment Schedule)
- Thanh toán (Bank Transfer / LC / Cash)
- Cập nhật công nợ NCC

## Outputs
### Luồng P2P (BPMN)
- **Định dạng:** Mermaid Flowchart
### Ma trận phê duyệt
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| Giá trị | PR Approver | PO Approver |
|---|---|---|
| < 10 triệu | Trưởng phòng | Trưởng phòng Mua |
| 10 - 100 triệu | Giám đốc | Giám đốc |
| > 100 triệu | CEO | CEO |
```

### Bảng so sánh báo giá
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| Tiêu chí | NCC A | NCC B | NCC C |
|---|---|---|---|
| Đơn giá | 25tr | 24tr | 26tr |
| Giao hàng | 3 ngày | 7 ngày | 2 ngày |
| Thanh toán | 30 ngày | 45 ngày | COD |
| Bảo hành | 12 tháng | 24 tháng | 12 tháng |
```

## Sub-Skills (Kỹ năng con)
- Thiết kế Approval Workflow
- Thiết kế RFQ Process
- Thiết kế 3-Way Matching
- Thiết kế Vendor Evaluation

## Business Rules
- BR-ERP-PO-01: PO > 50 triệu bắt buộc phải có ít nhất 3 báo giá.
- BR-ERP-PO-02: 3-Way Matching chênh lệch > 2% phải Hold Invoice.
- BR-ERP-PO-03: NCC mới phải qua quy trình Vendor Onboarding trước khi tạo PO.
- BR-ERP-PO-04: PR quá 7 ngày chưa duyệt phải escalate lên cấp trên.

## Edge Cases & Exceptions
- NCC giao hàng trước khi PO được duyệt → Xử lý Retrospective PO?
- Cần mua khẩn cấp (Emergency Purchase) → Bỏ qua RFQ được không?
- NCC phá sản giữa chừng → Chuyển sang NCC backup

## Checklist
- [ ] Đã thiết kế luồng PR → RFQ → PO → GRN → Invoice → Payment
- [ ] Đã có ma trận phê duyệt theo giá trị
- [ ] Đã có 3-Way Matching
- [ ] Đã có quy trình đánh giá NCC (Vendor Scorecard)
- [ ] Đã có Emergency Purchase procedure

## Example
Xem Process section.

## Related Skills
- Phân tích Inbound Flow
- Phân tích Kế toán công nợ
