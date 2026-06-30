# Write SRS

## Level
Level 1 - Basic Skill

## Purpose
Soạn thảo Software Requirements Specification (SRS) chi tiết mức độ team Dev có thể code được ngay, bao gồm đặc tả chức năng (Functional), phi chức năng (Non-Functional), giao diện, API, và ràng buộc hệ thống.

## When to Use
Sử dụng sau khi BRD đã được duyệt, cần chuyển yêu cầu nghiệp vụ thành đặc tả kỹ thuật chi tiết.

## Prerequisites
- Đã hoàn thành BRD
- Đã viết User Stories

## Inputs
### BRD đã duyệt
- **Mô tả:** Tài liệu yêu cầu nghiệp vụ cấp cao.
- **Bắt buộc:** Có
- **Ví dụ:** BRD v1.0 Module WMS với 35 Business Requirements.

### User Stories
- **Mô tả:** Danh sách User Stories đã viết.
- **Bắt buộc:** Có
- **Ví dụ:** 45 User Stories đã estimate Story Points.

### Wireframes / Mockups
- **Mô tả:** Bản thiết kế giao diện sơ bộ.
- **Bắt buộc:** Không
- **Ví dụ:** Figma mockups cho 15 màn hình chính.

## Process
### Bước 1: Mô tả tổng quan hệ thống
Giới thiệu mục đích, phạm vi và kiến trúc tổng thể.

- Mục đích hệ thống
- Phạm vi (In-scope / Out-of-scope)
- Kiến trúc tổng quan (Client-Server, Microservices...)
- Công nghệ sử dụng (Tech Stack)
- Danh sách User Roles

### Bước 2: Đặc tả chức năng (Functional Requirements)
Mô tả chi tiết từng chức năng hệ thống.

- Mỗi FR có ID duy nhất: FR-WMS-001, FR-WMS-002...
- Mô tả: Hệ thống phải [làm gì] khi [điều kiện]
- Input: User nhập gì? Từ đâu?
- Processing: Hệ thống xử lý như thế nào? Business Rules?
- Output: Hệ thống hiển thị/lưu/gửi gì?
- Validation Rules: Trường nào bắt buộc? Format? Min/Max?
- Error Handling: Thông báo lỗi gì khi nhập sai?
- Security: Ai được dùng tính năng này?

### Bước 3: Đặc tả phi chức năng (Non-Functional Requirements)
Mô tả các yêu cầu chất lượng hệ thống.

- Performance: Response time < 2s cho 95% requests. Hỗ trợ 500 CCU.
- Security: Encrypt mật khẩu bcrypt, JWT Token expire 24h, OWASP Top 10
- Availability: Uptime 99.5% (Tối đa 43.8 giờ downtime/năm)
- Scalability: Horizontal scaling khi CCU > 1000
- Backup: Daily backup, Retention 30 ngày
- Compatibility: Chrome 90+, Firefox 85+, Edge, Safari. Mobile responsive

### Bước 4: Đặc tả giao diện (Interface Requirements)
Mô tả các giao diện tích hợp.

- User Interface: Responsive Web, Mobile App (nếu có)
- API Interface: RESTful API, Authentication method
- Hardware Interface: Máy quét barcode, Máy in, Máy chấm công
- Software Interface: Tích hợp ERP, Tích hợp Email, Tích hợp SMS Gateway

### Bước 5: Data Model
Mô tả cấu trúc dữ liệu.

- ERD tổng quan
- Data Dictionary cho các bảng chính
- Quy ước đặt tên (Naming Convention)

## Outputs
### Tài liệu SRS
- **Định dạng:** Markdown Document
- **Mẫu:**

```
# Software Requirements Specification (SRS)

## 1. Introduction
### 1.1. Purpose
### 1.2. Scope
### 1.3. Definitions & Acronyms
### 1.4. References

## 2. Overall Description
### 2.1. Product Perspective
### 2.2. User Classes and Characteristics
### 2.3. Operating Environment
### 2.4. Assumptions and Dependencies

## 3. System Features (Functional Requirements)
### 3.1. [Module Name]
#### FR-001: [Feature Name]
- **Description:** Hệ thống phải...
- **Input:** ...
- **Processing:** ...
- **Output:** ...
- **Validation:** ...
- **Error Handling:** ...
- **Permission:** ...
- **Priority:** Must/Should/Could

## 4. Non-Functional Requirements
### 4.1. Performance
### 4.2. Security
### 4.3. Availability
### 4.4. Scalability

## 5. Interface Requirements
### 5.1. User Interfaces
### 5.2. API Interfaces
### 5.3. Hardware Interfaces

## 6. Data Requirements
### 6.1. ERD
### 6.2. Data Dictionary

## 7. Appendix
```

## Sub-Skills (Kỹ năng con)
- Viết Functional Requirements chi tiết
- Viết Non-Functional Requirements
- Thiết kế Data Model
- Viết Validation Rules

## Business Rules
- BR-SRS-01: Mỗi Functional Requirement phải có ID, Input, Processing, Output, Validation.
- BR-SRS-02: Non-Functional Requirements phải có thể đo lường được (Measurable).
- BR-SRS-03: SRS phải cover Error Handling cho mỗi chức năng.
- BR-SRS-04: SRS phải có Traceability ngược về BRD (Mỗi FR link về BR tương ứng).

## Edge Cases & Exceptions
- Yêu cầu quá phức tạp để viết SRS → Chia thành nhiều tài liệu SRS theo module
- Wireframe chưa có → Mô tả bằng lời, bổ sung sau

## Checklist
- [ ] Có đủ FR cho mỗi User Story?
- [ ] Mỗi FR có Input/Processing/Output/Validation/Error?
- [ ] Có NFR (Performance, Security, Availability)?
- [ ] NFR có đo lường được không (không dùng từ 'nhanh', 'tốt')?
- [ ] Có Data Model (ERD + Data Dictionary)?
- [ ] Có Interface Requirements (API, Hardware)?
- [ ] SRS có trace ngược về BRD không?

## Example
Xem SRS Template trong Outputs.

## Related Skills
- Write BRD
- Write User Story
- Thiết kế ERD
- Create Data Dictionary
