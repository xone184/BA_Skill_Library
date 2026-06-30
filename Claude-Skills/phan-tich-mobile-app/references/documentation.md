# Phân tích Mobile App

## Level
Level 2 - Business Skill

## Purpose
Phân tích và đặc tả các yêu cầu riêng biệt khi xây dựng ứng dụng di động (Mobile App) hoặc ứng dụng trên Máy tính bảng Công nghiệp (Rugged Tablet) dùng trực tiếp tại hiện trường (Shopfloor, Warehouse).

## When to Use
Sử dụng cho các dự án MES, WMS, hoặc App giao hàng, nơi người dùng thao tác trong môi trường khắc nghiệt, thao tác nhanh bằng phần cứng (máy quét).

## Prerequisites
- Đã có luồng nghiệp vụ cơ bản

## Inputs
### Mục đích App
- **Mô tả:** App này dùng để làm gì?
- **Bắt buộc:** Có
- **Ví dụ:** App cài trên Tablet tại máy CNC để công nhân nhận lệnh sản xuất.

## Process
### Bước 1: Phân tích Môi trường & Phần cứng (Hardware Context)
Dùng ở đâu, bằng cái gì?

- Thiết bị: iPad, Android Rugged Tablet, hay PDA Scanner?
- Môi trường: Sáng lóa (cần Contrast cao), Bụi bẩn (cần Icon to), Công nhân đeo găng tay (Touch target > 48dp).

### Bước 2: Tối ưu hóa thao tác nhập liệu (Data Entry)
Hạn chế gõ phím.

- Ưu tiên dùng Camera hoặc Máy quét tia laser (Barcode/QR code) thay cho gõ phím.
- Dùng màn hình Numpad to (như máy tính cầm tay) thay vì bàn phím QWERTY khi nhập số lượng.
- Hạn chế cuộn (Scrolling), 1 màn hình chỉ nên hiển thị vừa vặn 1 thao tác.

### Bước 3: Đặc tả tính năng Offline / Poor Network
Mạng ở xưởng thường rất yếu.

- Ứng dụng phải làm gì khi mất mạng mạng (VD: Lưu dữ liệu dưới Local DB/SQLite).
- Cơ chế Sync (Đồng bộ) tự động khi có mạng trở lại.
- Hiển thị icon trạng thái mạng rõ ràng.

### Bước 4: Luồng thông báo và Âm thanh
Tương tác phi hình ảnh.

- Quét mã đúng: App kêu 'Bíp' ngắn, rung 1 lần, nháy xanh.
- Quét mã sai: App kêu 'Tít tít tít', rung dài, nháy đỏ.

## Outputs
### Mobile/Tablet App Specification
- **Định dạng:** Markdown
- **Mẫu:**

```
### Đặc tả Tablet App: Trạm máy CNC

**1. Môi trường & Phần cứng**
- Thiết bị: Zebra Rugged Android Tablet 10-inch.
- Tương tác: Màn hình cảm ứng (Công nhân đeo găng tay vải).

**2. Yêu cầu UI/UX đặc thù**
- Kích thước nút tối thiểu: 60x60 pixels.
- Không dùng bàn phím chữ. Chỉ có bàn phím số (Numpad).
- Thao tác chính: Bấm cò súng quét mã QR, hệ thống tự động điền thông tin và nhảy sang bước tiếp theo không cần bấm Submit.

**3. Offline Mode & Đồng bộ**
- Nếu rớt mạng WIFI xưởng: Tablet vẫn cho phép bấm 'Nhập kho', dữ liệu đẩy vào hàng đợi (Queue local).
- Có biểu tượng đám mây gạch chéo góc phải màn hình.

**4. Phản hồi âm thanh**
- Lỗi nghiệp vụ -> Bật chuông cảnh báo lớn, rung 2 giây.
```

## Sub-Skills (Kỹ năng con)
- Offline Capability Design
- Hardware Interaction Design
- Shopfloor UX

## Business Rules
- BR-MOB-01: Số lần chạm (Tap) để hoàn thành một tác vụ lặp lại hàng ngày không được vượt quá 3 lần.
- BR-MOB-02: Dữ liệu thao tác tại hiện trường không bao giờ được phép mất (Bắt buộc thiết kế Offline Queue).

## Edge Cases & Exceptions
- Máy quét mã vạch bị hỏng laser -> Bắt buộc thiết kế ô Input dự phòng để công nhân gõ tay mã số vào.

## Checklist
- [ ] Đã tối ưu cho việc thao tác bằng găng tay chưa (Nút bấm to)?
- [ ] Đã loại bỏ tối đa việc gõ phím QWERTY chưa?
- [ ] Đã mô tả cơ chế Offline (mất mạng) chưa?
- [ ] Đã mô tả phản hồi âm thanh/đèn LED chưa?

## Example
Xem Mobile/Tablet App Specification trong Outputs.

## Related Skills
- Thiết kế Role-based UI
- Activity Diagram
