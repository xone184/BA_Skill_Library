# Sprint Review

## Level
Level 2 - Business Skill

## Purpose
Hỗ trợ chuẩn bị và tổ chức buổi Sprint Review (Demo). Mục tiêu là trình diễn (Demo) sản phẩm hoàn thiện (Increment) cho Khách hàng (Stakeholders), thu thập phản hồi, và cập nhật Product Backlog dựa trên tình hình thực tế.

## When to Use
Sử dụng vào ngày cuối cùng của Sprint, trước buổi Sprint Retrospective.

## Prerequisites
- Sprint đã kết thúc
- Các tính năng Demo phải đạt Definition of Done (DoD)

## Inputs
### Sprint Goal & Sprint Backlog
- **Mô tả:** Mục tiêu và các task đã làm.
- **Bắt buộc:** Có
- **Ví dụ:** Mục tiêu: Ra mắt module Login. Hoàn thành 4/5 User Stories.

### Sản phẩm thực tế (Increment)
- **Mô tả:** Phần mềm chạy được.
- **Bắt buộc:** Không
- **Ví dụ:** URL staging để demo.

## Process
### Bước 1: Đánh giá Sprint Goal
So sánh kế hoạch và thực tế.

- Tuyên bố rõ: Những item nào đã 'Done' (Đạt DoD).
- Những item nào KHÔNG 'Done' (Không được mang ra Demo, đẩy về Product Backlog).

### Bước 2: Trình diễn Sản phẩm (Demo)
Cho khách hàng xem thành quả.

- Không dùng slide PowerPoint, phải demo trực tiếp trên phần mềm (Working Software).
- Chạy theo luồng nghiệp vụ (End-to-End) thay vì bấm từng nút rời rạc.

### Bước 3: Thu thập Phản hồi (Feedback Collection)
Lắng nghe Stakeholders.

- Ghi nhận ý kiến khen/chê.
- Ghi nhận các yêu cầu thay đổi (Change Requests) hoặc ý tưởng mới.

### Bước 4: Cập nhật Product Backlog
Đưa feedback vào Backlog.

- Phản hồi của khách sẽ biến thành User Story mới.
- PO thảo luận với Stakeholders về định hướng cho Sprint tiếp theo.

## Outputs
### Sprint Review Report
- **Định dạng:** Markdown Document
- **Mẫu:**

```
## 1. Kết quả Sprint
- **Sprint Goal:** [Đạt / Không đạt]
- **Done Items:** US-01, US-02.
- **Not Done Items:** US-03 (Thiếu test).

## 2. Stakeholder Feedback
- Giao diện đăng nhập đẹp, nhưng khách muốn thêm nút 'Đăng nhập bằng Google'.

## 3. Product Backlog Update
- **Tạo mới:** US-04 (Login by Google) - Priority: High.
- **Đẩy lại:** Đưa US-03 về đầu Backlog cho Sprint sau.
```

## Sub-Skills (Kỹ năng con)
- Demo Facilitation
- Feedback Structuring

## Business Rules
- BR-REVIEW-01: Tuyệt đối KHÔNG demo những tính năng chưa hoàn thành (Chưa đạt DoD).
- BR-REVIEW-02: Sprint Review KHÔNG PHẢI là buổi báo cáo tiến độ (Status report), mà là buổi lấy ý kiến về SẢN PHẨM.

## Edge Cases & Exceptions
- Khách hàng đòi thêm tính năng 'ngay lập tức' -> PO phải ghi nhận vào Backlog, không cam kết làm ngay trong lúc họp.

## Checklist
- [ ] Chỉ demo phần mềm chạy được (Không dùng slide)?
- [ ] Đã tuyên bố rõ item nào Done / Not Done?
- [ ] Đã ghi nhận Feedback thành các Backlog item mới?

## Example
Xem Sprint Review Report trong Outputs.

## Related Skills
- Sprint Retrospective
- Sprint Planning
