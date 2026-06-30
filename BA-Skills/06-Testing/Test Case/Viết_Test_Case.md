# Viết Test Case

## Level
Level 1 - Basic Skill

## Purpose
Viết kịch bản kiểm thử (Test Case) chi tiết dựa trên Requirement/User Story để đảm bảo tính năng hoạt động đúng nghiệp vụ. Test Case phải rõ ràng đến mức bất kỳ ai (BA, QC, Khách hàng) đều có thể đọc và thực hiện được.

## When to Use
Sử dụng sau khi chốt Requirement hoặc trong Sprint để QC/BA thực hiện test trước khi UAT.

## Prerequisites
- Đã có User Story / SRS đã duyệt

## Inputs
### Requirement (User Story / SRS)
- **Mô tả:** Tài liệu đầu vào mô tả tính năng.
- **Bắt buộc:** Có
- **Ví dụ:** User Story: Khách hàng thanh toán giỏ hàng bằng thẻ tín dụng. AC: Thẻ hợp lệ → Thành công. Thẻ hết hạn → Từ chối.

## Process
### Bước 1: Phân tích Acceptance Criteria
Từ AC, xác định các kịch bản cần test.

- 1 AC thường tạo ra nhiều Test Cases
- Xác định Happy Path (Kịch bản chuẩn, mọi thứ đều đúng)
- Xác định Negative Path (Nhập sai, lỗi hệ thống, thiếu quyền)
- Xác định Boundary Value (Giá trị biên: Giới hạn ký tự, số tiền tối thiểu/tối đa)

### Bước 2: Thiết lập Pre-conditions
Điều kiện cần thiết trước khi chạy test.

- Tài khoản (VD: Đăng nhập bằng Role Admin)
- Dữ liệu sẵn có (VD: Đơn hàng số #123 đang ở trạng thái Pending)
- Cấu hình hệ thống (VD: Đã bật tính năng thanh toán VNPay)

### Bước 3: Viết các bước thực hiện (Test Steps)
Liệt kê thao tác từng bước một.

- Bước phải cụ thể, thao tác trên giao diện: Click nút X, Nhập Y vào ô Z
- Không ghi chung chung (VD: 'Thanh toán đơn hàng' là sai. Phải là 'Click Thanh toán → Chọn VNPay → Nhập thẻ → Bấm Submit')

### Bước 4: Xác định Expected Result
Kết quả mong đợi sau khi thực hiện thao tác.

- Hệ thống phải hiển thị cái gì? (VD: Thông báo 'Thành công' màu xanh)
- Dữ liệu thay đổi thế nào? (VD: Trạng thái đơn đổi thành 'Paid')
- Email/SMS có được gửi không?

### Bước 5: Review & Cập nhật Traceability
Đảm bảo Test Case phủ hết Requirement.

- Mỗi Test Case phải link về Requirement ID / User Story ID
- Kiểm tra xem có AC nào chưa có Test Case tương ứng không?

## Outputs
### Test Case Document
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| TC ID | Requirement ID | Tên Test Case | Pre-conditions | Test Steps | Expected Result | Priority |
|---|---|---|---|---|---|---|
| TC-001 | US-PAY-01 | Thanh toán thành công thẻ tín dụng | User đã login, Giỏ hàng có sp | 1. Chọn CC<br>2. Nhập số thẻ hợp lệ<br>3. Bấm Thanh toán | Hiện popup 'Thành công'. Đơn hàng chuyển 'Paid' | High |
| TC-002 | US-PAY-01 | Thanh toán thẻ hết hạn | User đã login | 1. Chọn CC<br>2. Nhập số thẻ hết hạn<br>3. Bấm Thanh toán | Báo lỗi 'Thẻ hết hạn'. Đơn vẫn 'Pending' | Medium |
```

## Sub-Skills (Kỹ năng con)
- Equivalence Partitioning (Phân vùng tương đương)
- Boundary Value Analysis (Phân tích giá trị biên)
- Error Guessing

## Business Rules
- BR-TC-01: Mỗi Test Case chỉ nên test 1 kịch bản cụ thể.
- BR-TC-02: Test Steps phải rõ ràng, có thể lặp lại (Repeatable) với kết quả nhất quán.
- BR-TC-03: Expected Result phải bao gồm UI (Giao diện) và Data (Dữ liệu).
- BR-TC-04: Luôn có Test Case cho trường hợp dữ liệu rỗng (Empty/Null) nếu là Form.

## Edge Cases & Exceptions
- Test tích hợp (Integration): Hệ thống bên thứ 3 chậm/không phản hồi (Timeout)
- Test đồng thời (Concurrency): 2 người cùng mua món hàng cuối cùng

## Checklist
- [ ] Đã có Happy Path?
- [ ] Đã có Negative Path (Lỗi nghiệp vụ)?
- [ ] Đã test giá trị biên (Min/Max)?
- [ ] Pre-conditions đã rõ ràng?
- [ ] Test Steps có thao tác được không?
- [ ] Expected Result có đo lường/quan sát được không?
- [ ] Đã cover hết Acceptance Criteria?

## Example
Xem Test Case mẫu trong Outputs.

## Related Skills
- Write User Story
- Phân tích CRUD
- UAT
