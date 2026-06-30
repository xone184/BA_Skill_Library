# Thiết kế module

## Level
Level 3 - Architecture Skill

## Purpose
Thiết kế kiến trúc module cho hệ thống doanh nghiệp, bao gồm phân rã module, thiết kế menu, phân quyền (RBAC), workflow, database schema, API endpoints, danh sách màn hình và đảm bảo không thiếu bất kỳ thành phần nào nhờ checklist toàn diện.

## When to Use
Sử dụng khi bắt đầu giai đoạn thiết kế kiến trúc tổng thể (High-Level Design) cho một module mới.

## Prerequisites
- Đã hoàn thành BRD/SRS

## Inputs
### Business Requirements
- **Mô tả:** Danh sách yêu cầu nghiệp vụ đã duyệt.
- **Bắt buộc:** Có
- **Ví dụ:** Module WMS: 35 Functional Requirements, 8 Non-Functional Requirements.

### Domain Knowledge
- **Mô tả:** Kiến thức chuyên ngành liên quan.
- **Bắt buộc:** Có
- **Ví dụ:** Kho vận: Inbound, Outbound, Inventory, Cycle Count, Lot/Batch management.

## Process
### Bước 1: Phân rã Module (Module Decomposition)
Chia nhỏ module lớn thành các sub-module.

- Nhóm các Requirement có liên quan thành Sub-module
- Ví dụ Module WMS: Sub-module Inbound, Outbound, Inventory, Master Data
- Mỗi Sub-module phải độc lập về mặt logic

### Bước 2: Thiết kế Menu & Navigation
Cấu trúc menu cho module.

- Menu Level 1: Tên module (VD: Quản lý Kho)
- Menu Level 2: Sub-module (Nhập kho, Xuất kho, Tồn kho, Kiểm kê)
- Menu Level 3: Chức năng con (Tạo phiếu nhập, Danh sách phiếu nhập, Báo cáo nhập)

### Bước 3: Thiết kế Permission Matrix
Ma trận phân quyền RBAC.

- Xác định Roles: Admin, Manager, Operator, Viewer
- Mapping Role vs Feature vs Action (View/Create/Edit/Delete/Approve)
- Xác định data-level permission (Chỉ thấy dữ liệu của mình / của phòng ban / toàn bộ)

### Bước 4: Thiết kế Workflow
Các luồng phê duyệt và trạng thái.

- State Machine: Draft → Submitted → Approved → Done
- Ai có quyền Approve? Điều kiện gì?
- Có cho phép Reject / Return to Draft không?

### Bước 5: Thiết kế Database Schema
Xác định các bảng dữ liệu chính.

- Entity List: Các bảng cần tạo
- Relationship: 1-1, 1-N, N-N
- Key fields: PK, FK, Unique, Index

### Bước 6: Thiết kế API Endpoints
Danh sách API cho Front-end gọi.

- CRUD APIs cho mỗi Entity
- Workflow APIs (Submit, Approve, Reject)
- Report/Export APIs

### Bước 7: Danh sách Screens (Wireframe)
Liệt kê tất cả các màn hình cần thiết kế.

- List Page (Danh sách) cho mỗi Entity
- Detail/Form Page cho Create/Edit
- Dashboard Page
- Report Page

## Outputs
### Module Blueprint
- **Định dạng:** Markdown Document bao gồm tất cả phần trên
### Permission Matrix
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| Chức năng | Admin | Manager | Operator | Viewer |
|---|---|---|---|---|
| Xem phiếu nhập | ✅ | ✅ | ✅ | ✅ |
| Tạo phiếu nhập | ✅ | ✅ | ✅ | ❌ |
| Duyệt phiếu nhập | ✅ | ✅ | ❌ | ❌ |
| Xóa phiếu nhập | ✅ | ❌ | ❌ | ❌ |
```

## Sub-Skills (Kỹ năng con)
- Module Decomposition
- Permission Matrix Design
- Workflow Design
- Screen Listing

## Business Rules
- BR-MOD-01: Mỗi module phải có Dashboard riêng.
- BR-MOD-02: Mỗi danh sách (List) phải có Search, Filter, Pagination.
- BR-MOD-03: Mọi thao tác quan trọng phải có Audit Log.

## Edge Cases & Exceptions
- Module cần tích hợp với module khác → Xác định rõ Integration Points
- Yêu cầu Multi-tenant → Mỗi tenant thấy dữ liệu riêng

## Checklist
- [ ] Có Dashboard chưa?
- [ ] Có CRUD cho mỗi entity chưa?
- [ ] Có Import (Excel/CSV) chưa?
- [ ] Có Export (Excel/PDF) chưa?
- [ ] Có Approval workflow chưa?
- [ ] Có Audit Log chưa?
- [ ] Có Notification (Email/In-app) chưa?
- [ ] Có Search chưa?
- [ ] Có Filter chưa?
- [ ] Có Pagination chưa?
- [ ] Có Permission matrix chưa?
- [ ] Có Report chưa?
- [ ] Có Audit Trail chưa?
- [ ] Có Multi-language chưa (nếu cần)?
- [ ] Có Soft Delete chưa?

## Example
Xem Permission Matrix template.

## Related Skills
- Thiết kế ERD
- Thiết kế API Contract
- Thiết kế Dashboard
