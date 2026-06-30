# Sprint Planning

## Level
Level 2 - Business Skill

## Purpose
Hỗ trợ Product Owner (PO) và Scrum Team lập kế hoạch cho một Sprint, bao gồm: xác định Sprint Goal, chọn User Stories từ Backlog, estimate effort (Story Points) và lập Sprint Backlog.

## When to Use
Sử dụng vào ngày đầu tiên của mỗi Sprint.

## Prerequisites
- Đã có Product Backlog được ưu tiên (Groomed)
- Team biết Capacity của mình

## Inputs
### Product Backlog
- **Mô tả:** Danh sách User Stories đã sẵn sàng (Ready).
- **Bắt buộc:** Có
- **Ví dụ:** Top 10 User Stories đã có Acceptance Criteria.

### Team Capacity
- **Mô tả:** Tổng số Story Points hoặc Giờ team có thể làm trong Sprint này.
- **Bắt buộc:** Có
- **Ví dụ:** Team có 5 Dev, làm 2 tuần. Capacity = 40 Story Points. Trừ đi ngày lễ, nghỉ phép.

## Process
### Bước 1: Xác định Sprint Goal
Mục tiêu kinh doanh của Sprint này là gì?

- PO đưa ra mục tiêu. VD: 'Hoàn thành luồng thanh toán qua VNPay'
- Goal phải ngắn gọn, truyền cảm hứng, và đo lường được

### Bước 2: Chọn Item từ Product Backlog
Kéo các item phù hợp với Goal vào Sprint.

- Bắt đầu từ item ưu tiên cao nhất
- Chỉ chọn những item thỏa mãn Definition of Ready (Đã rõ ràng, có AC, có Mockup)

### Bước 3: Estimation (Ước lượng)
Team Dev ước lượng độ lớn của từng item.

- Sử dụng Planning Poker (Fibonacci: 1, 2, 3, 5, 8, 13)
- Nếu item > 8 points → Bắt buộc phải chia nhỏ (Story Splitting)
- Chỉ Dev mới có quyền estimate, PO/BA chỉ giải thích nghiệp vụ

### Bước 4: Lập Task (Phân rã kỹ thuật)
Dev chia Story thành các sub-tasks.

- 1 User Story → Task DB, Task API, Task Frontend, Task QC
- Task thường estimate bằng giờ (1-8 giờ)

### Bước 5: Chốt Sprint Backlog (Commitment)
Kiểm tra xem khối lượng công việc có vượt quá Capacity không.

- Tổng Story Points được chọn <= Team Capacity
- Nếu vượt quá → Đẩy bớt item độ ưu tiên thấp xuống cuối Sprint hoặc trả về Backlog
- Team cam kết (Commit) hoàn thành Sprint Goal

## Outputs
### Sprint Plan Document
- **Định dạng:** Markdown Table
- **Mẫu:**

```
# Sprint [N] Planning
**Sprint Goal:** Hoàn thành luồng thanh toán VNPay.
**Capacity:** 40 Story Points.

## Sprint Backlog
| ID | User Story | Priority | Points | Status (DOR) |
|---|---|---|---|---|
| US-20 | Tích hợp API VNPay | High | 5 | Ready |
| US-21 | Giao diện nút thanh toán VNPay | High | 3 | Ready |
| US-22 | Webhook nhận kết quả từ VNPay | High | 5 | Ready |
| US-25 | Báo cáo giao dịch lỗi | Medium | 8 | Ready |

**Total Points Committed:** 21 / 40 (Sẽ kéo thêm Bug/Tech debt)
```

## Sub-Skills (Kỹ năng con)
- Story Splitting
- Planning Poker
- Capacity Calculation

## Business Rules
- BR-SPRINT-01: KHÔNG đưa item chưa thỏa mãn Definition of Ready vào Sprint.
- BR-SPRINT-02: Item > 8 points phải được chia nhỏ.
- BR-SPRINT-03: Không thay đổi Sprint Goal sau khi Sprint đã bắt đầu.
- BR-SPRINT-04: Team không nhận khối lượng công việc vượt quá Capacity đã thống nhất.

## Edge Cases & Exceptions
- Có task Support/Hotfix gấp giữa Sprint → Phải bỏ bớt 1 Story có điểm tương đương ra khỏi Sprint
- Thiếu chuyên môn trong team (VD: Thiếu QA) → Ảnh hưởng capacity, cần cân nhắc

## Checklist
- [ ] Đã có Sprint Goal?
- [ ] Đã tính Team Capacity (trừ ngày nghỉ)?
- [ ] Tất cả item chọn đều 'Ready' (Có AC)?
- [ ] Không có item nào > 8 points?
- [ ] Tổng points <= Capacity?
- [ ] Team đã Commit?

## Example
Xem Sprint Plan template trong Outputs.

## Related Skills
- Write User Story
- Review Requirement
