# Phân tích Lead Management

## Level
Level 2 - Business Skill

## Purpose
Phân tích toàn diện quy trình quản lý khách hàng tiềm năng (Lead), từ lúc tiếp nhận thông tin đến khi chuyển đổi thành cơ hội bán hàng (Opportunity), bao gồm quy tắc chấm điểm (Scoring), phân bổ (Routing) và chống trùng lặp (Deduplication).

## When to Use
Sử dụng khi:
- Doanh nghiệp cần xây dựng hệ thống CRM mới có module quản lý Lead.
- Muốn cải thiện tỷ lệ chuyển đổi Lead thành khách hàng.
- Cần tích hợp nhiều kênh Marketing (Website, Facebook, Zalo, Google Ads) vào một hệ thống duy nhất.

## Prerequisites
- Hiểu cơ bản về Sales Funnel
- Biết quy trình bán hàng của doanh nghiệp

## Inputs
### Nguồn Lead (Lead Sources)
- **Mô tả:** Danh sách tất cả các kênh mà doanh nghiệp thu thập khách hàng tiềm năng.
- **Bắt buộc:** Có
- **Ví dụ:** Website form, Facebook Ads, Zalo OA, Giới thiệu, Sự kiện, Cold Call

### Trạng thái Lead (Lead Status)
- **Mô tả:** Các giai đoạn mà một Lead sẽ trải qua trong vòng đời.
- **Bắt buộc:** Có
- **Ví dụ:** New → Contacted → Qualified → Converted / Disqualified

### Tiêu chí chấm điểm (Scoring Criteria)
- **Mô tả:** Các yếu tố để chấm điểm mức độ tiềm năng của Lead.
- **Bắt buộc:** Không
- **Ví dụ:** Ngân sách > 100tr = +20 điểm, Đã xem demo = +30 điểm, Không trả lời 3 ngày = -10 điểm

### Kênh Marketing
- **Mô tả:** Các kênh quảng cáo đang chạy để tracking nguồn Lead.
- **Bắt buộc:** Không
- **Ví dụ:** Google Ads, Facebook, SEO, Email Marketing

## Process
### Bước 1: Thu thập và Ghi nhận Lead
Phân tích tất cả các điểm chạm (Touchpoints) mà khách hàng tiềm năng có thể liên hệ với doanh nghiệp. Đảm bảo mọi kênh đều tự động tạo Lead trong hệ thống.

- Liệt kê toàn bộ kênh thu thập Lead (Online & Offline)
- Xác định trường dữ liệu bắt buộc khi tạo Lead (Họ tên, SĐT, Email, Nguồn)
- Thiết kế rule tự động tạo Lead từ Web form, Landing page, Chatbot
- Quy định cách nhập Lead thủ công (Import Excel, Nhập tay)

### Bước 2: Chống trùng lặp (Deduplication)
Thiết kế quy tắc phát hiện và xử lý Lead trùng lặp để đảm bảo dữ liệu sạch.

- Xác định trường khóa chống trùng (SĐT, Email, hoặc cả hai)
- Khi phát hiện trùng: Merge (Gộp), Block (Chặn tạo mới), hay Alert (Cảnh báo)?
- Quy tắc ưu tiên dữ liệu khi Merge (Giữ bản gốc hay bản mới hơn?)

### Bước 3: Chấm điểm Lead (Lead Scoring)
Thiết kế hệ thống scoring tự động để xếp hạng mức độ tiềm năng.

- Scoring theo hồ sơ (Demographic): Ngành nghề, Quy mô, Vị trí
- Scoring theo hành vi (Behavioral): Xem trang báo giá, Tải tài liệu, Đăng ký demo
- Xác định ngưỡng (Threshold): Bao nhiêu điểm thì chuyển thành MQL (Marketing Qualified Lead)?
- Bao nhiêu điểm thì chuyển thành SQL (Sales Qualified Lead)?

### Bước 4: Phân bổ Lead (Lead Routing)
Thiết kế quy tắc tự động gán Lead cho nhân viên kinh doanh phù hợp.

- Phân bổ theo khu vực địa lý (Territory)
- Phân bổ theo ngành (Industry Vertical)
- Phân bổ Round-robin (Lần lượt công bằng)
- Phân bổ theo Workload (Ai có ít Lead nhất thì nhận)

### Bước 5: Nuôi dưỡng Lead (Lead Nurturing)
Thiết kế quy trình chăm sóc Lead chưa sẵn sàng mua.

- Email tự động theo chuỗi (Drip Campaign)
- Nhắc việc gọi lại cho Sales (Follow-up Reminder)
- Gửi nội dung giáo dục (Content Marketing)

### Bước 6: Chuyển đổi Lead (Lead Conversion)
Thiết kế quy trình chuyển Lead thành Account + Contact + Opportunity.

- Dữ liệu Lead nào map sang Account? (Tên công ty, Địa chỉ)
- Dữ liệu Lead nào map sang Contact? (Tên người, SĐT, Email)
- Tự động tạo Opportunity kèm theo hay không?
- Lead sau khi convert thì xóa hay giữ lại để truy vết?

