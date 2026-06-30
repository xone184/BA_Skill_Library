# Phân tích Outbound Flow

## Level
Level 2 - Business Skill

## Purpose
Phân tích toàn diện quy trình xuất kho, từ lúc nhận lệnh xuất (Sales Order/Transfer Order) đến khi hàng rời kho, bao gồm các chiến lược Picking (Wave, Zone, Batch), đóng gói (Packing), kiểm tra xuất (Shipping Verification) và tích hợp đơn vị vận chuyển.

## When to Use
Sử dụng khi:
- Xây dựng module Xuất kho cho WMS.
- Cần tối ưu hóa năng suất nhặt hàng (Picking Productivity).
- Cần tích hợp với các hãng vận chuyển (GHN, GHTK, Viettel Post).

## Prerequisites
- Đã phân tích Inbound Flow
- Hiểu nguyên tắc FIFO/FEFO/LIFO

## Inputs
### Sales Order (SO) / Transfer Order
- **Mô tả:** Lệnh xuất hàng từ module Bán hàng hoặc Điều phối.
- **Bắt buộc:** Có
- **Ví dụ:** SO-2024-500: 20 thùng Sữa TH (Lot #L001, HSD 15/12/2024), giao cho KH ABC tại HCM

### Nguyên tắc xuất kho
- **Mô tả:** FIFO, FEFO, LIFO hoặc theo Lot/Batch chỉ định.
- **Bắt buộc:** Có
- **Ví dụ:** Hàng thực phẩm: FEFO (hết hạn sớm nhất xuất trước). Hàng công nghiệp: FIFO.

### Thông tin vận chuyển
- **Mô tả:** Đơn vị vận chuyển, địa chỉ giao, thời gian cắt đơn.
- **Bắt buộc:** Không
- **Ví dụ:** GHN, cut-off time 14:00 hàng ngày

## Process
### Bước 1: Tiếp nhận & Xác nhận lệnh xuất
Hệ thống nhận SO/Transfer Order và kiểm tra tồn kho khả dụng (Available Stock).

- Kiểm tra tồn kho đủ không (Available Qty >= Ordered Qty)
- Phân bổ tồn kho (Allocation/Reservation) để khóa hàng cho đơn này
- Nếu thiếu hàng: Partial shipment hay chờ đủ hàng? (Backorder handling)
- Tạo Wave (nhóm nhiều SO để xử lý cùng lúc) hoặc xử lý từng SO

### Bước 2: Lấy hàng (Picking)
Nhân viên kho di chuyển đến vị trí trên kệ và lấy đúng số lượng hàng.

- Hệ thống tạo Pick List (Danh sách lấy hàng) với vị trí cụ thể (Zone-Aisle-Rack-Bin)
- Áp dụng FIFO/FEFO để xác định lấy Lot/Batch nào trước
- Chiến lược Picking:
-   - Discrete Picking: 1 nhân viên xử lý 1 đơn → Chính xác nhưng chậm
-   - Batch Picking: 1 nhân viên gom nhiều đơn → Nhanh, giảm di chuyển
-   - Zone Picking: Mỗi nhân viên chỉ pick trong Zone được gán → Chuyên môn hóa
-   - Wave Picking: Gom nhiều đơn cùng Zone/cùng hãng vận chuyển → Tối ưu nhất
- Nhân viên quét mã vạch tại vị trí Pick để xác nhận (Pick Confirmation)
- Nếu hết hàng tại vị trí Pick → Trigger Replenishment

### Bước 3: Đóng gói (Packing)
Nhân viên đóng gói hàng vào thùng carton và dán nhãn vận chuyển.

- Kiểm tra lại số lượng & chủng loại hàng (Packing Verification)
- Chọn loại thùng carton phù hợp kích thước
- In phiếu giao hàng (Delivery Note) kèm trong thùng
- In nhãn vận chuyển (Shipping Label) với mã vạch tracking
- Cân trọng lượng thùng và ghi nhận vào hệ thống

### Bước 4: Xuất hàng (Shipping)
Giao hàng cho đơn vị vận chuyển.

- Tập kết thùng tại khu vực Staging Outbound theo hãng vận chuyển
- Quét mã vạch Shipping Label khi bàn giao cho tài xế
- In Biên bản giao nhận (Handover Form)
- Cập nhật trạng thái SO: Shipped
- Gửi thông tin tracking cho khách hàng (Email/SMS)

## Outputs
### Quy trình Xuất kho (BPMN)
- **Định dạng:** Mermaid Flowchart
- **Mẫu:**

```
graph TD
    A[Nhận SO] --> B{Tồn kho đủ?}
    B -->|Có| C[Allocation]
    B -->|Không| D[Backorder / Partial]
    C --> E[Tạo Pick List]
    E --> F[Picking - Quét mã vạch]
    F --> G[Packing - Đóng gói]
    G --> H[In Shipping Label]
    H --> I[Staging Outbound]
    I --> J[Bàn giao cho Vận chuyển]
    J --> K[Cập nhật Shipped]
```

### Ma trận Picking Strategy
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| Chiến lược | Phù hợp khi | Ưu điểm | Nhược điểm |
|---|---|---|---|
| Discrete | Ít đơn, hàng giá trị cao | Chính xác cao | Chậm, di chuyển nhiều |
| Batch | Nhiều đơn nhỏ cùng SKU | Nhanh | Cần phân loại sau pick |
| Zone | Kho lớn, nhiều Zone | Chuyên môn hóa | Cần tổng hợp cuối |
| Wave | Nhiều đơn cùng hãng vận chuyển | Tối ưu nhất | Phức tạp thiết lập |
```

### Cấu trúc Pick List
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| SO | SKU | Tên hàng | Qty | Location | Lot | Status |
|---|---|---|---|---|---|---|
| SO-001 | SKU-A01 | Sữa TH 1L | 20 | A-01-03-B02 | L001 | Pending |
```

## Sub-Skills (Kỹ năng con)
- Thiết kế Picking Strategy
- Thiết kế Packing Station
- Thiết kế Shipping Integration
- Thiết kế Backorder Logic

## Business Rules
- BR-WMS-OUT-01: Hàng thực phẩm bắt buộc xuất theo FEFO (hết hạn sớm lấy trước).
- BR-WMS-OUT-02: Không xuất hàng có HSD dưới 30 ngày cho khách hàng (trừ khi khách đồng ý).
- BR-WMS-OUT-03: Mỗi lần Pick phải quét mã vạch xác nhận đúng vị trí và đúng hàng.
- BR-WMS-OUT-04: Đơn hàng phải hoàn thành Packing trước cut-off time của hãng vận chuyển.
- BR-WMS-OUT-05: Partial Shipment phải được khách hàng đồng ý trước.

## Edge Cases & Exceptions
- Hàng hết tại vị trí Pick nhưng còn tại Reserve Zone → Trigger Replenishment hay pick từ Reserve?
- Khách yêu cầu giao hàng theo Lot chỉ định nhưng Lot đó đã cất ở vị trí khó lấy → Xử lý sao?
- Nhiều SO cùng 1 SKU nhưng tồn kho chỉ đủ 1 SO → Ưu tiên SO nào? (Priority rules)
- Picking nhầm hàng → Luồng xử lý Return-to-Shelf
- Hãng vận chuyển đến trễ → Hàng đã packed nằm ở Staging quá lâu

## Checklist
- [ ] Đã kiểm tra tồn kho trước khi tạo Pick List (Allocation)
- [ ] Đã thiết kế chiến lược Picking phù hợp (Discrete/Batch/Zone/Wave)
- [ ] Đã áp dụng nguyên tắc FIFO/FEFO cho Picking
- [ ] Đã thiết kế Packing Station với Verification
- [ ] Đã tích hợp in Shipping Label
- [ ] Đã thiết kế xử lý Backorder (Thiếu hàng)
- [ ] Đã có Replenishment trigger khi vị trí Pick hết hàng
- [ ] Đã có luồng bàn giao cho hãng vận chuyển
- [ ] Đã gửi thông tin tracking cho khách hàng

## Example
Xem Process section.

## Related Skills
- Phân tích Inbound Flow
- Phân tích Inventory Management
- Phân tích Replenishment
