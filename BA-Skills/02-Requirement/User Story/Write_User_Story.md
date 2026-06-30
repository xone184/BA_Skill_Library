# Write User Story

## Level
Level 1 - Basic Skill

## Purpose
Viết User Story chuẩn Agile đúng format, kèm Acceptance Criteria chi tiết, tuân thủ nguyên tắc INVEST để đảm bảo Story có thể estimate và deliver trong 1 Sprint.

## When to Use
Sử dụng khi cần chuyển đổi yêu cầu nghiệp vụ thành các đơn vị công việc (Work Item) cho đội Scrum.

## Prerequisites
- Hiểu cơ bản về Scrum/Agile

## Inputs
### Requirement / Nghiệp vụ
- **Mô tả:** Mô tả yêu cầu cần làm.
- **Bắt buộc:** Có
- **Ví dụ:** Nhân viên kho cần có khả năng kiểm kê tồn kho bằng cách quét mã vạch.

### Actor / Persona
- **Mô tả:** Ai là người sử dụng tính năng.
- **Bắt buộc:** Có
- **Ví dụ:** Nhân viên kho, Quản lý kho, Kế toán kho

## Process
### Bước 1: Xác định Actor (Vai trò)
Xác định rõ ai sẽ sử dụng tính năng này. Không dùng 'User' chung chung.

- Liệt kê tất cả các vai trò liên quan
- Chọn vai trò chính (Primary Actor) cho mỗi Story
- Ví dụ đúng: 'As a Warehouse Staff' thay vì 'As a User'

### Bước 2: Xác định Action (Hành động)
Xác định rõ người dùng muốn LÀM GÌ.

- Hành động phải cụ thể, có thể thao tác trên hệ thống
- Ví dụ đúng: 'I want to scan barcode to count inventory'
- Ví dụ sai: 'I want to manage inventory' (Quá rộng)

### Bước 3: Xác định Benefit (Giá trị)
Giải thích TẠI SAO người dùng cần tính năng này.

- Benefit phải hướng đến giá trị kinh doanh thật sự
- Ví dụ đúng: 'So that I can reduce counting time from 4 hours to 1 hour'
- Ví dụ sai: 'So that I can use the system' (Không có giá trị)

### Bước 4: Viết Acceptance Criteria (Tiêu chí chấp nhận)
Viết các điều kiện cụ thể để xác nhận Story đã hoàn thành.

- Sử dụng format Given-When-Then cho mỗi AC:
-   Given [Điều kiện ban đầu]
-   When [Hành động]
-   Then [Kết quả mong đợi]
- Mỗi Story phải có ít nhất 3 Acceptance Criteria
- Phải bao gồm: Happy Path (Đúng), Error Case (Sai), Edge Case (Biên)

### Bước 5: Kiểm tra INVEST
Đảm bảo Story tuân thủ nguyên tắc INVEST.

- Independent: Story không phụ thuộc vào Story khác
- Negotiable: Có thể thương lượng với PO
- Valuable: Mang lại giá trị cho người dùng hoặc doanh nghiệp
- Estimable: Đội Dev có thể ước lượng effort
- Small: Hoàn thành được trong 1 Sprint (2-3 ngày dev)
- Testable: Có thể viết Test Case để kiểm tra

## Outputs
### User Story
- **Định dạng:** Markdown Template
- **Mẫu:**

```
## US-[ID]: [Tên Story]

**As a** [Vai trò]
**I want to** [Hành động]
**So that** [Giá trị/Lợi ích]

### Acceptance Criteria

**AC1: [Happy Path]**
- Given: [Điều kiện]
- When: [Hành động]
- Then: [Kết quả]

**AC2: [Error Case]**
- Given: [Điều kiện]
- When: [Hành động sai]
- Then: [Thông báo lỗi]

**AC3: [Edge Case]**
- Given: [Điều kiện đặc biệt]
- When: [Hành động]
- Then: [Kết quả xử lý biên]

### Notes
- Priority: [Must/Should/Could]
- Story Points: [1/2/3/5/8]
- Sprint: [Sprint X]
```

### Danh sách User Stories
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| ID | Story | Actor | Priority | Points |
|---|---|---|---|---|
| US-001 | Scan barcode để kiểm kê | Nhân viên kho | Must | 5 |
| US-002 | Xem báo cáo chênh lệch | Quản lý kho | Should | 3 |
```

## Sub-Skills (Kỹ năng con)
- Viết Acceptance Criteria (Given-When-Then)
- Story Splitting (Chia nhỏ Story)
- Story Mapping

## Business Rules
- BR-US-01: Mỗi User Story chỉ có 1 Actor duy nhất.
- BR-US-02: Mỗi User Story phải có ít nhất 3 Acceptance Criteria.
- BR-US-03: Story Point không vượt quá 8 (nếu vượt phải chia nhỏ).
- BR-US-04: User Story KHÔNG được chứa giải pháp kỹ thuật (Technical Solution).

## Edge Cases & Exceptions
- Yêu cầu quá lớn → Tách thành Epic + nhiều Story
- Yêu cầu kỹ thuật thuần (Refactoring) → Technical Story, không dùng As a...
- Acceptance Criteria mâu thuẫn nhau → PO phải quyết định

## Checklist
- [ ] Story có đúng format As a... I want to... So that...?
- [ ] Actor có cụ thể (không dùng 'User' chung chung)?
- [ ] Benefit có giá trị kinh doanh thật?
- [ ] Có ít nhất 3 Acceptance Criteria?
- [ ] AC có bao gồm Happy Path + Error + Edge Case?
- [ ] Story đủ nhỏ để hoàn thành trong 1 Sprint?
- [ ] Story tuân thủ INVEST?

## Example
### Ví dụ: User Story cho tính năng Kiểm kê kho

**US-042: Scan Barcode để kiểm kê**

**As a** Nhân viên kho
**I want to** quét mã vạch sản phẩm tại từng vị trí kệ và nhập số lượng đếm được
**So that** tôi có thể hoàn thành kiểm kê nhanh hơn 70% so với đếm tay và giảm sai sót

**AC1: Quét barcode thành công**
- Given: Nhân viên đang ở màn hình Kiểm kê, phiếu kiểm kê CC-001 đang mở
- When: Quét mã vạch SKU-A01 tại Location A-01-03
- Then: Hệ thống hiển thị tên sản phẩm "Sữa TH 1L", ô nhập số lượng sẵn sàng

**AC2: Quét barcode không tồn tại**
- Given: Nhân viên quét mã vạch không có trong hệ thống
- When: Hệ thống không tìm thấy SKU
- Then: Hiển thị thông báo lỗi "Mã vạch không hợp lệ" + Cho phép quét lại

**AC3: Mất kết nối mạng giữa chừng**
- Given: Nhân viên đang quét kiểm kê nhưng mất WiFi
- When: Quét thêm 5 sản phẩm trong chế độ Offline
- Then: Dữ liệu lưu local, tự đồng bộ lên server khi có mạng lại

## Related Skills
- Write BRD
- Write SRS
- Phân tích Use Case
- Viết Test Case
