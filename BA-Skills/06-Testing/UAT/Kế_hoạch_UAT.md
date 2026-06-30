# Kế hoạch UAT

## Level
Level 3 - Architecture Skill

## Purpose
Lập User Acceptance Testing (UAT) Plan để hướng dẫn Khách hàng (End Users) tự kiểm thử hệ thống trước khi Go-live. Đảm bảo UAT diễn ra suôn sẻ, đúng nghiệp vụ thực tế và nhận được Sign-off.

## When to Use
Sử dụng trước khi dự án/Sprint kết thúc và bàn giao cho khách hàng kiểm tra.

## Prerequisites
- Hệ thống đã qua Internal QA
- Đã có UAT Environment

## Inputs
### BRD / Scope
- **Mô tả:** Phạm vi các chức năng cần UAT.
- **Bắt buộc:** Có
- **Ví dụ:** UAT cho Phase 1: Inbound & Outbound WMS.

### Danh sách End Users
- **Mô tả:** Những người sẽ tham gia test.
- **Bắt buộc:** Có
- **Ví dụ:** Thủ kho, Quản lý kho, Kế toán kho.

## Process
### Bước 1: Chuẩn bị Kế hoạch UAT (UAT Plan)
Xác định Scope, Timeline, Participants.

- In-scope: Các module sẽ test
- Out-of-scope: Các tính năng chưa test hoặc thuộc Phase sau
- Timeline: Bắt đầu khi nào, kết thúc khi nào (VD: 15/07 - 20/07)
- Participants: Gán từng kịch bản cho đúng Role (Thủ kho test Nhập hàng, Kế toán test Báo cáo)

### Bước 2: Viết UAT Scenarios (Kịch bản nghiệp vụ)
Viết kịch bản theo luồng nghiệp vụ thực tế (End-to-end), không test từng nút lẻ.

- Thay vì test 'Tạo SO', viết kịch bản 'Nhận đơn từ KH → Tạo SO → Xuất kho → Giao hàng'
- Ngôn ngữ dùng trong UAT Scenario phải là ngôn ngữ business, KHÔNG dùng từ kỹ thuật (API, DB)
- Chuẩn bị dữ liệu mẫu (Test Data) thật giống thực tế

### Bước 3: Chuẩn bị Môi trường UAT
Setup hệ thống cho khách test.

- Cài đặt URL môi trường UAT (tách biệt với DEV/PROD)
- Tạo sẵn tài khoản cho từng End User
- Tạo sẵn Master Data (Sản phẩm, Khách hàng, Tồn kho ban đầu)

### Bước 4: Thực hiện UAT & Ghi nhận Issue
Quản lý quá trình test.

- Hướng dẫn (Kick-off) người dùng cách test và log lỗi
- Phân loại phản hồi: Bug (Làm sai yêu cầu) vs Change Request (Yêu cầu mới/đổi ý)
- Triage (Đánh giá Issue): Blocker (Sửa ngay), Minor (Sửa sau Go-live)

### Bước 5: UAT Sign-off
Nghiệm thu.

- Tỷ lệ Pass > 95% và không có Blocker/Critical bug → Sign-off
- Khách hàng ký biên bản nghiệm thu UAT (UAT Sign-off Document)
- Sẵn sàng Go-live

## Outputs
### UAT Plan
- **Định dạng:** Markdown Document
- **Mẫu:**

```
# UAT Plan: [Tên dự án]

## 1. Scope & Timeline
- **In-scope:** [Module]
- **Timeline:** [Dates]

## 2. Participants
| Tên | Role | Scope Test |
|---|---|---|
| Nguyễn Văn A | Thủ kho | Inbound, Outbound |
| Lê Thị B | Kế toán | Inventory, Report |

## 3. UAT Scenarios
| Kịch bản | Mô tả nghiệp vụ (End-to-End) | Role thực hiện | Trạng thái (Pass/Fail) | Ghi chú |
|---|---|---|---|---|
| UAT-01 | Quy trình nhập kho hoàn chỉnh: Tạo PO → Nhận hàng → QC → Putaway | Thủ kho + QC | | |
| UAT-02 | Trả hàng NCC: Lập phiếu trả → Xuất hàng → Cập nhật tồn | Kế toán kho | | |

## 4. Defect Management
- Công cụ báo lỗi: [Jira / Google Sheet]
- Tiêu chí ưu tiên: Blocker, High, Medium, Low

## 5. Sign-off Criteria
- 100% Blocker/High bugs được fix.
- Kịch bản Pass > 95%.
```

### UAT Sign-off Form
- **Định dạng:** Markdown Document
- **Mẫu:**

```
## BIÊN BẢN NGHIỆM THU UAT

- **Dự án:**
- **Ngày:**
- **Kết quả UAT:** [Số Pass] / [Tổng số]
- **Kết luận:** Đồng ý Go-live / Không đồng ý

**Đại diện Khách hàng (Ký tên):**
```

## Sub-Skills (Kỹ năng con)
- End-to-End Scenario Design
- Test Data Preparation
- Defect Triage (Phân loại lỗi)

## Business Rules
- BR-UAT-01: UAT Scenarios PHẢI mô tả theo luồng nghiệp vụ đầu cuối (End-to-end), không test module rời rạc.
- BR-UAT-02: Phải phân định rõ ràng giữa Bug và CR (Change Request) trong UAT.
- BR-UAT-03: KHÔNG Go-live nếu UAT chưa được Sign-off bởi Key User/Sponsor.

## Edge Cases & Exceptions
- Khách hàng log CR nhưng bảo là Bug → BA phải dùng SRS/BRD để đối chiếu và scope quản lý
- Khách hàng bận không chịu test → Đặt deadline cứng, 'auto sign-off' nếu không phản hồi sau X ngày (cần thỏa thuận trong hợp đồng)

## Checklist
- [ ] Đã có danh sách người test (Participants)?
- [ ] Đã viết UAT Scenarios dạng End-to-end?
- [ ] Scenarios có dễ hiểu với người không biết IT?
- [ ] Đã chuẩn bị Test Data (Master data)?
- [ ] Đã có công cụ/biểu mẫu để khách báo lỗi?
- [ ] Đã định nghĩa Sign-off Criteria?

## Example
Xem UAT Plan template trong Outputs.

## Related Skills
- Write BRD
- Viết Test Case
