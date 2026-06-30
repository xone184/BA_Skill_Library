# Write SRS (Ultra)

## Level
Level 1 - Basic Skill

## Purpose
Soạn thảo SRS phiên bản siêu chi tiết. Cung cấp bộ công cụ mạnh mẽ để AI có thể làm Micro-tasking (Ví dụ: Chỉ sinh ra bộ Non-Functional Requirements theo chuẩn FURPS+, hoặc chỉ thiết kế Traceability Matrix) thay vì sinh ra 1 tài liệu quá dài.

## When to Use
Khi cần viết đặc tả kỹ thuật, HOẶC khi cần AI hỗ trợ bổ sung một phần bị thiếu (VD: NFR) cho một tài liệu đã có.

## Prerequisites
- Đã có BRD hoặc User Stories

## Inputs
### Tính năng / Module
- **Mô tả:** Phạm vi cần viết SRS.
- **Bắt buộc:** Có
- **Ví dụ:** Module Quản lý Tồn kho.

### Lệnh Micro-tasking (Tùy chọn)
- **Mô tả:** Lệnh yêu cầu AI chỉ viết 1 phần của SRS.
- **Bắt buộc:** Không
- **Ví dụ:** Chỉ liệt kê NFR theo mô hình FURPS+ cho module này.

## Process
### Bước 1: Xử lý Micro-tasking (Quan trọng nhất)
Xác định AI cần sinh toàn bộ SRS hay chỉ một phần.

- Nếu User yêu cầu 'Chỉ NFR' → Chuyển thẳng sang Bước 3.
- Nếu User yêu cầu 'Chỉ Data Dictionary' → Chuyển thẳng sang Bước 4.
- Nếu không có yêu cầu đặc biệt → Sinh cấu trúc SRS tổng quan.

### Bước 2: Đặc tả Functional (FR)
Chi tiết chức năng hệ thống.

- Mỗi FR có Input, Processing logic, Output, Error Handling, Validation Rules
- Áp dụng Business Rules cụ thể thay vì chung chung

### Bước 3: Đặc tả Non-Functional (NFR) chuẩn FURPS+
Phân tích NFR sâu theo chuẩn ngành.

- F (Functionality): Security, Logging, Auditing
- U (Usability): UI standards, Accessibility, Localization
- R (Reliability): Availability (99.9%), Fault tolerance, Recoverability
- P (Performance): Response time (<2s), Throughput (1000 TPS), Capacity
- S (Supportability): Maintainability, Configurable params
- + (Plus): Ràng buộc phần cứng, pháp lý (GDPR)

### Bước 4: Thiết lập Traceability Matrix
Liên kết Requirement.

- Map Business Requirement (BR) → Functional Req (FR) → Test Case (TC)

## Outputs
### FURPS+ NFR Report (Dành cho Micro-tasking)
- **Định dạng:** Markdown Table
- **Mẫu:**

```
### NFR Report (FURPS+)

| Nhóm (FURPS) | ID | Mô tả chi tiết | Phương pháp đo lường (Measurable) |
|---|---|---|---|
| **R**eliability | NFR-01 | Hệ thống phải tự động failover sang máy chủ dự phòng trong < 30s khi Crash. | Giả lập crash, đếm thời gian downtime. |
| **P**erformance | NFR-02 | Thời gian tải trang Dashboard < 2 giây với 100,000 bản ghi dữ liệu. | Dùng JMeter test load 1000 CCU. |
| **S**upportability| NFR-03 | Mọi tham số cấu hình (Thuế, Phí ship) phải thay đổi được trên giao diện Admin không cần restart code. | Test thay đổi giá trị và xem hiệu ứng tức thời. |
```

## Sub-Skills (Kỹ năng con)
- FURPS+ NFR Design
- Traceability Mapping
- Micro-tasking Document Section

## Business Rules
- BR-SRS-U1: NFR PHẢI có phương pháp đo lường (Measurable). Không dùng từ 'Nhanh', 'Bảo mật cao'.
- BR-SRS-U2: Nếu có lệnh Micro-tasking, AI PHẢI loại bỏ các phần không liên quan để tránh loãng thông tin.

## Edge Cases & Exceptions
- Hệ thống yêu cầu pháp lý đặc biệt (Health data, Financial data) → Tập trung cực sâu vào Security (F) và Plus (+).

## Checklist
- [ ] Nếu sinh NFR, đã đủ 5 khía cạnh FURPS+ chưa?
- [ ] Các chỉ số Performance có định lượng (giây, TPS, %) không?
- [ ] Đã thực hiện đúng lệnh Micro-tasking của User chưa?

## Example
Xem FURPS+ NFR Report trong Outputs.

## Related Skills
- Phân tích Use Case
- Thiết kế API Contract
