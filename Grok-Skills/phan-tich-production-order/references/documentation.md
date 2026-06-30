# Phân tích Production Order

## Level
Level 2 - Business Skill

## Purpose
Phân tích toàn diện quy trình tạo và quản lý lệnh sản xuất (Production Order / Work Order), từ khi nhận kế hoạch sản xuất đến khi thành phẩm nhập kho, bao gồm kiểm tra vật tư (Material Availability), định mức sản xuất (Routing/BOM), theo dõi tiến độ theo thời gian thực và xử lý phế phẩm (Scrap).

## When to Use
Sử dụng khi xây dựng hệ thống MES cho nhà máy sản xuất, từ nhà máy thực phẩm, cơ khí đến điện tử.

## Prerequisites
- Hiểu BOM (Bill of Materials)
- Hiểu Routing (Định mức công đoạn)

## Inputs
### Kế hoạch sản xuất (Production Plan)
- **Mô tả:** Số lượng thành phẩm cần sản xuất theo ngày/tuần/tháng.
- **Bắt buộc:** Có
- **Ví dụ:** Sản xuất 5000 chai nước suối 500ml trong tuần 28, chia 3 ca/ngày.

### BOM (Bill of Materials)
- **Mô tả:** Danh sách nguyên vật liệu cần cho 1 đơn vị thành phẩm.
- **Bắt buộc:** Có
- **Ví dụ:** 1 chai nước suối 500ml = 1 vỏ chai PET + 1 nắp + 500ml nước + 1 nhãn dán

### Routing (Định mức công đoạn)
- **Mô tả:** Các bước sản xuất và thời gian tiêu chuẩn.
- **Bắt buộc:** Có
- **Ví dụ:** Công đoạn 1: Thổi chai (5s/chai) → Công đoạn 2: Rót nước (3s) → Công đoạn 3: Đóng nắp (2s) → Công đoạn 4: Dán nhãn (2s) → Công đoạn 5: Đóng thùng (10s/12 chai)

## Process
### Bước 1: Tiếp nhận kế hoạch & Tạo Work Order
Chuyển kế hoạch sản xuất thành các Work Order cụ thể.

- Phân tách kế hoạch thành WO theo ngày/ca/máy
- Tính toán số lượng NVL cần dựa trên BOM (Bill of Materials Explosion)
- Kiểm tra tồn kho NVL (Material Availability Check)
- Nếu thiếu NVL → Tạo yêu cầu mua hàng (Purchase Requisition) hoặc chờ
- Gán WO cho dây chuyền/máy cụ thể

### Bước 2: Phát lệnh sản xuất (Release WO)
Xác nhận NVL đủ và phát lệnh xuống xưởng.

- Trạng thái WO: Planned → Released
- In phiếu lệnh sản xuất cho Quản đốc
- Xuất NVL từ kho sang dây chuyền (Material Issue)
- Ghi nhận thời gian bắt đầu sản xuất

### Bước 3: Theo dõi tiến độ (Production Tracking)
Ghi nhận số lượng sản xuất theo thời gian thực.

- Nhân viên quét barcode hoặc hệ thống IoT tự động đếm sản phẩm tại mỗi công đoạn
- Dashboard hiển thị: Kế hoạch vs Thực tế (Planned vs Actual)
- Ghi nhận thời gian dừng máy (Downtime) và lý do
- Ghi nhận phế phẩm (Scrap/Reject) và lý do
- Cảnh báo nếu sản lượng thực tế < 80% kế hoạch

### Bước 4: Kiểm tra chất lượng (QC)
QC kiểm tra thành phẩm trước khi nhập kho.

- Lấy mẫu theo tỷ lệ quy định (AQL Sampling)
- Kiểm tra các chỉ tiêu: Ngoại quan, Kích thước, Trọng lượng, Chức năng
- Pass → Chuyển sang nhập kho thành phẩm
- Fail → Rework (Sửa chữa) hoặc Scrap (Tiêu hủy)

