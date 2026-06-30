import sys
sys.path.insert(0, r"e:\BA Skill Library")
from skill_generator import run

skills = [
    # ================================================================
    # Modeling - BPMN
    # ================================================================
    {
        "path": "03-Modeling/BPMN",
        "name": "Vẽ BPMN",
        "level": "Level 2 - Business Skill",
        "domain": "Modeling",
        "tags": ["Modeling", "BPMN", "Process", "Flowchart", "Workflow"],
        "purpose": "Mô hình hóa quy trình nghiệp vụ bằng chuẩn BPMN (Business Process Model and Notation) 2.0. Sử dụng Swimlanes để phân định rõ trách nhiệm của từng vai trò (Role/Department) và các Gateways để xử lý logic rẽ nhánh.",
        "when_to_use": "Sử dụng khi cần thống nhất quy trình làm việc (As-Is hoặc To-Be) với khách hàng hoặc tài liệu hóa quy trình cho đội Dev.",
        "prerequisites": ["Đã phỏng vấn lấy yêu cầu quy trình", "Hiểu chuẩn BPMN cơ bản"],
        "inputs_detail": [
            {"name": "Mô tả quy trình", "description": "Text mô tả các bước thực hiện công việc.", "required": True, "example": "Nhân viên kho nhận hàng. Kế toán kiểm tra hóa đơn. Nếu khớp thì thủ kho cất hàng, nếu không khớp thì trả lại NCC."}
        ],
        "process_detail": [
            {"step": 1, "title": "Xác định Scope & Participants", "description": "Quy trình bắt đầu/kết thúc khi nào và ai tham gia?", "sub_steps": [
                "Xác định Pool (Tổ chức/Hệ thống) và Swimlanes (Vai trò: User, Admin, System)",
                "Xác định Start Event (Trigger: Khi nào quy trình bắt đầu?)",
                "Xác định End Event (Kết quả cuối cùng là gì?)"
            ]},
            {"step": 2, "title": "Mô hình hóa chuỗi hoạt động (Tasks)", "description": "Vẽ các bước thực hiện.", "sub_steps": [
                "Sử dụng User Task cho thao tác của con người",
                "Sử dụng Service Task cho xử lý tự động của hệ thống",
                "Ghi nhãn Task bằng Động từ + Danh từ (VD: 'Tạo đơn hàng' thay vì 'Đơn hàng')"
            ]},
            {"step": 3, "title": "Xử lý logic rẽ nhánh (Gateways)", "description": "Sử dụng các cổng quyết định.", "sub_steps": [
                "Exclusive Gateway (X): Rẽ 1 trong nhiều nhánh (VD: Approved OR Rejected)",
                "Parallel Gateway (+): Thực hiện đồng thời nhiều nhánh (VD: Vừa gửi email VÀ vừa in phiếu)",
                "Inclusive Gateway (O): Có thể rẽ 1 hoặc nhiều nhánh (VD: Đặt hàng A, B hoặc cả A và B)"
            ]},
            {"step": 4, "title": "Xử lý sự kiện (Events)", "description": "Các sự kiện xảy ra trong quá trình.", "sub_steps": [
                "Timer Event: Chờ 3 ngày, hoặc gửi nhắc nhở mỗi thứ Hai",
                "Message Event: Chờ phản hồi từ NCC, hoặc Gửi email cho khách",
                "Error Event: Xử lý ngoại lệ (VD: Lỗi API thanh toán)"
            ]},
            {"step": 5, "title": "Review & Tối ưu", "description": "Kiểm tra tính hợp lý.", "sub_steps": [
                "Có đường cụt (Dead end) nào không? Mọi luồng đều phải dẫn đến End Event.",
                "Quy trình có quá phức tạp không? Nếu > 20 tasks, nên tách thành Sub-process."
            ]}
        ],
        "outputs_detail": [
            {"name": "BPMN Code (Mermaid)", "format": "Mermaid stateDiagram hoặc flowchart", "template": "```mermaid\nsequenceDiagram\n    actor Khách\n    participant HệThống\n    participant Kho\n    Khách->>HệThống: Đặt hàng\n    HệThống-->>Kho: Báo đơn mới\n``` (Ghi chú: Mermaid không hỗ trợ BPMN native tốt, dùng flowchart kết hợp subgraph làm swimlane)"},
            {"name": "Mô tả Text của Quy trình", "format": "Markdown List", "template": "1. **[Thủ kho]** Nhận hàng từ NCC.\n2. **[Hệ thống]** Kiểm tra PO khớp với GRN.\n  - Nếu khớp: Chuyển sang bước 3.\n  - Nếu KHÔNG khớp: Trả lại NCC (Kết thúc)."}
        ],
        "sub_skills": ["Gateway Logic", "Swimlane Design", "Sub-process Identification"],
        "business_rules": [
            "BR-BPMN-01: Mọi quy trình đều phải có Start Event và End Event.",
            "BR-BPMN-02: Tên Task phải bắt đầu bằng động từ.",
            "BR-BPMN-03: Không để đường cụt (Dead-end) trong quy trình, mọi nhánh rẽ phải dẫn đến kết quả cuối.",
            "BR-BPMN-04: Gateway dùng để kiểm tra điều kiện, không phải để thực hiện công việc (VD: Nút kim cương chứa 'Tổng > 100?' thay vì 'Kiểm tra tổng')."
        ],
        "edge_cases": [
            "Quy trình có vòng lặp (Loop/Rework) → Dùng mũi tên quay ngược lại task trước (VD: Yêu cầu sửa lại báo giá)",
            "Quy trình có Timeout → Dùng Timer Boundary Event (VD: Sau 24h không duyệt thì tự động Reject)"
        ],
        "checklist": [
            "Có Start và End Event?",
            "Đã chia Swimlane theo Role chưa?",
            "Tên Task có bắt đầu bằng động từ?",
            "Gateway có dán nhãn điều kiện (Yes/No)?",
            "Mọi nhánh rẽ đều có điểm kết thúc?",
            "Có xử lý ngoại lệ (Error/Timeout)?",
            "Nếu quá dài, đã chia thành Sub-process chưa?"
        ],
        "example": "Xem mô tả flowchart trong phần Outputs.",
        "related_skills": ["Phân tích Use Case", "Gap Analysis"],
        "quality_criteria": ["Không có đường cụt", "Tên task là Action", "Phân định rõ Role (Swimlane)"],
        "estimated_effort": "0.5-1 ngày",
        "prompt_role": "Senior Business Analyst chuyên vẽ mô hình BPMN.",
        "prompt_task": "Chuyển đổi mô tả quy trình bằng text thành mô hình BPMN (dưới dạng Mermaid flowchart/sequence) và mô tả từng bước chi tiết.",
        "prompt_context": "Cần tài liệu hóa quy trình để thống nhất với khách hàng và làm đầu vào cho team Dev thiết kế hệ thống.",
        "prompt_rules": [
            "PHẢI sử dụng Swimlane (Subgraph trong Mermaid) để phân định vai trò.",
            "PHẢI có Start và End rõ ràng.",
            "Tên các bước PHẢI bắt đầu bằng động từ.",
            "Cổng rẽ nhánh (Gateway) PHẢI có điều kiện rõ ràng (vd: Yes/No, Approved/Rejected).",
            "Output PHẢI bao gồm Mermaid code và danh sách mô tả các bước bằng Text."
        ],
        "prompt_example": ""
    },
    # ================================================================
    # Modeling - Sequence Diagram
    # ================================================================
    {
        "path": "03-Modeling/Sequence",
        "name": "Vẽ Sequence Diagram",
        "level": "Level 3 - Architecture Skill",
        "domain": "Modeling",
        "tags": ["Modeling", "UML", "Sequence", "API", "System", "Integration"],
        "purpose": "Mô hình hóa luồng giao tiếp (Tương tác) giữa các đối tượng (Người dùng, Frontend, Backend, Database, 3rd Party API) theo trình tự thời gian. Giúp team Dev hiểu rõ thứ tự gọi API và luồng dữ liệu.",
        "when_to_use": "Sử dụng khi thiết kế luồng đăng nhập (SSO/OAuth), tích hợp cổng thanh toán (VNPay, Momo), hoặc các luồng nghiệp vụ phức tạp đòi hỏi nhiều hệ thống tham gia.",
        "prerequisites": ["Đã có API Contract hoặc luồng nghiệp vụ", "Hiểu kiến trúc hệ thống cơ bản"],
        "inputs_detail": [
            {"name": "Luồng nghiệp vụ phức tạp", "description": "Mô tả tương tác giữa các hệ thống.", "required": True, "example": "User thanh toán VNPay: User click thanh toán → Web gọi Backend → Backend gọi VNPay tạo URL → Trả về Web → Web redirect sang VNPay → User quẹt thẻ → VNPay gọi Webhook về Backend."}
        ],
        "process_detail": [
            {"step": 1, "title": "Xác định Lifelines (Đối tượng)", "description": "Ai/Cái gì tham gia vào luồng?", "sub_steps": [
                "Liệt kê các thành phần: Actor (User), Frontend (Web/App), API Server, Database, 3rd Party (VNPay, SendGrid, Firebase)"
            ]},
            {"step": 2, "title": "Vẽ các Message (Lời gọi) theo thời gian", "description": "Trình tự gọi hàm/API từ trên xuống dưới.", "sub_steps": [
                "Synchronous Message (Mũi tên nét liền, mũi nhọn): Đợi phản hồi (VD: API Call `POST /checkout`)",
                "Asynchronous Message (Mũi tên nét liền, mũi hở): Gọi và không cần chờ ngay (VD: Publish message to Queue)",
                "Return Message (Mũi tên nét đứt): Trả về kết quả (VD: Trả về URL thanh toán)"
            ]},
            {"step": 3, "title": "Sử dụng Fragments (Khối logic)", "description": "Thể hiện rẽ nhánh hoặc vòng lặp.", "sub_steps": [
                "Alt (Alternative / If-Else): Nếu thẻ hợp lệ → Trừ tiền. Ngược lại → Báo lỗi.",
                "Opt (Optional / If): Khối chỉ thực hiện khi thỏa điều kiện (VD: Nếu User dùng Voucher thì gọi API kiểm tra Voucher).",
                "Loop (Vòng lặp): Chạy nhiều lần (VD: Gửi thông báo cho từng người trong danh sách)."
            ]},
            {"step": 4, "title": "Bổ sung tham số (Payload/Response)", "description": "Ghi rõ truyền cái gì và nhận cái gì.", "sub_steps": [
                "Trên mũi tên gọi: Ghi rõ method và tham số quan trọng (VD: `POST /payment {amount, orderId}`)",
                "Trên mũi tên trả về: Ghi rõ HTTP Status hoặc dữ liệu chính (VD: `200 OK {paymentUrl}`)"
            ]}
        ],
        "outputs_detail": [
            {"name": "Sequence Diagram", "format": "Mermaid sequenceDiagram", "template": "```mermaid\nsequenceDiagram\n    autonumber\n    actor User\n    participant Web\n    participant API as Backend API\n    participant DB as Database\n    participant VNPay\n\n    User->>Web: Click Thanh toán\n    Web->>API: POST /checkout {orderId}\n    API->>DB: Check Order Status\n    DB-->>API: Status = Pending\n    API->>VNPay: Create Payment URL {amount, returnUrl}\n    VNPay-->>API: paymentUrl\n    API-->>Web: 200 OK {paymentUrl}\n    Web->>User: Redirect to VNPay\n    \n    alt Thanh toán thành công\n        User->>VNPay: Nhập OTP\n        VNPay->>API: Webhook (IPN) {status=00}\n        API->>DB: Update Order Status = Paid\n    else Thanh toán thất bại\n        User->>VNPay: Hủy giao dịch\n        VNPay->>API: Webhook (IPN) {status=24}\n        API->>DB: Update Order Status = Failed\n    end\n```"}
        ],
        "sub_skills": ["System Identification", "API Flow Design", "Fragment Logic (Alt/Opt/Loop)"],
        "business_rules": [
            "BR-SEQ-01: Trình tự thời gian phải chảy từ trên xuống dưới.",
            "BR-SEQ-02: API calls phải dùng mũi tên liền (Synchronous) và có Return message (mũi tên đứt).",
            "BR-SEQ-03: Bắt buộc dùng block 'Alt' nếu có nhánh Thành công / Thất bại.",
            "BR-SEQ-04: Actor (Người dùng) luôn nằm ngoài cùng bên trái."
        ],
        "edge_cases": [
            "Hệ thống bên thứ 3 chậm (Timeout) → Xử lý Timeout bằng khối Alt",
            "Webhook (IPN) đến trễ hoặc đến trước Return URL → Thiết kế Idempotent (Chống trùng lặp)"
        ],
        "checklist": [
            "Đã đủ các Lifeline (FE, BE, DB, 3rd Party)?",
            "Đã phân biệt Sync và Async Message?",
            "Đã ghi tham số Input/Output trên mũi tên chưa?",
            "Đã có khối Alt cho Happy Path và Negative Path?",
            "Actor có ở bên trái cùng không?",
            "Code Mermaid đã chạy được chưa?"
        ],
        "example": "Xem ví dụ thanh toán VNPay trong Outputs.",
        "related_skills": ["Thiết kế API Contract", "Vẽ BPMN"],
        "quality_criteria": ["Đủ thành phần hệ thống", "Có xử lý lỗi (Alt block)", "Ghi rõ API method/payload"],
        "estimated_effort": "0.5 ngày / luồng",
        "prompt_role": "Senior Solution Architect / Technical Business Analyst.",
        "prompt_task": "Thiết kế Sequence Diagram chi tiết cho luồng tích hợp hệ thống.",
        "prompt_context": "Cần mô hình hóa luồng gọi API và tương tác giữa các hệ thống để team Dev implement đúng thứ tự.",
        "prompt_rules": [
            "PHẢI sử dụng ngôn ngữ Mermaid sequenceDiagram.",
            "PHẢI xác định đầy đủ các participant (Actor, Frontend, Backend, DB, 3rd Party).",
            "PHẢI sử dụng khối `alt` để xử lý nhánh rẽ (Thành công / Thất bại).",
            "PHẢI ghi rõ HTTP Method (GET/POST) và dữ liệu truyền đi trên mũi tên.",
            "Mỗi luồng Request (mũi tên liền) PHẢI có một luồng Response tương ứng (mũi tên đứt)."
        ],
        "prompt_example": ""
    },
    # ================================================================
    # Templates - Email / Notification
    # ================================================================
    {
        "path": "04-UIUX/Templates",
        "name": "Thiết kế Notification",
        "level": "Level 1 - Basic Skill",
        "domain": "UIUX",
        "tags": ["UIUX", "Notification", "Email", "SMS", "Push"],
        "purpose": "Thiết kế nội dung, điều kiện kích hoạt (Trigger), đối tượng nhận và cấu trúc cho các mẫu thông báo đa kênh (Email, SMS, Push Notification, In-app).",
        "when_to_use": "Sử dụng khi hệ thống cần gửi thông báo (VD: Đăng ký thành công, Quên mật khẩu, Có đơn hàng mới, Cảnh báo tồn kho).",
        "prerequisites": ["Đã có SRS hoặc luồng quy trình"],
        "inputs_detail": [
            {"name": "Sự kiện (Event)", "description": "Hành động kích hoạt thông báo.", "required": True, "example": "Sự kiện: Khách hàng đặt hàng thành công."},
            {"name": "Loại thông báo", "description": "Kênh gửi.", "required": True, "example": "Email (gửi khách hàng), In-app (gửi Admin)."}
        ],
        "process_detail": [
            {"step": 1, "title": "Xác định Trigger & Recipient", "description": "Khi nào gửi và gửi cho ai?", "sub_steps": [
                "Trigger: Hành động kích hoạt (VD: SO status change to 'Paid')",
                "Recipient: Người nhận (VD: Email mua hàng, Quản lý kho, Admin)"
            ]},
            {"step": 2, "title": "Chọn Kênh (Channel) phù hợp", "description": "Email, SMS hay Push?", "sub_steps": [
                "Email: Gửi tài liệu dài, hóa đơn, OTP (nếu không gấp)",
                "SMS: Gửi OTP, thông báo giao hàng gấp (chi phí cao)",
                "Push Notification (Mobile): Nhắc nhở app, promotion",
                "In-app Notification (Web): Thông báo hệ thống, duyệt đơn"
            ]},
            {"step": 3, "title": "Thiết kế nội dung (Copywriting)", "description": "Viết nội dung thông báo.", "sub_steps": [
                "Tiêu đề (Subject): Ngắn gọn, rõ mục đích (VD: Xác nhận đơn hàng #12345)",
                "Lời chào: Cá nhân hóa (VD: Chào {{customer_name}})",
                "Nội dung chính: Đi thẳng vào vấn đề",
                "Call-to-Action (CTA): Nút hành động (VD: [Xem chi tiết đơn hàng])"
            ]},
            {"step": 4, "title": "Xác định Biến (Variables/Dynamic Data)", "description": "Các trường dữ liệu động.", "sub_steps": [
                "Sử dụng syntax {{variable_name}}",
                "VD: {{order_id}}, {{total_amount}}, {{payment_method}}, {{reset_link}}"
            ]},
            {"step": 5, "title": "Quy định tần suất & Ràng buộc", "description": "Chống spam.", "sub_steps": [
                "Không gửi SMS quá 3 lần/ngày cho 1 số",
                "Gom thông báo (Batching): VD Gửi email tổng hợp cuối ngày thay vì gửi từng email"
            ]}
        ],
        "outputs_detail": [
            {"name": "Notification Matrix", "format": "Markdown Table", "template": "| ID | Event Trigger | Channel | Recipient | Subject / Title | Variables |\n|---|---|---|---|---|---|\n| NTF-01 | Đặt hàng thành công | Email | Customer | Xác nhận đơn hàng {{order_id}} | {{customer_name}}, {{order_id}}, {{total_amount}} |\n| NTF-02 | Có đơn hàng mới | In-app | Admin | Đơn hàng mới từ {{customer_name}} | {{customer_name}}, {{order_id}} |"},
            {"name": "Email Template Detail", "format": "Markdown", "template": "**Template ID:** TPL-EMAIL-01\n**Event:** Reset Password\n**Subject:** Yêu cầu đặt lại mật khẩu của bạn\n\n**Body:**\nChào {{user_name}},\n\nChúng tôi nhận được yêu cầu đặt lại mật khẩu cho tài khoản liên kết với email này. Vui lòng click vào nút bên dưới để thiết lập mật khẩu mới:\n\n[ĐẶT LẠI MẬT KHẨU] (Link to: {{reset_link}})\n\n*Link này sẽ hết hạn sau {{expire_time}} phút.*\n\nNếu bạn không thực hiện yêu cầu này, vui lòng bỏ qua email.\n\nTrân trọng,\nTeam Hỗ trợ."}
        ],
        "sub_skills": ["UX Copywriting", "Variable Mapping", "Channel Selection"],
        "business_rules": [
            "BR-NTF-01: Mọi Email thông báo phải có link Unsubscribe (nếu là Marketing).",
            "BR-NTF-02: Thông báo OTP phải có thời gian hết hạn rõ ràng.",
            "BR-NTF-03: Nội dung In-app / Push không dài quá 100 ký tự.",
            "BR-NTF-04: Phải cá nhân hóa lời chào (Chèn Tên)."
        ],
        "edge_cases": [
            "Gửi thất bại (Bounced/Failed) → Hệ thống tự động retry 3 lần",
            "Khách hàng tắt nhận thông báo (Opt-out) → Chỉ gửi các thông báo cực kỳ quan trọng (OTP, Hóa đơn)"
        ],
        "checklist": [
            "Đã xác định đúng Trigger Event?",
            "Đã chọn đúng Kênh (Email/SMS/In-app)?",
            "Đã thiết kế tiêu đề (Subject) rõ ràng?",
            "Đã cá nhân hóa bằng Biến (Variables)?",
            "Đã có nút CTA (Call to action)?",
            "Đã thiết kế nội dung khi Lỗi (VD: Gửi lại mã)?"
        ],
        "example": "Xem Notification Matrix và Template trong Outputs.",
        "related_skills": ["Phân tích CRUD", "Write SRS"],
        "quality_criteria": ["Đủ 5 phần của Template", "Có Variable", "Có Trigger rõ ràng"],
        "estimated_effort": "0.5 ngày",
        "prompt_role": "Senior UX/BA Analyst chuyên thiết kế giao tiếp hệ thống.",
        "prompt_task": "Thiết kế ma trận thông báo (Notification Matrix) và chi tiết các template cho tính năng được yêu cầu.",
        "prompt_context": "Hệ thống cần gửi thông báo tự động cho người dùng qua các kênh (Email, SMS, App) khi có sự kiện xảy ra.",
        "prompt_rules": [
            "PHẢI xác định rõ Trigger Event (Khi nào kích hoạt).",
            "PHẢI lựa chọn Channel phù hợp (SMS dùng cho OTP/gấp, Email dùng cho Chi tiết/Hóa đơn).",
            "PHẢI sử dụng biến động theo cú pháp {{variable_name}}.",
            "PHẢI thiết kế Call-to-action (CTA) nếu yêu cầu người dùng hành động.",
            "Output PHẢI bao gồm Notification Matrix (Dạng bảng) và nội dung Template chi tiết."
        ],
        "prompt_example": ""
    },
    # ================================================================
    # Project - Sprint Retrospective
    # ================================================================
    {
        "path": "07-Project/Sprint",
        "name": "Sprint Retrospective",
        "level": "Level 2 - Business Skill",
        "domain": "Project",
        "tags": ["Agile", "Scrum", "Sprint", "Retrospective", "Improvement"],
        "purpose": "Hỗ trợ Scrum Master / Đội ngũ đánh giá lại quá trình làm việc trong Sprint vừa qua, nhận diện những điểm tốt, điểm chưa tốt và đề xuất Action Items cụ thể để cải tiến cho Sprint tiếp theo (Continuous Improvement).",
        "when_to_use": "Sử dụng vào ngày cuối cùng của Sprint, sau khi kết thúc Sprint Review.",
        "prerequisites": ["Đã hoàn thành Sprint"],
        "inputs_detail": [
            {"name": "Kết quả Sprint (Sprint Metrics)", "description": "Dữ liệu thực tế của Sprint.", "required": True, "example": "Kế hoạch 40 Points, Thực tế hoàn thành 32 Points. Có 5 Bug phát sinh."},
            {"name": "Ý kiến của Team", "description": "Feedback từ Dev, QA, PO.", "required": False, "example": "Mọi người cảm thấy requirements thay đổi giữa chừng."}
        ],
        "process_detail": [
            {"step": 1, "title": "Thu thập dữ liệu Sprint", "description": "Nhìn lại các chỉ số.", "sub_steps": [
                "Velocity (Tốc độ hoàn thành)",
                "Sprint Goal có đạt không?",
                "Số lượng Bug/Escalation phát sinh",
                "Chất lượng (Code coverage, Review comments)"
            ]},
            {"step": 2, "title": "Tổ chức phiên Brainstorming", "description": "Khuyến khích mọi người chia sẻ.", "sub_steps": [
                "Sử dụng format chuẩn: What went well? (Điều gì tốt?)",
                "What didn't go well? (Điều gì chưa tốt?)",
                "What can we improve? (Cần cải thiện gì?)",
                "Đảm bảo nguyên tắc: Không đổ lỗi (No blame game), tập trung vào quy trình."
            ]},
            {"step": 3, "title": "Phân tích nguyên nhân (Root Cause)", "description": "Tìm hiểu tại sao điều chưa tốt lại xảy ra.", "sub_steps": [
                "Sử dụng 5 Whys. (VD: Tại sao chậm tiến độ? → Vì QA test chậm → Tại sao test chậm? → Vì môi trường test lỗi...)"
            ]},
            {"step": 4, "title": "Thiết lập Action Items", "description": "Đưa ra hành động cải tiến.", "sub_steps": [
                "Hành động phải cụ thể, đo lường được (SMART)",
                "Chỉ chọn tối đa 2-3 Action Items quan trọng nhất để làm trong Sprint tiếp theo",
                "Phân công người chịu trách nhiệm (Owner) cho từng Action Item"
            ]},
            {"step": 5, "title": "Review Action Items cũ", "description": "Kiểm tra xem cải tiến của Sprint trước có hiệu quả không.", "sub_steps": [
                "Nếu Action cũ hiệu quả → Giữ thành Process mới",
                "Nếu không hiệu quả → Bỏ hoặc thử cách khác"
            ]}
        ],
        "outputs_detail": [
            {"name": "Retrospective Minutes", "format": "Markdown Document", "template": "# Sprint [N] Retrospective\n\n## 1. Metrics Review\n- Goal: Thất bại\n- Velocity: 32/40 Points\n\n## 2. Feedback (Mad/Sad/Glad hoặc Start/Stop/Continue)\n**What went well (Glad):**\n- API tích hợp nhanh chóng, BE và FE phối hợp tốt.\n\n**What didn't go well (Sad):**\n- Requirement luồng Thanh toán bị đổi vào giữa Sprint.\n- Môi trường Test chết 1 ngày.\n\n## 3. Action Items cho Sprint tới\n| # | Action Item | Phân loại | Owner | Deadline |\n|---|---|---|---|---|\n| 1 | Block mọi thay đổi requirement sau khi Sprint bắt đầu | Quy trình | PO | Ngay lập tức |\n| 2 | Setup tool monitor cho Môi trường Test | Kỹ thuật | DevOps | Đầu Sprint [N+1] |"}
        ],
        "sub_skills": ["Root Cause Analysis", "Meeting Facilitation", "SMART Goal Setting"],
        "business_rules": [
            "BR-RETRO-01: Không đổ lỗi cho cá nhân, mọi vấn đề là do hệ thống/quy trình.",
            "BR-RETRO-02: Action Item phải có Chủ sở hữu (Owner) cụ thể.",
            "BR-RETRO-03: Mỗi Sprint chỉ nên tập trung cải thiện 1-3 vấn đề lớn nhất."
        ],
        "edge_cases": [
            "Team không ai chịu nói (Im lặng) → Dùng hình thức bỏ phiếu ẩn danh (Anonymous board)",
            "Xung đột cá nhân trong buổi Retro → Scrum Master can thiệp, đưa cuộc họp về chủ đề công việc"
        ],
        "checklist": [
            "Đã review lại Metrics của Sprint?",
            "Đã có mục 'What went well'?",
            "Đã có mục 'What didn't go well'?",
            "Đã dùng 5 Whys để tìm nguyên nhân chưa?",
            "Đã chốt được Action Items cụ thể (SMART)?",
            "Action Items đã có người phụ trách (Owner)?"
        ],
        "example": "Xem Retrospective Minutes template trong Outputs.",
        "related_skills": ["Sprint Planning", "Root Cause Analysis"],
        "quality_criteria": ["Phải có Action Items", "Phải có Owner", "Không có ngôn từ đổ lỗi"],
        "estimated_effort": "1-2 giờ (Meeting)",
        "prompt_role": "Scrum Master / Agile Coach chuyên tổ chức các sự kiện Agile hiệu quả.",
        "prompt_task": "Tổng hợp phản hồi và tạo báo cáo Sprint Retrospective với các Action Items cụ thể.",
        "prompt_context": "Team vừa kết thúc Sprint và có một số vấn đề cần giải quyết, cần một báo cáo Retro chuẩn để cải thiện quy trình.",
        "prompt_rules": [
            "PHẢI chia phản hồi thành 3 nhóm: Went Well, Didn't Go Well, Ideas for Improvement.",
            "PHẢI đưa ra tối đa 3 Action Items khả thi nhất.",
            "Action Items PHẢI tuân thủ nguyên tắc SMART và có Chủ sở hữu (Owner).",
            "Văn phong PHẢI trung lập, hướng tới quy trình, KHÔNG đổ lỗi cho cá nhân.",
            "Output PHẢI sử dụng format Retrospective Minutes dạng Markdown."
        ],
        "prompt_example": ""
    }
]

if __name__ == "__main__":
    print("=== Expanding: BPMN, Sequence Diagram, Notification Templates, Sprint Retro ===")
    run(skills)
