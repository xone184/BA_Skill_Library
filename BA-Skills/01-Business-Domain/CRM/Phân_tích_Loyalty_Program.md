# Phân tích Loyalty Program

## Level
Level 2 - Business Skill

## Purpose
Phân tích hệ thống điểm thưởng và khách hàng thân thiết (Loyalty Program), bao gồm cơ chế tích điểm, cấu trúc hạng thành viên (Tier), quy đổi điểm, xử lý gian lận và tích hợp với POS/E-commerce.

## When to Use
Sử dụng khi doanh nghiệp bán lẻ, F&B, hoặc dịch vụ muốn xây dựng chương trình khách hàng thân thiết.

## Prerequisites
- Hiểu mô hình kinh doanh B2C
- Biết quy trình bán hàng

## Inputs
### Chính sách tích điểm
- **Mô tả:** Quy tắc quy đổi chi tiêu thành điểm thưởng.
- **Bắt buộc:** Có
- **Ví dụ:** Chi 10.000 VNĐ = 1 điểm. Mua ngày sinh nhật = x2 điểm.

### Cấu trúc hạng thành viên (Tier)
- **Mô tả:** Các mức thành viên và điều kiện thăng/giáng hạng.
- **Bắt buộc:** Có
- **Ví dụ:** Bạc (0-499 điểm), Vàng (500-1499), Kim Cương (1500+)

### Danh mục quà đổi (Reward Catalog)
- **Mô tả:** Những gì khách hàng có thể dùng điểm để đổi.
- **Bắt buộc:** Có
- **Ví dụ:** Voucher giảm 50k = 100 điểm, Sản phẩm miễn phí = 500 điểm

## Process
### Bước 1: Thiết kế cơ chế Tích điểm (Earn)
Xây dựng quy tắc quy đổi chi tiêu thành điểm.

- Tỷ lệ quy đổi cơ bản (Base rate)
- Bonus multiplier theo hạng thành viên (VD: Kim Cương x3)
- Bonus theo sự kiện (Sinh nhật, Lễ tết x2)
- Bonus theo sản phẩm/danh mục (Hàng mới x1.5)
- Điểm có thời hạn hay vĩnh viễn?

### Bước 2: Thiết kế cấu trúc Hạng (Tier)
Định nghĩa các hạng thành viên.

- Điều kiện lên hạng (Tổng chi tiêu / Tổng điểm trong 12 tháng)
- Chu kỳ đánh giá hạng (Hàng năm / Hàng quý)
- Quyền lợi mỗi hạng (Chiết khấu, Quà tặng, Ưu tiên)
- Quy tắc giáng hạng (Downgrade)

### Bước 3: Thiết kế cơ chế Đổi điểm (Redeem)
Quy trình sử dụng điểm.

- Đổi điểm lấy Voucher giảm giá
- Đổi điểm lấy sản phẩm miễn phí
- Thanh toán bằng điểm (Partial/Full)
- Tặng điểm cho người thân

### Bước 4: Xử lý hoàn trả & Gian lận (Return & Fraud)
Quy tắc trừ điểm khi hoàn trả và phát hiện gian lận.

- Hoàn hàng → Trừ lại số điểm tương ứng đã cộng
- Phát hiện giao dịch bất thường (Mua rồi trả ngay để lấy điểm)
- Giới hạn số lần đổi điểm/ngày
- Block tài khoản nghi ngờ gian lận

## Outputs
### Bảng cấu trúc Tier
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| Hạng | Điều kiện | Chiết khấu | Multiplier | Quyền lợi đặc biệt |
|---|---|---|---|---|
| Bạc | 0 - 499 điểm | 0% | x1 | Tích điểm cơ bản |
| Vàng | 500 - 1499 | 5% | x1.5 | Quà sinh nhật |
| Kim Cương | 1500+ | 10% | x2 | Ưu tiên hỗ trợ, Sự kiện VIP |
```

### Luật Tích/Trừ điểm
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| Sự kiện | Điểm | Ghi chú |
|---|---|---|
| Chi 10.000 VNĐ | +1 | Base rate |
| Mua ngày sinh nhật | x2 | Bonus |
| Hoàn hàng | -N | Trừ lại đúng số điểm đã cộng |
| Điểm quá hạn 12 tháng | -All | Hết hạn |
```

## Sub-Skills (Kỹ năng con)
- Thiết kế Point Earning Rules
- Thiết kế Tier Structure
- Thiết kế Redemption Flow
- Anti-fraud Logic

## Business Rules
- BR-LOY-01: Điểm chỉ được cộng sau khi giao dịch hoàn tất (không tính đơn hủy).
- BR-LOY-02: Hoàn hàng bắt buộc phải trừ lại điểm đã cộng cho giao dịch đó.
- BR-LOY-03: Điểm thưởng hết hạn sau 12 tháng nếu không sử dụng.
- BR-LOY-04: Tài khoản bị nghi ngờ gian lận sẽ bị đóng băng điểm.
- BR-LOY-05: Điểm không được chuyển nhượng giữa các tài khoản (trừ gói Gia đình).

## Edge Cases & Exceptions
- Khách hàng hoàn trả nhưng đã dùng điểm đó để đổi quà rồi → Xử lý sao?
- Hệ thống lỗi cộng nhầm điểm hàng loạt → Rollback procedure?
- Khách tạo nhiều tài khoản để lấy ưu đãi thành viên mới → Anti-fraud?

## Checklist
- [ ] Đã thiết kế tỷ lệ quy đổi (Earn rate) rõ ràng
- [ ] Đã thiết kế cấu trúc Tier với điều kiện lên/xuống hạng
- [ ] Đã có cơ chế đổi điểm (Redeem) đa dạng
- [ ] Đã xử lý trường hợp hoàn hàng (Trừ điểm)
- [ ] Đã có cơ chế chống gian lận (Anti-fraud)
- [ ] Đã có thời hạn điểm (Expiration)
- [ ] Đã tích hợp với POS/E-commerce

## Example
Xem Process section.

## Related Skills
- Phân tích Lead Management
- Phân tích Bán hàng tại quầy (POS)
