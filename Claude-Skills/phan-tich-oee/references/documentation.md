# Phân tích OEE

## Level
Level 2 - Business Skill

## Purpose
Đo lường và phân tích hiệu quả thiết bị tổng thể (Overall Equipment Effectiveness), xác định 6 tổn thất lớn (Six Big Losses) và đề xuất giải pháp cải thiện.

## When to Use
Sử dụng khi nhà máy cần đo lường hiệu suất máy móc và tìm cách cải thiện sản lượng.

## Prerequisites
- Đã phân tích Production Order
- Hiểu các loại Downtime

## Inputs
### Dữ liệu máy móc (Machine Data)
- **Mô tả:** Thời gian chạy, thời gian dừng, lý do dừng.
- **Bắt buộc:** Có
- **Ví dụ:** Máy CNC-01: Tổng thời gian ca = 480p, Planned Downtime (nghỉ trưa) = 30p, Unplanned Downtime (hỏng máy) = 45p

### Dữ liệu sản xuất
- **Mô tả:** Số lượng sản phẩm sản xuất và Cycle Time.
- **Bắt buộc:** Có
- **Ví dụ:** Sản lượng = 350 sản phẩm, Cycle Time lý thuyết = 1p/sp, Cycle Time thực tế = 1.2p/sp

### Dữ liệu chất lượng
- **Mô tả:** Số lượng hàng tốt và hàng lỗi.
- **Bắt buộc:** Có
- **Ví dụ:** Hàng tốt = 340, Hàng lỗi = 10

## Process
### Bước 1: Thu thập dữ liệu 3 yếu tố
Thu thập Availability, Performance, Quality.

- Availability = (Planned Production Time - Unplanned Downtime) / Planned Production Time
- Planned Production Time = Total Time - Planned Downtime (nghỉ trưa, bảo trì kế hoạch)
- Performance = (Ideal Cycle Time × Total Pieces) / Operating Time
- Quality = Good Pieces / Total Pieces

### Bước 2: Tính toán OEE
OEE = Availability × Performance × Quality.

- Ví dụ: Availability = 90%, Performance = 85%, Quality = 97%
- OEE = 0.90 × 0.85 × 0.97 = 74.2%
- World-class OEE = 85%. Trung bình = 60%. Dưới 40% = Cần cải thiện gấp.

### Bước 3: Phân tích 6 tổn thất lớn (Six Big Losses)
Xác định nguyên nhân gây giảm OEE.

- Availability Losses: (1) Breakdowns (Hỏng máy), (2) Setup/Changeover (Chuyển đổi sản phẩm)
- Performance Losses: (3) Small Stops (Dừng ngắn), (4) Reduced Speed (Chạy chậm)
- Quality Losses: (5) Startup Rejects (Lỗi khởi động), (6) Production Rejects (Lỗi sản xuất)

### Bước 4: Đề xuất cải thiện
Dựa trên phân tích Six Big Losses, đề xuất giải pháp.

- Availability thấp → Tăng cường bảo trì phòng ngừa (Preventive Maintenance)
- Performance thấp → Rà soát Cycle Time, kiểm tra máy chạy không đúng tốc độ
- Quality thấp → Cải thiện quy trình QC, đào tạo Operator

## Outputs
### Bảng tính OEE
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| Yếu tố | Công thức | Giá trị | Ghi chú |
|---|---|---|---|
| Planned Production Time | 480p - 30p (nghỉ) | 450p | |
| Operating Time | 450p - 45p (hỏng máy) | 405p | |
| Availability | 405/450 | 90% | |
| Ideal Cycle Time | | 1p/sp | |
| Total Pieces | | 350 sp | |
| Performance | (1 × 350)/405 | 86.4% | |
| Good Pieces | | 340 sp | |
| Quality | 340/350 | 97.1% | |
| **OEE** | 90% × 86.4% × 97.1% | **75.5%** | Target: 85% |
```

### Dashboard OEE
- **Định dạng:** Mô tả chi tiết
- **Mẫu:**

```
Dashboard cần có:
- Gauge chart hiển thị OEE tổng
- Bar chart so sánh OEE theo máy
- Trend line OEE theo tuần/tháng
- Pareto chart: Top 5 lý do Downtime
- Breakdown: Availability / Performance / Quality
```

## Sub-Skills (Kỹ năng con)
- Thiết kế Downtime Tracking
- Thiết kế OEE Dashboard
- Six Big Losses Analysis

## Business Rules
- BR-MES-OEE-01: Chỉ sử dụng công thức chuẩn OEE = Availability × Performance × Quality.
- BR-MES-OEE-02: Planned Downtime (nghỉ trưa, bảo trì kế hoạch) KHÔNG tính vào mất Availability.
- BR-MES-OEE-03: Setup/Changeover time phải được ghi nhận riêng, không gộp vào Breakdown.
- BR-MES-OEE-04: OEE phải được tính cho từng máy, từng ca, từng sản phẩm.

## Edge Cases & Exceptions
- Máy chạy nhưng không có hàng để sản xuất (Starving) → Tính vào mất gì?
- Máy chạy nhưng không có người vận hành → Tính Availability hay Performance?
- Sản phẩm Rework (sửa lại) thành tốt → Tính vào Good hay Reject?

## Checklist
- [ ] Đã thu thập đủ 3 yếu tố: Availability, Performance, Quality
- [ ] Đã phân biệt Planned vs Unplanned Downtime
- [ ] Đã phân tích Six Big Losses
- [ ] Đã thiết kế Dashboard OEE
- [ ] Đã có Pareto chart cho Downtime reasons
- [ ] Đã so sánh OEE theo máy/ca/sản phẩm
- [ ] Đã đề xuất giải pháp cải thiện

## Example
Xem Bảng tính OEE trong Outputs.

## Related Skills
- Phân tích Production Order
- Phân tích Quality Control
- Root Cause Analysis
