# Thiết kế Dashboard

## Level
Level 2 - Business Skill

## Purpose
Thiết kế Dashboard quản trị cho hệ thống doanh nghiệp bao gồm: xác định đúng KPI cho từng vai trò (Role), chọn đúng loại biểu đồ (Chart Type), bố trí layout theo nguyên tắc Information Hierarchy, thiết kế bộ lọc (Filter) và drill-down chi tiết.

## When to Use
Sử dụng khi cần thiết kế trang Dashboard cho bất kỳ module nào (CRM, WMS, MES, HRM, Finance...).

## Prerequisites
- Hiểu nghiệp vụ của module cần Dashboard
- Biết các loại biểu đồ cơ bản

## Inputs
### Module & Vai trò người xem
- **Mô tả:** Dashboard cho module nào và ai xem.
- **Bắt buộc:** Có
- **Ví dụ:** Module: WMS. Người xem: Quản lý kho muốn thấy tổng quan tồn kho, hiệu suất xuất nhập, cảnh báo hết hàng.

### KPI / Metrics cần theo dõi
- **Mô tả:** Các chỉ số quan trọng cần hiển thị.
- **Bắt buộc:** Có
- **Ví dụ:** Số lượng xuất kho hôm nay, Tỷ lệ chính xác Picking, Top 10 SKU bán chạy, Cảnh báo hàng sắp hết.

### Nguồn dữ liệu
- **Mô tả:** Dữ liệu lấy từ bảng/API nào.
- **Bắt buộc:** Không
- **Ví dụ:** Bảng orders, inventory, picking_logs.

## Process
### Bước 1: Xác định KPI theo vai trò
Mỗi vai trò (Role) cần những KPI khác nhau.

- CEO/Director: Tổng doanh thu, Lợi nhuận, So sánh kỳ trước, Dự báo
- Manager: Hiệu suất team, Tỷ lệ hoàn thành, Cảnh báo bất thường
- Operator: Tác vụ cần làm hôm nay, Trạng thái công việc đang xử lý
- Quy tắc: Cấp càng cao → Tổng hợp hơn. Cấp càng thấp → Chi tiết thao tác.

### Bước 2: Chọn đúng loại biểu đồ (Chart Type)
Mỗi loại dữ liệu phù hợp với 1 loại biểu đồ cụ thể.

- So sánh giá trị → Bar Chart (Doanh thu theo tháng, Tồn kho theo kho)
- Xu hướng theo thời gian → Line Chart (Doanh thu 12 tháng, OEE theo tuần)
- Tỷ lệ phần trăm → Pie/Donut Chart (Tỷ lệ Lead theo nguồn) - CHỈ dùng khi ≤ 5 phần
- Tiến độ → Gauge Chart (OEE %, SLA Compliance %)
- Bảng xếp hạng → Table / Horizontal Bar (Top 10 SKU, Top 5 Sales)
- Phân bố địa lý → Map Chart (Doanh thu theo vùng)
- Số đơn lẻ nổi bật → KPI Card / Metric Tile (Tổng đơn hàng hôm nay: 152)
- KHÔNG dùng 3D chart, KHÔNG dùng Pie cho > 5 categories

### Bước 3: Thiết kế Layout (Bố cục)
Sắp xếp các widget theo nguyên tắc Information Hierarchy.

- Row 1 (Top): KPI Cards - Các chỉ số tổng quan quan trọng nhất (4-6 cards)
- Row 2 (Middle): Charts chính - Biểu đồ xu hướng và so sánh
- Row 3 (Bottom): Tables chi tiết - Danh sách cần hành động (Alerts, Tasks)
- Sidebar/Top: Bộ lọc (Date Range, Warehouse, Product Category...)
- Quy tắc: Thông tin quan trọng nhất → Góc trên bên trái (Eye Tracking F-pattern)

### Bước 4: Thiết kế bộ lọc (Filters)
Cho phép người dùng lọc dữ liệu theo nhiều tiêu chí.

- Date Range Picker: Hôm nay, Tuần này, Tháng này, Quý này, Tùy chọn
- Filter theo đơn vị: Kho, Chi nhánh, Phòng ban
- Filter theo danh mục: Nhóm sản phẩm, Loại đơn hàng
- Global Filter: Áp dụng cho tất cả widget trên Dashboard
- Quick Filter: Preset buttons (Hôm nay, 7 ngày, 30 ngày)

