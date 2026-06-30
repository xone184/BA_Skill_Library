# Cẩm nang Xây dựng Hệ thống MES với Claude Skills

Tài liệu này hướng dẫn bạn cách áp dụng **chuỗi các kỹ năng (Skill Chaining)** đã được tối ưu hóa chuyên biệt cho Sản xuất (MES) vào Claude. Bằng cách thực hiện tuần tự theo các bước dưới đây, bạn có thể hướng dẫn Claude thiết kế toàn bộ một phân hệ MES từ con số 0.

---

## Chuẩn bị: Import Skills vào Claude

Trước khi bắt đầu, hãy đảm bảo bạn đã upload các file nén `.zip` của các kỹ năng sau từ thư mục `Claude-Skills-Zip` vào giao diện Custom Skills của Claude (`claude.ai/customize/skills`):

1. `phan-tich-production-order.zip` (Cốt lõi MES)
2. `state-machine-diagram.zip` (Quản lý trạng thái)
3. `activity-diagram.zip` (Luồng thao tác xưởng)
4. `phan-tich-business-rules.zip` (Quy tắc và Ràng buộc)
5. `thiet-ke-role-based-ui.zip` (Giao diện Quản đốc/Công nhân)
6. `phan-tich-mobile-app.zip` (Giao diện Tablet/Scanner)
7. `write-srs-ultra.zip` (Tổng hợp tài liệu)
---

## 6 Bước Quy trình (MES Skill Playbook)

Dưới đây là một kịch bản mẫu: Thiết kế phân hệ **Thực thi Lệnh Sản Xuất tại Máy CNC**. Hãy nhập các prompt sau vào Claude theo đúng thứ tự (trong cùng 1 luồng chat).

### Bước 1: Khởi tạo và Phân tích Lõi nghiệp vụ
Bắt đầu bằng việc định nghĩa đối tượng cốt lõi nhất của MES: Lệnh sản xuất (Production Order).

> **Prompt cho Claude:**
> "Claude, hãy dùng kỹ năng **Phân tích Production Order** để khởi tạo cấu trúc cho một Lệnh sản xuất tại máy CNC cắt kim loại. Lệnh này cần có BOM (Định mức vật tư) và Routing (Quy trình các bước)."

*Claude sẽ sinh ra cấu trúc dữ liệu, các thuật ngữ và thành phần cơ bản của Lệnh Sản Xuất.*

### Bước 2: Đặc tả Vòng đời (Lifecycle)
Không có Lệnh sản xuất nào đứng im. Nó phải chuyển đổi trạng thái liên tục.

> **Prompt cho Claude:**
> "Dựa vào thông tin Lệnh sản xuất vừa phân tích, hãy dùng kỹ năng **State Machine Diagram** để vẽ sơ đồ trạng thái (Draft -> Released -> Running -> Paused -> Completed). Yêu cầu mô tả rõ Trigger (Công nhân làm gì) và Guard Condition (Chặn điều kiện gì) tại mỗi mũi tên."

*Claude sẽ vẽ sơ đồ Mermaid và ma trận chuyển đổi, đảm bảo Lệnh không bị nhảy cóc trạng thái sai quy trình.*

### Bước 3: Đặc tả Thao tác Vật lý (Shopfloor Workflow)
Tiếp theo, ta cần vẽ luồng thao tác thực tế của người công nhân tại trạm máy.

> **Prompt cho Claude:**
> "Tuyệt vời. Giờ hãy dùng kỹ năng **Activity Diagram** để vẽ luồng thao tác của người công nhân tại máy CNC này. 
> Bối cảnh: Công nhân cầm Tablet, quét mã vạch Lệnh, hệ thống kiểm tra. Nếu pass, công nhân lấy phôi nạp vào máy, bấm Start trên Tablet, máy bắt đầu chạy và hệ thống tự động trừ kho vật tư."

*Claude sẽ tách bạch các luồng song song (Fork/Join) giữa hành động vật lý của con người và hệ thống.*

### Bước 4: Chốt Ràng buộc & QC (Quality Control)
Máy CNC rất đắt tiền và phôi cũng đắt, không thể để công nhân làm sai quy trình.

> **Prompt cho Claude:**
> "Tôi thấy bước Công nhân quét mã và bấm Start rất rủi ro. Hãy dùng kỹ năng **Phân tích Business Rules** để lập Decision Table cho bước này.
> Điều kiện: Chỉ được Start nếu Vật tư đã xuất kho đủ VÀ Công nhân có thẻ chứng chỉ vận hành máy CNC. Hãy đưa ra cả hướng dẫn test QA thực tế tại xưởng."

*Claude sẽ sinh ra Bảng Quyết Định (Decision Table), bao gồm các trường hợp thiếu vật tư, thiếu chứng chỉ, và cách QC (KCS) đi tuần tra test như thế nào.*

### Bước 5: Thiết kế Giao diện Hiện trường (Shopfloor UI)
Cuối cùng, chuyển logic thành giao diện thực tế. Giao diện dưới xưởng phải hoàn toàn khác giao diện văn phòng.

