# Phân tích Return Management

## Level
Level 2 - Business Skill

## Purpose
Quản lý toàn diện luồng hàng hoàn trả (RMA) từ khách hàng, bao gồm tiếp nhận yêu cầu, nhận hàng trả về, kiểm tra chất lượng (QC), phân loại xử lý (Tái nhập kho, Sửa chữa, Tiêu hủy) và hoàn tiền/đổi hàng.

## When to Use
Khi xây dựng module Return trong WMS hoặc E-commerce.

## Prerequisites
- Đã phân tích Inbound Flow

## Inputs
### Đơn yêu cầu hoàn trả (RMA Request)
- **Mô tả:** Thông tin đơn hàng gốc, lý do trả, số lượng trả.
- **Bắt buộc:** Có
- **Ví dụ:** RMA-001: Trả 5 thùng Sữa TH từ SO-500, lý do: Hàng bị hư hỏng trong vận chuyển.

### Chính sách đổi trả (Return Policy)
- **Mô tả:** Điều kiện được trả, thời hạn, ai chịu phí ship.
- **Bắt buộc:** Có
- **Ví dụ:** Được trả trong 7 ngày, hàng còn nguyên seal. Hàng khuyến mãi không được trả.

## Process
### Bước 1: Tiếp nhận yêu cầu trả hàng
Xác nhận đơn hàng gốc, kiểm tra điều kiện trả hàng.

- Kiểm tra SO gốc còn trong thời hạn đổi trả không
- Kiểm tra hàng có nằm trong danh sách không được trả không
- Tạo RMA Number và gửi cho khách hàng

### Bước 2: Nhận hàng trả về
Nhận hàng vật lý tại kho.

- Nhận hàng tại dock Return riêng (tách biệt với Inbound)
- Kiểm đếm số lượng khớp RMA
- Chụp ảnh hiện trạng hàng

### Bước 3: QC hàng trả
Kiểm tra chất lượng và phân loại.

- Grade A: Hàng tốt, có thể bán lại → Tái nhập kho
- Grade B: Hàng có khuyết điểm nhỏ → Bán giảm giá (Refurbished)
- Grade C: Hàng hỏng nặng → Tiêu hủy hoặc trả NCC
- Nếu lỗi do NCC → Tạo Supplier Claim

### Bước 4: Xử lý hoàn tiền/đổi hàng
Thực hiện hoàn tiền hoặc gửi hàng thay thế.

- Hoàn tiền → Cập nhật công nợ, thông báo Kế toán
- Đổi hàng → Tạo SO thay thế tự động
- Cập nhật tồn kho (Nếu tái nhập) hoặc ghi giảm (Nếu tiêu hủy)

## Outputs
### Quy trình Return (BPMN)
- **Định dạng:** Mermaid Flowchart
### Ma trận phân loại hàng trả
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| Grade | Tình trạng | Xử lý | Ảnh hưởng tồn kho |
|---|---|---|---|
| A | Nguyên vẹn | Tái nhập kho | +Qty |
| B | Khuyết điểm nhỏ | Bán giảm giá | +Qty (vùng Outlet) |
| C | Hỏng nặng | Tiêu hủy | Write-off |
```

## Sub-Skills (Kỹ năng con)
- Thiết kế RMA Workflow
- Thiết kế QC Return Grading
- Thiết kế Supplier Claim

## Business Rules
- BR-WMS-RET-01: Chỉ nhận hàng trả có RMA Number hợp lệ.
- BR-WMS-RET-02: Hàng trả về phải qua QC trước khi tái nhập kho.
- BR-WMS-RET-03: Hàng Grade C phải có biên bản tiêu hủy có chữ ký Quản lý.
- BR-WMS-RET-04: Hoàn tiền chỉ được xử lý sau khi QC hoàn tất.

## Edge Cases & Exceptions
- Khách trả hàng không có trong SO gốc (gửi nhầm) → Xử lý hàng vô chủ
- Hàng trả bị nhiễm bẩn → Có cần cách ly không?

## Checklist
- [ ] Đã thiết kế luồng RMA Request
- [ ] Đã có dock riêng cho hàng trả (tách biệt Inbound)
- [ ] Đã có QC Grading (A/B/C)
- [ ] Đã xử lý hoàn tiền/đổi hàng
- [ ] Đã cập nhật tồn kho sau khi xử lý
- [ ] Đã tạo Supplier Claim khi lỗi NCC

## Example
Xem Process.

## Related Skills
- Phân tích Inbound Flow
- Phân tích Quality Control