### Bước 5: Thiết kế Drill-down & Action
Cho phép click vào chart để xem chi tiết.

- Click vào Bar → Xem danh sách chi tiết đằng sau số liệu
- Click vào KPI Card đỏ (cảnh báo) → Xem danh sách items bất thường
- Click vào hàng trong Table → Mở trang chi tiết
- Auto-refresh: Dashboard tự cập nhật mỗi 30s-5p (tùy module)

## Outputs
### Dashboard Specification
- **Định dạng:** Markdown Document
- **Mẫu:**

```
# Dashboard Specification: [Tên Module]

## Target User: [Role]

## KPI Cards (Row 1)
| # | KPI | Biểu đồ | Nguồn dữ liệu | Drill-down |
|---|---|---|---|---|
| 1 | Tổng đơn hàng hôm nay | KPI Card (số) | orders WHERE date = today | Danh sách đơn |
| 2 | Tỷ lệ Pick chính xác | Gauge (%) | picking_logs | Chi tiết lỗi |
| 3 | Cảnh báo hết hàng | KPI Card (đỏ) | inventory WHERE qty < min | Danh sách SKU |

## Charts (Row 2)
| # | Tên Chart | Loại | Dữ liệu | Filter |
|---|---|---|---|---|
| 1 | Xu hướng xuất nhập 30 ngày | Line Chart | Nhập (xanh) + Xuất (cam) | Date range |
| 2 | Tồn kho theo Zone | Stacked Bar | Qty by zone | Warehouse |

## Tables (Row 3)
| # | Tên | Columns | Sort | Action |
|---|---|---|---|---|
| 1 | Đơn hàng chờ Picking | SO#, Khách, Items, Priority | Priority DESC | Click → Pick |

## Filters
- Date Range (Default: Hôm nay)
- Warehouse (Default: Tất cả)
```

### Chart Type Guide
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| Mục đích | Chart Type | Ví dụ |
|---|---|---|
| Giá trị đơn lẻ | KPI Card | Tổng doanh thu: 5.2 tỷ |
| So sánh | Bar Chart | Doanh thu theo chi nhánh |
| Xu hướng | Line Chart | Doanh thu 12 tháng |
| Tỷ lệ (≤5 phần) | Donut Chart | Trạng thái đơn hàng |
| Tiến độ % | Gauge Chart | OEE = 78% |
| Xếp hạng | Horizontal Bar | Top 10 sản phẩm |
```

## Sub-Skills (Kỹ năng con)
- Chọn Chart Type phù hợp
- Thiết kế KPI Cards
- Thiết kế Dashboard Layout
- Thiết kế Drill-down

## Business Rules
- BR-DASH-01: Dashboard PHẢI load trong 3 giây hoặc ít hơn.
- BR-DASH-02: KHÔNG dùng Pie Chart cho > 5 categories.
- BR-DASH-03: KHÔNG dùng 3D chart (Gây hiểu sai dữ liệu).
- BR-DASH-04: KPI Card cảnh báo phải dùng màu đỏ/vàng rõ ràng.
- BR-DASH-05: Mỗi Dashboard phải có ít nhất 1 bộ lọc Date Range.
- BR-DASH-06: Dữ liệu Dashboard phải realtime hoặc near-realtime (< 5 phút).

## Edge Cases & Exceptions
- Không có dữ liệu (mới triển khai) → Hiển thị 'Chưa có dữ liệu' thay vì chart trống
- Dữ liệu quá lớn → Giới hạn Top N hoặc phân trang
- Người dùng có 2 Role → Dashboard nào? (Hiển thị Dashboard theo Role cao nhất)

## Checklist
- [ ] Đã xác định KPI theo vai trò (Role-based)?
- [ ] Đã chọn đúng Chart Type cho mỗi KPI?
- [ ] Đã bố trí Layout theo F-pattern (Quan trọng nhất → Góc trên trái)?
- [ ] Đã có bộ lọc Date Range + các filter phù hợp?
- [ ] Đã có Drill-down khi click vào chart?
- [ ] Đã có cảnh báo (Alert) bằng màu sắc?
- [ ] Đã có Auto-refresh?
- [ ] Dashboard load < 3 giây?

## Example
Xem Dashboard Specification template trong Outputs.

## Related Skills
- Thiết kế module
- Phân tích Báo cáo động
- Thiết kế Role-based UI
