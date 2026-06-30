# Phân tích Payroll

## Level
Level 2 - Business Skill

## Purpose
Phân tích toàn diện luồng tính lương nhân viên, từ thu thập dữ liệu công đến ra bảng lương cuối cùng, bao gồm tính lương cơ bản, phụ cấp, thưởng, khấu trừ thuế TNCN, BHXH/BHYT/BHTN, và quy trình duyệt + phát lương.

## When to Use
Sử dụng khi xây dựng module Payroll cho hệ thống HRM.

## Prerequisites
- Đã phân tích Chấm công
- Hiểu Luật Thuế TNCN và BHXH Việt Nam

## Inputs
### Bảng công đã duyệt
- **Mô tả:** Dữ liệu chấm công tổng hợp cuối tháng.
- **Bắt buộc:** Có
- **Ví dụ:** NV Nguyễn Văn A: 22 ngày đi làm, 8 giờ OT ngày thường, 4 giờ OT ngày nghỉ.

### Cấu trúc lương
- **Mô tả:** Các thành phần cấu thành thu nhập.
- **Bắt buộc:** Có
- **Ví dụ:** Lương cơ bản: 15tr. Phụ cấp ăn: 730k. Phụ cấp xăng: 500k. Phụ cấp điện thoại: 300k.

### Bảng thuế TNCN & BHXH
- **Mô tả:** Biểu thuế lũy tiến và tỷ lệ đóng BHXH.
- **Bắt buộc:** Có
- **Ví dụ:** Thuế TNCN: 0-5tr = 5%, 5-10tr = 10%, 10-18tr = 15%... BHXH: NV đóng 10.5%, DN đóng 21.5%.

## Process
### Bước 1: Thu thập dữ liệu đầu vào
Gom tất cả dữ liệu cần thiết cho tính lương.

- Bảng công đã duyệt (từ module Chấm công)
- Dữ liệu OT đã duyệt
- Phụ cấp đặc biệt tháng này (Thưởng dự án, Hoa hồng Sales...)
- Khấu trừ đặc biệt (Tạm ứng lương, Phạt, Đền bù...)
- Thay đổi nhân sự: Nhân viên mới (tính theo ngày thực tế), Nhân viên nghỉ việc

### Bước 2: Tính lương Gross (Tổng thu nhập)
Tính toàn bộ thu nhập trước thuế.

- Lương cơ bản theo ngày: (Lương tháng / 26 ngày) × Số ngày đi làm
- Lương OT: Ngày thường × 150%, Ngày nghỉ × 200%, Ngày lễ × 300%
- Phụ cấp cố định: Ăn trưa, Xăng xe, Điện thoại, Chức vụ
- Thu nhập không thường xuyên: Thưởng, Hoa hồng, Phúc lợi
- Gross Salary = Lương cơ bản + OT + Phụ cấp + Thưởng

### Bước 3: Tính khấu trừ (Deductions)
Tính các khoản phải trừ theo luật.

- BHXH (8%): Tính trên mức lương đóng BH (có mức trần = 20 × lương cơ sở)
- BHYT (1.5%): Tính trên mức lương đóng BH
- BHTN (1%): Tính trên mức lương đóng BH
- Tổng BH nhân viên đóng = 10.5% × Lương đóng BH
- Thuế TNCN: Thu nhập chịu thuế = Gross - BH - Giảm trừ bản thân (11tr) - Giảm trừ người phụ thuộc (4.4tr/người)
- Áp biểu thuế lũy tiến từng phần (7 bậc: 5%, 10%, 15%, 20%, 25%, 30%, 35%)
- Khấu trừ khác: Tạm ứng, Phạt, Hoàn ứng công tác

### Bước 4: Tính lương Net (Thực nhận)
Tính số tiền nhân viên thực nhận.

- Net Salary = Gross Salary - BHXH/BHYT/BHTN - Thuế TNCN - Khấu trừ khác
- Kiểm tra: Net Salary > 0 (Nếu < 0 → Cảnh báo bất thường)
- Làm tròn đến hàng nghìn đồng

### Bước 5: Duyệt và Phát lương
Luồng phê duyệt và thanh toán.

