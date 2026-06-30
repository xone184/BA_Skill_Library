# Phân tích Kế toán công nợ

## Level
Level 2 - Business Skill

## Purpose
Phân tích toàn diện luồng quản lý công nợ phải thu (Accounts Receivable - AR) và công nợ phải trả (Accounts Payable - AP), bao gồm hạn mức tín dụng (Credit Limit), tuổi nợ (Aging), đối chiếu công nợ và xử lý xóa nợ (Write-off).

## When to Use
Sử dụng khi xây dựng module Kế toán cho ERP hoặc tích hợp CRM/WMS với Kế toán.

## Prerequisites
- Hiểu cơ bản về kế toán doanh nghiệp
- Đã phân tích Procurement

## Inputs
### Chính sách tín dụng (Credit Policy)
- **Mô tả:** Quy định về hạn mức nợ và thời hạn thanh toán cho khách hàng.
- **Bắt buộc:** Có
- **Ví dụ:** Khách hàng hạng A: Credit Limit = 500tr, Payment Term = Net 30. Khách hàng hạng B: Credit Limit = 200tr, Payment Term = Net 15.

### Hóa đơn (Invoice)
- **Mô tả:** Danh sách hóa đơn phát sinh từ Bán hàng hoặc Mua hàng.
- **Bắt buộc:** Có
- **Ví dụ:** INV-001: Khách ABC, Giá trị 100tr, Ngày xuất 01/06, Hạn thanh toán 30/06.

### Quy tắc nhắc nợ (Dunning Rules)
- **Mô tả:** Kịch bản nhắc nợ theo thời gian quá hạn.
- **Bắt buộc:** Không
- **Ví dụ:** Quá hạn 7 ngày → Email nhắc. 15 ngày → Gọi điện. 30 ngày → Thư cảnh cáo. 60 ngày → Chặn bán hàng.

## Process
### Bước 1: Ghi nhận phát sinh công nợ
Tạo bản ghi công nợ khi có hóa đơn bán hàng (AR) hoặc hóa đơn mua hàng (AP).

- AR: Khi xuất hóa đơn bán hàng → Tự động tạo bản ghi Phải Thu liên kết với Invoice + SO
- AP: Khi nhận hóa đơn NCC (đã qua 3-Way Matching) → Tự động tạo bản ghi Phải Trả liên kết với Invoice + PO + GRN
- Kiểm tra Credit Limit: Nếu tổng nợ hiện tại + đơn mới > Credit Limit → Block đơn hàng, cần phê duyệt đặc biệt

### Bước 2: Theo dõi tuổi nợ (Aging Analysis)
Phân loại công nợ theo thời gian quá hạn.

- Bucket 1: Chưa đến hạn (Current)
- Bucket 2: Quá hạn 1-30 ngày
- Bucket 3: Quá hạn 31-60 ngày
- Bucket 4: Quá hạn 61-90 ngày
- Bucket 5: Quá hạn > 90 ngày (Nợ khó đòi)
- Dashboard: Biểu đồ Aging theo khách hàng, theo khu vực

### Bước 3: Nhắc nợ tự động (Dunning)
Gửi thông báo nhắc nợ theo kịch bản.

- Level 1 (Quá hạn 7 ngày): Email nhắc nhở nhẹ nhàng
- Level 2 (Quá hạn 15 ngày): Gọi điện thoại + Email
- Level 3 (Quá hạn 30 ngày): Thư cảnh cáo chính thức
- Level 4 (Quá hạn 60 ngày): Chặn bán hàng (Block Sales Order)
- Level 5 (Quá hạn 90 ngày): Chuyển cho bộ phận Pháp lý

### Bước 4: Đối chiếu công nợ (Reconciliation)
Đối chiếu số liệu giữa Sổ công nợ và Sổ ngân hàng/Sổ cái.

- Khớp thanh toán (Payment Matching): Khi nhận tiền → Khớp với Invoice nào?
- Hỗ trợ khớp tự động (Auto-matching) theo số Invoice trên mã giao dịch ngân hàng
- Xử lý thanh toán dư (Overpayment): Trả lại hay giữ Credit Memo?
- Xử lý thanh toán thiếu (Underpayment): Tạo Debit Note hay chờ?
- Đối chiếu cuối kỳ: Gửi Statement of Account cho khách ký xác nhận

