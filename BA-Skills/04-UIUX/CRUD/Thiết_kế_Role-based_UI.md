# Skill Name
Thiết kế Role-based UI

## Level
Level 3 - Architecture Skill

## Purpose
Phân tích giao diện thay đổi linh hoạt theo quyền của người dùng (RBAC).

## Inputs
- Ma trận phân quyền (Permission Matrix)

## Process
1. Xác định các Roles
2. Ánh xạ Role với View/Edit/Delete
3. Mô tả trạng thái UI (Hidden vs Disabled)

## Outputs
- Luồng hiển thị/ẩn các nút thao tác
- Điều hướng tùy chỉnh

## Checklist
- [ ] Nút bấm mà User không có quyền thì Ẩn đi hay Làm mờ (Disabled)?
- [ ] Có kiểm tra quyền lại ở dưới Backend (API) không?