## Outputs
### Quy trình Lead Lifecycle (BPMN)
- **Định dạng:** Sơ đồ BPMN hoặc Mermaid Flowchart
- **Mẫu:**

```
graph TD
    A[Tiếp nhận Lead] --> B{Trùng lặp?}
    B -->|Có| C[Merge/Alert]
    B -->|Không| D[Lead Scoring]
    D --> E{Score >= Threshold?}
    E -->|Có| F[Assign to Sales]
    E -->|Không| G[Nurturing Campaign]
    F --> H[Contact & Qualify]
    H --> I{Qualified?}
    I -->|Có| J[Convert to Opportunity]
    I -->|Không| K[Disqualified]
```

### Cấu trúc dữ liệu Lead
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| Tên trường | Kiểu dữ liệu | Bắt buộc | Mô tả |
|---|---|---|---|
| lead_id | INT (PK) | Có | Mã Lead tự tăng |
| full_name | VARCHAR(200) | Có | Họ và tên |
| phone | VARCHAR(20) | Có | Số điện thoại |
| email | VARCHAR(100) | Không | Email |
| source | ENUM | Có | Nguồn Lead |
| status | ENUM | Có | Trạng thái Lead |
| score | INT | Không | Điểm Lead |
| assigned_to | INT (FK) | Không | Nhân viên phụ trách |
| created_at | DATETIME | Có | Ngày tạo |
```

### Ma trận Lead Scoring
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| Tiêu chí | Điều kiện | Điểm |
|---|---|---|
| Ngành nghề | Sản xuất, Bán lẻ | +20 |
| Quy mô | > 100 nhân viên | +15 |
| Đã xem Demo | Có | +30 |
| Không phản hồi | > 7 ngày | -15 |
```

## Sub-Skills (Kỹ năng con)
- Thiết kế Lead Scoring Model
- Thiết kế Deduplication Rules
- Thiết kế Lead Routing Rules
- Thiết kế Nurturing Campaign

## Business Rules
- BR-CRM-LEAD-01: Mỗi Lead bắt buộc phải có ít nhất SĐT hoặc Email.
- BR-CRM-LEAD-02: Lead mới tạo phải được gán cho Sales trong vòng 24 giờ.
- BR-CRM-LEAD-03: Lead không có tương tác sau 90 ngày sẽ tự động chuyển sang trạng thái 'Dormant'.
- BR-CRM-LEAD-04: Không cho phép tạo Lead trùng SĐT với Lead đang ở trạng thái Active.
- BR-CRM-LEAD-05: Lead Score phải được tính lại mỗi khi có hành vi mới.

## Edge Cases & Exceptions
- Lead có cả SĐT cá nhân và SĐT công ty → Chọn SĐT nào làm khóa chống trùng?
- Một người nhưng đại diện cho nhiều công ty → Tạo nhiều Lead hay gộp?
- Lead đã Disqualified quay lại hỏi mua → Mở lại Lead cũ hay tạo mới?
- Lead từ đối thủ cạnh tranh giả mạo khách hàng → Cần rule phát hiện.
- Import 10.000 Lead từ Excel cùng lúc → Xử lý trùng lặp hàng loạt ra sao?

## Checklist
- [ ] Đã xác định đủ tất cả nguồn Lead (Online + Offline)
- [ ] Đã thiết kế quy tắc chống trùng lặp (Deduplication)
- [ ] Đã thiết kế mô hình Lead Scoring
- [ ] Đã thiết kế quy tắc phân bổ Lead (Routing)
- [ ] Đã thiết kế luồng Nurturing cho Lead chưa qualified
- [ ] Đã thiết kế quy trình Convert Lead → Account/Contact/Opportunity
- [ ] Đã xác định SLA phản hồi Lead (ví dụ: < 24 giờ)
- [ ] Đã thiết kế Dashboard theo dõi Lead (Số lượng, Tỷ lệ chuyển đổi, Nguồn hiệu quả nhất)
- [ ] Đã thiết kế cảnh báo (Notification) cho Sales khi có Lead mới
- [ ] Đã thiết kế báo cáo ROI theo kênh Marketing

## Example
### Ví dụ: Công ty ABC (Phần mềm ERP) muốn xây dựng module Lead Management

**Input từ khách hàng:**
- Nguồn Lead: Website (40%), Facebook Ads (30%), Giới thiệu (20%), Sự kiện (10%)
- Đội Sales: 10 người, chia theo 3 khu vực (Bắc, Trung, Nam)
- Mục tiêu: Tăng tỷ lệ chuyển đổi từ 5% lên 15%

**Output của BA:**
1. Lead Lifecycle gồm 6 trạng thái: New → Contacted → Qualified → Proposal → Won / Lost
2. Scoring Model: Website form = +10, Download brochure = +20, Request demo = +40, Budget > 500tr = +30
3. Routing: Lead Bắc → Team A, Lead Trung → Team B, Lead Nam → Team C
4. SLA: Lead mới phải được gọi trong vòng 4 giờ làm việc
5. Dedup: Trùng SĐT → Alert cho Sales, Trùng Email → Auto-merge

## Related Skills
- Phân tích Opportunity
- Phân tích Customer Support
- Phân tích Loyalty Program