### Bước 5: Hoàn thành & Nhập kho thành phẩm
Đóng Work Order và nhập hàng vào kho thành phẩm.

- Ghi nhận số lượng thực sản xuất (Good Qty + Scrap Qty)
- Trả NVL dư về kho (Material Return)
- Tính chi phí sản xuất thực tế (Actual Cost vs Standard Cost)
- Tạo phiếu nhập kho thành phẩm (Finished Goods Receipt)
- Trạng thái WO: Released → Completed

## Outputs
### Luồng Production Order
- **Định dạng:** Mermaid Flowchart
- **Mẫu:**

```
graph TD
    A[Nhận kế hoạch] --> B[Tạo Work Order]
    B --> C{NVL đủ?}
    C -->|Có| D[Release WO]
    C -->|Không| E[Tạo PR mua NVL]
    E --> C
    D --> F[Xuất NVL cho sản xuất]
    F --> G[Sản xuất & Tracking]
    G --> H[QC kiểm tra]
    H -->|Pass| I[Nhập kho thành phẩm]
    H -->|Fail| J[Rework / Scrap]
    I --> K[Đóng WO]
```

### Cấu trúc dữ liệu Work Order
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| Trường | Kiểu | Mô tả |
|---|---|---|
| wo_id | INT (PK) | Mã lệnh SX |
| product_id | INT (FK) | Thành phẩm |
| planned_qty | DECIMAL | SL kế hoạch |
| actual_qty | DECIMAL | SL thực tế |
| scrap_qty | DECIMAL | SL phế phẩm |
| start_date | DATETIME | Ngày bắt đầu |
| end_date | DATETIME | Ngày kết thúc |
| status | ENUM | Planned/Released/In Progress/Completed |
| machine_id | INT (FK) | Máy/Dây chuyền |
| shift | ENUM | Ca 1/2/3 |
```

### BOM Explosion
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| NVL | Đơn vị | Qty/TP | WO Qty | Tổng NVL cần | Tồn kho | Thiếu |
|---|---|---|---|---|---|---|
| Vỏ chai PET | Cái | 1 | 5000 | 5000 | 6000 | 0 |
| Nắp chai | Cái | 1 | 5000 | 5000 | 4500 | 500 |
```

## Sub-Skills (Kỹ năng con)
- Thiết kế BOM Structure
- Thiết kế Routing
- Thiết kế Production Dashboard
- Thiết kế Scrap Management

## Business Rules
- BR-MES-WO-01: Không được Release WO nếu NVL không đủ.
- BR-MES-WO-02: Scrap Rate > 5% phải có điều tra nguyên nhân.
- BR-MES-WO-03: WO phải ghi nhận chính xác ca làm việc và máy sản xuất.
- BR-MES-WO-04: NVL dư sau khi hoàn thành WO phải được trả về kho.
- BR-MES-WO-05: Chi phí thực tế chênh lệch > 10% so với Standard Cost phải báo cáo cho Kế toán.

## Edge Cases & Exceptions
- Máy hỏng giữa chừng → Chuyển WO sang máy khác hay chờ sửa?
- NVL nhận từ NCC không đạt QC → WO phải chờ hay dùng NVL thay thế?
- Khách hàng đột ngột thay đổi số lượng → Điều chỉnh WO mid-production

## Checklist
- [ ] Đã thiết kế BOM đa cấp (Multi-level BOM)
- [ ] Đã có Material Availability Check trước khi Release
- [ ] Đã theo dõi sản lượng realtime (IoT/Manual)
- [ ] Đã ghi nhận Downtime với lý do
- [ ] Đã ghi nhận Scrap với lý do
- [ ] Đã tích hợp QC tại cuối dây chuyền
- [ ] Đã tính toán Actual Cost vs Standard Cost
- [ ] Đã có Dashboard: Planned vs Actual

## Example
Xem Process section.

## Related Skills
- Phân tích OEE
- Phân tích Quality Control
- Phân tích Inbound Flow
