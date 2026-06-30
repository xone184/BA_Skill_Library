# Phân tích Inbound Flow

## Level
Level 2 - Business Skill

## Purpose
Phân tích toàn diện quy trình nhập kho hàng hóa, từ lúc nhận thông báo giao hàng (ASN) đến khi hàng được cất lên kệ (Putaway), bao gồm kiểm tra chất lượng đầu vào, xử lý chênh lệch so với PO, in mã vạch/QR code và chiến lược Putaway tự động.

## When to Use
Sử dụng khi:
- Xây dựng module Nhập kho cho hệ thống WMS.
- Cần tối ưu hóa quy trình nhận hàng tại dock.
- Cần thiết kế chiến lược cất hàng (Putaway Strategy) tự động.

## Prerequisites
- Hiểu cơ bản về quản lý kho
- Biết các loại hàng hóa (Pallet, Thùng, Lẻ)

## Inputs
### Purchase Order (PO)
- **Mô tả:** Đơn đặt hàng từ module Mua hàng, chứa thông tin hàng cần nhận.
- **Bắt buộc:** Có
- **Ví dụ:** PO-2024-001: 100 thùng Sữa TH True Milk, 50 thùng Nước ngọt Pepsi

### Advance Shipping Notice (ASN)
- **Mô tả:** Thông báo giao hàng trước từ nhà cung cấp.
- **Bắt buộc:** Không
- **Ví dụ:** NCC ABC sẽ giao 100 thùng vào ngày 15/7, xe biển số 51C-12345

### Sơ đồ kho (Warehouse Layout)
- **Mô tả:** Bản đồ kho với các Zone, Aisle, Rack, Bin.
- **Bắt buộc:** Có
- **Ví dụ:** Zone A: Hàng khô. Zone B: Hàng lạnh. Zone C: Hàng nguy hiểm.

## Process
### Bước 1: Tiếp nhận thông báo giao hàng
Hệ thống nhận ASN từ NCC (qua API/Email/Nhập tay) và tạo lịch nhận hàng tại dock.

- Kiểm tra ASN có khớp với PO đang mở không
- Đặt lịch dock (Dock Scheduling) để tránh ùn tắc
- Thông báo cho bộ phận kho chuẩn bị nhân lực dỡ hàng
- In phiếu tiếp nhận hàng (Receiving Slip)

### Bước 2: Dỡ hàng & Kiểm đếm (Unloading & Tally)
Nhân viên kho dỡ hàng và kiểm đếm số lượng thực tế so với PO.

- Dỡ hàng từ xe tải vào khu vực Staging (Tạm)
- Quét mã vạch từng thùng/pallet (hoặc đếm thủ công nếu chưa có barcode)
- So khớp số lượng thực nhận vs số lượng trên PO
- Ghi nhận chênh lệch: Thừa (Overage), Thiếu (Shortage), Hư hỏng (Damage)
- Chụp ảnh làm bằng chứng nếu hàng bị hư hỏng

### Bước 3: Kiểm tra chất lượng đầu vào (QC Inbound)
Kiểm tra chất lượng hàng nhận theo tiêu chuẩn đã quy định.

- Kiểm tra hạn sử dụng (Expiry Date) cho hàng thực phẩm/dược phẩm
- Kiểm tra ngoại quan (Visual Inspection): Bao bì rách, ẩm ướt, biến dạng
- Lấy mẫu kiểm tra (Sampling) theo AQL nếu hàng sản xuất
- Quyết định: Accept (Nhận), Reject (Từ chối), Conditional Accept (Nhận có điều kiện)

### Bước 4: Tạo phiếu nhận hàng (Goods Receipt Note - GRN)
Ghi nhận chính thức hàng đã nhập kho vào hệ thống.

- Tạo GRN liên kết với PO
- Cập nhật tồn kho (Inventory) tức thì
- In tem mã vạch/QR code dán lên từng Pallet/Thùng nếu NCC chưa dán
- Ghi nhận Lot Number, Batch Number, Serial Number (nếu có)

### Bước 5: Cất hàng lên kệ (Putaway)
Di chuyển hàng từ khu vực Staging lên vị trí lưu trữ cố định trên kệ.

