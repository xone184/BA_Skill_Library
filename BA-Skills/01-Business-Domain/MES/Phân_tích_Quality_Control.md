# Phân tích Quality Control

## Level
Level 2 - Business Skill

## Purpose
Phân tích toàn diện quy trình quản lý chất lượng trong sản xuất, từ IQC (Incoming), PQC (Process), OQC (Outgoing), bao gồm tiêu chuẩn lấy mẫu (AQL), xử lý hàng lỗi (Rework/Scrap) và truy xuất nguồn gốc (Traceability).

## When to Use
Sử dụng khi nhà máy cần hệ thống QC chuyên nghiệp.

## Prerequisites
- Đã phân tích Production Order

## Inputs
### Tiêu chuẩn chất lượng (Quality Standards)
- **Mô tả:** Các chỉ tiêu kiểm tra cho từng sản phẩm.
- **Bắt buộc:** Có
- **Ví dụ:** Chai nước: Dung tích 500ml ± 5ml, Nắp đóng chặt (lực xoay > 2Nm), Nhãn dán ngay ngắn

### AQL Level (Acceptable Quality Level)
- **Mô tả:** Tỷ lệ lỗi chấp nhận được.
- **Bắt buộc:** Có
- **Ví dụ:** AQL = 1.0 (Major), AQL = 2.5 (Minor)

### Quy trình sản xuất
- **Mô tả:** Các công đoạn cần kiểm tra.
- **Bắt buộc:** Có
- **Ví dụ:** IQC: Kiểm NVL đầu vào. PQC: Kiểm tại mỗi công đoạn. OQC: Kiểm thành phẩm trước khi nhập kho.

## Process
### Bước 1: IQC - Kiểm tra NVL đầu vào (Incoming QC)
Kiểm tra chất lượng nguyên vật liệu từ NCC trước khi đưa vào sản xuất.

- Lấy mẫu theo AQL (VD: Lô 1000 chai → Kiểm 80 chai)
- Kiểm tra ngoại quan, kích thước, chức năng
- Pass → Nhận hàng. Fail → Reject hoặc Nhận có điều kiện
- Ghi nhận kết quả QC vào hồ sơ NCC (Vendor Scorecard)

### Bước 2: PQC - Kiểm tra trong quá trình (Process QC)
Kiểm tra tại các công đoạn sản xuất then chốt.

- Kiểm tra đầu ca (First Piece Inspection)
- Kiểm tra định kỳ (Hourly/Per Batch)
- Kiểm tra khi chuyển đổi sản phẩm (Changeover Inspection)
- Nếu phát hiện lỗi → Dừng dây chuyền (Stop the Line) nếu Critical

### Bước 3: OQC - Kiểm tra thành phẩm (Outgoing QC)
Kiểm tra lô thành phẩm trước khi nhập kho hoặc xuất cho khách.

- Lấy mẫu theo AQL
- Kiểm tra đầy đủ tiêu chí
- Pass → Nhập kho thành phẩm
- Fail → Giữ lại (Hold) để điều tra

### Bước 4: Xử lý hàng lỗi (NCR - Non-Conformance Report)
Quy trình khi phát hiện sản phẩm không đạt.

- Tạo NCR (Non-Conformance Report) mô tả lỗi chi tiết
- Phân loại: Rework (Sửa lại), Scrap (Tiêu hủy), Downgrade (Hạ cấp)
- Rework → Sửa → QC lại → Nếu Pass thì nhập kho
- Scrap → Ghi nhận tiêu hủy, tính vào chi phí
- Truy tìm nguyên nhân gốc (Root Cause) để ngăn tái diễn

## Outputs
### Quy trình QC (BPMN)
- **Định dạng:** Mermaid Flowchart
### Ma trận tiêu chí QC
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| Giai đoạn | Đối tượng | Tiêu chí | Phương pháp | AQL |
|---|---|---|---|---|
| IQC | Vỏ chai PET | Kích thước, Độ trong | Đo + Visual | 1.0 |
| PQC | Chai đã rót | Dung tích ± 5ml | Cân | - |
| OQC | Thành phẩm | Toàn bộ | Lấy mẫu | 2.5 |
```

## Sub-Skills (Kỹ năng con)
- Thiết kế AQL Sampling Plan
- Thiết kế NCR Workflow
- Thiết kế Vendor Scorecard
- Thiết kế Traceability

## Business Rules
- BR-MES-QC-01: Mọi lô hàng phải qua QC trước khi nhập kho thành phẩm.
- BR-MES-QC-02: Lỗi Critical phải dừng dây chuyền ngay lập tức.
- BR-MES-QC-03: Hàng Rework chỉ được phép Rework tối đa 1 lần.
- BR-MES-QC-04: NCR phải được điều tra Root Cause trong 48 giờ.
- BR-MES-QC-05: NCC có tỷ lệ lỗi IQC > 5% phải đánh giá lại hợp đồng.

## Edge Cases & Exceptions
- Hàng Rework lại fail lần 2 → Bắt buộc Scrap
- Lỗi chỉ phát hiện khi hàng đã giao cho khách → Recall (Thu hồi)
- QC không đồng ý nhưng Production ép xuất hàng → Escalation

## Checklist
- [ ] Đã thiết kế IQC, PQC, OQC
- [ ] Đã có AQL Sampling Plan
- [ ] Đã có NCR Workflow
- [ ] Đã có luồng Rework và giới hạn số lần
- [ ] Đã có Traceability (Truy xuất lô sản phẩm)
- [ ] Đã tích hợp kết quả QC với OEE (Quality factor)

## Example
Xem Process section.

## Related Skills
- Phân tích Production Order
- Phân tích OEE
- Root Cause Analysis
