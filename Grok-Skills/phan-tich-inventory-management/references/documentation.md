# Phân tích Inventory Management

## Level
Level 2 - Business Skill

## Purpose
Phân tích toàn diện quy trình quản lý tồn kho, bao gồm kiểm kê (Cycle Count / Full Count), điều chỉnh tồn kho (Stock Adjustment), luân chuyển nội bộ (Internal Transfer), quản lý tồn kho tối thiểu/tối đa (Min-Max) và các báo cáo phân tích tồn kho.

## When to Use
Sử dụng khi xây dựng module Inventory cho WMS hoặc ERP.

## Prerequisites
- Đã phân tích Inbound/Outbound Flow

## Inputs
### Dữ liệu tồn kho hiện tại
- **Mô tả:** Snapshot số lượng hàng hiện có trên hệ thống.
- **Bắt buộc:** Có
- **Ví dụ:** SKU-A01: On-hand = 500, Allocated = 120, Available = 380

### Phương pháp kiểm kê
- **Mô tả:** Full Count (Kiểm kê toàn bộ) hay Cycle Count (Kiểm kê luân phiên).
- **Bắt buộc:** Có
- **Ví dụ:** Cycle Count hàng ngày theo phân loại ABC: Loại A kiểm hàng tuần, Loại B hàng tháng, Loại C hàng quý

### Ngưỡng Min-Max
- **Mô tả:** Mức tồn kho tối thiểu và tối đa cho từng SKU.
- **Bắt buộc:** Không
- **Ví dụ:** SKU-A01: Min = 100, Max = 500, Reorder Point = 200

## Process
### Bước 1: Phân loại tồn kho (ABC Analysis)
Phân loại hàng hóa theo giá trị/tần suất để ưu tiên quản lý.

- Loại A (20% SKU, 80% giá trị): Kiểm kê thường xuyên, quản lý chặt
- Loại B (30% SKU, 15% giá trị): Kiểm kê định kỳ
- Loại C (50% SKU, 5% giá trị): Kiểm kê ít thường xuyên
- Kết hợp XYZ Analysis (theo biến động nhu cầu) nếu cần

### Bước 2: Kiểm kê (Counting)
Thực hiện kiểm đếm tồn kho thực tế.

- Cycle Count: Chọn ngẫu nhiên hoặc theo lịch một số SKU/Location để đếm mỗi ngày
- Full Count: Đóng kho (Freeze) và kiểm toàn bộ (thường cuối năm)
- Blind Count: Nhân viên đếm mà không thấy số lượng hệ thống → Giảm bias
- Quét mã vạch tại từng Location và nhập số lượng đếm được

### Bước 3: Xử lý chênh lệch (Variance)
So sánh số đếm thực tế với số trên hệ thống.

- Nếu chênh lệch ≤ Tolerance (VD: ≤ 2%) → Tự động điều chỉnh
- Nếu chênh lệch > Tolerance → Yêu cầu đếm lại (Recount)
- Nếu sau Recount vẫn chênh → Quản lý kho phê duyệt Stock Adjustment
- Ghi nhận lý do chênh lệch (Mất mát, Hư hỏng, Lỗi nhập liệu)

### Bước 4: Luân chuyển nội bộ (Internal Transfer)
Di chuyển hàng giữa các kho hoặc các Zone trong cùng kho.

- Tạo Transfer Order (Kho A → Kho B)
- Trừ tồn kho Kho A, Cộng tồn kho Kho B
- Hỗ trợ Transfer đang trên đường (In-Transit stock)

### Bước 5: Báo cáo & Cảnh báo
Dashboard và cảnh báo tồn kho.

- Cảnh báo tồn kho dưới MIN (Low Stock Alert)
- Cảnh báo tồn kho vượt MAX (Overstock Alert)
- Cảnh báo hàng sắp hết hạn (Expiring Soon Alert)
- Báo cáo: Inventory Aging (Hàng tồn quá lâu), Turnover Rate, Stock Value

## Outputs
### Quy trình Kiểm kê (BPMN)
- **Định dạng:** Mermaid Flowchart
### Bảng phân loại ABC
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| Loại | % SKU | % Giá trị | Tần suất kiểm kê | VD |
|---|---|---|---|---|
| A | 20% | 80% | Hàng tuần | Linh kiện đắt tiền |
| B | 30% | 15% | Hàng tháng | Vật tư phổ thông |
| C | 50% | 5% | Hàng quý | Văn phòng phẩm |
```

### Cấu trúc dữ liệu Inventory
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| Trường | Kiểu | Mô tả |
|---|---|---|
| sku | VARCHAR | Mã hàng |
| warehouse_id | INT (FK) | Kho |
| location | VARCHAR | Vị trí kệ |
| on_hand_qty | DECIMAL | Tồn thực |
| allocated_qty | DECIMAL | Đã đặt |
| available_qty | DECIMAL | Khả dụng |
| lot_number | VARCHAR | Số lô |
| expiry_date | DATE | Hạn dùng |
```

## Sub-Skills (Kỹ năng con)
- Thiết kế ABC Analysis
- Thiết kế Cycle Count Plan
- Thiết kế Stock Adjustment Approval
- Thiết kế Min-Max Rules

## Business Rules
- BR-WMS-INV-01: Cycle Count phải chặn giao dịch Inbound/Outbound tại Location đang đếm.
- BR-WMS-INV-02: Stock Adjustment chênh lệch > 2% phải có phê duyệt Manager.
- BR-WMS-INV-03: Available Qty = On-hand Qty - Allocated Qty.
- BR-WMS-INV-04: Không cho phép Available Qty âm (Overselling).
- BR-WMS-INV-05: Hàng tồn > 180 ngày phải đánh giá lại giá trị (Inventory Write-down).

## Edge Cases & Exceptions
- Đang kiểm kê thì có hàng nhập kho → Chặn GRN hay vẫn cho phép?
- Tồn kho hệ thống = 100 nhưng thực tế = 0 → Nguyên nhân gì?
- Hàng đã Allocated cho SO nhưng SO bị hủy → Giải phóng Allocation
- Multi-warehouse: Tồn kho Kho A = 0 nhưng Kho B = 500 → Tự động Transfer?

## Checklist
- [ ] Đã thiết kế phân loại ABC/XYZ
- [ ] Đã có quy trình Cycle Count và Full Count
- [ ] Đã xử lý chênh lệch với Tolerance threshold
- [ ] Đã có luồng Stock Adjustment phê duyệt
- [ ] Đã quản lý Available vs On-hand vs Allocated
- [ ] Đã có cảnh báo Min/Max/Expiry
- [ ] Đã có báo cáo Inventory Aging và Turnover

## Example
Xem Process section.

## Related Skills
- Phân tích Inbound Flow
- Phân tích Outbound Flow
- Phân tích Replenishment