### Bước 5: Xóa nợ và trích lập dự phòng (Write-off & Provision)
Xử lý nợ không thể thu hồi.

- Nợ quá hạn > 12 tháng: Trích lập dự phòng (Provision) 100%
- Nợ xác nhận không thu được: Lập hồ sơ xóa nợ (Write-off)
- Phê duyệt xóa nợ: Kế toán trưởng → Giám đốc Tài chính → CEO (tùy giá trị)
- Hạch toán kế toán: Nợ TK Chi phí / Có TK Phải thu

## Outputs
### Báo cáo Aging (Tuổi nợ)
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| Khách hàng | Current | 1-30 ngày | 31-60 ngày | 61-90 ngày | >90 ngày | Tổng |
|---|---|---|---|---|---|---|
| ABC Corp | 100tr | 50tr | 20tr | 0 | 0 | 170tr |
| XYZ Ltd | 0 | 0 | 30tr | 45tr | 80tr | 155tr |
```

### Dunning Schedule
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| Level | Quá hạn | Hành động | Người thực hiện | Kênh |
|---|---|---|---|---|
| 1 | 7 ngày | Nhắc nhở | Hệ thống tự động | Email |
| 2 | 15 ngày | Gọi điện | Kế toán | Phone + Email |
| 3 | 30 ngày | Cảnh cáo | Kế toán trưởng | Thư chính thức |
| 4 | 60 ngày | Chặn bán | Hệ thống tự động | Block SO |
| 5 | 90 ngày | Pháp lý | Pháp chế | Công văn |
```

### Cấu trúc dữ liệu AR/AP
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| Trường | Kiểu | Mô tả |
|---|---|---|
| receivable_id | INT (PK) | Mã công nợ |
| customer_id | INT (FK) | Khách hàng |
| invoice_id | INT (FK) | Hóa đơn |
| amount | DECIMAL | Số tiền |
| due_date | DATE | Ngày đến hạn |
| paid_amount | DECIMAL | Đã thanh toán |
| balance | DECIMAL | Còn lại |
| status | ENUM | Open/Partial/Paid/Overdue/WriteOff |
```

## Sub-Skills (Kỹ năng con)
- Thiết kế Credit Limit Policy
- Thiết kế Aging Report
- Thiết kế Dunning Automation
- Thiết kế Payment Matching

## Business Rules
- BR-FIN-AR-01: Tổng nợ hiện tại + Đơn hàng mới > Credit Limit → Block Sales Order.
- BR-FIN-AR-02: Khách hàng quá hạn > 60 ngày tự động bị chặn bán hàng.
- BR-FIN-AR-03: Write-off nợ > 50 triệu phải có phê duyệt của CFO.
- BR-FIN-AR-04: Nợ quá hạn > 6 tháng phải trích lập dự phòng 50%, > 12 tháng = 100%.
- BR-FIN-AP-05: Không thanh toán cho NCC nếu Invoice chưa qua 3-Way Matching.

## Edge Cases & Exceptions
- Khách thanh toán bằng tiền mặt nhưng không ghi số Invoice → Xử lý Unidentified Payment
- Khách thanh toán gộp nhiều Invoice trong 1 lần chuyển khoản → Cần tách (Split Payment)
- NCC gửi Invoice trùng → Cần phát hiện Duplicate Invoice
- Tỷ giá thay đổi giữa ngày xuất Invoice và ngày thanh toán → Xử lý chênh lệch tỷ giá (Exchange Rate Difference)

## Checklist
- [ ] Đã thiết kế Credit Limit cho khách hàng
- [ ] Đã có Aging Report (5 Buckets)
- [ ] Đã thiết kế Dunning tự động theo cấp
- [ ] Đã có luồng đối chiếu công nợ (Reconciliation)
- [ ] Đã xử lý Payment Matching (tự động + thủ công)
- [ ] Đã có luồng Write-off với phê duyệt nhiều cấp
- [ ] Đã xử lý Overpayment / Underpayment
- [ ] Đã có Statement of Account gửi khách hàng cuối kỳ

## Example
Xem Aging Report và Dunning Schedule trong phần Outputs.

## Related Skills
- Phân tích Procurement
- Phân tích Opportunity
