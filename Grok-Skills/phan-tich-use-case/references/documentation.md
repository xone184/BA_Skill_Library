# Phân tích Use Case

## Level
Level 2 - Business Skill

## Purpose
Đặc tả siêu chi tiết sự tương tác giữa Người dùng (Actor) và Hệ thống (System) thông qua Use Case Specification. Kỹ năng này cung cấp sức mạnh để phân rã luồng chính (Basic Flow), luồng rẽ nhánh hợp lệ (Alternate Flow), luồng lỗi (Exception Flow). Đặc biệt hỗ trợ Micro-tasking (bóc tách 1 luồng nhỏ).

## When to Use
Sử dụng khi cần đặc tả yêu cầu chức năng một cách chi tiết theo góc nhìn tương tác người-máy. Rất hiệu quả khi User yêu cầu AI 'chỉ làm 1 phần nhỏ' (Micro-tasking).

## Prerequisites
- Đã xác định được các Actor trong hệ thống

## Inputs
### Mô tả tính năng
- **Mô tả:** Mô tả ngắn gọn về tính năng cần phân tích.
- **Bắt buộc:** Có
- **Ví dụ:** Tính năng Đăng nhập bằng Số điện thoại.

### Lệnh Micro-tasking (Tùy chọn)
- **Mô tả:** Lệnh yêu cầu AI chỉ thực thi 1 phần của Use Case.
- **Bắt buộc:** Không
- **Ví dụ:** Chỉ viết Exception Flows cho luồng gửi OTP.

## Process
### Bước 1: Xác định Use Case Profile
Thông tin cơ bản của Use Case.

- Actor (Ai thực hiện?)
- Pre-conditions (Điều kiện tiên quyết trước khi bắt đầu? VD: Đã mở app, chưa login)
- Post-conditions (Trạng thái hệ thống sau khi UC thành công? VD: Bảng Session tạo record mới)
- Includes / Extends (Có gọi Use Case khác không? VD: Include UC_Send_SMS)

### Bước 2: Thiết kế Basic Flow (Luồng chính/Happy Path)
Kịch bản mọi thứ diễn ra suôn sẻ.

- Đánh số thứ tự từng bước: 1, 2, 3...
- Bắt đầu bằng Actor action: 'User nhập SĐT và bấm Gửi OTP'
- Theo sau là System response: 'Hệ thống validate SĐT và gửi OTP qua SMS'

### Bước 3: Thiết kế Alternate Flows (Luồng rẽ nhánh hợp lệ)
Luồng đi đường vòng nhưng vẫn đạt kết quả.

- Chỉ định rõ nhánh này tách ra từ bước nào của Basic Flow (VD: Tại bước 2, User chọn Đăng nhập bằng Mật khẩu thay vì OTP)
- Mô tả các bước của luồng này
- Quay lại bước nào của Basic Flow hoặc Kết thúc?

### Bước 4: Thiết kế Exception Flows (Luồng lỗi/ngoại lệ)
Luồng gặp lỗi và không đạt kết quả.

- Tách ra từ bước nào? (VD: Tại bước 3, User nhập sai OTP)
- Hệ thống xử lý thế nào? (VD: Hiển thị lỗi 'OTP không đúng, còn 2 lần thử')
- Dừng Use Case hay cho User thử lại?

### Bước 5: Xử lý Micro-tasking (Theo yêu cầu)
Nếu người dùng có yêu cầu cụ thể (chỉ xuất 1 luồng).

- Nếu User bảo 'Chỉ viết Alternate Flow' → Bỏ qua Basic/Exception Flow, chỉ sinh ra Alternate.
- Nếu User bảo 'Tìm lỗ hổng trong luồng này' → Áp dụng Error Guessing để tìm các ngoại lệ bị sót.

## Outputs
### Use Case Specification
- **Định dạng:** Markdown Table & Lists
- **Mẫu:**

```
### UC-001: Đăng nhập bằng SĐT

**1. Profile**
- **Actor:** Khách hàng
- **Pre-condition:** Đã tải App.
- **Post-condition:** Đăng nhập thành công, tạo Token.

**2. Basic Flow**
1. User nhập SĐT và bấm 'Lấy OTP'.
2. System kiểm tra SĐT hợp lệ và gọi `UC_Send_SMS`.
3. System chuyển sang màn hình nhập OTP (đếm ngược 60s).
4. User nhập 6 số OTP.
5. System xác thực OTP đúng, sinh JWT Token.
6. System chuyển hướng vào Home Screen.

**3. Alternate Flows**
*3.1. Đăng nhập bằng Mật khẩu (Từ bước 1)*
- 1a1. User click 'Dùng Mật khẩu'.
- 1a2. System chuyển sang màn hình nhập Mật khẩu.
- 1a3. User nhập Mật khẩu và submit. (Quay lại bước 5).

**4. Exception Flows**
*4.1. SĐT không tồn tại (Từ bước 2)*
- 2e1. System phát hiện SĐT chưa đăng ký.
- 2e2. System báo lỗi 'Số điện thoại chưa đăng ký'. Use Case kết thúc.
```

## Sub-Skills (Kỹ năng con)
- Include/Extend Definition
- Micro-tasking Flow Extract
- Exception Handling Design

## Business Rules
- BR-UC-01: Mọi bước trong Basic Flow phải rõ ràng Chủ ngữ (User làm gì / System phản hồi gì).
- BR-UC-02: Alternate/Exception Flow PHẢI trỏ rõ ràng nó tách ra từ bước nào của Basic Flow (VD: 3a, 2e).
- BR-UC-03: Exception Flow phải ghi rõ là Kết thúc Use Case hay Quay lại bước nào.

## Edge Cases & Exceptions
- Tương tác với hệ thống ngoài (3rd Party) bị lỗi → Đưa vào Exception Flow
- Timeout (Quá thời gian nhập OTP) → Đưa vào Exception Flow

## Checklist
- [ ] Có Basic Flow rõ ràng (Actor-System ping pong)?
- [ ] Đã bóc tách Alternate Flows chưa?
- [ ] Đã xử lý đủ các Exception Flows (Validation, Timeout, Lỗi mạng)?
- [ ] Các luồng phụ có chỉ định rõ điểm bắt đầu từ Basic Flow không?
- [ ] Có đáp ứng đúng lệnh Micro-tasking của User không?

## Example
Xem Use Case Specification template trong phần Outputs.

## Related Skills
- Viết Test Case (Ultra)
- Write SRS (Ultra)
