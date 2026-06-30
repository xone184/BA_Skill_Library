# Phân tích Cross Docking

## Level
Level 2 - Business Skill

## Purpose
Phân tích quy trình hàng đến kho nhưng không lưu trữ mà chuyển thẳng ra cửa xuất (Cross-docking), nhằm giảm thời gian lưu kho và tăng tốc giao hàng.

## When to Use
Sử dụng khi kho trung chuyển, trung tâm phân phối cần tối ưu thời gian lưu hàng.

## Prerequisites
- Đã phân tích Inbound Flow
- Đã phân tích Outbound Flow

## Inputs
### ASN + SO đã match
- **Mô tả:** Hàng đến từ NCC đã có sẵn đơn hàng xuất đang chờ.
- **Bắt buộc:** Có
- **Ví dụ:** ASN từ NCC A giao 200 thùng → SO-101 cần 120 thùng, SO-102 cần 80 thùng

### Loại Cross-dock
- **Mô tả:** Pre-distributed (đã biết phân bổ trước) hay Post-distributed (phân bổ tại kho).
- **Bắt buộc:** Có
- **Ví dụ:** Pre-distributed: NCC đã đóng gói sẵn theo từng đơn hàng. Post-distributed: Kho phải phân loại lại.

## Process
### Bước 1: Nhận diện hàng Cross-dock
Hệ thống tự động nhận diện hàng đến có thể Cross-dock dựa trên SO đang chờ.

- Matching ASN items với SO items đang Pending
- Nếu match 100% → Full Cross-dock
- Nếu match một phần → Partial Cross-dock (phần dư Putaway bình thường)
- Flag hàng Cross-dock trên GRN để nhân viên biết

### Bước 2: Phân loại tại Staging (Sorting)
Hàng được dỡ xuống khu Staging và phân theo đơn hàng.

- Pre-distributed: Quét mã → Chuyển thẳng ra dock xuất tương ứng
- Post-distributed: Mở thùng → Chia hàng theo SO → Đóng gói lại
- Kiểm đếm nhanh (Quick Tally) để đảm bảo số lượng đúng

### Bước 3: Chuyển ra dock Outbound
Di chuyển hàng đã phân loại sang khu vực Shipping.

- Gán Shipping Label cho từng đơn
- Tập kết theo hãng vận chuyển hoặc tuyến đường
- Thời gian tồn tại tại Staging PHẢI < 24 giờ

## Outputs
### Quy trình Cross-dock
- **Định dạng:** Mermaid Flowchart
### Ma trận loại Cross-dock
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| Loại | Mô tả | Phù hợp khi |
|---|---|---|
| Pre-distributed | NCC đã chia sẵn | NCC có hệ thống tốt |
| Post-distributed | Kho chia tại chỗ | Nhiều đơn nhỏ |
| Hybrid | Kết hợp cả hai | Kho trung chuyển lớn |
```

## Sub-Skills (Kỹ năng con)
- Thiết kế Cross-dock Detection Rules
- Thiết kế Staging Layout

## Business Rules
- BR-WMS-XD-01: Hàng Cross-dock không được ở Staging quá 24 giờ.
- BR-WMS-XD-02: Chỉ cho phép Cross-dock khi có SO đang chờ match với hàng đến.
- BR-WMS-XD-03: Hàng Cross-dock vẫn phải được ghi nhận qua GRN (để Kế toán có chứng từ).

## Edge Cases & Exceptions
- SO bị hủy sau khi hàng đã dỡ xuống Staging → Putaway thay vì Cross-dock
- NCC giao thiếu so với ASN → Ưu tiên Cross-dock cho SO nào trước?

## Checklist
- [ ] Đã thiết kế rule tự động nhận diện hàng Cross-dock
- [ ] Đã phân biệt Pre-distributed vs Post-distributed
- [ ] Đã giới hạn thời gian hàng nằm tại Staging
- [ ] Đã có fallback (Putaway) khi không thể Cross-dock
- [ ] Đã ghi nhận GRN cho chứng từ kế toán

## Example
Xem Process.

## Related Skills
- Phân tích Inbound Flow
- Phân tích Outbound Flow
