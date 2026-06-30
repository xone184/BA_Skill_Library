# Viết Test Case (Ultra)

## Level
Level 2 - Business Skill

## Purpose
Viết Test Case ứng dụng các kỹ thuật kiểm thử phần mềm nâng cao: Phân tích giá trị biên (BVA), Phân vùng tương đương (EP), và Bảng quyết định (Decision Table). Hỗ trợ Micro-tasking cực mạnh để AI đóng vai trò như một Senior QA Engineer chuyên 'bắt bug'.

## When to Use
Sử dụng để tạo bộ test case phủ 100% case lỗi, HOẶC dùng Micro-tasking để nhờ AI phân tích các giá trị biên của một trường dữ liệu phức tạp.

## Prerequisites
- Đã có Functional Requirement hoặc Use Case rõ ràng

## Inputs
### Rule nghiệp vụ / Feature
- **Mô tả:** Tính năng cần test.
- **Bắt buộc:** Có
- **Ví dụ:** Ô nhập Tuổi yêu cầu >= 18 và <= 60.

### Lệnh Micro-tasking
- **Mô tả:** Yêu cầu kỹ thuật test cụ thể.
- **Bắt buộc:** Không
- **Ví dụ:** Chỉ sinh Test Case phân tích giá trị biên (Boundary Value) cho trường Tuổi.

## Process
### Bước 1: Xử lý Micro-tasking
Xác định kỹ thuật test cần áp dụng.

- Nếu User yêu cầu 'Boundary Value' → Tập trung vào các mốc Min-1, Min, Min+1, Max-1, Max, Max+1.
- Nếu User yêu cầu 'Decision Table' → Vẽ bảng kết hợp các rule (Ví dụ: Trạng thái = Active AND Hạng = VIP → Kết quả).
- Nếu yêu cầu 'Equivalence' → Chia vùng dữ liệu hợp lệ (Valid) và vùng lỗi (Invalid).

### Bước 2: Equivalence Partitioning (Phân vùng tương đương)
Tìm vùng dữ liệu để test.

- Rule: Tuổi 18-60. Vùng hợp lệ (Valid): 18-60 (Chọn đại 1 số VD: 30).
- Vùng không hợp lệ (Invalid 1): < 18 (Chọn đại: 10).
- Vùng không hợp lệ (Invalid 2): > 60 (Chọn đại: 70).

### Bước 3: Boundary Value Analysis (Phân tích giá trị biên)
Tìm lỗi ở viền giới hạn.

- Rule: Tuổi 18-60.
- Biên dưới: 17 (Min-1 -> Lỗi), 18 (Min -> Pass), 19 (Min+1 -> Pass).
- Biên trên: 59 (Max-1 -> Pass), 60 (Max -> Pass), 61 (Max+1 -> Lỗi).

### Bước 4: Error Guessing & Edge Cases
Đoán lỗi dựa trên kinh nghiệm.

- Dữ liệu null/empty.
- Dữ liệu sai định dạng (Nhập chữ vào ô số, nhập số âm).
- Dữ liệu chứa ký tự đặc biệt, XSS, SQL Injection (nếu field text).

### Bước 5: Viết Test Case chi tiết
Đóng gói thành format Test Case chuẩn.

- Test Case ID, Title, Test Data, Test Steps, Expected Result, Status

## Outputs
### Boundary Value Test Cases (Micro-tasking)
- **Định dạng:** Markdown Table
- **Mẫu:**

```
### Kỹ thuật áp dụng: Phân tích giá trị biên (BVA) cho Rule [Tuổi 18-60]

| TC ID | Kịch bản biên | Test Data | Expected Result |
|---|---|---|---|
| TC-BVA-01 | Min - 1 | Tuổi = 17 | Báo lỗi 'Phải >= 18 tuổi' |
| TC-BVA-02 | Min | Tuổi = 18 | Thành công |
| TC-BVA-03 | Min + 1 | Tuổi = 19 | Thành công |
| TC-BVA-04 | Max - 1 | Tuổi = 59 | Thành công |
| TC-BVA-05 | Max | Tuổi = 60 | Thành công |
| TC-BVA-06 | Max + 1 | Tuổi = 61 | Báo lỗi 'Phải <= 60 tuổi' |
```

### Decision Table (Micro-tasking)
- **Định dạng:** Markdown Table
- **Mẫu:**

```
### Kỹ thuật áp dụng: Decision Table cho Giảm giá

| Condition / Rule | Rule 1 | Rule 2 | Rule 3 | Rule 4 |
|---|---|---|---|---|
| Là thẻ VIP? | Yes | Yes | No | No |
| Đơn > 5 triệu? | Yes | No | Yes | No |
| **Action (Giảm giá)** | **20%** | **10%** | **5%** | **0%** |
```

## Sub-Skills (Kỹ năng con)
- Boundary Value Analysis
- Equivalence Partitioning
- Decision Table Testing

## Business Rules
- BR-QA-U1: Nếu có khoảng giá trị (Range), PHẢI sinh ra tối thiểu 6 Test Cases cho phần Boundary (Min-1, Min, Min+1, Max-1, Max, Max+1).
- BR-QA-U2: Nếu có logic kết hợp nhiều điều kiện AND/OR, PHẢI sinh ra Decision Table.

## Edge Cases & Exceptions
- Trường dữ liệu là Date/Time → Min là Yesterday, Max là Tomorrow hoặc End of Year.

## Checklist
- [ ] Đã thực hiện đúng kỹ thuật Micro-tasking User yêu cầu chưa?
- [ ] BVA đã đủ 6 điểm cận biên chưa?
- [ ] Equivalence đã có cả vùng Valid và Invalid chưa?
- [ ] Decision Table đã cover đủ các tổ hợp Yes/No chưa?

## Example
Xem các bảng kỹ thuật Test trong phần Outputs.

## Related Skills
- Phân tích Use Case (Ultra)
- Write SRS (Ultra)
