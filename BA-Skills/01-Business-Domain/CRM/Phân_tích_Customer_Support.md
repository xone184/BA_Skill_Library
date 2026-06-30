# Phân tích Customer Support

## Level
Level 2 - Business Skill

## Purpose
Phân tích toàn diện quy trình tiếp nhận và xử lý yêu cầu hỗ trợ khách hàng (Ticket Management), bao gồm phân loại ticket, escalation tự động, theo dõi SLA, đo lường CSAT/NPS và thiết kế Knowledge Base.

## When to Use
Sử dụng khi:
- Xây dựng module Customer Support / Helpdesk cho CRM.
- Doanh nghiệp cần quản lý yêu cầu hỗ trợ từ nhiều kênh (Email, Chat, Call, Social Media).
- Cần thiết kế SLA tự động và cảnh báo vi phạm.

## Prerequisites
- Hiểu các kênh liên hệ khách hàng
- Biết SLA là gì

## Inputs
### Kênh tiếp nhận (Support Channels)
- **Mô tả:** Tất cả các kênh mà khách hàng có thể gửi yêu cầu hỗ trợ.
- **Bắt buộc:** Có
- **Ví dụ:** Email, Hotline, Live Chat, Facebook Messenger, Zalo, Cổng tự phục vụ (Portal)

### Hợp đồng SLA (Service Level Agreement)
- **Mô tả:** Cam kết thời gian phản hồi và xử lý cho từng loại yêu cầu.
- **Bắt buộc:** Có
- **Ví dụ:** Critical: Phản hồi 1h / Giải quyết 4h. High: 4h / 8h. Medium: 8h / 24h. Low: 24h / 72h.

### Cấu trúc đội hỗ trợ (Support Tiers)
- **Mô tả:** Phân cấp đội ngũ xử lý theo mức độ chuyên môn.
- **Bắt buộc:** Có
- **Ví dụ:** Tier 1: Agent tổng đài (FAQ). Tier 2: Chuyên viên kỹ thuật. Tier 3: Dev/Vendor.

## Process
### Bước 1: Tiếp nhận & Tạo Ticket
Thiết kế cách hệ thống tiếp nhận yêu cầu từ mọi kênh và tạo Ticket tự động.

- Email gửi vào support@company.com → Tự động tạo Ticket
- Chat/Call → Agent tạo Ticket thủ công hoặc hệ thống tự động
- Portal → Khách hàng tự tạo Ticket và theo dõi trạng thái
- Social Media → Tích hợp chuyển thành Ticket

### Bước 2: Phân loại & Ưu tiên (Categorization & Priority)
Thiết kế quy tắc phân loại ticket tự động và thủ công.

- Phân loại theo Type: Bug, Feature Request, Question, Complaint
- Phân loại theo Module: CRM, WMS, MES, Kế toán
- Xác định Priority: Critical / High / Medium / Low
- Auto-priority: Keyword 'khẩn cấp', 'không hoạt động' → Tự động đặt Critical

### Bước 3: Routing & Assignment
Phân bổ ticket cho đúng người xử lý.

- Round-robin trong Tier 1
- Skill-based routing: Ticket về WMS → Gán cho agent chuyên WMS
- VIP routing: Khách hàng hạng Gold/Platinum → Ưu tiên xử lý trước

### Bước 4: Xử lý & Escalation
Quy trình xử lý và leo thang ticket.

- Tier 1 xử lý FAQ, hướng dẫn cơ bản
- Nếu không giải quyết được trong SLA → Escalate lên Tier 2
- Tier 2 xử lý vấn đề kỹ thuật, cấu hình
- Tier 3 xử lý bug, lỗi hệ thống, cần sửa code
- Auto-escalation: Ticket quá SLA tự động leo thang + gửi email cảnh báo cho Manager

### Bước 5: Đóng Ticket & Đo lường
Quy trình đóng ticket và thu thập phản hồi.

- Agent đóng ticket → Gửi khảo sát CSAT cho khách hàng
- Khách hàng xác nhận hoặc mở lại ticket nếu chưa hài lòng
- Tự động đóng ticket sau 7 ngày nếu khách không phản hồi
- Đo lường: First Response Time, Resolution Time, CSAT Score, Ticket Volume

## Outputs
### Quy trình quản lý Ticket (BPMN)
- **Định dạng:** Mermaid Flowchart
### Ma trận SLA
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| Priority | First Response | Resolution | Escalation |
|---|---|---|---|
| Critical | 1 giờ | 4 giờ | Auto → Tier 2 sau 2h |
| High | 4 giờ | 8 giờ | Auto → Tier 2 sau 6h |
| Medium | 8 giờ | 24 giờ | Alert Manager sau 20h |
| Low | 24 giờ | 72 giờ | Không auto-escalate |
```

### Ma trận phân quyền (Tier Matrix)
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| Loại vấn đề | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|
| Hướng dẫn sử dụng | ✅ | | |
| Reset mật khẩu | ✅ | | |
| Lỗi cấu hình | | ✅ | |
| Bug phần mềm | | | ✅ |
| Yêu cầu tùy chỉnh | | | ✅ |
```

## Sub-Skills (Kỹ năng con)
- Thiết kế SLA Matrix
- Thiết kế Escalation Rules
- Thiết kế Knowledge Base
- Thiết kế CSAT Survey

## Business Rules
- BR-SUP-01: Mọi yêu cầu từ khách hàng phải tạo Ticket, không xử lý ngoài hệ thống.
- BR-SUP-02: Ticket Critical phải được phản hồi trong vòng 1 giờ làm việc.
- BR-SUP-03: Ticket quá SLA phải tự động escalate và gửi cảnh báo.
- BR-SUP-04: Không được phép đóng Ticket nếu chưa có phản hồi từ khách hàng.
- BR-SUP-05: Mỗi Ticket đóng phải gửi khảo sát CSAT.

## Edge Cases & Exceptions
- Khách hàng gửi cùng 1 vấn đề qua Email + Chat → Tạo 1 hay 2 Ticket? (Merge)
- Ticket thuộc về nhiều module → Assign cho ai?
- Agent nghỉ phép → Ticket đang xử lý dở chuyển cho ai?
- Khách hàng spam Ticket → Cần rate limiting

## Checklist
- [ ] Đã xác định tất cả kênh tiếp nhận (Omnichannel)
- [ ] Đã thiết kế ma trận SLA với 4 mức Priority
- [ ] Đã thiết kế luồng Escalation tự động
- [ ] Đã thiết kế Tier 1/2/3 với phân quyền rõ ràng
- [ ] Đã có cơ chế Merge Ticket trùng lặp
- [ ] Đã thiết kế CSAT Survey sau khi đóng Ticket
- [ ] Đã có Dashboard theo dõi (Ticket Volume, SLA Compliance, CSAT)
- [ ] Đã thiết kế Knowledge Base cho self-service

## Example
Xem Process section.

## Related Skills
- Phân tích Lead Management
- Phân tích Loyalty Program
