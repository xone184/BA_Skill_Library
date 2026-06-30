# Gap Analysis

## Level
Level 4 - Thinking Skill

## Purpose
Phân tích khoảng cách giữa trạng thái hiện tại (As-Is) và trạng thái mong muốn (To-Be), sau đó đề xuất kế hoạch hành động (Action Plan) để thu hẹp khoảng cách, phân theo 3 nhóm: Business Process, Technology/System, và People/Organization.

## When to Use
Sử dụng khi:
- Chuyển đổi từ hệ thống cũ sang mới.
- Cải thiện quy trình nghiệp vụ hiện tại.
- Đánh giá sản phẩm hiện có so với yêu cầu mới.

## Prerequisites
- Hiểu quy trình hiện tại (As-Is)
- Hiểu mục tiêu (To-Be)

## Inputs
### Mô tả trạng thái hiện tại (As-Is)
- **Mô tả:** Quy trình, hệ thống, con người hiện tại đang hoạt động ra sao.
- **Bắt buộc:** Có
- **Ví dụ:** Hiện tại: Kho quản lý bằng Excel, kiểm kê thủ công, không có barcode, mỗi lần kiểm kê mất 2 ngày.

### Mục tiêu mong muốn (To-Be)
- **Mô tả:** Trạng thái lý tưởng sau khi cải thiện.
- **Bắt buộc:** Có
- **Ví dụ:** Mong muốn: Hệ thống WMS quét barcode, kiểm kê Cycle Count hàng ngày, sai lệch tồn kho < 1%.

## Process
### Bước 1: Mô tả chi tiết As-Is
Vẽ sơ đồ và mô tả quy trình hiện tại.

- Vẽ luồng As-Is dưới dạng BPMN hoặc Flowchart
- Ghi nhận Pain Points (Điểm đau): Chậm, sai sót, tốn nhân lực
- Ghi nhận Workarounds (Cách chữa cháy) hiện tại
- Phỏng vấn người dùng: Điều gì khiến bạn khó chịu nhất?

### Bước 2: Mô tả chi tiết To-Be
Vẽ sơ đồ và mô tả trạng thái mong muốn.

- Vẽ luồng To-Be lý tưởng
- Xác định các KPI đo lường mục tiêu
- Best Practices từ ngành tham khảo

### Bước 3: Xác định Gaps (Khoảng cách)
So sánh As-Is vs To-Be và liệt kê các điểm khác biệt.

- Business Process Gaps: Quy trình nào cần thay đổi?
- Technology/System Gaps: Hệ thống nào cần xây mới/nâng cấp?
- People/Organization Gaps: Nhân sự nào cần đào tạo? Cần tuyển mới?
- Data Gaps: Dữ liệu nào thiếu hoặc không đúng format?

### Bước 4: Lập Action Plan
Đề xuất giải pháp thu hẹp từng Gap.

- Mỗi Gap → 1 hoặc nhiều Action Items
- Mỗi Action Item có: Owner, Timeline, Priority, Estimated Cost
- Sắp xếp theo Quick Wins (Dễ làm, hiệu quả cao) trước

## Outputs
### Gap Analysis Report
- **Định dạng:** Markdown Table
- **Mẫu:**

```
| # | Nhóm | As-Is | To-Be | Gap | Action | Priority | Owner |
|---|---|---|---|---|---|---|---|
| 1 | Process | Kiểm kê bằng tay 2 ngày | Cycle Count barcode 2h | Không có barcode | Triển khai hệ thống barcode | High | IT |
| 2 | System | Quản lý kho bằng Excel | WMS chuyên dụng | Không có phần mềm | Mua/Xây WMS | High | PM |
| 3 | People | Nhân viên kho không biết dùng máy tính | Nhân viên sử dụng thành thạo PDA | Thiếu kỹ năng | Đào tạo 2 tuần | Medium | HR |
```

## Sub-Skills (Kỹ năng con)
- As-Is Process Mapping
- To-Be Vision Design
- Action Plan Creation

## Business Rules
- BR-GAP-01: Gap phải được chia thành 3 nhóm: Process, System, People.
- BR-GAP-02: Mỗi Gap phải có Action Item cụ thể.
- BR-GAP-03: Action Plan phải có Owner và Timeline.

## Edge Cases & Exceptions
- As-Is quá hỗn loạn, không ai mô tả được chính xác → Quan sát thực tế (Observation)
- To-Be quá lý tưởng, không khả thi → Chia thành To-Be Phase 1 (khả thi) + To-Be Phase 2 (lý tưởng)

## Checklist
- [ ] Đã vẽ As-Is Process?
- [ ] Đã vẽ To-Be Process?
- [ ] Đã liệt kê đủ Gaps theo 3 nhóm (Process, System, People)?
- [ ] Mỗi Gap có Action Item?
- [ ] Action Plan có Owner và Timeline?
- [ ] Đã đánh giá rủi ro khi thay đổi?

## Example
Xem Gap Analysis Report template trong Outputs.

## Related Skills
- Root Cause Analysis
- Impact Analysis
- Risk Analysis