- HR tạo bảng lương → Kế toán trưởng review → Giám đốc phê duyệt
- Sau khi duyệt: Tạo file chuyển khoản hàng loạt (Bank Transfer File)
- In phiếu lương (Payslip) gửi cho từng nhân viên
- Lock bảng lương (không cho chỉnh sửa) sau khi phát lương
- Lưu trữ hồ sơ lương ít nhất 5 năm theo quy định

## Outputs
### Bảng lương chi tiết
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| Mục | Công thức | NV Nguyễn Văn A |
|---|---|---|
| Lương cơ bản | 15tr / 26 × 22 ngày | 12,692,308 |
| OT ngày thường | (15tr/26/8) × 8h × 150% | 865,385 |
| OT ngày nghỉ | (15tr/26/8) × 4h × 200% | 576,923 |
| Phụ cấp ăn | Cố định | 730,000 |
| Phụ cấp xăng | Cố định | 500,000 |
| **Gross** | | **15,364,616** |
| BHXH (8%) | 15tr × 8% | -1,200,000 |
| BHYT (1.5%) | 15tr × 1.5% | -225,000 |
| BHTN (1%) | 15tr × 1% | -150,000 |
| Giảm trừ bản thân | | -11,000,000 |
| Thu nhập chịu thuế | 15,364,616 - 1,575,000 - 11,000,000 | 2,789,616 |
| Thuế TNCN (5%) | 2,789,616 × 5% | -139,481 |
| **Net Salary** | | **13,650,135** |
```

### Payslip Template
- **Định dạng:** Markdown
- **Mẫu:**

```
# PHIẾU LƯƠNG THÁNG [MM/YYYY]

**Nhân viên:** [Tên]
**Mã NV:** [Mã]
**Phòng ban:** [PB]

| Thu nhập | Số tiền | Khấu trừ | Số tiền |
|---|---|---|---|
| Lương cơ bản | xxx | BHXH | xxx |
| OT | xxx | BHYT | xxx |
| Phụ cấp | xxx | BHTN | xxx |
| Thưởng | xxx | Thuế TNCN | xxx |
| **Tổng thu nhập** | **xxx** | **Tổng khấu trừ** | **xxx** |

**THỰC NHẬN: xxx VNĐ**
```

## Sub-Skills (Kỹ năng con)
- Tính OT theo Luật LĐ
- Tính Thuế TNCN lũy tiến
- Tính BHXH/BHYT/BHTN
- Thiết kế Payslip

## Business Rules
- BR-HRM-PAY-01: Lương OT ngày thường = 150%, ngày nghỉ = 200%, ngày lễ = 300%.
- BR-HRM-PAY-02: Thuế TNCN tính theo biểu lũy tiến từng phần 7 bậc.
- BR-HRM-PAY-03: Mức lương đóng BHXH không vượt quá 20 × lương cơ sở (hiện tại 1,800,000 × 20 = 36,000,000).
- BR-HRM-PAY-04: Giảm trừ bản thân = 11,000,000 VNĐ/tháng. Giảm trừ người phụ thuộc = 4,400,000/người/tháng.
- BR-HRM-PAY-05: Bảng lương phải được duyệt bởi ít nhất 2 cấp trước khi phát lương.

## Edge Cases & Exceptions
- Nhân viên vào giữa tháng → Tính lương pro-rata theo ngày thực tế
- Nhân viên nghỉ thai sản → Hưởng BHXH thay vì lương công ty
- Nhân viên có thu nhập từ nhiều nơi → Quyết toán thuế cuối năm
- Thay đổi mức lương giữa tháng → Chia 2 giai đoạn tính lương

## Checklist
- [ ] Đã tính lương cơ bản theo ngày công thực tế
- [ ] Đã tính OT đúng hệ số (150%, 200%, 300%)
- [ ] Đã trừ BHXH/BHYT/BHTN đúng tỷ lệ
- [ ] Đã tính thuế TNCN theo biểu lũy tiến
- [ ] Đã áp dụng giảm trừ bản thân + người phụ thuộc
- [ ] Đã có luồng duyệt bảng lương
- [ ] Đã thiết kế Payslip template
- [ ] Đã có file chuyển khoản hàng loạt cho ngân hàng
- [ ] Đã lock bảng lương sau khi phát

## Example
Xem Bảng lương chi tiết và Payslip Template trong Outputs.

## Related Skills
- Phân tích Chấm công
- Phân tích KPI và Đánh giá
