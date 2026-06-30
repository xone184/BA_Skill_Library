# Thiết kế ERD

## Level
Level 2 - Business Skill

## Purpose
Thiết kế Entity-Relationship Diagram (ERD) cho hệ thống, xác định rõ các Entity (Bảng), Attributes (Cột), Primary Key, Foreign Key, Relationships (1-1, 1-N, N-N), Indexes, và Constraints. ERD phải đủ chi tiết để DBA có thể tạo database trực tiếp.

## When to Use
Sử dụng khi cần thiết kế cấu trúc database cho một module hoặc toàn bộ hệ thống.

## Prerequisites
- Đã hoàn thành SRS hoặc User Stories

## Inputs
### Danh sách Entity (từ SRS/User Stories)
- **Mô tả:** Các đối tượng cần lưu trữ dữ liệu.
- **Bắt buộc:** Có
- **Ví dụ:** Module WMS: product, warehouse, location, purchase_order, goods_receipt, inventory, picking_order.

### Business Rules
- **Mô tả:** Các quy tắc ảnh hưởng đến cấu trúc dữ liệu.
- **Bắt buộc:** Có
- **Ví dụ:** 1 Product có thể nằm ở nhiều Location. 1 PO có nhiều PO Lines. 1 Warehouse có nhiều Zones, mỗi Zone có nhiều Locations.

## Process
### Bước 1: Xác định Entity (Bảng)
Liệt kê tất cả các Entity cần tạo.

- Mỗi danh từ chính trong SRS thường là 1 Entity
- Phân biệt Entity chính (Master: Product, Customer) và Entity giao dịch (Transaction: Order, Invoice)
- Phân biệt Entity chính và bảng phụ (Lookup: Status, Category)
- Naming Convention: snake_case, số ít (product thay vì products)

### Bước 2: Xác định Attributes (Cột)
Liệt kê tất cả trường dữ liệu cho mỗi Entity.

- Mỗi cột phải có: Tên, Kiểu dữ liệu, Nullable?, Default value, Mô tả
- Kiểu dữ liệu chuẩn: INT, BIGINT, VARCHAR(N), TEXT, DECIMAL(P,S), DATE, DATETIME, BOOLEAN, ENUM
- Audit Columns bắt buộc: id (PK), created_at, updated_at, created_by, updated_by, is_deleted
- Soft Delete: Dùng is_deleted (BOOLEAN) thay vì xóa thật

### Bước 3: Xác định Relationships
Xác định quan hệ giữa các Entity.

- 1-1 (One-to-One): user ↔ user_profile (Hiếm gặp)
- 1-N (One-to-Many): customer → orders (1 KH có nhiều đơn hàng). FK ở bảng con (orders.customer_id)
- N-N (Many-to-Many): product ↔ tag → Cần bảng trung gian (product_tag)
- Self-referencing: employee.manager_id → employee.id (Cây tổ chức)
- Polymorphic: activity_log.entity_type + activity_log.entity_id (Log cho nhiều entity)

### Bước 4: Thiết kế Indexes
Tối ưu hiệu suất query.

- Primary Key: Mọi bảng phải có PK (thường là id INT AUTO_INCREMENT)
- Foreign Key: Tạo Index cho mỗi FK
- Unique Index: Trường unique (email, product_code)
- Composite Index: Cho query thường xuyên (VD: (warehouse_id, product_id) trên bảng inventory)
- Index cho Filter/Sort: Trường thường dùng trong WHERE và ORDER BY

### Bước 5: Vẽ ERD Diagram
Vẽ sơ đồ ERD dạng Mermaid hoặc công cụ khác.

- Sử dụng Mermaid erDiagram syntax
- Hiển thị: Entity name, PK/FK, Relationship lines
- Gom nhóm theo Module nếu ERD quá lớn

## Outputs
### ERD Diagram
- **Định dạng:** Mermaid erDiagram
- **Mẫu:**

```
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ ORDER_LINE : contains
    PRODUCT ||--o{ ORDER_LINE : appears_in
    WAREHOUSE ||--|{ LOCATION : has
    PRODUCT ||--o{ INVENTORY : stored_at
    LOCATION ||--o{ INVENTORY : holds
```

### Data Dictionary
- **Định dạng:** Markdown Table
- **Mẫu:**

```
## Table: product
| # | Column | Type | Nullable | Default | Constraint | Description |
|---|---|---|---|---|---|---|
| 1 | id | INT | No | AUTO_INCREMENT | PK | Mã sản phẩm |
| 2 | code | VARCHAR(50) | No | | UNIQUE | Mã SP hiển thị |
| 3 | name | VARCHAR(200) | No | | | Tên sản phẩm |
| 4 | category_id | INT | No | | FK → category.id | Danh mục |
| 5 | unit_price | DECIMAL(15,2) | No | 0 | CHECK > 0 | Đơn giá |
| 6 | is_deleted | BOOLEAN | No | false | | Soft delete |
| 7 | created_at | DATETIME | No | NOW() | | Ngày tạo |
| 8 | updated_at | DATETIME | Yes | | | Ngày cập nhật |
```

## Sub-Skills (Kỹ năng con)
- Entity Identification
- Relationship Design
- Data Dictionary Creation
- Index Design

## Business Rules
- BR-ERD-01: Mọi bảng phải có Primary Key (id INT AUTO_INCREMENT).
- BR-ERD-02: Mọi bảng phải có audit columns (created_at, updated_at, created_by, updated_by).
- BR-ERD-03: Sử dụng Soft Delete (is_deleted) thay vì xóa thật.
- BR-ERD-04: Naming Convention: snake_case, số ít, tiếng Anh.
- BR-ERD-05: FK phải có Index.

## Edge Cases & Exceptions
- Bảng N-N với dữ liệu bổ sung → Bảng trung gian trở thành Entity riêng (VD: order_line có quantity, price)
- Dữ liệu lịch sử (History) → Bảng snapshot (product_price_history) hoặc Audit table

## Checklist
- [ ] Mọi bảng có PK?
- [ ] Mọi bảng có Audit columns?
- [ ] Đã sử dụng Soft Delete?
- [ ] FK đã tạo Index?
- [ ] Đã xử lý N-N bằng bảng trung gian?
- [ ] Naming convention nhất quán (snake_case)?
- [ ] Data Dictionary đầy đủ cho mỗi bảng?
- [ ] ERD Diagram đã vẽ đầy đủ Relationship?

## Example
Xem ERD và Data Dictionary trong Outputs.

## Related Skills
- Create Data Dictionary
- Thiết kế module
- Write SRS