> **Prompt cho Claude:**
> "Cuối cùng, hãy dùng kỹ năng **Thiết kế Role-based UI** kết hợp với **Phân tích Mobile App** để thiết kế màn hình chạy máy cho người Công nhân. 
> Lưu ý: Công nhân đang đeo găng tay, môi trường xưởng rất ồn và WIFI chập chờn. Không dùng bàn phím nhập liệu, chỉ có máy quét Barcode và các nút bấm siêu to. Cần có cơ chế Offline."

*Claude sẽ mô tả chi tiết kích thước nút bấm, phản hồi âm thanh (do xưởng ồn), và cơ chế lưu Queue nội bộ khi rớt mạng WIFI.*

### Bước 6: Tổng hợp thành Tài liệu SRS (Skill Chaining)
Sau khi đã bóc tách xong toàn bộ luồng, ràng buộc và giao diện, đây là lúc gom tất cả lại thành một tài liệu phân tích chính thức để gửi cho đội Dev.

> **Prompt cho Claude:**
> "Rất tốt. Bây giờ hãy sử dụng kỹ năng **Write SRS (Ultra)**. Nhiệm vụ của bạn là tổng hợp TẤT CẢ các thông tin chúng ta vừa thảo luận (từ Lệnh sản xuất, Luồng Activity, Business Rules, đến Giao diện Tablet) để cấu trúc thành một tài liệu Phân tích Yêu cầu Phần mềm (SRS) hoàn chỉnh. Hãy chắc chắn phân tách rõ ràng giữa Functional Requirements (FR) và Non-Functional Requirements (NFR) theo chuẩn FURPS+."

*Claude sẽ đóng vai trò như một cỗ máy in tài liệu, thu thập mọi dữ liệu đã có trong luồng chat để đúc kết thành một bản SRS cực kỳ chuyên nghiệp và chuẩn xác.*

---

## 💡 Mẹo nhỏ (Pro-Tips)

- **Lựa chọn Skill theo nhu cầu (Pick & Choose):** Quy trình 6 bước trên là một luồng mẫu hoàn chỉnh (Full Flow). Tuy nhiên, nếu bạn chỉ có một yêu cầu cụ thể (Ví dụ: Chỉ muốn thiết kế Database, hoặc chỉ muốn viết Kịch bản Test), bạn hoàn toàn có thể mở thư mục **`Claude-Skills`** ra, chọn đúng thư mục skill bạn cần (VD: `thiet-ke-erd` hoặc `viet-test-case-ultra`) và ném vào Claude để xử lý tác vụ lẻ đó. Có tới **87 kỹ năng** khác nhau đang chờ bạn khám phá!
- **Giữ Context:** Khi áp dụng quy trình chuỗi (Chaining), luôn chạy các bước trong **cùng một luồng chat (Conversation)** để Claude nhớ bối cảnh của bước trước và áp dụng dữ liệu vào bước sau.
- **Tuỳ biến:** Nếu nhà máy của bạn làm về May mặc hoặc Thực phẩm (thay vì Cơ khí CNC), chỉ cần đổi Input ở **Bước 1**, các kỹ năng của Claude sẽ tự động điều chỉnh logic toàn bộ quy trình cho phù hợp.
- **Thử nghiệm mã lỗi:** MES rất quan tâm đến lỗi (Defect). Bạn có thể gọi thêm kỹ năng `phan-tich-oee` (Hiệu suất thiết bị tổng thể) và hỏi Claude: *"Phân tích các nguyên nhân gây Downtime (Dừng máy) tại trạm này"*.

---

## 🔒 Chuẩn hóa Tài liệu Enterprise (Enterprise Standards v1.0)

**QUAN TRỌNG:** Kể từ bản cập nhật mới nhất, toàn bộ các luồng kỹ năng trên đều đã được tiêm (inject) **Bộ quy tắc chuẩn hóa Tài liệu & Diagram Nghiệp vụ (v1.0)**. 

Khi thực thi cho các hệ thống MES, Claude sẽ luôn bám sát các chỉ thị ngầm sau:
1. **BPMN vs Activity Diagram:** Claude sẽ tự động chọn vẽ BPMN khi quy trình đi xuyên qua nhiều phòng ban (VD: Lệnh sản xuất từ Kho vật tư → Máy CNC → Kho thành phẩm). Chỉ dùng Activity Diagram (chế độ Trắng/Đen không màu) cho thao tác chi tiết của công nhân tại một trạm duy nhất.
2. **Data Model:** Claude sẽ luôn nhắc nhở về tần suất đồng bộ dữ liệu (real-time vs batching) và bắt buộc khai báo Unit of Measurement (Đơn vị đo lường) khi thiết kế Data Model cho MES.
3. **Acceptance Criteria:** Sẽ luôn xuất ra theo định dạng Gherkin (Given-When-Then) nhằm phục vụ trực tiếp cho đội QC/Tester tại xưởng.
