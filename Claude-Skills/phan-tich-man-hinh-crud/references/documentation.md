# Phân tích màn hình CRUD

## Level
Level 2 - Business Skill

## Purpose
Đặc tả chi tiết bộ màn hình CRUD (Create-Read-Update-Delete) cho một entity, bao gồm: màn hình List (Search/Filter/Pagination/Bulk Actions), màn hình Create/Edit (Form Validation), màn hình Detail View, và tất cả Confirmation/Error Dialogs.

## When to Use
Sử dụng khi cần đặc tả bất kỳ màn hình quản lý entity nào trong hệ thống (Quản lý Khách hàng, Quản lý Sản phẩm, Quản lý Đơn hàng...).

## Prerequisites
- Đã có Data Model/ERD
- Hiểu cơ bản về UIUX

## Inputs
### Entity & Trường dữ liệu
- **Mô tả:** Entity nào và có những trường nào.
- **Bắt buộc:** Có
- **Ví dụ:** Entity: Product. Trường: product_code, name, category, unit_price, stock_qty, status, created_at.

### Permission Matrix
- **Mô tả:** Ai được CRUD trên entity này.
- **Bắt buộc:** Có
- **Ví dụ:** Admin: CRUD. Manager: CRU. Staff: R (chỉ xem). Guest: Không thấy.

## Process
### Bước 1: Đặc tả màn hình List (Danh sách)
Thiết kế trang danh sách entity.

- Columns: Chọn cột nào hiển thị (KHÔNG hiển thị tất cả trường)
- Search: Tìm theo trường nào? (VD: Tên, Mã sản phẩm)
- Filters: Lọc theo trường nào? (VD: Category dropdown, Status radio, Date range)
- Sort: Cột nào cho sort? Default sort? (VD: Mới nhất trước)
- Pagination: 10/25/50 items per page. Hiển thị 'Showing 1-10 of 150'
- Bulk Actions: Chọn nhiều → Xóa hàng loạt, Export, Thay đổi status
- Row Actions: Mỗi hàng có nút: View, Edit, Delete (hoặc icon)
- Button 'Tạo mới' ở góc phải trên
- Empty State: Hiển thị gì khi chưa có dữ liệu?
- Export: Nút Export Excel/CSV

### Bước 2: Đặc tả màn hình Create/Edit (Form)
Thiết kế form nhập liệu.

- Bố trí trường: 1 cột hay 2 cột? Nhóm thành Section?
- Mỗi trường PHẢI có: Label, Placeholder, Loại control (Input/Select/DatePicker/TextArea), Bắt buộc (*), Validation rule
- Trường khóa (VD: Mã sản phẩm): Auto-generate hay nhập tay? Unique?
- Trường Foreign Key (VD: Category): Dropdown, Searchable Select, hay Popup chọn?
- Trường Upload: Ảnh sản phẩm → Crop, Resize, Preview trước khi upload
- Nút: [Lưu] [Lưu & Tiếp tục] [Hủy]
- Confirm khi Hủy: 'Bạn có chắc muốn hủy? Dữ liệu chưa lưu sẽ mất.'
- Loading state: Nút Lưu bị disable khi đang submit

### Bước 3: Đặc tả Validation Rules
Chi tiết rule kiểm tra cho từng trường.

- Required: 'Vui lòng nhập [tên trường]'
- Min/Max Length: 'Tên sản phẩm phải từ 3-200 ký tự'
- Format: Email (abc@xyz.com), SĐT (10 số, bắt đầu 0), Mã (chỉ chữ và số)
- Unique: 'Mã sản phẩm đã tồn tại, vui lòng nhập mã khác'
- Range: 'Giá bán phải > 0'
- Dependency: 'Nếu chọn Loại = Thực phẩm → Bắt buộc nhập Hạn sử dụng'
- Realtime validation (onBlur) vs Submit validation

### Bước 4: Đặc tả Delete (Xóa)
Xử lý xóa entity.

- Soft Delete (Đánh dấu xóa, không xóa thật) → Khuyến khích
- Confirm Dialog: 'Bạn có chắc chắn muốn xóa [Tên]? Hành động này không thể hoàn tác.'
- Kiểm tra ràng buộc: Nếu entity có child records → 'Không thể xóa vì còn [N] đơn hàng liên quan.'
- Bulk Delete: Confirm 'Bạn sắp xóa [N] mục. Tiếp tục?'

