# BA Skill Library

Hệ thống **BA Skill Library** được thiết kế dành riêng cho Claude AI (hoặc các AI Assistant khác) để hoạt động như một **Knowledge Base + Skill Engine**. Đây không phải là một thư viện prompt tĩnh đơn thuần, mà là một kho chứa các kỹ năng nghiệp vụ chuyên sâu đã được mô-đun hóa. 

Bằng việc cung cấp cho AI quyền truy cập vào thư viện này, AI có thể hoạt động như một Senior Business Analyst thực thụ: hiểu ngữ cảnh, áp dụng đúng kỹ năng chuyên môn, tuân thủ các quy tắc nghiệp vụ khắt khe và xuất ra tài liệu chuẩn mực.

---

## 1. Kiến trúc cốt lõi: Bộ 3 File (The Triad Architecture)

Mỗi kỹ năng trong thư viện được thiết kế chặt chẽ và lưu trữ dưới dạng **3 file liên kết với nhau**:

1. **File `.json` (Metadata & Routing):** Chứa các thẻ phân loại, mức độ, danh sách Input/Output. Công dụng: Giúp AI (hoặc hệ thống RAG) search và lấy đúng kỹ năng cần thiết một cách nhanh chóng.
2. **File `.md` (Knowledge Base & Documentation):** Tài liệu đặc tả siêu chi tiết của kỹ năng. Chứa các bước thực hiện (Process), quy tắc (Business Rules), tình huống ngoại lệ (Edge Cases), Checklist kiểm tra chất lượng và các Markdown Templates.
3. **File `.prompt` (Execution Engine):** Đóng gói toàn bộ kiến thức từ file `.md` thành một System Prompt chuẩn mực. Chứa Role, Context, Constraints và các bước bắt AI phải làm theo thứ tự để sinh ra kết quả chính xác nhất.

---

## 2. Hướng dẫn Import vào Claude (Native Skills)

Gần đây, Claude đã cập nhật tính năng **Custom Skills** (`claude.ai/customize/skills`). Đây là nơi bạn có thể import trực tiếp các kỹ năng của thư viện này để Claude tự động sử dụng khi cần, giống hệt một Agent thực thụ.

Chúng tôi đã cung cấp sẵn thư mục **`Claude-Skills-Zip`** chứa toàn bộ các kỹ năng đã được nén thành file `.zip` theo đúng chuẩn định dạng của Claude.

### Cách import và sử dụng:

* **Bước 1:** Trong máy tính của bạn, mở thư mục `BA Skill Library/Claude-Skills-Zip`. Ở đây bạn sẽ thấy hàng chục file nén như `write-user-story.zip`, `write-srs-ultra.zip`...
* **Bước 2:** Truy cập vào `claude.ai/customize/skills` (hoặc click vào nút **Browse plugins** trên giao diện của Claude).
* **Bước 3:** Tạo một skill mới hoặc click **Upload**, sau đó chọn file `.zip` của kỹ năng bạn muốn (Ví dụ: `write-srs-ultra.zip`) để tải lên. *(Lưu ý: Claude chỉ chấp nhận định dạng .zip hoặc .plugin).*
* **Bước 4:** Claude sẽ tự động giải nén, đọc file `SKILL.md` bên trong để lấy tên, mô tả và cấu hình toàn bộ Prompt, Tài liệu tham khảo (References) cho Agent.
* **Bước 5:** Bật (Enable) skill đó lên cho Project hoặc Workspace của bạn.
* **Kết quả:** Từ bây giờ, bạn không cần phải dán prompt dài dòng nữa. Bạn chỉ cần chat tự nhiên: *"Claude, hãy dùng kỹ năng Write User Story để viết US cho tính năng Đăng nhập"*. Claude sẽ tự động load file `SKILL.md` tương ứng và thực thi một cách hoàn hảo!

*(Lưu ý: Nếu bạn dùng bản miễn phí không có tính năng Skills, bạn vẫn có thể copy nội dung file `SKILL.md` hoặc `.prompt` và dán thẳng vào khung chat như cách truyền thống).*

