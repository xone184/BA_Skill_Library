# Thiết kế Role-based UI

## Level
Level 3 - Architecture Skill

## Purpose
Thiết kế đặc tả giao diện tùy biến theo vai trò người dùng (Role-based). Đảm bảo mỗi Role chỉ nhìn thấy dữ liệu, nút bấm và chức năng mà họ được cấp quyền, giảm thiểu sai sót và tối ưu hóa trải nghiệm làm việc thực tế.

## When to Use
Khi thiết kế phần mềm doanh nghiệp (MES, ERP) có sự phân cấp rõ ràng: Công nhân (dùng Tablet ở xưởng), Quản đốc (dùng Web theo dõi), Giám đốc (xem Dashboard tổng).

## Prerequisites
- Đã có danh sách User Roles và luồng nghiệp vụ

## Inputs
### Danh sách Roles
- **Mô tả:** Ai sẽ dùng hệ thống?
- **Bắt buộc:** Có
- **Ví dụ:** Operator (Công nhân), Supervisor (Quản đốc), QC (KCS).

### Tính năng
- **Mô tả:** Tính năng cần phân quyền UI.
- **Bắt buộc:** Có
- **Ví dụ:** Màn hình Chi tiết Lệnh Sản Xuất.

## Process
### Bước 1: Xây dựng Ma trận Phân quyền (Permission Matrix)
Map Role với Action.

- Xác định quyền CRUD (Create, Read, Update, Delete) hoặc Execute.
- VD: Công nhân -> Read lệnh, Bấm nút 'Start/Stop'.
- Quản đốc -> Create lệnh, Update lệnh, Bấm nút 'Approve'.

### Bước 2: Thiết kế UI cho Role: Công nhân (Operator Level)
Tập trung vào tính thực thi.

- Giao diện tinh gọn, nút bấm cực lớn (Touch-friendly).
- Chỉ hiển thị thông tin Đang làm (Current task), ẩn đi toàn bộ menu phức tạp.
- Hiển thị cảnh báo màu sắc rực rỡ (Xanh = Chạy, Đỏ = Lỗi).

### Bước 3: Thiết kế UI cho Role: Quản đốc (Supervisor Level)
Tập trung vào giám sát và điều phối.

- Giao diện dạng Danh sách / Kanban Board.
- Cho phép lọc, tìm kiếm nhiều tham số.
- Có các nút hành động hàng loạt (Bulk action: Duyệt 10 lệnh cùng lúc).

### Bước 4: Đặc tả các trạng thái Ẩn/Hiện phần tử UI
Dynamic rendering.

- Nếu là Công nhân -> Nút 'Xóa lệnh' hoàn toàn biến mất (Invisible) chứ không chỉ mờ đi (Disabled) để đỡ rối mắt.
- Nếu không có quyền sửa -> Các ô Input biến thành dạng Text (Read-only).

## Outputs
### Role-based UI Specification
- **Định dạng:** Markdown
- **Mẫu:**

```
### Giao diện: Chi tiết Lệnh Sản Xuất

#### 1. Góc nhìn Công nhân (Operator UI - Tablet)
- **Layout:** Full screen, Nút to, Màu tương phản cao.
- **Data hiển thị:** Tên SP, Số lượng cần làm, Định mức vật tư.
- **Actions:** Chỉ có 2 nút [BẮT ĐẦU] (Màu xanh lá) và [BÁO LỖI] (Màu đỏ).
- **Ẩn đi:** Menu bar, Nút sửa lệnh, Giá tiền sản phẩm.

#### 2. Góc nhìn Quản đốc (Supervisor UI - Web PC)
- **Layout:** Standard Dashboard.
- **Data hiển thị:** Toàn bộ thông tin + Giá thành + Báo cáo tiến độ.
- **Actions:** Nút [Sửa], [Hủy lệnh], [Duyệt].
- **Trạng thái:** Nếu lệnh đang 'Running', nút [Sửa] bị Disabled.
```

## Sub-Skills (Kỹ năng con)
- Permission Matrix Design
- Contextual UI/UX

## Business Rules
- BR-RBUI-01: Nguyên tắc quyền tối thiểu (Least Privilege): Chỉ hiển thị/cấp quyền đúng những gì Role đó cần để làm việc.
- BR-RBUI-02: User dưới xưởng phải được thiết kế UI 'Fail-safe' (Chống bấm nhầm).

## Edge Cases & Exceptions
- Một người kiêm nhiệm 2 Roles (Vừa làm công nhân, vừa làm QC) -> Tích hợp cơ chế 'Switch Role' trên góc màn hình thay vì gộp chung UI gây rối.

## Checklist
- [ ] Đã lập Ma trận phân quyền chưa?
- [ ] Giao diện công nhân đã đủ đơn giản chưa (Touch-friendly)?
- [ ] Đã mô tả rõ hành vi của nút bấm (Ẩn hẳn vs Mờ đi)?

## Example
Xem Role-based UI Specification trong Outputs.

## Related Skills
- Phân tích màn hình CRUD
- Phân tích Mobile App
