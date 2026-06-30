# Phân tích Tuyển dụng

## Level
Level 2 - Business Skill

## Purpose
Phân tích toàn diện quy trình Applicant Tracking System (ATS), từ tạo yêu cầu tuyển dụng (Job Requisition) đến Onboarding nhân viên mới, bao gồm quản lý Pipeline ứng viên, đánh giá phỏng vấn, và Talent Pool.

## When to Use
Sử dụng khi xây dựng module Tuyển dụng cho HRM.

## Prerequisites
- Hiểu quy trình tuyển dụng doanh nghiệp

## Inputs
### Yêu cầu tuyển dụng (Job Requisition)
- **Mô tả:** Phiếu đề xuất tuyển dụng từ trưởng phòng.
- **Bắt buộc:** Có
- **Ví dụ:** Phòng IT đề xuất tuyển 2 Backend Developer, mức lương 20-30tr, kinh nghiệm 3 năm Java.

### Kênh tuyển dụng
- **Mô tả:** Các kênh đăng tin tuyển dụng.
- **Bắt buộc:** Có
- **Ví dụ:** VietnamWorks, LinkedIn, TopDev, Facebook Groups, Website công ty, Headhunter

### Quy trình phỏng vấn
- **Mô tả:** Các vòng phỏng vấn và tiêu chí.
- **Bắt buộc:** Có
- **Ví dụ:** Vòng 1: HR screening (Phone). Vòng 2: Technical Test. Vòng 3: Interview with Manager. Vòng 4: Culture Fit with CEO.

## Process
### Bước 1: Tạo & Duyệt Yêu cầu tuyển dụng
Trưởng phòng tạo JR, gửi HR duyệt.

- Điền thông tin: Vị trí, Số lượng, Mức lương, Mô tả công việc (JD), Tiêu chí
- HR review: Kiểm tra ngân sách headcount, mức lương thị trường
- Phê duyệt: Manager → HR Director → CEO (nếu cấp cao)
- JR được duyệt → HR bắt đầu đăng tuyển

### Bước 2: Đăng tuyển & Thu nhận CV
Đăng tin và thu thập hồ sơ ứng viên.

- Đăng trên nhiều kênh đồng thời
- Nhận CV qua Email/Portal → Tự động tạo bản ghi Applicant trong hệ thống
- Parse CV tự động (Extract tên, SĐT, Email, Kinh nghiệm)
- Gửi email xác nhận đã nhận CV cho ứng viên

### Bước 3: Sàng lọc (Screening)
Lọc hồ sơ phù hợp.

- HR review CV: Khớp JD? Kinh nghiệm đủ? Mức lương phù hợp?
- Trạng thái: Shortlisted (Vào vòng trong) / Rejected (Loại) / KIP (Giữ lại cho vị trí khác)
- Gọi điện screening: Xác nhận thông tin, mức lương kỳ vọng, khả năng onboard

### Bước 4: Phỏng vấn nhiều vòng
Tiến hành phỏng vấn và đánh giá.

- Mỗi vòng có Scorecard riêng (Tiêu chí + Thang điểm 1-5)
- Interviewer nhập nhận xét và điểm vào hệ thống
- Sau mỗi vòng: Pass / Fail / On Hold
- Hệ thống gửi email hẹn lịch tự động (tích hợp Google Calendar)

### Bước 5: Offer & Onboarding
Đưa ra lời mời và hoàn tất thủ tục.

- HR tạo Offer Letter với điều khoản (Lương, Benefits, Ngày bắt đầu)
- Gửi Offer → Ứng viên Accept / Negotiate / Reject
- Accept → Tạo hồ sơ Employee (chuyển từ Applicant sang Employee)
- Chuẩn bị Onboarding: Laptop, Email, Seat, Training plan
- Ứng viên Reject → Gửi cho backup candidate

## Outputs
### Hiring Pipeline
- **Định dạng:** Mermaid Flowchart
- **Mẫu:**

```
graph LR
    A[JR Created] --> B[Approved]
    B --> C[Job Posted]
    C --> D[CVs Received]
    D --> E[Screening]
    E --> F[Interview Round 1-N]
    F --> G[Offer]
    G --> H[Onboarded]
```

### Interview Scorecard
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| Tiêu chí | Trọng số | Điểm (1-5) | Ghi chú |
|---|---|---|---|
| Kỹ năng chuyên môn | 40% | | |
| Kinh nghiệm liên quan | 25% | | |
| Communication | 15% | | |
| Culture Fit | 10% | | |
| Motivation | 10% | | |
| **Tổng điểm (Weighted)** | **100%** | | |
```

## Sub-Skills (Kỹ năng con)
- Thiết kế JD Template
- Thiết kế Interview Scorecard
- Thiết kế Talent Pool
- Thiết kế Onboarding Checklist

## Business Rules
- BR-HRM-REC-01: Mọi tuyển dụng phải có Job Requisition được duyệt.
- BR-HRM-REC-02: Ứng viên bị Reject phải được giữ trong Talent Pool ít nhất 12 tháng.
- BR-HRM-REC-03: Offer Letter phải được HR Director duyệt trước khi gửi.
- BR-HRM-REC-04: Mỗi vòng phỏng vấn phải có Scorecard với tiêu chí rõ ràng.

## Edge Cases & Exceptions
- Ứng viên accept Offer nhưng không đến ngày đầu tiên (No-show) → Activate backup
- Hiring Manager muốn tuyển vượt headcount → Cần phê duyệt đặc biệt
- Ứng viên nội bộ (Internal Transfer) → Quy trình riêng, ưu tiên

## Checklist
- [ ] Đã thiết kế luồng Job Requisition + Approval
- [ ] Đã tích hợp đa kênh tuyển dụng
- [ ] Đã có Parse CV tự động
- [ ] Đã thiết kế Interview Scorecard
- [ ] Đã có Talent Pool cho ứng viên tiềm năng
- [ ] Đã thiết kế Offer Letter workflow
- [ ] Đã có Onboarding Checklist
- [ ] Đã có Dashboard: Time-to-Hire, Source Effectiveness, Offer Accept Rate

## Example
Xem Interview Scorecard và Hiring Pipeline trong Outputs.

## Related Skills
- Phân tích KPI và Đánh giá
- Phân tích Chấm công
