import sys
sys.path.insert(0, r"e:\BA Skill Library")
from skill_generator import run

skills = [
    # ================================================================
    # MES Focus: State Machine Diagram
    # ================================================================
    {
        "path": "03-Modeling/UML",
        "name": "State Machine Diagram",
        "level": "Level 3 - Architecture Skill",
        "domain": "Modeling",
        "tags": ["Modeling", "UML", "State", "Lifecycle", "MES", "Production"],
        "purpose": "Đặc tả vòng đời (Lifecycle) của một thực thể nghiệp vụ cốt lõi (Ví dụ: Lệnh sản xuất, Lô hàng, Máy móc) từ lúc sinh ra đến lúc kết thúc. Cung cấp chi tiết các Trạng thái (States), Sự kiện kích hoạt (Triggers), và Điều kiện chặn (Guard Conditions).",
        "when_to_use": "Sử dụng cực kỳ thường xuyên trong các hệ thống lõi (MES, ERP, Core Banking) nơi dữ liệu không bao giờ bị xóa vật lý (Hard delete) mà chỉ thay đổi trạng thái theo vòng đời khắt khe.",
        "prerequisites": ["Xác định được thực thể chính cần quản lý trạng thái (Ví dụ: Production Order)"],
        "inputs_detail": [
            {"name": "Tên Thực thể (Entity)", "description": "Đối tượng cần phân tích.", "required": True, "example": "Lệnh sản xuất (Production Order)"},
            {"name": "Luồng nghiệp vụ (Business Flow)", "description": "Cách thực thể này hoạt động thực tế.", "required": True, "example": "Lệnh tạo ra -> Chờ cấp vật tư -> Đang chạy -> Đóng lệnh."}
        ],
        "process_detail": [
            {"step": 1, "title": "Xác định các Trạng thái (States)", "description": "Các cột mốc tĩnh.", "sub_steps": [
                "Bắt đầu (Initial State) và Kết thúc (Final State).",
                "Các trạng thái trung gian. VD cho MES: Draft, Planned, Released, Setup, Running, Paused, Completed, Closed, Canceled."
            ]},
            {"step": 2, "title": "Xác định Hành động chuyển trạng thái (Transitions & Triggers)", "description": "Cái gì làm thay đổi trạng thái?", "sub_steps": [
                "Hành động của user (VD: Quản đốc bấm 'Release').",
                "Tín hiệu từ máy móc (VD: Cảm biến PLC báo 'Machine Started').",
                "Hành động của hệ thống (VD: Scheduled Job chạy vào nửa đêm)."
            ]},
            {"step": 3, "title": "Thiết lập Điều kiện chặn (Guard Conditions)", "description": "Rule để được phép chuyển.", "sub_steps": [
                "VD: [Đã cấp đủ vật tư] thì mới được chuyển từ Released -> Running.",
                "VD: [QC Passed] thì mới được chuyển từ Running -> Completed."
            ]},
            {"step": 4, "title": "Hành động khi vào/ra trạng thái (Entry/Exit Actions)", "description": "Hệ thống tự làm gì khi đổi state?", "sub_steps": [
                "Entry Action (Khi vào trạng thái): VD Khi vào 'Running' -> Gửi Zalo cho Quản đốc báo máy bắt đầu chạy.",
                "Exit Action (Khi rời trạng thái): VD Khi rời 'Paused' -> Ghi nhận tổng thời gian Downtime."
            ]}
        ],
        "outputs_detail": [
            {"name": "State Machine Diagram (Mermaid)", "format": "Mermaid stateDiagram", "template": "```mermaid\nstateDiagram-v2\n    [*] --> Draft\n    Draft --> Planned : Cập nhật KH\n    Planned --> Released : Quản đốc Approve\n    Released --> Running : [Vật tư đủ] Công nhân Start\n    Running --> Paused : Kẹt máy\n    Paused --> Running : Sửa xong\n    Running --> Completed : [Đạt số lượng] Bấm Finish\n    Completed --> Closed : Kế toán tất toán\n    Closed --> [*]\n```"},
            {"name": "State Transition Table", "format": "Markdown Table", "template": "### Ma trận chuyển đổi trạng thái (State Matrix)\n| Từ trạng thái (From) | Đến trạng thái (To) | Trigger (Sự kiện) | Guard (Điều kiện) | Action (Hệ thống làm gì) |\n|---|---|---|---|---|\n| Released | Running | Công nhân bấm 'Start' | Đã cấp đủ vật tư | Ghi nhận thời gian bắt đầu |\n| Running | Completed | Đạt Target SL | SL Đạt + SL Lỗi = Target | Gửi Noti cho Kế toán kho |"}
        ],
        "sub_skills": ["Guard Condition Analysis", "Lifecycle Design"],
        "business_rules": [
            "BR-STATE-01: Một thực thể tại một thời điểm chỉ có duy nhất 1 trạng thái.",
            "BR-STATE-02: Mọi State đều phải có đường đi đến Final State (Không tạo Trạng thái chết / Dead-end)."
        ],
        "edge_cases": [
            "Công nhân bấm nhầm trạng thái (Ví dụ từ Released bấm nhầm sang Closed) -> Thiết kế các flow 'Reopen' hoặc chặn cứng trên UI."
        ],
        "checklist": [
            "Có Initial và Final state chưa?",
            "Mỗi mũi tên chuyển đều có mô tả Trigger chưa?",
            "Có các điều kiện chặn (Guard) cho các bước quan trọng không?",
            "Bảng State Matrix có khớp với sơ đồ Mermaid không?"
        ],
        "example": "Xem State Matrix mẫu trong phần Outputs.",
        "related_skills": ["Phân tích Production Order", "Phân tích Business Rules"],
        "quality_criteria": ["Không có Dead-end", "Guard conditions logic rõ ràng"],
        "estimated_effort": "0.5 ngày",
        "prompt_role": "Senior System Architect / Business Analyst am hiểu sâu sắc về State Machine và hệ thống MES/ERP.",
        "prompt_task": "Đặc tả vòng đời của thực thể thông qua State Machine Diagram (Mermaid) và Ma trận chuyển trạng thái.",
        "prompt_context": "Hệ thống cần quản lý trạng thái khắt khe, không được phép lặp bước hoặc nhảy cóc trạng thái sai quy trình.",
        "prompt_rules": [
            "PHẢI vẽ sơ đồ bằng ngôn ngữ `mermaid stateDiagram-v2`.",
            "PHẢI định nghĩa rõ các Trạng thái (Ví dụ MES: Draft, Released, Running...).",
            "Trọng tâm: Mọi mũi tên chuyển trạng thái ĐỀU PHẢI có Trigger (Ai/Cái gì kích hoạt) và Guard Condition (Trong ngoặc vuông `[...]` - Điều kiện bắt buộc).",
            "PHẢI cung cấp bảng State Transition Table chi tiết giải thích sơ đồ."
        ],
        "prompt_example": ""
    },

    # ================================================================
    # MES Focus: Activity Diagram
    # ================================================================
    {
        "path": "03-Modeling/UML",
        "name": "Activity Diagram",
        "level": "Level 2 - Business Skill",
        "domain": "Modeling",
        "tags": ["Modeling", "UML", "Activity", "Flowchart", "MES", "Shopfloor"],
        "purpose": "Mô hình hóa luồng hoạt động (Workflow) và thao tác nghiệp vụ, đặc biệt hiệu quả để mô tả thao tác vật lý của con người kết hợp với phản hồi của máy móc/hệ thống tại dưới xưởng (Shopfloor).",
        "when_to_use": "Dùng để phác thảo nhanh một quy trình, một thuật toán, hoặc thao tác tại một Trạm làm việc (Work Center) trước khi code.",
        "prerequisites": ["Hiểu các bước thực hiện của quy trình"],
        "inputs_detail": [
            {"name": "Quy trình vật lý / hệ thống", "description": "Chuỗi các bước thực hiện.", "required": True, "example": "Công nhân lại máy tiện -> Quét mã vạch -> Máy tính bảng báo xanh -> Nhấn nút chạy -> QC lấy mẫu đo."}
        ],
        "process_detail": [
            {"step": 1, "title": "Liệt kê các Action Nodes (Hành động)", "description": "Các thao tác cụ thể.", "sub_steps": [
                "Bao gồm thao tác vật lý: Lấy phôi thép, đo kích thước bằng thước kẹp.",
                "Bao gồm thao tác phần mềm: Quét mã vạch, Bấm nút Start trên Tablet."
            ]},
            {"step": 2, "title": "Sử dụng Decision Nodes (Rẽ nhánh)", "description": "Các điểm kiểm tra.", "sub_steps": [
                "VD: QC đo kích thước -> [Pass] -> Chuyển bước tiếp theo. [Fail] -> Cho vào thùng phế phẩm (Scrap)."
            ]},
            {"step": 3, "title": "Sử dụng Fork/Join (Luồng song song)", "description": "Các việc xảy ra cùng lúc.", "sub_steps": [
                "Fork (Tách luồng): Hệ thống MES vừa ghi nhận số lượng VÀ vừa kích hoạt đèn báo xanh.",
                "Join (Gộp luồng): Phải hoàn thành cả việc [Máy cắt xong] VÀ [Công nhân dọn phoi] thì mới qua bước [Chuyển hàng]."
            ]},
            {"step": 4, "title": "Phân chia Swimlanes (Tùy chọn)", "description": "Ai làm việc gì?", "sub_steps": [
                "Chia cột: Công nhân (Operator) | Hệ thống MES | Quản lý Chất lượng (QC)."
            ]}
        ],
        "outputs_detail": [
            {"name": "Activity Diagram (Mermaid)", "format": "Mermaid flowchart", "template": "```mermaid\ngraph TD\n    Start((Start)) --> A[Công nhân quét mã Lệnh]\n    A --> B{Mã hợp lệ?}\n    B -- Không --> C[Báo lỗi đỏ] --> A\n    B -- Có --> D[Hiển thị thông số máy trên Tablet]\n    D --> E[Công nhân nạp phôi]\n    E --> F[Bấm Start]\n    F --> Fork1{ }\n    Fork1 --> G1[Máy bắt đầu cắt]\n    Fork1 --> G2[Hệ thống trừ kho vật tư]\n    G1 --> Join1{ }\n    G2 --> Join1\n    Join1 --> End((End))\n```"}
        ],
        "sub_skills": ["Fork/Join Logic", "Physical/System Interaction"],
        "business_rules": [
            "BR-ACT-01: Mọi nhánh rẽ từ khối Decision (Hình thoi) phải có nhãn rõ ràng (Đúng/Sai, Pass/Fail).",
            "BR-ACT-02: Phải mô tả chân thực sự tương tác giữa vật lý (cầm, nắm, quét) và hệ thống."
        ],
        "edge_cases": [
            "Máy mất kết nối mạng (Offline) khi đang chạy -> Activity Diagram phải mô tả luồng lưu cache cục bộ trên Tablet."
        ],
        "checklist": [
            "Có Start và End node?",
            "Khối Decision đã cover đủ nhánh (vd Yes/No)?",
            "Có sử dụng luồng song song (Fork) khi máy và người cùng làm việc không?"
        ],
        "example": "Xem sơ đồ Mermaid trong Outputs.",
        "related_skills": ["Phân tích Mobile App", "Thiết kế Role-based UI"],
        "quality_criteria": ["Rõ ràng hành động vật lý vs hệ thống", "Sử dụng đúng Fork/Join"],
        "estimated_effort": "2-4 giờ",
        "prompt_role": "Senior BA am hiểu quy trình sản xuất nhà máy (Shopfloor workflows).",
        "prompt_task": "Mô hình hóa quy trình thao tác nghiệp vụ thông qua Activity Diagram (Mermaid flowchart).",
        "prompt_context": "Cần một quy trình đặc tả sự tương tác liên tục giữa con người (thao tác tay, quét mã) và hệ thống (phản hồi màn hình, kết nối máy móc).",
        "prompt_rules": [
            "PHẢI sử dụng ngôn ngữ `mermaid flowchart TD`.",
            "Tên các bước (Action) PHẢI là động từ (Ví dụ: Quét mã vạch, Bấm nút Start, Cấp phôi).",
            "PHẢI thiết kế các luồng rẽ nhánh (Decision) khi có kiểm tra điều kiện (QC pass/fail, Mã hợp lệ/Không).",
            "Khuyến khích sử dụng luồng song song (Ví dụ: Hệ thống lưu DB đồng thời gửi cảnh báo) để sơ đồ giống thực tế nhà máy."
        ],
        "prompt_example": ""
    },

    # ================================================================
    # MES Focus: Phân tích Business Rules
    # ================================================================
    {
        "path": "02-Requirement/Elicitation",
        "name": "Phân tích Business Rules",
        "level": "Level 2 - Business Skill",
        "domain": "Requirement",
        "tags": ["Requirement", "Rules", "Constraints", "Decision Table", "MES", "QA"],
        "purpose": "Bóc tách, định nghĩa và kiểm soát các Ràng buộc nghiệp vụ (Business Rules). Đặc biệt quan trọng để ánh xạ các quy tắc quản trị/sản xuất vật lý vào hệ thống, từ đó làm cơ sở sinh tài liệu luồng nghiệp vụ và kịch bản Test (cả test hệ thống lẫn test QC thực tế).",
        "when_to_use": "Khi một chức năng có quá nhiều điều kiện Nếu-Thì (If-Else), hoặc khi áp dụng vào các ngành có rủi ro cao (MES, Y tế, Tài chính) cần tuân thủ nghiêm ngặt chuẩn mực.",
        "prerequisites": ["Có văn bản quy định của công ty, hoặc đã phỏng vấn chuyên gia (SME)"],
        "inputs_detail": [
            {"name": "Mô tả nghiệp vụ", "description": "Đoạn văn mô tả lỏng lẻo cần được chuẩn hóa.", "required": True, "example": "Công nhân chỉ được chạy máy nếu đã học an toàn và QC đã ký duyệt vật tư."}
        ],
        "process_detail": [
            {"step": 1, "title": "Phân loại Business Rules", "description": "Chia nhóm để quản lý.", "sub_steps": [
                "Validation Rule (Ràng buộc nhập liệu): Số lượng nhập phải > 0.",
                "Access Control Rule (Quyền hạn): Chỉ Quản đốc mới được sửa lệnh.",
                "Process/Transition Rule (Quy trình): Không được chuyển trạng thái Running nếu chưa nhập kho Vật tư.",
                "Calculation Rule (Tính toán): OEE = Availability * Performance * Quality."
            ]},
            {"step": 2, "title": "Chuẩn hóa bằng Decision Table", "description": "Bóc tách điều kiện IF - THEN.", "sub_steps": [
                "Liệt kê các Condition (Điều kiện) ở dạng Boolean (Đúng/Sai).",
                "Liệt kê các Action (Hành động hệ thống) xảy ra tương ứng.",
                "Lập bảng kết hợp các logic lại với nhau."
            ]},
            {"step": 3, "title": "Map Rules vào Luồng Nghiệp Vụ (Business Flow)", "description": "Chèn rule vào tài liệu.", "sub_steps": [
                "Tại bước 3 của Use Case / BPMN, ghi rõ 'Áp dụng BR-001'.",
                "Đảm bảo rule không bị trôi nổi mà gắn chặt với màn hình/thao tác cụ thể."
            ]},
            {"step": 4, "title": "Map Rules vào Kịch bản Test (QA & System)", "description": "Biến rule thành test case.", "sub_steps": [
                "System Test: QA IT tạo test case cố tình vi phạm Rule để xem hệ thống có chặn và văng lỗi không.",
                "Manufacturing QA Test: Thiết lập chốt chặn QC vật lý dưới xưởng dựa trên rule (VD: QC lấy mẫu 5% sản phẩm trên dây chuyền)."
            ]}
        ],
        "outputs_detail": [
            {"name": "Business Rules Catalog & Decision Table", "format": "Markdown", "template": "### Danh mục Business Rules\n- **BR-MES-01 (Process Rule):** Lệnh sản xuất chỉ được phép bắt đầu (Start) khi (1) Vật tư đã được cấp đủ 100% tại xưởng VÀ (2) Nhân viên có chứng chỉ vận hành khớp với máy.\n\n### Decision Table cho BR-MES-01\n| Vật tư đủ? | Đạt chứng chỉ? | Action (Được Start máy?) | QA Test / System Test Case |\n|---|---|---|---|\n| Yes | Yes | **YES (Nút xanh)** | Test thành công |\n| Yes | No | **NO (Báo lỗi đỏ)** | Cảnh báo: Nhân viên chưa đào tạo |\n| No | Yes | **NO (Báo lỗi đỏ)** | Cảnh báo: Thiếu vật tư |\n| No | No | **NO (Báo lỗi đỏ)** | Cảnh báo: Thiếu VT + Chưa ĐT |"}
        ],
        "sub_skills": ["Decision Table Creation", "QA & Test Mapping", "Rule Categorization"],
        "business_rules": [
            "BR-RULE-01: Mọi Business Rule phải được viết bằng câu khẳng định, không dùng từ ngữ đa nghĩa (nên, có thể).",
            "BR-RULE-02: Phải gán ID (Mã định danh) duy nhất cho mỗi rule để dễ tracking."
        ],
        "edge_cases": [
            "Trường hợp khẩn cấp (Emergency): Giám đốc nhà máy ra lệnh chạy máy dù thiếu vật tư trên hệ thống -> Thiết kế cơ chế 'Override' có ghi log Audit."
        ],
        "checklist": [
            "Rule có rõ ràng, không đa nghĩa?",
            "Đã chia nhóm (Validation, Access, Process, Calculation)?",
            "Đã lập Decision Table cho các Rule phức tạp?",
            "Đã map Rule này với tài liệu Luồng (Flow) và Kịch bản Test chưa?"
        ],
        "example": "Xem Decision Table mẫu trong Outputs.",
        "related_skills": ["Viết Test Case (Ultra)", "State Machine Diagram"],
        "quality_criteria": ["Quy tắc IF-THEN chặt chẽ", "Phục vụ tốt cho QA Test"],
        "estimated_effort": "0.5 - 1 ngày",
        "prompt_role": "Senior Business Analyst & Quality Control Expert.",
        "prompt_task": "Bóc tách, chuẩn hóa các Business Rules phức tạp và ánh xạ chúng vào tài liệu luồng nghiệp vụ cũng như định hướng Kịch bản Test.",
        "prompt_context": "Hệ thống cần các quy tắc kiểm soát cực kỳ chặt chẽ (đặc biệt trong môi trường sản xuất MES), mọi lỗ hổng logic đều có thể gây thiệt hại thực tế.",
        "prompt_rules": [
            "PHẢI phân loại Rule (Validation, Process, Access Control, Calculation).",
            "PHẢI gán ID cho mỗi rule (Ví dụ: BR-001).",
            "NẾU rule có nhiều điều kiện logic AND/OR, BẮT BUỘC lập Bảng Quyết Định (Decision Table).",
            "Mỗi Rule / Dòng trong Decision Table PHẢI đề xuất luôn hướng đi cho kịch bản Test (Ví dụ: QA sẽ test case này như thế nào?)."
        ],
        "prompt_example": ""
    },

    # ================================================================
    # MES Focus: Thiết kế Role-based UI
    # ================================================================
    {
        "path": "04-UIUX/Design",
        "name": "Thiết kế Role-based UI",
        "level": "Level 3 - Architecture Skill",
        "domain": "UIUX",
        "tags": ["UIUX", "Role", "Permission", "MES", "Interface"],
        "purpose": "Thiết kế đặc tả giao diện tùy biến theo vai trò người dùng (Role-based). Đảm bảo mỗi Role chỉ nhìn thấy dữ liệu, nút bấm và chức năng mà họ được cấp quyền, giảm thiểu sai sót và tối ưu hóa trải nghiệm làm việc thực tế.",
        "when_to_use": "Khi thiết kế phần mềm doanh nghiệp (MES, ERP) có sự phân cấp rõ ràng: Công nhân (dùng Tablet ở xưởng), Quản đốc (dùng Web theo dõi), Giám đốc (xem Dashboard tổng).",
        "prerequisites": ["Đã có danh sách User Roles và luồng nghiệp vụ"],
        "inputs_detail": [
            {"name": "Danh sách Roles", "description": "Ai sẽ dùng hệ thống?", "required": True, "example": "Operator (Công nhân), Supervisor (Quản đốc), QC (KCS)."},
            {"name": "Tính năng", "description": "Tính năng cần phân quyền UI.", "required": True, "example": "Màn hình Chi tiết Lệnh Sản Xuất."}
        ],
        "process_detail": [
            {"step": 1, "title": "Xây dựng Ma trận Phân quyền (Permission Matrix)", "description": "Map Role với Action.", "sub_steps": [
                "Xác định quyền CRUD (Create, Read, Update, Delete) hoặc Execute.",
                "VD: Công nhân -> Read lệnh, Bấm nút 'Start/Stop'.",
                "Quản đốc -> Create lệnh, Update lệnh, Bấm nút 'Approve'."
            ]},
            {"step": 2, "title": "Thiết kế UI cho Role: Công nhân (Operator Level)", "description": "Tập trung vào tính thực thi.", "sub_steps": [
                "Giao diện tinh gọn, nút bấm cực lớn (Touch-friendly).",
                "Chỉ hiển thị thông tin Đang làm (Current task), ẩn đi toàn bộ menu phức tạp.",
                "Hiển thị cảnh báo màu sắc rực rỡ (Xanh = Chạy, Đỏ = Lỗi)."
            ]},
            {"step": 3, "title": "Thiết kế UI cho Role: Quản đốc (Supervisor Level)", "description": "Tập trung vào giám sát và điều phối.", "sub_steps": [
                "Giao diện dạng Danh sách / Kanban Board.",
                "Cho phép lọc, tìm kiếm nhiều tham số.",
                "Có các nút hành động hàng loạt (Bulk action: Duyệt 10 lệnh cùng lúc)."
            ]},
            {"step": 4, "title": "Đặc tả các trạng thái Ẩn/Hiện phần tử UI", "description": "Dynamic rendering.", "sub_steps": [
                "Nếu là Công nhân -> Nút 'Xóa lệnh' hoàn toàn biến mất (Invisible) chứ không chỉ mờ đi (Disabled) để đỡ rối mắt.",
                "Nếu không có quyền sửa -> Các ô Input biến thành dạng Text (Read-only)."
            ]}
        ],
        "outputs_detail": [
            {"name": "Role-based UI Specification", "format": "Markdown", "template": "### Giao diện: Chi tiết Lệnh Sản Xuất\n\n#### 1. Góc nhìn Công nhân (Operator UI - Tablet)\n- **Layout:** Full screen, Nút to, Màu tương phản cao.\n- **Data hiển thị:** Tên SP, Số lượng cần làm, Định mức vật tư.\n- **Actions:** Chỉ có 2 nút [BẮT ĐẦU] (Màu xanh lá) và [BÁO LỖI] (Màu đỏ).\n- **Ẩn đi:** Menu bar, Nút sửa lệnh, Giá tiền sản phẩm.\n\n#### 2. Góc nhìn Quản đốc (Supervisor UI - Web PC)\n- **Layout:** Standard Dashboard.\n- **Data hiển thị:** Toàn bộ thông tin + Giá thành + Báo cáo tiến độ.\n- **Actions:** Nút [Sửa], [Hủy lệnh], [Duyệt].\n- **Trạng thái:** Nếu lệnh đang 'Running', nút [Sửa] bị Disabled."}
        ],
        "sub_skills": ["Permission Matrix Design", "Contextual UI/UX"],
        "business_rules": [
            "BR-RBUI-01: Nguyên tắc quyền tối thiểu (Least Privilege): Chỉ hiển thị/cấp quyền đúng những gì Role đó cần để làm việc.",
            "BR-RBUI-02: User dưới xưởng phải được thiết kế UI 'Fail-safe' (Chống bấm nhầm)."
        ],
        "edge_cases": [
            "Một người kiêm nhiệm 2 Roles (Vừa làm công nhân, vừa làm QC) -> Tích hợp cơ chế 'Switch Role' trên góc màn hình thay vì gộp chung UI gây rối."
        ],
        "checklist": [
            "Đã lập Ma trận phân quyền chưa?",
            "Giao diện công nhân đã đủ đơn giản chưa (Touch-friendly)?",
            "Đã mô tả rõ hành vi của nút bấm (Ẩn hẳn vs Mờ đi)?"
        ],
        "example": "Xem Role-based UI Specification trong Outputs.",
        "related_skills": ["Phân tích màn hình CRUD", "Phân tích Mobile App"],
        "quality_criteria": ["Khác biệt rõ ràng giữa các Role", "Tuân thủ Least Privilege"],
        "estimated_effort": "1 ngày / Màn hình lõi",
        "prompt_role": "Senior UX Researcher / Enterprise System Designer.",
        "prompt_task": "Thiết kế đặc tả giao diện người dùng dựa trên vai trò (Role-based UI), đảm bảo phân quyền và tối ưu UX cho từng đối tượng.",
        "prompt_context": "Hệ thống có nhiều lớp người dùng (từ công nhân trình độ IT thấp đến quản lý cấp cao). Cùng 1 dữ liệu nhưng cách thao tác phải hoàn toàn khác biệt.",
        "prompt_rules": [
            "BẮT BUỘC thiết kế Ma trận phân quyền (Permission Matrix) dạng Bảng.",
            "PHẢI tách biệt thiết kế UI cho ít nhất 2 nhóm Role (Ví dụ: Thực thi dưới xưởng vs Quản lý trên văn phòng).",
            "Đặc tả UI PHẢI chú trọng vào yếu tố tương tác (Nút bấm to/nhỏ, Dùng chuột hay cảm ứng, Ẩn phần tử hay làm mờ)."
        ],
        "prompt_example": ""
    },

    # ================================================================
    # MES Focus: Phân tích Mobile App / Tablet Shopfloor
    # ================================================================
    {
        "path": "04-UIUX/Platform",
        "name": "Phân tích Mobile App",
        "level": "Level 2 - Business Skill",
        "domain": "UIUX",
        "tags": ["UIUX", "Mobile", "Tablet", "Shopfloor", "MES", "Hardware"],
        "purpose": "Phân tích và đặc tả các yêu cầu riêng biệt khi xây dựng ứng dụng di động (Mobile App) hoặc ứng dụng trên Máy tính bảng Công nghiệp (Rugged Tablet) dùng trực tiếp tại hiện trường (Shopfloor, Warehouse).",
        "when_to_use": "Sử dụng cho các dự án MES, WMS, hoặc App giao hàng, nơi người dùng thao tác trong môi trường khắc nghiệt, thao tác nhanh bằng phần cứng (máy quét).",
        "prerequisites": ["Đã có luồng nghiệp vụ cơ bản"],
        "inputs_detail": [
            {"name": "Mục đích App", "description": "App này dùng để làm gì?", "required": True, "example": "App cài trên Tablet tại máy CNC để công nhân nhận lệnh sản xuất."}
        ],
        "process_detail": [
            {"step": 1, "title": "Phân tích Môi trường & Phần cứng (Hardware Context)", "description": "Dùng ở đâu, bằng cái gì?", "sub_steps": [
                "Thiết bị: iPad, Android Rugged Tablet, hay PDA Scanner?",
                "Môi trường: Sáng lóa (cần Contrast cao), Bụi bẩn (cần Icon to), Công nhân đeo găng tay (Touch target > 48dp)."
            ]},
            {"step": 2, "title": "Tối ưu hóa thao tác nhập liệu (Data Entry)", "description": "Hạn chế gõ phím.", "sub_steps": [
                "Ưu tiên dùng Camera hoặc Máy quét tia laser (Barcode/QR code) thay cho gõ phím.",
                "Dùng màn hình Numpad to (như máy tính cầm tay) thay vì bàn phím QWERTY khi nhập số lượng.",
                "Hạn chế cuộn (Scrolling), 1 màn hình chỉ nên hiển thị vừa vặn 1 thao tác."
            ]},
            {"step": 3, "title": "Đặc tả tính năng Offline / Poor Network", "description": "Mạng ở xưởng thường rất yếu.", "sub_steps": [
                "Ứng dụng phải làm gì khi mất mạng mạng (VD: Lưu dữ liệu dưới Local DB/SQLite).",
                "Cơ chế Sync (Đồng bộ) tự động khi có mạng trở lại.",
                "Hiển thị icon trạng thái mạng rõ ràng."
            ]},
            {"step": 4, "title": "Luồng thông báo và Âm thanh", "description": "Tương tác phi hình ảnh.", "sub_steps": [
                "Quét mã đúng: App kêu 'Bíp' ngắn, rung 1 lần, nháy xanh.",
                "Quét mã sai: App kêu 'Tít tít tít', rung dài, nháy đỏ."
            ]}
        ],
        "outputs_detail": [
            {"name": "Mobile/Tablet App Specification", "format": "Markdown", "template": "### Đặc tả Tablet App: Trạm máy CNC\n\n**1. Môi trường & Phần cứng**\n- Thiết bị: Zebra Rugged Android Tablet 10-inch.\n- Tương tác: Màn hình cảm ứng (Công nhân đeo găng tay vải).\n\n**2. Yêu cầu UI/UX đặc thù**\n- Kích thước nút tối thiểu: 60x60 pixels.\n- Không dùng bàn phím chữ. Chỉ có bàn phím số (Numpad).\n- Thao tác chính: Bấm cò súng quét mã QR, hệ thống tự động điền thông tin và nhảy sang bước tiếp theo không cần bấm Submit.\n\n**3. Offline Mode & Đồng bộ**\n- Nếu rớt mạng WIFI xưởng: Tablet vẫn cho phép bấm 'Nhập kho', dữ liệu đẩy vào hàng đợi (Queue local).\n- Có biểu tượng đám mây gạch chéo góc phải màn hình.\n\n**4. Phản hồi âm thanh**\n- Lỗi nghiệp vụ -> Bật chuông cảnh báo lớn, rung 2 giây."}
        ],
        "sub_skills": ["Offline Capability Design", "Hardware Interaction Design", "Shopfloor UX"],
        "business_rules": [
            "BR-MOB-01: Số lần chạm (Tap) để hoàn thành một tác vụ lặp lại hàng ngày không được vượt quá 3 lần.",
            "BR-MOB-02: Dữ liệu thao tác tại hiện trường không bao giờ được phép mất (Bắt buộc thiết kế Offline Queue)."
        ],
        "edge_cases": [
            "Máy quét mã vạch bị hỏng laser -> Bắt buộc thiết kế ô Input dự phòng để công nhân gõ tay mã số vào."
        ],
        "checklist": [
            "Đã tối ưu cho việc thao tác bằng găng tay chưa (Nút bấm to)?",
            "Đã loại bỏ tối đa việc gõ phím QWERTY chưa?",
            "Đã mô tả cơ chế Offline (mất mạng) chưa?",
            "Đã mô tả phản hồi âm thanh/đèn LED chưa?"
        ],
        "example": "Xem Mobile/Tablet App Specification trong Outputs.",
        "related_skills": ["Thiết kế Role-based UI", "Activity Diagram"],
        "quality_criteria": ["Tối ưu thao tác vật lý", "Có phương án Offline/Mất mạng"],
        "estimated_effort": "1-2 ngày",
        "prompt_role": "Senior Mobile Product Manager / UIUX Expert chuyên về hệ thống nhà máy/kho bãi.",
        "prompt_task": "Đặc tả yêu cầu phần mềm cho ứng dụng Mobile/Tablet sử dụng tại hiện trường (Shopfloor).",
        "prompt_context": "Ứng dụng được cài đặt trên thiết bị cầm tay cho công nhân trong môi trường khắt khe (bụi, ồn, mạng yếu), ưu tiên tốc độ, tính ổn định và chống thao tác sai.",
        "prompt_rules": [
            "KHÔNG thiết kế giao diện như các App tiêu dùng (Shopee, Facebook). Thiết kế theo nguyên lý Shopfloor (Ít nút, Nút cực to, Tương phản mạnh).",
            "BẮT BUỘC phải mô tả luồng thao tác với phần cứng (Barcode scanner, Camera, NFC).",
            "BẮT BUỘC phải đặc tả cơ chế xử lý khi mất mạng (Offline Mode / Local Cache).",
            "Đặc tả phản hồi bằng Âm thanh và Rung để công nhân biết kết quả mà không cần nhìn màn hình liên tục."
        ],
        "prompt_example": ""
    }
]

if __name__ == "__main__":
    print("=== Expanding: MES Focus (State Machine, Activity, Business Rules, Role UI, Tablet UX) ===")
    run(skills)