### Cách 3: Chaining Skills (Lắp ghép dự án lớn)
Khi bạn cần Claude đóng vai PM/BA điều phối một dự án từ đầu đến cuối trong cùng một luồng hội thoại. Bạn dùng kết quả của Prompt A làm Input cho Prompt B.

1. Đầu tiên, dán `Viết_User_Story.prompt` và bảo Claude viết danh sách User Stories cho luồng Đăng nhập.
2. Claude trả kết quả (danh sách US-01, US-02...).
3. Tiếp theo, dán `Vẽ_BPMN.prompt` vào và bảo: *"Từ danh sách User Story trên, hãy vẽ cho tôi luồng BPMN có Swimlanes"*.
4. Claude trả kết quả Mermaid BPMN.
5. Cuối cùng, dán `Thiết_kế_API_Contract.prompt` vào và bảo: *"Dựa vào luồng BPMN trên, thiết kế RESTful API cho tôi"*.

---

## 3. Danh sách 33 Kỹ năng cốt lõi (Deep Expanded)

Thư viện hiện tại đã được nâng cấp chuyên sâu (Deep Expand) với 33 kỹ năng quan trọng nhất:

**1. Khảo sát & Đặc tả Yêu cầu (Requirement):**
- Write User Story (chuẩn INVEST, Given-When-Then).
- Write BRD (Business Requirement Document).
- Write SRS (Ultra) - Bóc tách NFR theo FURPS+.
- Review Requirement (Kiểm tra chéo 10 khía cạnh).
- Phân tích Use Case (Ultra) - Bóc tách luồng rẽ nhánh, ngoại lệ (Exception).

**2. Phân tích Nghiệp vụ Lõi (Business Domain):**
- **CRM:** Lead Management, Opportunity, Customer Support, Loyalty Program.
- **WMS (Kho):** Inbound, Outbound, Inventory, Cross Docking, Return, Replenishment.
- **MES (Sản xuất):** Production Order, OEE, Quality Control.
- **ERP:** Procurement (P2P), Kế toán công nợ (AR/AP).
- **HRM:** Chấm công, Payroll, Tuyển dụng (ATS).

**3. Đặc tả UIUX & Database (Design & Data):**
- Thiết kế Dashboard (Role-based, Chart selection).
- Phân tích màn hình CRUD (Search, Filter, Validation).
- Thiết kế Notification (Email/SMS Template, Variables).
- Thiết kế ERD (Entity Relationship Diagram).
- Create Data Dictionary (Database constraints, data mapping).

**4. Kỹ thuật Mô hình hóa (Modeling):**
- Vẽ BPMN (Dùng Mermaid, xử lý Swimlanes & Gateways).
- Vẽ Sequence Diagram (Dùng Mermaid, đặc tả luồng gọi API và 3rd Party).

**5. Kiểm thử & Tích hợp (Testing & Integration):**
- Viết Test Case (Ultra) - Áp dụng Boundary Value, Equivalence Partitioning, Decision Table.
- Lập kế hoạch UAT (User Acceptance Testing) với End-to-End Scenarios.
- Thiết kế API Contract (RESTful, Payloads, HTTP Error Codes).

**6. Tư duy Phân tích & Quản lý Dự án (Agile & Thinking):**
- Sprint Planning (Story Points, Capacity, Commitment).
- Sprint Retrospective (Mad/Sad/Glad, Root Cause 5 Whys).
- Gap Analysis (As-Is vs To-Be).
- Root Cause Analysis (5 Whys, Fishbone 6M).

---

## 4. Dành cho Developer / Người bảo trì

Thư viện được quản lý tự động bằng Python script. Để cập nhật hoặc thêm hàng loạt kỹ năng mới:
1. Copy template từ file `expand_01_crm.py`.
2. Định nghĩa cấu trúc Dictionary (JSON) chứa thông tin chi tiết kỹ năng.
3. Chạy lệnh: `python ten_file_cua_ban.py`. Hệ thống sẽ tự động parse dữ liệu và sinh ra bộ 3 file `.md`, `.json`, `.prompt` chuẩn mực vào thư mục tương ứng.
