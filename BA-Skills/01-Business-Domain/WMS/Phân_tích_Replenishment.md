# Phân tích Replenishment

## Level
Level 2 - Business Skill

## Purpose
Phân tích quy trình bổ sung hàng tự động từ khu vực dự trữ (Reserve) sang khu vực nhặt hàng (Picking), và từ NCC vào kho khi tồn kho chạm mức tối thiểu.

## When to Use
Khi kho lớn có tách biệt Reserve Zone và Picking Zone.

## Prerequisites
- Đã phân tích Inventory Management

## Inputs
### Reorder Point / Min Level
- **Mô tả:** Ngưỡng tồn kho tại vị trí Picking để trigger bổ sung.
- **Bắt buộc:** Có
- **Ví dụ:** SKU-A01 tại Zone A: Min = 20 thùng. Khi tồn Picking < 20 → Trigger Replenishment.

### Safety Stock
- **Mô tả:** Lượng tồn kho an toàn để phòng biến động.
- **Bắt buộc:** Có
- **Ví dụ:** Safety Stock = 50 thùng (Dựa trên Lead time NCC là 3 ngày và nhu cầu trung bình 15 thùng/ngày)

## Process
### Bước 1: Giám sát ngưỡng tồn kho
Hệ thống liên tục theo dõi Available Qty tại Picking Location.

- So sánh Available Qty vs Min Level theo realtime hoặc batch (mỗi giờ)
- Khi Available Qty < Min Level → Trigger Replenishment Task

### Bước 2: Tạo lệnh bổ sung (Replenishment Task)
Hệ thống tự động tạo lệnh di chuyển hàng.

- Xác định nguồn: Reserve Location cùng SKU gần nhất
- Số lượng bổ sung = Max Level - Current Qty (Top-off) hoặc = Fixed Qty
- Gán cho nhân viên kho thực hiện

### Bước 3: Thực hiện & Xác nhận
Nhân viên di chuyển hàng từ Reserve sang Picking.

- Quét mã vạch tại Reserve Location → Pick
- Di chuyển hàng đến Picking Location
- Quét mã vạch tại Picking Location → Confirm
- Hệ thống cập nhật Qty tại cả hai Location

## Outputs
### Replenishment Rules
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| SKU | Picking Location | Min | Max | Replenish Qty | Reserve Source |
|---|---|---|---|---|---|
| SKU-A01 | A-01-01 | 20 | 100 | 80 | R-05-03 |
| SKU-B02 | A-02-05 | 10 | 50 | 40 | R-08-01 |
```

## Sub-Skills (Kỹ năng con)
- Thiết kế Min-Max Rules
- Thiết kế Safety Stock Calculation

## Business Rules
- BR-WMS-REP-01: Replenishment phải hoàn thành trước khi hết hàng tại Picking (Prevent stockout).
- BR-WMS-REP-02: Ưu tiên Replenish SKU đang có SO chờ trước.
- BR-WMS-REP-03: Không Replenish quá Max Level.

## Edge Cases & Exceptions
- Reserve cũng hết hàng → Trigger PO cho NCC
- Nhiều Picking Location cùng SKU đều cần Replenish → Ưu tiên Location nào?

## Checklist
- [ ] Đã thiết kế Min/Max cho từng SKU
- [ ] Đã có trigger tự động khi chạm Min
- [ ] Đã có logic tính Safety Stock (dựa trên Lead Time + Demand Variability)
- [ ] Đã có fallback khi Reserve hết hàng

## Example
Xem Process.

## Related Skills
- Phân tích Inventory Management
- Phân tích Outbound Flow
