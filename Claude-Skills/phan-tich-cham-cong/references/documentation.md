# Phân tích Chấm công

## Level
Level 2 - Business Skill

## Purpose
Phân tích toàn diện quy trình quản lý thời gian làm việc (Time & Attendance), bao gồm thiết lập ca làm việc (Shift), tích hợp máy chấm công, xử lý đi trễ/về sớm/vắng mặt, quản lý nghỉ phép (Leave Management) và tính làm thêm giờ (OT).

## When to Use
Sử dụng khi xây dựng module Chấm công cho HRM.

## Prerequisites
- Hiểu Luật Lao động Việt Nam về giờ làm việc và OT

## Inputs
### Cấu trúc ca làm việc
- **Mô tả:** Giờ vào/ra của các ca.
- **Bắt buộc:** Có
- **Ví dụ:** Ca Hành chính: 08:00-17:00 (nghỉ trưa 12:00-13:00). Ca 1: 06:00-14:00. Ca 2: 14:00-22:00. Ca 3: 22:00-06:00.

### Dữ liệu máy chấm công
- **Mô tả:** Log vào/ra từ máy vân tay, thẻ từ, Face ID.
- **Bắt buộc:** Có
- **Ví dụ:** Employee ID: E001, Check-in: 07:58, Check-out: 17:05, Machine: Cổng chính

### Chính sách nghỉ phép
- **Mô tả:** Số ngày phép/năm, điều kiện nghỉ.
- **Bắt buộc:** Có
- **Ví dụ:** 12 ngày phép năm (sau 12 tháng). Nghỉ ốm: Theo sổ BHXH. Nghỉ không lương: Tối đa 5 ngày/năm.

## Process
### Bước 1: Thiết lập Master Data
Cấu hình ca làm việc, lịch công ty, ngày lễ.

- Tạo các Shift với giờ vào/ra chính xác
- Cấu hình Tolerance (VD: Trễ ≤ 5 phút vẫn tính đúng giờ)
- Cấu hình ngày lễ, ngày nghỉ bù
- Gán ca cho từng nhân viên (Fixed Shift hoặc Rotating Shift)

### Bước 2: Thu thập & Xử lý dữ liệu chấm công
Đồng bộ dữ liệu từ máy chấm công về hệ thống.

- API/File sync từ máy chấm công mỗi 5-15 phút
- Ghép cặp Check-in / Check-out (Matching)
- Phát hiện bất thường: Chỉ có Check-in không có Check-out, hoặc ngược lại
- Tự động tính giờ làm việc thực tế
- So sánh với ca đã gán → Tính Trễ / Sớm / Vắng

### Bước 3: Quản lý nghỉ phép (Leave Management)
Quy trình đăng ký và phê duyệt nghỉ phép.

- Nhân viên tạo đơn nghỉ phép trên hệ thống (Loại phép, Ngày, Lý do)
- Quản lý duyệt → Trừ phép còn lại
- Đối soát với dữ liệu chấm công: Vắng mặt nhưng chưa có đơn → Cảnh báo
- Hệ thống hiển thị số ngày phép còn lại realtime

### Bước 4: Tính OT (Overtime)
Ghi nhận và phê duyệt làm thêm giờ.

- Đăng ký OT trước (Pre-approved) hoặc hệ thống tự phát hiện giờ dư
- OT ngày thường: x150%. OT ngày nghỉ: x200%. OT ngày lễ: x300%
- Giới hạn OT: Không quá 40h/tháng (theo Luật LĐ VN)
- Manager duyệt OT → Chuyển sang Payroll

### Bước 5: Tổng hợp bảng công
Tạo bảng công tổng hợp cuối tháng.

- Tổng hợp: Số ngày đi làm, Số ngày nghỉ phép, Số ngày vắng, Số giờ OT
- Quản lý xác nhận bảng công cho từng nhân viên
- HR duyệt bảng công tổng → Chuyển cho Payroll
- Lock bảng công (không cho sửa) sau khi duyệt

## Outputs
### Bảng công mẫu
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| Nhân viên | Ngày đi làm | Trễ (lần) | Vắng KP | Phép năm | OT (giờ) | Ghi chú |
|---|---|---|---|---|---|---|
| Nguyễn Văn A | 22 | 2 | 0 | 1 | 8 | |
| Trần Thị B | 20 | 0 | 1 | 2 | 12 | Vắng ngày 15 chưa có đơn |
```

## Sub-Skills (Kỹ năng con)
- Thiết kế Shift Management
- Thiết kế Leave Management
- Thiết kế OT Calculation
- Thiết kế Attendance Dashboard

## Business Rules
- BR-HRM-ATT-01: Trễ ≤ 5 phút không tính phạt. Trễ > 5 phút tính nửa công sáng.
- BR-HRM-ATT-02: Vắng không phép (Absent without Leave) > 3 ngày/tháng → Cảnh cáo.
- BR-HRM-ATT-03: OT phải được đăng ký/duyệt trước, không chấp nhận OT tự phát.
- BR-HRM-ATT-04: Bảng công phải được Lock sau ngày 5 của tháng tiếp theo.
- BR-HRM-ATT-05: Nhân viên Ca đêm (22:00-06:00) được phụ cấp đêm 30%.

## Edge Cases & Exceptions
- Máy chấm công hỏng → Cho phép chấm công thủ công (Manual Attendance)
- Nhân viên đi công tác không thể chấm công → Xử lý Business Trip Attendance
- Làm việc từ xa (WFH) → Chấm công bằng gì?
- Nhân viên quẹt thẻ hộ người khác → Gian lận chấm công (Buddy Punching)

## Checklist
- [ ] Đã thiết kế cấu trúc Ca làm việc (Shift)
- [ ] Đã tích hợp máy chấm công (API/File)
- [ ] Đã xử lý ghép cặp Check-in/Check-out
- [ ] Đã có quy tắc tính Trễ/Sớm/Vắng
- [ ] Đã thiết kế Leave Management (Đăng ký, Duyệt, Trừ phép)
- [ ] Đã thiết kế OT Registration & Approval
- [ ] Đã tổng hợp bảng công cuối tháng
- [ ] Đã có chống gian lận chấm công

## Example
Xem bảng công mẫu trong Outputs.

## Related Skills
- Phân tích Payroll
- Phân tích KPI và Đánh giá
