# Vẽ BPMN

## Level
Level 2 - Business Skill

## Purpose
Mô hình hóa quy trình nghiệp vụ bằng chuẩn BPMN (Business Process Model and Notation) 2.0. Sử dụng Swimlanes để phân định rõ trách nhiệm của từng vai trò (Role/Department) và các Gateways để xử lý logic rẽ nhánh.

## When to Use
Sử dụng khi cần thống nhất quy trình làm việc (As-Is hoặc To-Be) với khách hàng hoặc tài liệu hóa quy trình cho đội Dev.

## Prerequisites
- Đã phỏng vấn lấy yêu cầu quy trình
- Hiểu chuẩn BPMN cơ bản

## Inputs
### Mô tả quy trình
- **Mô tả:** Text mô tả các bước thực hiện công việc.
- **Bắt buộc:** Có
- **Ví dụ:** Nhân viên kho nhận hàng. Kế toán kiểm tra hóa đơn. Nếu khớp thì thủ kho cất hàng, nếu không khớp thì trả lại NCC.

## Process
### Bước 1: Xác định Scope & Participants
Quy trình bắt đầu/kết thúc khi nào và ai tham gia?

- Xác định Pool (Tổ chức/Hệ thống) và Swimlanes (Vai trò: User, Admin, System)
- Xác định Start Event (Trigger: Khi nào quy trình bắt đầu?)
- Xác định End Event (Kết quả cuối cùng là gì?)

### Bước 2: Mô hình hóa chuỗi hoạt động (Tasks)
Vẽ các bước thực hiện.

- Sử dụng User Task cho thao tác của con người
- Sử dụng Service Task cho xử lý tự động của hệ thống
- Ghi nhãn Task bằng Động từ + Danh từ (VD: 'Tạo đơn hàng' thay vì 'Đơn hàng')

### Bước 3: Xử lý logic rẽ nhánh (Gateways)
Sử dụng các cổng quyết định.

- Exclusive Gateway (X): Rẽ 1 trong nhiều nhánh (VD: Approved OR Rejected)
- Parallel Gateway (+): Thực hiện đồng thời nhiều nhánh (VD: Vừa gửi email VÀ vừa in phiếu)
- Inclusive Gateway (O): Có thể rẽ 1 hoặc nhiều nhánh (VD: Đặt hàng A, B hoặc cả A và B)

### Bước 4: Xử lý sự kiện (Events)
Các sự kiện xảy ra trong quá trình.

- Timer Event: Chờ 3 ngày, hoặc gửi nhắc nhở mỗi thứ Hai
- Message Event: Chờ phản hồi từ NCC, hoặc Gửi email cho khách
- Error Event: Xử lý ngoại lệ (VD: Lỗi API thanh toán)

### Bước 5: Review & Tối ưu
Kiểm tra tính hợp lý.

- Có đường cụt (Dead end) nào không? Mọi luồng đều phải dẫn đến End Event.
- Quy trình có quá phức tạp không? Nếu > 20 tasks, nên tách thành Sub-process.

## Outputs
### BPMN Code (Mermaid)
- **Định dạng:** Mermaid stateDiagram hoặc flowchart
- **Mẫu:**

```
```mermaid
sequenceDiagram
    actor Khách
    participant HệThống
    participant Kho
    Khách->>HệThống: Đặt hàng
    HệThống-->>Kho: Báo đơn mới
``` (Ghi chú: Mermaid không hỗ trợ BPMN native tốt, dùng flowchart kết hợp subgraph làm swimlane)
```

### Mô tả Text của Quy trình
- **Định dạng:** Markdown List
- **Mẫu:**

```
1. **[Thủ kho]** Nhận hàng từ NCC.
2. **[Hệ thống]** Kiểm tra PO khớp với GRN.
  - Nếu khớp: Chuyển sang bước 3.
  - Nếu KHÔNG khớp: Trả lại NCC (Kết thúc).
```

## Sub-Skills (Kỹ năng con)
- Gateway Logic
- Swimlane Design
- Sub-process Identification

## Business Rules
- BR-BPMN-01: Mọi quy trình đều phải có Start Event và End Event.
- BR-BPMN-02: Tên Task phải bắt đầu bằng động từ.
- BR-BPMN-03: Không để đường cụt (Dead-end) trong quy trình, mọi nhánh rẽ phải dẫn đến kết quả cuối.
- BR-BPMN-04: Gateway dùng để kiểm tra điều kiện, không phải để thực hiện công việc (VD: Nút kim cương chứa 'Tổng > 100?' thay vì 'Kiểm tra tổng').

## Edge Cases & Exceptions
- Quy trình có vòng lặp (Loop/Rework) → Dùng mũi tên quay ngược lại task trước (VD: Yêu cầu sửa lại báo giá)
- Quy trình có Timeout → Dùng Timer Boundary Event (VD: Sau 24h không duyệt thì tự động Reject)

## Checklist
- [ ] Có Start và End Event?
- [ ] Đã chia Swimlane theo Role chưa?
- [ ] Tên Task có bắt đầu bằng động từ?
- [ ] Gateway có dán nhãn điều kiện (Yes/No)?
- [ ] Mọi nhánh rẽ đều có điểm kết thúc?
- [ ] Có xử lý ngoại lệ (Error/Timeout)?
- [ ] Nếu quá dài, đã chia thành Sub-process chưa?

## Example
Xem mô tả flowchart trong phần Outputs.

## Related Skills
- Phân tích Use Case
- Gap Analysis
