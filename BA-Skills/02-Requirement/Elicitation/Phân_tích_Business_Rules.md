# Phân tích Business Rules

## Level
Level 2 - Business Skill

## Purpose
Bóc tách, định nghĩa và kiểm soát các Ràng buộc nghiệp vụ (Business Rules). Đặc biệt quan trọng để ánh xạ các quy tắc quản trị/sản xuất vật lý vào hệ thống, từ đó làm cơ sở sinh tài liệu luồng nghiệp vụ và kịch bản Test (cả test hệ thống lẫn test QC thực tế).

## When to Use
Khi một chức năng có quá nhiều điều kiện Nếu-Thì (If-Else), hoặc khi áp dụng vào các ngành có rủi ro cao (MES, Y tế, Tài chính) cần tuân thủ nghiêm ngặt chuẩn mực.

## Prerequisites
- Có văn bản quy định của công ty, hoặc đã phỏng vấn chuyên gia (SME)

## Inputs
### Mô tả nghiệp vụ
- **Mô tả:** Đoạn văn mô tả lỏng lẻo cần được chuẩn hóa.
- **Bắt buộc:** Có
- **Ví dụ:** Công nhân chỉ được chạy máy nếu đã học an toàn và QC đã ký duyệt vật tư.

## Process
### Bước 1: Phân loại Business Rules
Chia nhóm để quản lý.

- Validation Rule (Ràng buộc nhập liệu): Số lượng nhập phải > 0.
- Access Control Rule (Quyền hạn): Chỉ Quản đốc mới được sửa lệnh.
- Process/Transition Rule (Quy trình): Không được chuyển trạng thái Running nếu chưa nhập kho Vật tư.
- Calculation Rule (Tính toán): OEE = Availability * Performance * Quality.

### Bước 2: Chuẩn hóa bằng Decision Table
Bóc tách điều kiện IF - THEN.

- Liệt kê các Condition (Điều kiện) ở dạng Boolean (Đúng/Sai).
- Liệt kê các Action (Hành động hệ thống) xảy ra tương ứng.
- Lập bảng kết hợp các logic lại với nhau.

### Bước 3: Map Rules vào Luồng Nghiệp Vụ (Business Flow)
Chèn rule vào tài liệu.

- Tại bước 3 của Use Case / BPMN, ghi rõ 'Áp dụng BR-001'.
- Đảm bảo rule không bị trôi nổi mà gắn chặt với màn hình/thao tác cụ thể.

### Bước 4: Map Rules vào Kịch bản Test (QA & System)
Biến rule thành test case.

- System Test: QA IT tạo test case cố tình vi phạm Rule để xem hệ thống có chặn và văng lỗi không.
- Manufacturing QA Test: Thiết lập chốt chặn QC vật lý dưới xưởng dựa trên rule (VD: QC lấy mẫu 5% sản phẩm trên dây chuyền).

## Outputs
### Business Rules Catalog & Decision Table
- **Định dạng:** Markdown
- **Mẫu:**

```
### Danh mục Business Rules
- **BR-MES-01 (Process Rule):** Lệnh sản xuất chỉ được phép bắt đầu (Start) khi (1) Vật tư đã được cấp đủ 100% tại xưởng VÀ (2) Nhân viên có chứng chỉ vận hành khớp với máy.

### Decision Table cho BR-MES-01
| Vật tư đủ? | Đạt chứng chỉ? | Action (Được Start máy?) | QA Test / System Test Case |
|---|---|---|---|
| Yes | Yes | **YES (Nút xanh)** | Test thành công |
| Yes | No | **NO (Báo lỗi đỏ)** | Cảnh báo: Nhân viên chưa đào tạo |
| No | Yes | **NO (Báo lỗi đỏ)** | Cảnh báo: Thiếu vật tư |
| No | No | **NO (Báo lỗi đỏ)** | Cảnh báo: Thiếu VT + Chưa ĐT |
```

## Sub-Skills (Kỹ năng con)
- Decision Table Creation
- QA & Test Mapping
- Rule Categorization

## Business Rules
- BR-RULE-01: Mọi Business Rule phải được viết bằng câu khẳng định, không dùng từ ngữ đa nghĩa (nên, có thể).
- BR-RULE-02: Phải gán ID (Mã định danh) duy nhất cho mỗi rule để dễ tracking.

## Edge Cases & Exceptions
- Trường hợp khẩn cấp (Emergency): Giám đốc nhà máy ra lệnh chạy máy dù thiếu vật tư trên hệ thống -> Thiết kế cơ chế 'Override' có ghi log Audit.

## Checklist
- [ ] Rule có rõ ràng, không đa nghĩa?
- [ ] Đã chia nhóm (Validation, Access, Process, Calculation)?
- [ ] Đã lập Decision Table cho các Rule phức tạp?
- [ ] Đã map Rule này với tài liệu Luồng (Flow) và Kịch bản Test chưa?

## Example
Xem Decision Table mẫu trong Outputs.

## Related Skills
- Viết Test Case (Ultra)
- State Machine Diagram
