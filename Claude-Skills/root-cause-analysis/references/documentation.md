# Root Cause Analysis

## Level
Level 4 - Thinking Skill

## Purpose
Phân tích nguyên nhân gốc rễ của một vấn đề kinh doanh hoặc lỗi hệ thống bằng các kỹ thuật chuyên nghiệp (5 Whys, Fishbone Diagram) để đề xuất giải pháp triệt để thay vì chỉ xử lý triệu chứng.

## When to Use
Sử dụng khi phát hiện vấn đề lặp đi lặp lại hoặc lỗi hệ thống nghiêm trọng cần tìm ra nguyên nhân sâu xa.

## Prerequisites
- Nắm rõ vấn đề cần phân tích

## Inputs
### Problem Statement
- **Mô tả:** Mô tả vấn đề cụ thể, đo lường được.
- **Bắt buộc:** Có
- **Ví dụ:** Tỷ lệ hàng giao sai cho khách hàng tăng từ 1% lên 5% trong 3 tháng gần đây.

### Dữ liệu liên quan
- **Mô tả:** Số liệu, log, báo cáo để phân tích.
- **Bắt buộc:** Không
- **Ví dụ:** Log đơn hàng bị trả lại, Danh sách ca làm việc, Tỷ lệ lỗi theo sản phẩm

## Process
### Bước 1: Xác định vấn đề (Define Problem)
Mô tả vấn đề một cách cụ thể và đo lường được.

- Vấn đề là gì? (What happened?)
- Xảy ra ở đâu? (Where?)
- Xảy ra khi nào? (When? Từ bao giờ?)
- Ảnh hưởng bao nhiêu? (How much/many?)
- Ai bị ảnh hưởng? (Who?)

### Bước 2: Thu thập dữ liệu
Gom dữ liệu thực tế để phân tích.

- Phỏng vấn người liên quan
- Xem log hệ thống
- Phân tích xu hướng (Trend analysis)
- Đi xuống hiện trường quan sát (Gemba Walk)

### Bước 3: Phân tích bằng 5 Whys
Hỏi 'Tại sao?' liên tiếp 5 lần để đào sâu đến gốc rễ.

- Why 1: Tại sao hàng giao sai? → Vì nhân viên Picking lấy nhầm hàng.
- Why 2: Tại sao lấy nhầm? → Vì không quét barcode, dùng mắt tìm.
- Why 3: Tại sao không quét barcode? → Vì máy PDA hết pin.
- Why 4: Tại sao PDA hết pin? → Vì chỉ có 5 PDA cho 15 nhân viên.
- Why 5: Tại sao thiếu PDA? → Vì chưa được duyệt ngân sách mua thêm.
- → Root Cause: Thiếu thiết bị PDA + Quy trình không bắt buộc scan barcode.

### Bước 4: Phân tích bằng Fishbone (Ishikawa)
Sử dụng sơ đồ xương cá để phân loại nguyên nhân.

- Man (Con người): Thiếu đào tạo, thiếu nhân lực
- Machine (Máy móc): Thiếu PDA, máy cũ
- Method (Phương pháp): Quy trình chưa bắt buộc scan
- Material (Vật liệu): Nhãn hàng bị mờ, khó đọc
- Measurement (Đo lường): Không có KPI theo dõi tỷ lệ lỗi
- Mother Nature (Môi trường): Kho tối, chật hẹp

### Bước 5: Đề xuất giải pháp & Hành động
Đưa ra giải pháp cho Root Cause.

- Corrective Action: Sửa ngay (Mua thêm PDA, ép scan barcode)
- Preventive Action: Ngăn tái diễn (SOP mới, audit hàng tuần)
- Verification: Cách kiểm tra giải pháp có hiệu quả (Theo dõi tỷ lệ lỗi 30 ngày)

## Outputs
### RCA Report
- **Định dạng:** Markdown Document
- **Mẫu:**

```
# Root Cause Analysis Report

## Problem Statement
[Mô tả vấn đề cụ thể...]

## 5 Whys Analysis
| # | Question | Answer |
|---|---|---|
| 1 | Tại sao...? | Vì... |
| 2 | Tại sao...? | Vì... |
| 3 | Tại sao...? | Vì... |
| 4 | Tại sao...? | Vì... |
| 5 | Tại sao...? | Vì... |

**Root Cause:** [Nguyên nhân gốc rễ]

## Fishbone Diagram (6M)
| Category | Possible Causes |
|---|---|
| Man | ... |
| Machine | ... |
| Method | ... |
| Material | ... |
| Measurement | ... |
| Environment | ... |

## Action Plan
| # | Action | Type | Owner | Deadline |
|---|---|---|---|---|
| 1 | Mua 10 PDA | Corrective | IT | 2 tuần |
| 2 | Cập nhật SOP bắt buộc scan | Preventive | QC Manager | 1 tuần |
```

## Sub-Skills (Kỹ năng con)
- 5 Whys Technique
- Fishbone Diagram
- Corrective/Preventive Action

## Business Rules
- BR-RCA-01: Phải hỏi ít nhất 5 lần TẠI SAO.
- BR-RCA-02: Root Cause phải là nguyên nhân có thể hành động được (Actionable).
- BR-RCA-03: Giải pháp phải bao gồm cả Corrective (Sửa ngay) và Preventive (Ngăn tái diễn).

## Edge Cases & Exceptions
- Root cause nằm ngoài tầm kiểm soát (VD: Luật pháp) → Ghi nhận và đề xuất workaround
- Nhiều Root Cause đồng thời → Xử lý tất cả, ưu tiên cause có ảnh hưởng lớn nhất

## Checklist
- [ ] Vấn đề đã được mô tả cụ thể, đo lường được?
- [ ] Đã thu thập đủ dữ liệu?
- [ ] Đã hỏi ít nhất 5 lần Tại sao?
- [ ] Đã sử dụng Fishbone 6M?
- [ ] Root Cause đã xác định rõ?
- [ ] Giải pháp có cả Corrective và Preventive?
- [ ] Có cách kiểm tra hiệu quả giải pháp (Verification)?

## Example
Xem ví dụ 5 Whys trong Process section.

## Related Skills
- Gap Analysis
- Impact Analysis
- Risk Analysis
- Phân tích OEE
