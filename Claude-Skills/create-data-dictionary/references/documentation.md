# Create Data Dictionary

## Level
Level 2 - Business Skill

## Purpose
Tạo Data Dictionary toàn diện cho hệ thống, mô tả chi tiết mỗi bảng, mỗi cột, kiểu dữ liệu, ràng buộc, mối quan hệ và mô tả nghiệp vụ. Đây là tài liệu tham chiếu chính cho Dev, DBA, BA và QC.

## When to Use
Sử dụng sau khi thiết kế ERD, cần tạo tài liệu chi tiết cho database.

## Prerequisites
- Đã thiết kế ERD

## Inputs
### ERD Diagram
- **Mô tả:** Sơ đồ Entity-Relationship đã thiết kế.
- **Bắt buộc:** Có
- **Ví dụ:** ERD Module WMS với 12 bảng.

### Business Rules
- **Mô tả:** Các quy tắc nghiệp vụ ảnh hưởng đến dữ liệu.
- **Bắt buộc:** Có
- **Ví dụ:** Giá bán phải > 0. Email phải unique. Status chỉ có thể là: active, inactive, archived.

## Process
### Bước 1: Liệt kê tất cả bảng
Tạo danh sách tổng quan các bảng.

- Phân loại: Master (Dữ liệu chủ), Transaction (Giao dịch), Lookup (Tra cứu), System (Hệ thống)
- Mỗi bảng có: Tên, Mô tả, Loại, Số cột dự kiến, Kích thước dự kiến

### Bước 2: Chi tiết mỗi bảng
Mô tả chi tiết từng cột trong bảng.

- Column Name: snake_case
- Data Type: INT, VARCHAR(N), DECIMAL(P,S), DATETIME, BOOLEAN, TEXT, ENUM, JSON
- Nullable: Yes/No
- Default Value: AUTO_INCREMENT, NOW(), false, 0
- Constraint: PK, FK → table.column, UNIQUE, CHECK, INDEX
- Description: Mô tả nghiệp vụ bằng tiếng Việt rõ ràng
- Sample Data: Dữ liệu mẫu để minh họa

### Bước 3: Mô tả Enum / Lookup Values
Liệt kê giá trị cho các trường ENUM.

- VD: status ENUM → 'active', 'inactive', 'archived'
- VD: priority ENUM → 'low', 'medium', 'high', 'critical'
- Mỗi giá trị có mô tả nghiệp vụ

### Bước 4: Mô tả Indexes & Constraints
Liệt kê tất cả indexes.

- Primary Key Index
- Unique Indexes (email, code...)
- Foreign Key Indexes
- Composite Indexes cho query thường dùng
- Full-text Index (nếu cần search nội dung)

## Outputs
### Data Dictionary
- **Định dạng:** Markdown Document (1 section per table)
- **Mẫu:**

```
# Data Dictionary: [Module Name]

## Tổng quan
| # | Table | Type | Description | Est. Rows |
|---|---|---|---|---|
| 1 | product | Master | Sản phẩm | 10,000 |
| 2 | order | Transaction | Đơn hàng | 1,000,000 |
| 3 | category | Lookup | Danh mục SP | 50 |

---

## Table: product
**Mô tả:** Lưu trữ thông tin sản phẩm chính.
**Loại:** Master Data

| # | Column | Type | Null | Default | Constraint | Description | Sample |
|---|---|---|---|---|---|---|---|
| 1 | id | INT | No | AUTO_INC | PK | Mã sản phẩm | 1 |
| 2 | code | VARCHAR(50) | No | | UQ, IDX | Mã hiển thị | 'PRD-001' |
| 3 | name | VARCHAR(200) | No | | | Tên SP | 'Sữa TH 1L' |
| 4 | category_id | INT | No | | FK→category.id, IDX | Danh mục | 3 |
| 5 | unit_price | DECIMAL(15,2) | No | 0 | CHECK>0 | Đơn giá | 25000.00 |
| 6 | is_deleted | BOOLEAN | No | false | | Soft delete | false |
| 7 | created_at | DATETIME | No | NOW() | | Ngày tạo | '2024-01-15' |
```

## Sub-Skills (Kỹ năng con)
- Xác định Data Type
- Viết Constraint
- Ước lượng Data Volume

## Business Rules
- BR-DD-01: Mỗi cột PHẢI có mô tả nghiệp vụ bằng tiếng Việt.
- BR-DD-02: Mỗi bảng PHẢI có Sample Data.
- BR-DD-03: ENUM values phải được liệt kê đầy đủ với mô tả.
- BR-DD-04: Foreign Key phải ghi rõ bảng tham chiếu (FK → table.column).

## Edge Cases & Exceptions
- Cột lưu JSON → Cần mô tả cấu trúc JSON bên trong
- Cột tính toán (Computed Column) → Ghi rõ công thức

## Checklist
- [ ] Mỗi bảng có mô tả?
- [ ] Mỗi cột có Data Type chính xác?
- [ ] Mỗi cột có Description?
- [ ] ENUM đã liệt kê values?
- [ ] FK ghi rõ bảng tham chiếu?
- [ ] Có Sample Data?
- [ ] Có ước lượng Data Volume?

## Example
Xem Data Dictionary template trong Outputs.

## Related Skills
- Thiết kế ERD
- Write SRS
- Thiết kế module
