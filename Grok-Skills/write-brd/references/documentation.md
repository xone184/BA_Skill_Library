# Write BRD

## Level
Level 1 - Basic Skill

## Purpose
Soạn thảo Business Requirement Document (BRD) chuẩn mực, tập trung mô tả 'CÁI GÌ' (What) doanh nghiệp cần và 'TẠI SAO' (Why), KHÔNG đi vào chi tiết kỹ thuật 'NHƯ THẾ NÀO' (How).

## When to Use
Sử dụng ở giai đoạn đầu dự án để làm rõ phạm vi và mục tiêu kinh doanh trước khi đi vào thiết kế chi tiết.

## Prerequisites
- Đã phỏng vấn Stakeholders

## Inputs
### Yêu cầu nghiệp vụ tổng thể
- **Mô tả:** Mô tả vấn đề kinh doanh cần giải quyết.
- **Bắt buộc:** Có
- **Ví dụ:** Công ty muốn quản lý kho bằng phần mềm thay vì Excel.

### Phạm vi dự án (Scope)
- **Mô tả:** Danh sách module/chức năng thuộc phạm vi.
- **Bắt buộc:** Có
- **Ví dụ:** In-scope: Nhập kho, Xuất kho, Kiểm kê. Out-of-scope: Vận chuyển, CRM.

## Process
### Bước 1: Tóm tắt dự án (Executive Summary)
Viết phần giới thiệu ngắn gọn về dự án.

- Bối cảnh: Tại sao cần dự án này?
- Mục tiêu: Dự án giải quyết vấn đề gì?
- Lợi ích kỳ vọng: Tiết kiệm bao nhiêu %, tăng hiệu suất bao nhiêu?

### Bước 2: Xác định Stakeholders
Liệt kê tất cả các bên liên quan.

- Người tài trợ (Sponsor)
- Người dùng cuối (End Users) theo từng phòng ban
- Đội IT
- Các bên thứ ba (NCC phần mềm, Tư vấn)

### Bước 3: Định nghĩa Scope
Xác định rõ In-scope và Out-of-scope.

- In-scope: Liệt kê từng module/chức năng (đánh số ID)
- Out-of-scope: Liệt kê rõ những gì KHÔNG làm (để tránh hiểu nhầm)
- Assumptions: Các giả định
- Constraints: Các ràng buộc (Ngân sách, Timeline, Công nghệ)

### Bước 4: Liệt kê Business Requirements
Mô tả các yêu cầu nghiệp vụ cấp cao.

- Mỗi requirement có ID duy nhất (VD: BR-001, BR-002)
- Mỗi requirement có Priority (Must / Should / Could / Won't)
- Mỗi requirement mô tả WHAT không mô tả HOW
- Nhóm requirements theo module/chức năng

### Bước 5: Xác định Tiêu chí Thành công
Định nghĩa khi nào dự án được coi là thành công.

- KPI đo lường: Giảm thời gian xử lý 50%, Giảm sai sót 80%
- Tiêu chí nghiệm thu (Acceptance Criteria cấp dự án)
- Timeline dự kiến (Milestones)

## Outputs
### Tài liệu BRD
- **Định dạng:** Markdown Document
- **Mẫu:**

```
# Business Requirement Document (BRD)

## 1. Document Control
| Mục | Chi tiết |
|---|---|
| Tên dự án | [Tên] |
| Phiên bản | 1.0 |
| Ngày tạo | [Ngày] |
| Tác giả | [BA Name] |
| Trạng thái | Draft / Reviewed / Approved |

## 2. Revision History
| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | [Date] | [Name] | Tạo mới |

## 3. Executive Summary
[Mô tả ngắn gọn...]

## 4. Business Objectives
[Mục tiêu kinh doanh...]

## 5. Stakeholders
| Tên | Vai trò | Phòng ban | Mức độ ảnh hưởng |
|---|---|---|---|

## 6. Scope
### 6.1. In-Scope
### 6.2. Out-of-Scope
### 6.3. Assumptions
### 6.4. Constraints

## 7. Business Requirements
| ID | Requirement | Module | Priority | Status |
|---|---|---|---|---|
| BR-001 | ... | ... | Must | Draft |

## 8. Success Criteria

## 9. Risks

## 10. Approval
| Tên | Vai trò | Chữ ký | Ngày |
|---|---|---|---|
```

## Sub-Skills (Kỹ năng con)
- Phỏng vấn Stakeholder
- Xác định Scope
- Priority Assignment (MoSCoW)

## Business Rules
- BR-DOC-01: BRD chỉ mô tả WHAT và WHY, KHÔNG mô tả HOW.
- BR-DOC-02: Mỗi Business Requirement phải có ID duy nhất để truy vết.
- BR-DOC-03: Out-of-scope phải liệt kê rõ ràng để tránh Scope Creep.
- BR-DOC-04: BRD phải có ít nhất 1 lần Review trước khi Approve.

## Edge Cases & Exceptions
- Khách hàng yêu cầu quá rộng → Gợi ý chia thành Phase 1, Phase 2
- Stakeholders mâu thuẫn nhau → Escalate lên Sponsor quyết định
- Yêu cầu thay đổi liên tục → Đánh dấu phiên bản (Version Control)

## Checklist
- [ ] Có Executive Summary rõ ràng?
- [ ] Đã liệt kê đầy đủ Stakeholders?
- [ ] Có In-scope VÀ Out-of-scope rõ ràng?
- [ ] Mỗi Requirement có ID và Priority?
- [ ] BRD không chứa giải pháp kỹ thuật?
- [ ] Có Success Criteria đo lường được?
- [ ] Có Revision History?
- [ ] Có phần Sign-off (Ký duyệt)?

## Example
Xem Template BRD trong Outputs.

## Related Skills
- Write SRS
- Write User Story
- Interview Stakeholder
