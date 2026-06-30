import sys
sys.path.insert(0, r"e:\BA Skill Library")
from skill_generator import run

skills = [
    # ================================================================
    # Testing - Test Case
    # ================================================================
    {
        "path": "06-Testing/Test Case",
        "name": "Viết Test Case",
        "level": "Level 1 - Basic Skill",
        "domain": "Testing",
        "tags": ["Testing", "QA", "Test Case", "Validation"],
        "purpose": "Viết kịch bản kiểm thử (Test Case) chi tiết dựa trên Requirement/User Story để đảm bảo tính năng hoạt động đúng nghiệp vụ. Test Case phải rõ ràng đến mức bất kỳ ai (BA, QC, Khách hàng) đều có thể đọc và thực hiện được.",
        "when_to_use": "Sử dụng sau khi chốt Requirement hoặc trong Sprint để QC/BA thực hiện test trước khi UAT.",
        "prerequisites": ["Đã có User Story / SRS đã duyệt"],
        "inputs_detail": [
            {"name": "Requirement (User Story / SRS)", "description": "Tài liệu đầu vào mô tả tính năng.", "required": True, "example": "User Story: Khách hàng thanh toán giỏ hàng bằng thẻ tín dụng. AC: Thẻ hợp lệ → Thành công. Thẻ hết hạn → Từ chối."}
        ],
        "process_detail": [
            {"step": 1, "title": "Phân tích Acceptance Criteria", "description": "Từ AC, xác định các kịch bản cần test.", "sub_steps": [
                "1 AC thường tạo ra nhiều Test Cases",
                "Xác định Happy Path (Kịch bản chuẩn, mọi thứ đều đúng)",
                "Xác định Negative Path (Nhập sai, lỗi hệ thống, thiếu quyền)",
                "Xác định Boundary Value (Giá trị biên: Giới hạn ký tự, số tiền tối thiểu/tối đa)"
            ]},
            {"step": 2, "title": "Thiết lập Pre-conditions", "description": "Điều kiện cần thiết trước khi chạy test.", "sub_steps": [
                "Tài khoản (VD: Đăng nhập bằng Role Admin)",
                "Dữ liệu sẵn có (VD: Đơn hàng số #123 đang ở trạng thái Pending)",
                "Cấu hình hệ thống (VD: Đã bật tính năng thanh toán VNPay)"
            ]},
            {"step": 3, "title": "Viết các bước thực hiện (Test Steps)", "description": "Liệt kê thao tác từng bước một.", "sub_steps": [
                "Bước phải cụ thể, thao tác trên giao diện: Click nút X, Nhập Y vào ô Z",
                "Không ghi chung chung (VD: 'Thanh toán đơn hàng' là sai. Phải là 'Click Thanh toán → Chọn VNPay → Nhập thẻ → Bấm Submit')"
            ]},
            {"step": 4, "title": "Xác định Expected Result", "description": "Kết quả mong đợi sau khi thực hiện thao tác.", "sub_steps": [
                "Hệ thống phải hiển thị cái gì? (VD: Thông báo 'Thành công' màu xanh)",
                "Dữ liệu thay đổi thế nào? (VD: Trạng thái đơn đổi thành 'Paid')",
                "Email/SMS có được gửi không?"
            ]},
            {"step": 5, "title": "Review & Cập nhật Traceability", "description": "Đảm bảo Test Case phủ hết Requirement.", "sub_steps": [
                "Mỗi Test Case phải link về Requirement ID / User Story ID",
                "Kiểm tra xem có AC nào chưa có Test Case tương ứng không?"
            ]}
        ],
        "outputs_detail": [
            {"name": "Test Case Document", "format": "Markdown Table", "template": "| TC ID | Requirement ID | Tên Test Case | Pre-conditions | Test Steps | Expected Result | Priority |\n|---|---|---|---|---|---|---|\n| TC-001 | US-PAY-01 | Thanh toán thành công thẻ tín dụng | User đã login, Giỏ hàng có sp | 1. Chọn CC<br>2. Nhập số thẻ hợp lệ<br>3. Bấm Thanh toán | Hiện popup 'Thành công'. Đơn hàng chuyển 'Paid' | High |\n| TC-002 | US-PAY-01 | Thanh toán thẻ hết hạn | User đã login | 1. Chọn CC<br>2. Nhập số thẻ hết hạn<br>3. Bấm Thanh toán | Báo lỗi 'Thẻ hết hạn'. Đơn vẫn 'Pending' | Medium |"}
        ],
        "sub_skills": ["Equivalence Partitioning (Phân vùng tương đương)", "Boundary Value Analysis (Phân tích giá trị biên)", "Error Guessing"],
        "business_rules": [
            "BR-TC-01: Mỗi Test Case chỉ nên test 1 kịch bản cụ thể.",
            "BR-TC-02: Test Steps phải rõ ràng, có thể lặp lại (Repeatable) với kết quả nhất quán.",
            "BR-TC-03: Expected Result phải bao gồm UI (Giao diện) và Data (Dữ liệu).",
            "BR-TC-04: Luôn có Test Case cho trường hợp dữ liệu rỗng (Empty/Null) nếu là Form."
        ],
        "edge_cases": [
            "Test tích hợp (Integration): Hệ thống bên thứ 3 chậm/không phản hồi (Timeout)",
            "Test đồng thời (Concurrency): 2 người cùng mua món hàng cuối cùng"
        ],
        "checklist": [
            "Đã có Happy Path?",
            "Đã có Negative Path (Lỗi nghiệp vụ)?",
            "Đã test giá trị biên (Min/Max)?",
            "Pre-conditions đã rõ ràng?",
            "Test Steps có thao tác được không?",
            "Expected Result có đo lường/quan sát được không?",
            "Đã cover hết Acceptance Criteria?"
        ],
        "example": "Xem Test Case mẫu trong Outputs.",
        "related_skills": ["Write User Story", "Phân tích CRUD", "UAT"],
        "quality_criteria": ["Phải có Happy + Negative Path", "Steps phải action-oriented", "Expected Result phải rõ UI/Data"],
        "estimated_effort": "0.5-1 ngày / User Story",
        "prompt_role": "Senior QA/QC Analyst am hiểu quy trình test phần mềm.",
        "prompt_task": "Viết Test Case chi tiết từ Requirement được cung cấp.",
        "prompt_context": "Team chuẩn bị Release, cần bộ Test Case để đảm bảo chất lượng tính năng.",
        "prompt_rules": [
            "Mỗi Requirement/AC PHẢI có ít nhất 1 Happy Path và 1 Negative Path.",
            "Test Steps PHẢI là thao tác cụ thể trên giao diện (Nhập, Click, Chọn).",
            "Expected Result PHẢI mô tả cả thay đổi trên Giao diện VÀ Dữ liệu (nếu có).",
            "PHẢI đánh giá Priority (High/Medium/Low) cho mỗi Test Case.",
            "Output PHẢI là dạng bảng Test Case chuẩn."
        ],
        "prompt_example": ""
    },
    # ================================================================
    # Testing - UAT
    # ================================================================
    {
        "path": "06-Testing/UAT",
        "name": "Kế hoạch UAT",
        "level": "Level 3 - Architecture Skill",
        "domain": "Testing",
        "tags": ["Testing", "UAT", "User Acceptance", "Plan", "Sign-off"],
        "purpose": "Lập User Acceptance Testing (UAT) Plan để hướng dẫn Khách hàng (End Users) tự kiểm thử hệ thống trước khi Go-live. Đảm bảo UAT diễn ra suôn sẻ, đúng nghiệp vụ thực tế và nhận được Sign-off.",
        "when_to_use": "Sử dụng trước khi dự án/Sprint kết thúc và bàn giao cho khách hàng kiểm tra.",
        "prerequisites": ["Hệ thống đã qua Internal QA", "Đã có UAT Environment"],
        "inputs_detail": [
            {"name": "BRD / Scope", "description": "Phạm vi các chức năng cần UAT.", "required": True, "example": "UAT cho Phase 1: Inbound & Outbound WMS."},
            {"name": "Danh sách End Users", "description": "Những người sẽ tham gia test.", "required": True, "example": "Thủ kho, Quản lý kho, Kế toán kho."}
        ],
        "process_detail": [
            {"step": 1, "title": "Chuẩn bị Kế hoạch UAT (UAT Plan)", "description": "Xác định Scope, Timeline, Participants.", "sub_steps": [
                "In-scope: Các module sẽ test",
                "Out-of-scope: Các tính năng chưa test hoặc thuộc Phase sau",
                "Timeline: Bắt đầu khi nào, kết thúc khi nào (VD: 15/07 - 20/07)",
                "Participants: Gán từng kịch bản cho đúng Role (Thủ kho test Nhập hàng, Kế toán test Báo cáo)"
            ]},
            {"step": 2, "title": "Viết UAT Scenarios (Kịch bản nghiệp vụ)", "description": "Viết kịch bản theo luồng nghiệp vụ thực tế (End-to-end), không test từng nút lẻ.", "sub_steps": [
                "Thay vì test 'Tạo SO', viết kịch bản 'Nhận đơn từ KH → Tạo SO → Xuất kho → Giao hàng'",
                "Ngôn ngữ dùng trong UAT Scenario phải là ngôn ngữ business, KHÔNG dùng từ kỹ thuật (API, DB)",
                "Chuẩn bị dữ liệu mẫu (Test Data) thật giống thực tế"
            ]},
            {"step": 3, "title": "Chuẩn bị Môi trường UAT", "description": "Setup hệ thống cho khách test.", "sub_steps": [
                "Cài đặt URL môi trường UAT (tách biệt với DEV/PROD)",
                "Tạo sẵn tài khoản cho từng End User",
                "Tạo sẵn Master Data (Sản phẩm, Khách hàng, Tồn kho ban đầu)"
            ]},
            {"step": 4, "title": "Thực hiện UAT & Ghi nhận Issue", "description": "Quản lý quá trình test.", "sub_steps": [
                "Hướng dẫn (Kick-off) người dùng cách test và log lỗi",
                "Phân loại phản hồi: Bug (Làm sai yêu cầu) vs Change Request (Yêu cầu mới/đổi ý)",
                "Triage (Đánh giá Issue): Blocker (Sửa ngay), Minor (Sửa sau Go-live)"
            ]},
            {"step": 5, "title": "UAT Sign-off", "description": "Nghiệm thu.", "sub_steps": [
                "Tỷ lệ Pass > 95% và không có Blocker/Critical bug → Sign-off",
                "Khách hàng ký biên bản nghiệm thu UAT (UAT Sign-off Document)",
                "Sẵn sàng Go-live"
            ]}
        ],
        "outputs_detail": [
            {"name": "UAT Plan", "format": "Markdown Document", "template": "# UAT Plan: [Tên dự án]\n\n## 1. Scope & Timeline\n- **In-scope:** [Module]\n- **Timeline:** [Dates]\n\n## 2. Participants\n| Tên | Role | Scope Test |\n|---|---|---|\n| Nguyễn Văn A | Thủ kho | Inbound, Outbound |\n| Lê Thị B | Kế toán | Inventory, Report |\n\n## 3. UAT Scenarios\n| Kịch bản | Mô tả nghiệp vụ (End-to-End) | Role thực hiện | Trạng thái (Pass/Fail) | Ghi chú |\n|---|---|---|---|---|\n| UAT-01 | Quy trình nhập kho hoàn chỉnh: Tạo PO → Nhận hàng → QC → Putaway | Thủ kho + QC | | |\n| UAT-02 | Trả hàng NCC: Lập phiếu trả → Xuất hàng → Cập nhật tồn | Kế toán kho | | |\n\n## 4. Defect Management\n- Công cụ báo lỗi: [Jira / Google Sheet]\n- Tiêu chí ưu tiên: Blocker, High, Medium, Low\n\n## 5. Sign-off Criteria\n- 100% Blocker/High bugs được fix.\n- Kịch bản Pass > 95%."},
            {"name": "UAT Sign-off Form", "format": "Markdown Document", "template": "## BIÊN BẢN NGHIỆM THU UAT\n\n- **Dự án:**\n- **Ngày:**\n- **Kết quả UAT:** [Số Pass] / [Tổng số]\n- **Kết luận:** Đồng ý Go-live / Không đồng ý\n\n**Đại diện Khách hàng (Ký tên):**"}
        ],
        "sub_skills": ["End-to-End Scenario Design", "Test Data Preparation", "Defect Triage (Phân loại lỗi)"],
        "business_rules": [
            "BR-UAT-01: UAT Scenarios PHẢI mô tả theo luồng nghiệp vụ đầu cuối (End-to-end), không test module rời rạc.",
            "BR-UAT-02: Phải phân định rõ ràng giữa Bug và CR (Change Request) trong UAT.",
            "BR-UAT-03: KHÔNG Go-live nếu UAT chưa được Sign-off bởi Key User/Sponsor."
        ],
        "edge_cases": [
            "Khách hàng log CR nhưng bảo là Bug → BA phải dùng SRS/BRD để đối chiếu và scope quản lý",
            "Khách hàng bận không chịu test → Đặt deadline cứng, 'auto sign-off' nếu không phản hồi sau X ngày (cần thỏa thuận trong hợp đồng)"
        ],
        "checklist": [
            "Đã có danh sách người test (Participants)?",
            "Đã viết UAT Scenarios dạng End-to-end?",
            "Scenarios có dễ hiểu với người không biết IT?",
            "Đã chuẩn bị Test Data (Master data)?",
            "Đã có công cụ/biểu mẫu để khách báo lỗi?",
            "Đã định nghĩa Sign-off Criteria?"
        ],
        "example": "Xem UAT Plan template trong Outputs.",
        "related_skills": ["Write BRD", "Viết Test Case"],
        "quality_criteria": ["Scenario phải End-to-end", "Ngôn ngữ kinh doanh", "Có Sign-off Criteria rõ ràng"],
        "estimated_effort": "3-5 ngày",
        "prompt_role": "Senior Business Analyst / UAT Manager chuyên triển khai hệ thống doanh nghiệp.",
        "prompt_task": "Lập Kế hoạch UAT và các kịch bản nghiệp vụ cho khách hàng kiểm thử.",
        "prompt_context": "Dự án chuẩn bị Go-live, cần khách hàng vào hệ thống test nghiệp vụ thực tế.",
        "prompt_rules": [
            "UAT Scenarios PHẢI thiết kế theo luồng End-to-end (Quy trình xuyên suốt), KHÔNG test tính năng rời rạc.",
            "Ngôn ngữ sử dụng trong kịch bản PHẢI là ngôn ngữ nghiệp vụ, KHÔNG chứa từ vựng kỹ thuật.",
            "PHẢI phân công rõ Role nào test kịch bản nào.",
            "PHẢI có tiêu chí Sign-off rõ ràng.",
            "Output PHẢI bao gồm: UAT Plan, Danh sách Scenarios, Quy trình báo lỗi."
        ],
        "prompt_example": ""
    },
    # ================================================================
    # Project - Sprint Planning
    # ================================================================
    {
        "path": "07-Project/Sprint",
        "name": "Sprint Planning",
        "level": "Level 2 - Business Skill",
        "domain": "Project",
        "tags": ["Agile", "Scrum", "Sprint", "Planning", "Estimation"],
        "purpose": "Hỗ trợ Product Owner (PO) và Scrum Team lập kế hoạch cho một Sprint, bao gồm: xác định Sprint Goal, chọn User Stories từ Backlog, estimate effort (Story Points) và lập Sprint Backlog.",
        "when_to_use": "Sử dụng vào ngày đầu tiên của mỗi Sprint.",
        "prerequisites": ["Đã có Product Backlog được ưu tiên (Groomed)", "Team biết Capacity của mình"],
        "inputs_detail": [
            {"name": "Product Backlog", "description": "Danh sách User Stories đã sẵn sàng (Ready).", "required": True, "example": "Top 10 User Stories đã có Acceptance Criteria."},
            {"name": "Team Capacity", "description": "Tổng số Story Points hoặc Giờ team có thể làm trong Sprint này.", "required": True, "example": "Team có 5 Dev, làm 2 tuần. Capacity = 40 Story Points. Trừ đi ngày lễ, nghỉ phép."}
        ],
        "process_detail": [
            {"step": 1, "title": "Xác định Sprint Goal", "description": "Mục tiêu kinh doanh của Sprint này là gì?", "sub_steps": [
                "PO đưa ra mục tiêu. VD: 'Hoàn thành luồng thanh toán qua VNPay'",
                "Goal phải ngắn gọn, truyền cảm hứng, và đo lường được"
            ]},
            {"step": 2, "title": "Chọn Item từ Product Backlog", "description": "Kéo các item phù hợp với Goal vào Sprint.", "sub_steps": [
                "Bắt đầu từ item ưu tiên cao nhất",
                "Chỉ chọn những item thỏa mãn Definition of Ready (Đã rõ ràng, có AC, có Mockup)"
            ]},
            {"step": 3, "title": "Estimation (Ước lượng)", "description": "Team Dev ước lượng độ lớn của từng item.", "sub_steps": [
                "Sử dụng Planning Poker (Fibonacci: 1, 2, 3, 5, 8, 13)",
                "Nếu item > 8 points → Bắt buộc phải chia nhỏ (Story Splitting)",
                "Chỉ Dev mới có quyền estimate, PO/BA chỉ giải thích nghiệp vụ"
            ]},
            {"step": 4, "title": "Lập Task (Phân rã kỹ thuật)", "description": "Dev chia Story thành các sub-tasks.", "sub_steps": [
                "1 User Story → Task DB, Task API, Task Frontend, Task QC",
                "Task thường estimate bằng giờ (1-8 giờ)"
            ]},
            {"step": 5, "title": "Chốt Sprint Backlog (Commitment)", "description": "Kiểm tra xem khối lượng công việc có vượt quá Capacity không.", "sub_steps": [
                "Tổng Story Points được chọn <= Team Capacity",
                "Nếu vượt quá → Đẩy bớt item độ ưu tiên thấp xuống cuối Sprint hoặc trả về Backlog",
                "Team cam kết (Commit) hoàn thành Sprint Goal"
            ]}
        ],
        "outputs_detail": [
            {"name": "Sprint Plan Document", "format": "Markdown Table", "template": "# Sprint [N] Planning\n**Sprint Goal:** Hoàn thành luồng thanh toán VNPay.\n**Capacity:** 40 Story Points.\n\n## Sprint Backlog\n| ID | User Story | Priority | Points | Status (DOR) |\n|---|---|---|---|---|\n| US-20 | Tích hợp API VNPay | High | 5 | Ready |\n| US-21 | Giao diện nút thanh toán VNPay | High | 3 | Ready |\n| US-22 | Webhook nhận kết quả từ VNPay | High | 5 | Ready |\n| US-25 | Báo cáo giao dịch lỗi | Medium | 8 | Ready |\n\n**Total Points Committed:** 21 / 40 (Sẽ kéo thêm Bug/Tech debt)"}
        ],
        "sub_skills": ["Story Splitting", "Planning Poker", "Capacity Calculation"],
        "business_rules": [
            "BR-SPRINT-01: KHÔNG đưa item chưa thỏa mãn Definition of Ready vào Sprint.",
            "BR-SPRINT-02: Item > 8 points phải được chia nhỏ.",
            "BR-SPRINT-03: Không thay đổi Sprint Goal sau khi Sprint đã bắt đầu.",
            "BR-SPRINT-04: Team không nhận khối lượng công việc vượt quá Capacity đã thống nhất."
        ],
        "edge_cases": [
            "Có task Support/Hotfix gấp giữa Sprint → Phải bỏ bớt 1 Story có điểm tương đương ra khỏi Sprint",
            "Thiếu chuyên môn trong team (VD: Thiếu QA) → Ảnh hưởng capacity, cần cân nhắc"
        ],
        "checklist": [
            "Đã có Sprint Goal?",
            "Đã tính Team Capacity (trừ ngày nghỉ)?",
            "Tất cả item chọn đều 'Ready' (Có AC)?",
            "Không có item nào > 8 points?",
            "Tổng points <= Capacity?",
            "Team đã Commit?"
        ],
        "example": "Xem Sprint Plan template trong Outputs.",
        "related_skills": ["Write User Story", "Review Requirement"],
        "quality_criteria": ["Phải có Sprint Goal", "Không nhận vượt Capacity", "Mọi item phải được Estimate"],
        "estimated_effort": "2-4 giờ (Meeting)",
        "prompt_role": "Scrum Master / Agile Business Analyst.",
        "prompt_task": "Hỗ trợ lên kế hoạch cho một Sprint hiệu quả.",
        "prompt_context": "Team chuẩn bị bắt đầu Sprint mới, cần chọn danh sách việc phù hợp với năng lực và mục tiêu.",
        "prompt_rules": [
            "PHẢI yêu cầu thông tin về Team Capacity và Product Backlog trước khi lập plan.",
            "PHẢI đưa ra Sprint Goal.",
            "Nếu có Story > 8 points, PHẢI đề xuất cách chia nhỏ (Story Splitting).",
            "Tổng điểm chọn KHÔNG ĐƯỢC vượt quá Capacity.",
            "Output PHẢI là một bảng Sprint Backlog minh bạch."
        ],
        "prompt_example": ""
    },
    # ================================================================
    # API/Integration - API Contract
    # ================================================================
    {
        "path": "08-Integration/API",
        "name": "Thiết kế API Contract",
        "level": "Level 3 - Architecture Skill",
        "domain": "Integration",
        "tags": ["API", "Integration", "REST", "JSON", "Contract"],
        "purpose": "Thiết kế đặc tả giao tiếp giữa Front-end và Back-end (hoặc giữa 2 hệ thống) qua RESTful API. Cung cấp rõ ràng Endpoints, Method, Request Payload (Body/Params), Response Payload và Error Codes để 2 bên có thể làm việc độc lập.",
        "when_to_use": "Sử dụng trong giai đoạn System Design, trước khi Dev bắt đầu code.",
        "prerequisites": ["Đã có ERD và UI Mockups", "Hiểu RESTful API principles"],
        "inputs_detail": [
            {"name": "Nghiệp vụ chức năng", "description": "Chức năng API cần phục vụ.", "required": True, "example": "Chức năng: Lấy danh sách sản phẩm (có phân trang, filter) và Tạo mới sản phẩm."}
        ],
        "process_detail": [
            {"step": 1, "title": "Xác định Endpoints & Methods", "description": "Thiết kế URL chuẩn REST.", "sub_steps": [
                "Dùng danh từ số nhiều: `/api/v1/products`",
                "GET: Lấy dữ liệu (List, Detail)",
                "POST: Tạo mới",
                "PUT: Cập nhật toàn bộ",
                "PATCH: Cập nhật 1 phần (VD: update status)",
                "DELETE: Xóa"
            ]},
            {"step": 2, "title": "Thiết kế Request (Input)", "description": "Dữ liệu Front-end gửi lên.", "sub_steps": [
                "Headers: `Authorization: Bearer <token>`, `Content-Type: application/json`",
                "Path Variables: VD `/products/{id}`",
                "Query Params (dùng cho GET): `?page=1&limit=20&status=active`",
                "Body (JSON - dùng cho POST/PUT/PATCH): Xác định các trường, kiểu dữ liệu, required?"
            ]},
            {"step": 3, "title": "Thiết kế Response (Output) - Happy Path", "description": "Dữ liệu trả về khi thành công.", "sub_steps": [
                "Status Code: 200 OK (GET, PUT), 201 Created (POST)",
                "Body Data: Cấu trúc JSON trả về.",
                "Nên bọc data trong response chuẩn: `{ 'success': true, 'data': {...}, 'message': '' }`",
                "Có Pagination meta data nếu là API List"
            ]},
            {"step": 4, "title": "Thiết kế Error Codes - Negative Path", "description": "Các trường hợp lỗi.", "sub_steps": [
                "400 Bad Request: Lỗi validation (thiếu trường, sai format)",
                "401 Unauthorized: Chưa đăng nhập, token hết hạn",
                "403 Forbidden: Đã đăng nhập nhưng không có quyền",
                "404 Not Found: Không tìm thấy entity",
                "500 Internal Server Error: Lỗi hệ thống"
            ]}
        ],
        "outputs_detail": [
            {"name": "API Document (Swagger/OpenAPI style)", "format": "Markdown", "template": "## 1. Lấy danh sách sản phẩm\n- **Endpoint:** `GET /api/v1/products`\n- **Description:** Trả về danh sách sản phẩm có phân trang.\n\n### Request\n- **Query Params:**\n  - `page` (int, default=1)\n  - `limit` (int, default=20)\n  - `search` (string, optional)\n\n### Response (200 OK)\n```json\n{\n  \"success\": true,\n  \"data\": [\n    {\n      \"id\": 1,\n      \"code\": \"PRD-001\",\n      \"name\": \"Sản phẩm A\",\n      \"price\": 10000\n    }\n  ],\n  \"meta\": {\n    \"total\": 150,\n    \"page\": 1,\n    \"last_page\": 8\n  }\n}\n```\n\n## 2. Tạo sản phẩm mới\n- **Endpoint:** `POST /api/v1/products`\n### Request Body (JSON)\n```json\n{\n  \"code\": \"PRD-002\", // Required, Unique\n  \"name\": \"Sản phẩm B\", // Required\n  \"price\": 20000 // Required, > 0\n}\n```\n### Response (201 Created)\n...\n### Errors\n- `400 Bad Request`: {\"success\": false, \"message\": \"Mã sản phẩm đã tồn tại\"}"}
        ],
        "sub_skills": ["RESTful Design", "JSON Modeling", "Error Code Mapping"],
        "business_rules": [
            "BR-API-01: Endpoints phải dùng danh từ số nhiều (VD: /users, /orders).",
            "BR-API-02: Không dùng verb trong URL (VD SAI: /get-users. ĐÚNG: GET /users).",
            "BR-API-03: Mọi Response phải có cấu trúc chuẩn thống nhất (success, data, message, error).",
            "BR-API-04: API List bắt buộc phải có Pagination."
        ],
        "edge_cases": [
            "Payload quá lớn → Thiết kế Bulk Insert API hoặc Async Processing",
            "Rate Limiting → Cần trả về 429 Too Many Requests nếu spam API"
        ],
        "checklist": [
            "Method HTTP có chuẩn REST chưa?",
            "URL có đúng nguyên tắc số nhiều không?",
            "Request Body đã định nghĩa field/type/required chưa?",
            "Response Body (Thành công) có cấu trúc chưa?",
            "Đã mô tả mã lỗi 400, 401, 403, 404, 500 chưa?",
            "Có xử lý phân trang cho API danh sách không?"
        ],
        "example": "Xem API Document template trong Outputs.",
        "related_skills": ["Thiết kế ERD", "Thiết kế module", "Phân tích màn hình CRUD"],
        "quality_criteria": ["Chuẩn RESTful", "JSON hợp lệ", "Đủ Error Codes"],
        "estimated_effort": "1-2 ngày / module",
        "prompt_role": "Senior Integration Business Analyst / API Designer.",
        "prompt_task": "Thiết kế API Contract chuẩn RESTful cho tính năng yêu cầu.",
        "prompt_context": "Cần thiết kế API spec chi tiết để Backend và Frontend có thể code song song.",
        "prompt_rules": [
            "PHẢI tuân thủ nguyên tắc RESTful (Dùng GET, POST, PUT, DELETE, URL là danh từ số nhiều).",
            "PHẢI thiết kế Input (Headers, Query Params, JSON Body).",
            "PHẢI thiết kế Output (JSON Response cho trường hợp 200/201).",
            "PHẢI định nghĩa các Error Codes chuẩn (400, 401, 403, 404, 500).",
            "Output PHẢI sử dụng định dạng JSON rõ ràng trong Markdown block."
        ],
        "prompt_example": ""
    }
]

if __name__ == "__main__":
    print("=== Expanding: Testing + Project + API Skills ===")
    run(skills)