### Bước 5: Đặc tả Detail View (Xem chi tiết)
Thiết kế trang xem chi tiết.

- Hiển thị tất cả trường ở chế độ Read-only
- Tab layout nếu entity phức tạp (Tab Thông tin chung, Tab Lịch sử, Tab Đơn hàng liên quan)
- Activity Log / Audit Trail: Ai đã sửa gì, khi nào?
- Nút hành động: [Sửa] [Xóa] [In] [Export PDF]

## Outputs
### CRUD Screen Specification
- **Định dạng:** Markdown Document
- **Mẫu:**

```
# Screen Spec: Quản lý [Entity]

## 1. List Screen
### Columns
| # | Column | Source Field | Width | Sort | Filter |
|---|---|---|---|---|---|
| 1 | Mã SP | product_code | 100px | ✅ | Text search |
| 2 | Tên SP | name | 250px | ✅ | Text search |
| 3 | Danh mục | category.name | 150px | ✅ | Dropdown |
| 4 | Giá bán | unit_price | 120px | ✅ | Range |
| 5 | Trạng thái | status | 100px | | Radio |

### Actions
- [+ Tạo mới] (Góc phải trên)
- Row: [View] [Edit] [Delete]
- Bulk: [Delete] [Export Excel]

## 2. Create/Edit Form
| # | Field | Label | Control | Required | Validation |
|---|---|---|---|---|---|
| 1 | product_code | Mã SP | Text Input | ✅ | Unique, [A-Z0-9-]{3,20} |
| 2 | name | Tên SP | Text Input | ✅ | Length 3-200 |
| 3 | category_id | Danh mục | Searchable Select | ✅ | |
| 4 | unit_price | Giá bán | Number Input | ✅ | > 0 |
| 5 | image | Ảnh SP | File Upload | | JPG/PNG, max 2MB |
```

### Validation Rules Table
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| Field | Rule | Error Message |
|---|---|---|
| product_code | Required | 'Vui lòng nhập Mã sản phẩm' |
| product_code | Unique | 'Mã sản phẩm đã tồn tại' |
| product_code | Pattern [A-Z0-9-] | 'Mã chỉ chứa chữ in hoa, số và dấu gạch ngang' |
| name | Required | 'Vui lòng nhập Tên sản phẩm' |
| name | Length 3-200 | 'Tên phải từ 3-200 ký tự' |
| unit_price | > 0 | 'Giá bán phải lớn hơn 0' |
```

## Sub-Skills (Kỹ năng con)
- Thiết kế List Screen
- Thiết kế Form Screen
- Thiết kế Validation Rules
- Thiết kế Empty State & Loading State

## Business Rules
- BR-UI-CRUD-01: Mọi màn hình List phải có Search + Filter + Pagination + Sort.
- BR-UI-CRUD-02: Delete bắt buộc có Confirm Dialog.
- BR-UI-CRUD-03: Form Validation phải chạy realtime (onBlur) cho trường Required.
- BR-UI-CRUD-04: Nút Submit phải disable khi đang loading.
- BR-UI-CRUD-05: Mọi entity phải có Audit Log (created_by, updated_by, created_at, updated_at).

## Edge Cases & Exceptions
- 2 user cùng Edit 1 record → Optimistic Locking / Concurrency conflict
- Upload ảnh quá lớn → Validate file size trước khi upload
- Mất kết nối khi đang submit form → Retry hoặc lưu Draft local

## Checklist
- [ ] List: Có Search?
- [ ] List: Có Filter?
- [ ] List: Có Pagination?
- [ ] List: Có Sort?
- [ ] List: Có Export Excel?
- [ ] List: Có Bulk Actions?
- [ ] List: Có Empty State?
- [ ] Form: Mỗi field có Label + Control + Validation?
- [ ] Form: Có Confirm khi Cancel?
- [ ] Form: Nút disable khi loading?
- [ ] Delete: Có Confirm Dialog?
- [ ] Delete: Kiểm tra ràng buộc?
- [ ] Detail: Có Audit Log?

## Example
Xem CRUD Screen Specification template trong Outputs.

## Related Skills
- Thiết kế Dashboard
- Thiết kế Form
- Thiết kế module
