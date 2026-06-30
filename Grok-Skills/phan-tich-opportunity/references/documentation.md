# Phân tích Opportunity

## Level
Level 2 - Business Skill

## Purpose
Phân tích toàn diện luồng cơ hội bán hàng (Opportunity/Deal) từ khi Lead chuyển đổi đến khi ký hợp đồng hoặc mất cơ hội, bao gồm các giai đoạn (Stages), tỷ lệ thắng (Win Probability), dự báo doanh thu (Revenue Forecasting) và quy trình phê duyệt báo giá.

## When to Use
Sử dụng khi:
- Xây dựng module Sales Pipeline cho hệ thống CRM.
- Doanh nghiệp cần dự báo doanh thu chính xác hơn.
- Cần thiết kế luồng phê duyệt báo giá/chiết khấu nhiều cấp.

## Prerequisites
- Đã hoàn thành Phân tích Lead Management
- Hiểu quy trình bán hàng B2B/B2C

## Inputs
### Giai đoạn bán hàng (Sales Stages)
- **Mô tả:** Các bước trong quy trình bán hàng từ lúc có cơ hội đến khi chốt.
- **Bắt buộc:** Có
- **Ví dụ:** Qualification → Needs Analysis → Proposal → Negotiation → Closed Won/Lost

### Sản phẩm/Dịch vụ
- **Mô tả:** Danh mục sản phẩm bán kèm giá.
- **Bắt buộc:** Có
- **Ví dụ:** Phần mềm ERP = 500tr, Module WMS = 200tr, Tùy chỉnh = 100tr/ngày

### Ma trận phê duyệt chiết khấu
- **Mô tả:** Ai được duyệt chiết khấu bao nhiêu %.
- **Bắt buộc:** Không
- **Ví dụ:** Sales: ≤5%, Manager: ≤15%, Director: ≤30%

## Process
### Bước 1: Định nghĩa Sales Stages
Thiết kế các giai đoạn trong Sales Pipeline. Mỗi giai đoạn phải có tiêu chí vào (Entry Criteria) và tỷ lệ thắng tham khảo.

- Liệt kê tối đa 6-8 Stages (Ít hơn = Sales dễ dùng hơn)
- Mỗi Stage phải có Entry Criteria rõ ràng (VD: Đã gửi Proposal → mới được chuyển sang Negotiation)
- Gán Probability % cho mỗi Stage (VD: Qualification = 10%, Proposal = 50%, Negotiation = 75%)
- Xác định Stage nào bắt buộc (Mandatory) và Stage nào có thể bỏ qua (Optional)

### Bước 2: Thiết kế Cấu trúc Opportunity
Xác định các trường dữ liệu cần thiết trên bản ghi Opportunity.

- Trường bắt buộc: Tên Opportunity, Account, Amount, Close Date, Stage, Owner
- Trường bổ sung: Nguồn (Source), Đối thủ (Competitor), Next Step, Ghi chú
- Opportunity Products: Cho phép thêm nhiều sản phẩm vào 1 Opportunity
- Lịch sử thay đổi Stage (Stage History) để theo dõi tốc độ di chuyển

### Bước 3: Thiết kế luồng Quotation
Quy trình tạo và phê duyệt báo giá.

- Tạo Quotation từ Opportunity (Kéo sản phẩm, đơn giá, số lượng)
- Áp dụng chiết khấu và kiểm tra ngưỡng phê duyệt
- Luồng duyệt: Sales tạo → Manager duyệt → Gửi khách hàng
- Cho phép tạo nhiều phiên bản Quotation (v1, v2, v3)

### Bước 4: Thiết kế Revenue Forecasting
Xây dựng cơ chế dự báo doanh thu.

- Forecast = Tổng(Amount × Probability) của tất cả Opportunity
- Chia Forecast theo tháng/quý/năm
- Forecast Category: Pipeline, Best Case, Commit, Closed
- Dashboard hiển thị Target vs Actual vs Forecast

### Bước 5: Xử lý Closed Lost
Thiết kế quy trình khi mất cơ hội.

- Bắt buộc nhập Lost Reason (Giá cao, Đối thủ, Không có ngân sách, Timing)
- Bắt buộc nhập Competitor nếu lý do là Đối thủ
- Tự động tạo Reminder 6 tháng sau để re-engage

## Outputs
### Sales Pipeline Design
- **Định dạng:** Markdown Table + BPMN
- **Mẫu:**

```
| Stage | Entry Criteria | Probability | Activities |
|---|---|---|---|
| Qualification | Lead converted | 10% | Xác nhận nhu cầu, ngân sách |
| Needs Analysis | Khách xác nhận quan tâm | 25% | Demo, khảo sát chi tiết |
| Proposal | Đã hiểu rõ scope | 50% | Gửi báo giá |
| Negotiation | Khách đồng ý về scope | 75% | Thương lượng giá, hợp đồng |
| Closed Won | Ký hợp đồng | 100% | Bàn giao cho triển khai |
| Closed Lost | Khách từ chối | 0% | Ghi nhận lý do |
```

### Cấu trúc dữ liệu Opportunity
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| Trường | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| opp_id | INT (PK) | Có | Mã cơ hội |
| opp_name | VARCHAR(200) | Có | Tên cơ hội |
| account_id | INT (FK) | Có | Khách hàng |
| amount | DECIMAL | Có | Giá trị |
| close_date | DATE | Có | Ngày dự kiến chốt |
| stage | ENUM | Có | Giai đoạn |
| probability | INT | Có | % thắng |
| lost_reason | ENUM | Không | Lý do thua |
```

## Sub-Skills (Kỹ năng con)
- Thiết kế Sales Pipeline
- Thiết kế Quotation Approval
- Thiết kế Revenue Forecasting
- Phân tích Lost Reason

## Business Rules
- BR-CRM-OPP-01: Opportunity bắt buộc phải liên kết với Account.
- BR-CRM-OPP-02: Khi chuyển sang Closed Lost, phải nhập Lost Reason.
- BR-CRM-OPP-03: Chiết khấu > 5% phải qua Manager duyệt, > 15% phải qua Director.
- BR-CRM-OPP-04: Close Date không được là ngày trong quá khứ.
- BR-CRM-OPP-05: Probability % tự động theo Stage nhưng Sales có thể override.

## Edge Cases & Exceptions
- Opportunity đã Closed Won nhưng khách hàng hủy hợp đồng → Rollback hay tạo mới?
- Một Account có nhiều Opportunity cùng lúc → Hiển thị tổng giá trị ra sao?
- Sales nghỉ việc → Opportunity chuyển cho ai?
- Opportunity kéo dài > 6 tháng không chuyển Stage → Cảnh báo Stale Deal

## Checklist
- [ ] Đã định nghĩa đủ Sales Stages với Entry Criteria
- [ ] Đã gán Probability % cho mỗi Stage
- [ ] Đã thiết kế luồng phê duyệt chiết khấu (Discount Approval)
- [ ] Đã bắt buộc nhập Lost Reason khi đóng cơ hội
- [ ] Đã thiết kế Forecasting Dashboard
- [ ] Đã có cơ chế cảnh báo Stale Deal (Deal quá lâu không chuyển Stage)
- [ ] Đã có quy trình re-assign khi Sales nghỉ việc
- [ ] Đã tích hợp với module Quotation/Contract

## Example
Xem mô tả trong phần Process.

## Related Skills
- Phân tích Lead Management
- Thiết kế API Contract
- Write BRD