- Hệ thống gợi ý vị trí cất (Putaway Suggestion) dựa trên chiến lược
- Chiến lược Fixed Location: Mỗi SKU có vị trí cố định
- Chiến lược Random Location: Cất bất kỳ ô trống nào gần nhất
- Chiến lược Zone-based: Hàng nhanh (Fast-moving) → Zone gần lối ra, Hàng chậm → Zone xa
- Chiến lược FEFO: Hàng hết hạn sớm nhất cất ở vị trí dễ lấy nhất
- Nhân viên quét mã vạch tại vị trí cất để xác nhận (Putaway Confirmation)

## Outputs
### Quy trình Nhập kho (BPMN)
- **Định dạng:** Mermaid Flowchart
- **Mẫu:**

```
graph TD
    A[Nhận ASN] --> B[Đặt lịch Dock]
    B --> C[Dỡ hàng]
    C --> D[Kiểm đếm Tally]
    D --> E{Chênh lệch?}
    E -->|Không| F[QC Inbound]
    E -->|Có| G[Ghi nhận chênh lệch & Xử lý]
    G --> F
    F --> H{QC Pass?}
    H -->|Có| I[Tạo GRN + In tem]
    H -->|Không| J[Reject / Return NCC]
    I --> K[Putaway Suggestion]
    K --> L[Cất hàng & Confirm]
```

### Cấu trúc dữ liệu GRN
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| Trường | Kiểu | Mô tả |
|---|---|---|
| grn_id | INT (PK) | Mã phiếu nhận |
| po_id | INT (FK) | Liên kết PO |
| supplier_id | INT (FK) | Nhà cung cấp |
| received_date | DATETIME | Ngày nhận |
| status | ENUM | Draft/Confirmed/Cancelled |
| total_qty_ordered | DECIMAL | SL đặt |
| total_qty_received | DECIMAL | SL thực nhận |
| created_by | INT (FK) | Người tạo |
```

### Ma trận Putaway Strategy
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| Loại hàng | Chiến lược | Zone | Lý do |
|---|---|---|---|
| Fast-moving | Zone-based | A (gần dock) | Giảm di chuyển |
| Slow-moving | Random | C (xa dock) | Tối ưu diện tích |
| Có HSD | FEFO | B | Hết hạn sớm lấy trước |
| Nguy hiểm | Fixed | D (riêng biệt) | An toàn |
```

## Sub-Skills (Kỹ năng con)
- Thiết kế Dock Scheduling
- Thiết kế QC Inbound
- Thiết kế Putaway Strategy
- Thiết kế Barcode/Label

## Business Rules
- BR-WMS-IN-01: Không được nhập hàng nếu không có PO hoặc ASN.
- BR-WMS-IN-02: Hàng có HSD dưới 30% thời gian sử dụng → Từ chối nhận.
- BR-WMS-IN-03: Chênh lệch số lượng > 5% phải có phê duyệt của Quản lý kho.
- BR-WMS-IN-04: Mỗi Pallet/Thùng nhập kho phải có mã vạch trước khi Putaway.
- BR-WMS-IN-05: Hàng nguy hiểm (Dangerous Goods) chỉ được cất ở Zone riêng.
- BR-WMS-IN-06: Putaway phải hoàn thành trong vòng 4 giờ kể từ khi tạo GRN.

## Edge Cases & Exceptions
- NCC giao hàng không có trong PO (Unexpected Delivery) → Reject hay tạo PO bổ sung?
- Hàng bị hư hỏng 50% → Nhận phần tốt hay reject toàn bộ?
- Kho hết chỗ trống → Putaway đưa đi đâu? (Overflow handling)
- Mất điện khi đang scan → Dữ liệu có được lưu nháp không?
- NCC giao sai hàng (Wrong item) → Luồng xử lý Return to Vendor

## Checklist
- [ ] Đã thiết kế luồng tiếp nhận ASN
- [ ] Đã thiết kế Dock Scheduling
- [ ] Đã có quy trình kiểm đếm (Tally) và xử lý chênh lệch
- [ ] Đã có QC Inbound (Kiểm tra chất lượng đầu vào)
- [ ] Đã thiết kế in tem mã vạch/QR code
- [ ] Đã thiết kế chiến lược Putaway (Fixed/Random/Zone-based/FEFO)
- [ ] Đã có xử lý hàng hư hỏng (Damage handling)
- [ ] Đã có xử lý hàng thừa/thiếu so với PO
- [ ] Đã quản lý Lot/Batch/Serial Number
- [ ] Đã có thông báo cho Kế toán khi tạo GRN thành công

## Example
Xem Process section để biết chi tiết luồng nhập kho end-to-end.

## Related Skills
- Phân tích Outbound Flow
- Phân tích Inventory Management
- Phân tích Procurement
