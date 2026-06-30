# Thiết kế Notification

## Level
Level 1 - Basic Skill

## Purpose
Thiết kế nội dung, điều kiện kích hoạt (Trigger), đối tượng nhận và cấu trúc cho các mẫu thông báo đa kênh (Email, SMS, Push Notification, In-app).

## When to Use
Sử dụng khi hệ thống cần gửi thông báo (VD: Đăng ký thành công, Quên mật khẩu, Có đơn hàng mới, Cảnh báo tồn kho).

## Prerequisites
- Đã có SRS hoặc luồng quy trình

## Inputs
### Sự kiện (Event)
- **Mô tả:** Hành động kích hoạt thông báo.
- **Bắt buộc:** Có
- **Ví dụ:** Sự kiện: Khách hàng đặt hàng thành công.

### Loại thông báo
- **Mô tả:** Kênh gửi.
- **Bắt buộc:** Có
- **Ví dụ:** Email (gửi khách hàng), In-app (gửi Admin).

## Process
### Bước 1: Xác định Trigger & Recipient
Khi nào gửi và gửi cho ai?

- Trigger: Hành động kích hoạt (VD: SO status change to 'Paid')
- Recipient: Người nhận (VD: Email mua hàng, Quản lý kho, Admin)

### Bước 2: Chọn Kênh (Channel) phù hợp
Email, SMS hay Push?

- Email: Gửi tài liệu dài, hóa đơn, OTP (nếu không gấp)
- SMS: Gửi OTP, thông báo giao hàng gấp (chi phí cao)
- Push Notification (Mobile): Nhắc nhở app, promotion
- In-app Notification (Web): Thông báo hệ thống, duyệt đơn

### Bước 3: Thiết kế nội dung (Copywriting)
Viết nội dung thông báo.

- Tiêu đề (Subject): Ngắn gọn, rõ mục đích (VD: Xác nhận đơn hàng #12345)
- Lời chào: Cá nhân hóa (VD: Chào {{customer_name}})
- Nội dung chính: Đi thẳng vào vấn đề
- Call-to-Action (CTA): Nút hành động (VD: [Xem chi tiết đơn hàng])

### Bước 4: Xác định Biến (Variables/Dynamic Data)
Các trường dữ liệu động.

- Sử dụng syntax {{variable_name}}
- VD: {{order_id}}, {{total_amount}}, {{payment_method}}, {{reset_link}}

### Bước 5: Quy định tần suất & Ràng buộc
Chống spam.

- Không gửi SMS quá 3 lần/ngày cho 1 số
- Gom thông báo (Batching): VD Gửi email tổng hợp cuối ngày thay vì gửi từng email

## Outputs
### Notification Matrix
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| ID | Event Trigger | Channel | Recipient | Subject / Title | Variables |
|---|---|---|---|---|---|
| NTF-01 | Đặt hàng thành công | Email | Customer | Xác nhận đơn hàng {{order_id}} | {{customer_name}}, {{order_id}}, {{total_amount}} |
| NTF-02 | Có đơn hàng mới | In-app | Admin | Đơn hàng mới từ {{customer_name}} | {{customer_name}}, {{order_id}} |
```

### Email Template Detail
- **Định dạng:** Markdown
- **Mẫu:**

```
**Template ID:** TPL-EMAIL-01
**Event:** Reset Password
**Subject:** Yêu cầu đặt lại mật khẩu của bạn

**Body:**
Chào {{user_name}},

Chúng tôi nhận được yêu cầu đặt lại mật khẩu cho tài khoản liên kết với email này. Vui lòng click vào nút bên dưới để thiết lập mật khẩu mới:

[ĐẶT LẠI MẬT KHẨU] (Link to: {{reset_link}})

*Link này sẽ hết hạn sau {{expire_time}} phút.*

Nếu bạn không thực hiện yêu cầu này, vui lòng bỏ qua email.

Trân trọng,
Team Hỗ trợ.
```

## Sub-Skills (Kỹ năng con)
- UX Copywriting
- Variable Mapping
- Channel Selection

## Business Rules
- BR-NTF-01: Mọi Email thông báo phải có link Unsubscribe (nếu là Marketing).
- BR-NTF-02: Thông báo OTP phải có thời gian hết hạn rõ ràng.
- BR-NTF-03: Nội dung In-app / Push không dài quá 100 ký tự.
- BR-NTF-04: Phải cá nhân hóa lời chào (Chèn Tên).

## Edge Cases & Exceptions
- Gửi thất bại (Bounced/Failed) → Hệ thống tự động retry 3 lần
- Khách hàng tắt nhận thông báo (Opt-out) → Chỉ gửi các thông báo cực kỳ quan trọng (OTP, Hóa đơn)

## Checklist
- [ ] Đã xác định đúng Trigger Event?
- [ ] Đã chọn đúng Kênh (Email/SMS/In-app)?
- [ ] Đã thiết kế tiêu đề (Subject) rõ ràng?
- [ ] Đã cá nhân hóa bằng Biến (Variables)?
- [ ] Đã có nút CTA (Call to action)?
- [ ] Đã thiết kế nội dung khi Lỗi (VD: Gửi lại mã)?

## Example
Xem Notification Matrix và Template trong Outputs.

## Related Skills
- Phân tích CRUD
- Write SRS
