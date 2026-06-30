import sys
sys.path.insert(0, r"e:\BA Skill Library")
from skill_generator import run

skills = [
    # ================================================================
    # 02-Requirement / Write User Story
    # ================================================================
    {
        "path": "02-Requirement/User Story",
        "name": "Write User Story",
        "level": "Level 1 - Basic Skill",
        "domain": "Requirement",
        "tags": ["Requirement", "Agile", "User Story", "INVEST"],
        "purpose": "Viết User Story chuẩn Agile đúng format, kèm Acceptance Criteria chi tiết, tuân thủ nguyên tắc INVEST để đảm bảo Story có thể estimate và deliver trong 1 Sprint.",
        "when_to_use": "Sử dụng khi cần chuyển đổi yêu cầu nghiệp vụ thành các đơn vị công việc (Work Item) cho đội Scrum.",
        "prerequisites": ["Hiểu cơ bản về Scrum/Agile"],
        "inputs_detail": [
            {"name": "Requirement / Nghiệp vụ", "description": "Mô tả yêu cầu cần làm.", "required": True, "example": "Nhân viên kho cần có khả năng kiểm kê tồn kho bằng cách quét mã vạch."},
            {"name": "Actor / Persona", "description": "Ai là người sử dụng tính năng.", "required": True, "example": "Nhân viên kho, Quản lý kho, Kế toán kho"}
        ],
        "process_detail": [
            {"step": 1, "title": "Xác định Actor (Vai trò)", "description": "Xác định rõ ai sẽ sử dụng tính năng này. Không dùng 'User' chung chung.", "sub_steps": [
                "Liệt kê tất cả các vai trò liên quan",
                "Chọn vai trò chính (Primary Actor) cho mỗi Story",
                "Ví dụ đúng: 'As a Warehouse Staff' thay vì 'As a User'"
            ]},
            {"step": 2, "title": "Xác định Action (Hành động)", "description": "Xác định rõ người dùng muốn LÀM GÌ.", "sub_steps": [
                "Hành động phải cụ thể, có thể thao tác trên hệ thống",
                "Ví dụ đúng: 'I want to scan barcode to count inventory'",
                "Ví dụ sai: 'I want to manage inventory' (Quá rộng)"
            ]},
            {"step": 3, "title": "Xác định Benefit (Giá trị)", "description": "Giải thích TẠI SAO người dùng cần tính năng này.", "sub_steps": [
                "Benefit phải hướng đến giá trị kinh doanh thật sự",
                "Ví dụ đúng: 'So that I can reduce counting time from 4 hours to 1 hour'",
                "Ví dụ sai: 'So that I can use the system' (Không có giá trị)"
            ]},
            {"step": 4, "title": "Viết Acceptance Criteria (Tiêu chí chấp nhận)", "description": "Viết các điều kiện cụ thể để xác nhận Story đã hoàn thành.", "sub_steps": [
                "Sử dụng format Given-When-Then cho mỗi AC:",
                "  Given [Điều kiện ban đầu]",
                "  When [Hành động]",
                "  Then [Kết quả mong đợi]",
                "Mỗi Story phải có ít nhất 3 Acceptance Criteria",
                "Phải bao gồm: Happy Path (Đúng), Error Case (Sai), Edge Case (Biên)"
            ]},
            {"step": 5, "title": "Kiểm tra INVEST", "description": "Đảm bảo Story tuân thủ nguyên tắc INVEST.", "sub_steps": [
                "Independent: Story không phụ thuộc vào Story khác",
                "Negotiable: Có thể thương lượng với PO",
                "Valuable: Mang lại giá trị cho người dùng hoặc doanh nghiệp",
                "Estimable: Đội Dev có thể ước lượng effort",
                "Small: Hoàn thành được trong 1 Sprint (2-3 ngày dev)",
                "Testable: Có thể viết Test Case để kiểm tra"
            ]}
        ],
        "outputs_detail": [
            {"name": "User Story", "format": "Markdown Template", "template": "## US-[ID]: [Tên Story]\n\n**As a** [Vai trò]\n**I want to** [Hành động]\n**So that** [Giá trị/Lợi ích]\n\n### Acceptance Criteria\n\n**AC1: [Happy Path]**\n- Given: [Điều kiện]\n- When: [Hành động]\n- Then: [Kết quả]\n\n**AC2: [Error Case]**\n- Given: [Điều kiện]\n- When: [Hành động sai]\n- Then: [Thông báo lỗi]\n\n**AC3: [Edge Case]**\n- Given: [Điều kiện đặc biệt]\n- When: [Hành động]\n- Then: [Kết quả xử lý biên]\n\n### Notes\n- Priority: [Must/Should/Could]\n- Story Points: [1/2/3/5/8]\n- Sprint: [Sprint X]"},
            {"name": "Danh sách User Stories", "format": "Markdown Table", "template": "| ID | Story | Actor | Priority | Points |\n|---|---|---|---|---|\n| US-001 | Scan barcode để kiểm kê | Nhân viên kho | Must | 5 |\n| US-002 | Xem báo cáo chênh lệch | Quản lý kho | Should | 3 |"}
        ],
        "sub_skills": ["Viết Acceptance Criteria (Given-When-Then)", "Story Splitting (Chia nhỏ Story)", "Story Mapping"],
        "business_rules": [
            "BR-US-01: Mỗi User Story chỉ có 1 Actor duy nhất.",
            "BR-US-02: Mỗi User Story phải có ít nhất 3 Acceptance Criteria.",
            "BR-US-03: Story Point không vượt quá 8 (nếu vượt phải chia nhỏ).",
            "BR-US-04: User Story KHÔNG được chứa giải pháp kỹ thuật (Technical Solution)."
        ],
        "edge_cases": [
            "Yêu cầu quá lớn → Tách thành Epic + nhiều Story",
            "Yêu cầu kỹ thuật thuần (Refactoring) → Technical Story, không dùng As a...",
            "Acceptance Criteria mâu thuẫn nhau → PO phải quyết định"
        ],
        "checklist": [
            "Story có đúng format As a... I want to... So that...?",
            "Actor có cụ thể (không dùng 'User' chung chung)?",
            "Benefit có giá trị kinh doanh thật?",
            "Có ít nhất 3 Acceptance Criteria?",
            "AC có bao gồm Happy Path + Error + Edge Case?",
            "Story đủ nhỏ để hoàn thành trong 1 Sprint?",
            "Story tuân thủ INVEST?"
        ],
        "example": """### Ví dụ: User Story cho tính năng Kiểm kê kho

**US-042: Scan Barcode để kiểm kê**

**As a** Nhân viên kho
**I want to** quét mã vạch sản phẩm tại từng vị trí kệ và nhập số lượng đếm được
**So that** tôi có thể hoàn thành kiểm kê nhanh hơn 70% so với đếm tay và giảm sai sót

**AC1: Quét barcode thành công**
- Given: Nhân viên đang ở màn hình Kiểm kê, phiếu kiểm kê CC-001 đang mở
- When: Quét mã vạch SKU-A01 tại Location A-01-03
- Then: Hệ thống hiển thị tên sản phẩm "Sữa TH 1L", ô nhập số lượng sẵn sàng

**AC2: Quét barcode không tồn tại**
- Given: Nhân viên quét mã vạch không có trong hệ thống
- When: Hệ thống không tìm thấy SKU
- Then: Hiển thị thông báo lỗi "Mã vạch không hợp lệ" + Cho phép quét lại

**AC3: Mất kết nối mạng giữa chừng**
- Given: Nhân viên đang quét kiểm kê nhưng mất WiFi
- When: Quét thêm 5 sản phẩm trong chế độ Offline
- Then: Dữ liệu lưu local, tự đồng bộ lên server khi có mạng lại""",
        "related_skills": ["Write BRD", "Write SRS", "Phân tích Use Case", "Viết Test Case"],
        "quality_criteria": [
            "Story phải đúng format As a / I want to / So that",
            "Actor phải cụ thể",
            "AC phải dùng Given-When-Then",
            "Phải có ít nhất 1 Error Case trong AC",
            "Story phải tuân thủ INVEST"
        ],
        "estimated_effort": "0.5-1 ngày / Story",
        "prompt_role": "Senior Business Analyst với chuyên môn về Agile/Scrum. Đã viết hơn 1000 User Stories cho các dự án phần mềm doanh nghiệp.",
        "prompt_task": "Viết User Story chuẩn Agile với Acceptance Criteria chi tiết.",
        "prompt_context": "Đang làm việc trong một dự án Agile/Scrum, cần chuyển yêu cầu nghiệp vụ thành User Stories.",
        "prompt_rules": [
            "PHẢI sử dụng format: As a [Role], I want to [Action], So that [Benefit].",
            "Actor PHẢI cụ thể (KHÔNG dùng 'User').",
            "PHẢI có ít nhất 3 Acceptance Criteria dùng Given-When-Then.",
            "AC PHẢI bao gồm: 1 Happy Path + 1 Error Case + 1 Edge Case.",
            "Story KHÔNG được chứa giải pháp kỹ thuật.",
            "Story Point KHÔNG vượt quá 8 (nếu quá lớn, hãy đề xuất cách chia nhỏ).",
            "Nếu yêu cầu quá rộng, hãy tách thành Epic + nhiều Stories."
        ],
        "prompt_example": """**User yêu cầu:** "Viết User Story cho tính năng đăng nhập"

**AI trả lời:**
## US-001: Đăng nhập bằng Email/Password
**As a** Nhân viên công ty
**I want to** đăng nhập hệ thống bằng email công ty và mật khẩu
**So that** tôi có thể truy cập các tính năng được phân quyền cho mình

### Acceptance Criteria

**AC1: Đăng nhập thành công**
- Given: User có tài khoản email@company.com, mật khẩu hợp lệ
- When: Nhập đúng email + mật khẩu + Click "Đăng nhập"
- Then: Chuyển hướng đến Dashboard tương ứng với Role

**AC2: Sai mật khẩu**
- Given: User nhập đúng email nhưng sai mật khẩu
- When: Click "Đăng nhập"
- Then: Hiển thị "Email hoặc mật khẩu không đúng" (KHÔNG tiết lộ cái nào sai)

**AC3: Khóa tài khoản sau 5 lần sai**
- Given: User đã nhập sai mật khẩu 5 lần liên tiếp
- When: Nhập sai lần thứ 5
- Then: Khóa tài khoản 30 phút + Gửi email cảnh báo cho Admin"""
    },
    # ================================================================
    # 02-Requirement / Write BRD
    # ================================================================
    {
        "path": "02-Requirement/BRD",
        "name": "Write BRD",
        "level": "Level 1 - Basic Skill",
        "domain": "Requirement",
        "tags": ["Requirement", "BRD", "Document", "Scope"],
        "purpose": "Soạn thảo Business Requirement Document (BRD) chuẩn mực, tập trung mô tả 'CÁI GÌ' (What) doanh nghiệp cần và 'TẠI SAO' (Why), KHÔNG đi vào chi tiết kỹ thuật 'NHƯ THẾ NÀO' (How).",
        "when_to_use": "Sử dụng ở giai đoạn đầu dự án để làm rõ phạm vi và mục tiêu kinh doanh trước khi đi vào thiết kế chi tiết.",
        "prerequisites": ["Đã phỏng vấn Stakeholders"],
        "inputs_detail": [
            {"name": "Yêu cầu nghiệp vụ tổng thể", "description": "Mô tả vấn đề kinh doanh cần giải quyết.", "required": True, "example": "Công ty muốn quản lý kho bằng phần mềm thay vì Excel."},
            {"name": "Phạm vi dự án (Scope)", "description": "Danh sách module/chức năng thuộc phạm vi.", "required": True, "example": "In-scope: Nhập kho, Xuất kho, Kiểm kê. Out-of-scope: Vận chuyển, CRM."}
        ],
        "process_detail": [
            {"step": 1, "title": "Tóm tắt dự án (Executive Summary)", "description": "Viết phần giới thiệu ngắn gọn về dự án.", "sub_steps": [
                "Bối cảnh: Tại sao cần dự án này?",
                "Mục tiêu: Dự án giải quyết vấn đề gì?",
                "Lợi ích kỳ vọng: Tiết kiệm bao nhiêu %, tăng hiệu suất bao nhiêu?"
            ]},
            {"step": 2, "title": "Xác định Stakeholders", "description": "Liệt kê tất cả các bên liên quan.", "sub_steps": [
                "Người tài trợ (Sponsor)",
                "Người dùng cuối (End Users) theo từng phòng ban",
                "Đội IT",
                "Các bên thứ ba (NCC phần mềm, Tư vấn)"
            ]},
            {"step": 3, "title": "Định nghĩa Scope", "description": "Xác định rõ In-scope và Out-of-scope.", "sub_steps": [
                "In-scope: Liệt kê từng module/chức năng (đánh số ID)",
                "Out-of-scope: Liệt kê rõ những gì KHÔNG làm (để tránh hiểu nhầm)",
                "Assumptions: Các giả định",
                "Constraints: Các ràng buộc (Ngân sách, Timeline, Công nghệ)"
            ]},
            {"step": 4, "title": "Liệt kê Business Requirements", "description": "Mô tả các yêu cầu nghiệp vụ cấp cao.", "sub_steps": [
                "Mỗi requirement có ID duy nhất (VD: BR-001, BR-002)",
                "Mỗi requirement có Priority (Must / Should / Could / Won't)",
                "Mỗi requirement mô tả WHAT không mô tả HOW",
                "Nhóm requirements theo module/chức năng"
            ]},
            {"step": 5, "title": "Xác định Tiêu chí Thành công", "description": "Định nghĩa khi nào dự án được coi là thành công.", "sub_steps": [
                "KPI đo lường: Giảm thời gian xử lý 50%, Giảm sai sót 80%",
                "Tiêu chí nghiệm thu (Acceptance Criteria cấp dự án)",
                "Timeline dự kiến (Milestones)"
            ]}
        ],
        "outputs_detail": [
            {"name": "Tài liệu BRD", "format": "Markdown Document", "template": "# Business Requirement Document (BRD)\n\n## 1. Document Control\n| Mục | Chi tiết |\n|---|---|\n| Tên dự án | [Tên] |\n| Phiên bản | 1.0 |\n| Ngày tạo | [Ngày] |\n| Tác giả | [BA Name] |\n| Trạng thái | Draft / Reviewed / Approved |\n\n## 2. Revision History\n| Version | Date | Author | Changes |\n|---|---|---|---|\n| 1.0 | [Date] | [Name] | Tạo mới |\n\n## 3. Executive Summary\n[Mô tả ngắn gọn...]\n\n## 4. Business Objectives\n[Mục tiêu kinh doanh...]\n\n## 5. Stakeholders\n| Tên | Vai trò | Phòng ban | Mức độ ảnh hưởng |\n|---|---|---|---|\n\n## 6. Scope\n### 6.1. In-Scope\n### 6.2. Out-of-Scope\n### 6.3. Assumptions\n### 6.4. Constraints\n\n## 7. Business Requirements\n| ID | Requirement | Module | Priority | Status |\n|---|---|---|---|---|\n| BR-001 | ... | ... | Must | Draft |\n\n## 8. Success Criteria\n\n## 9. Risks\n\n## 10. Approval\n| Tên | Vai trò | Chữ ký | Ngày |\n|---|---|---|---|"}
        ],
        "sub_skills": ["Phỏng vấn Stakeholder", "Xác định Scope", "Priority Assignment (MoSCoW)"],
        "business_rules": [
            "BR-DOC-01: BRD chỉ mô tả WHAT và WHY, KHÔNG mô tả HOW.",
            "BR-DOC-02: Mỗi Business Requirement phải có ID duy nhất để truy vết.",
            "BR-DOC-03: Out-of-scope phải liệt kê rõ ràng để tránh Scope Creep.",
            "BR-DOC-04: BRD phải có ít nhất 1 lần Review trước khi Approve."
        ],
        "edge_cases": [
            "Khách hàng yêu cầu quá rộng → Gợi ý chia thành Phase 1, Phase 2",
            "Stakeholders mâu thuẫn nhau → Escalate lên Sponsor quyết định",
            "Yêu cầu thay đổi liên tục → Đánh dấu phiên bản (Version Control)"
        ],
        "checklist": [
            "Có Executive Summary rõ ràng?",
            "Đã liệt kê đầy đủ Stakeholders?",
            "Có In-scope VÀ Out-of-scope rõ ràng?",
            "Mỗi Requirement có ID và Priority?",
            "BRD không chứa giải pháp kỹ thuật?",
            "Có Success Criteria đo lường được?",
            "Có Revision History?",
            "Có phần Sign-off (Ký duyệt)?"
        ],
        "example": "Xem Template BRD trong Outputs.",
        "related_skills": ["Write SRS", "Write User Story", "Interview Stakeholder"],
        "quality_criteria": ["Phải có Scope rõ ràng", "Phải có Requirement IDs", "Không chứa Technical Solution"],
        "estimated_effort": "3-5 ngày",
        "prompt_role": "Senior Business Analyst chuyên soạn thảo tài liệu cấp cao.",
        "prompt_task": "Soạn thảo BRD chuẩn mực cho dự án.",
        "prompt_context": "Dự án đang ở giai đoạn Inception, cần tài liệu BRD để trình ban lãnh đạo phê duyệt.",
        "prompt_rules": [
            "BRD PHẢI tập trung vào WHAT và WHY, KHÔNG đi vào HOW.",
            "Mỗi Requirement PHẢI có ID duy nhất.",
            "PHẢI có In-scope VÀ Out-of-scope.",
            "PHẢI sử dụng MoSCoW để đánh Priority.",
            "Output PHẢI theo đúng template BRD chuẩn."
        ],
        "prompt_example": ""
    },
    # ================================================================
    # 02-Requirement / Review Requirement
    # ================================================================
    {
        "path": "02-Requirement",
        "name": "Review Requirement",
        "level": "Level 4 - Thinking Skill",
        "domain": "Requirement",
        "tags": ["Requirement", "Review", "Quality", "Gap"],
        "purpose": "Rà soát và kiểm tra tính đầy đủ, chính xác, nhất quán của yêu cầu nghiệp vụ. Đây là kỹ năng kiểm duyệt cuối cùng trước khi chốt scope, đảm bảo không bỏ sót bất kỳ Business Rule, Exception, Validation, Permission, UI, API, Database, Workflow, Report hay Notification nào.",
        "when_to_use": "Sử dụng ở cuối giai đoạn phân tích, trước khi chốt scope với khách hàng hoặc bàn giao cho team Dev.",
        "prerequisites": ["Đã hoàn thành viết Requirement List / BRD / SRS"],
        "inputs_detail": [
            {"name": "Tài liệu yêu cầu (BRD/SRS/Requirement List)", "description": "Bộ tài liệu cần review.", "required": True, "example": "File SRS v1.0 với 45 Functional Requirements và 10 Non-Functional Requirements."}
        ],
        "process_detail": [
            {"step": 1, "title": "Kiểm tra TÍNH ĐẦY ĐỦ (Completeness)", "description": "Rà soát xem có thiếu yêu cầu nào không.", "sub_steps": [
                "Missing Business Rule? Có quy tắc nghiệp vụ nào chưa được mô tả?",
                "Missing Exception? Các trường hợp ngoại lệ đã được xử lý hết chưa?",
                "Missing Validation? Các rule kiểm tra dữ liệu đầu vào đã đủ chưa?",
                "Missing Permission? Ai được làm gì trên mỗi chức năng?",
                "Missing UI? Có màn hình/form nào chưa được mô tả?",
                "Missing API? Có endpoint nào thiếu?",
                "Missing Database? Có trường dữ liệu nào chưa được định nghĩa?",
                "Missing Workflow? Luồng phê duyệt đã đủ chưa?",
                "Missing Report? Có báo cáo nào người dùng cần nhưng chưa liệt kê?",
                "Missing Notification? Có cảnh báo/email nào cần gửi nhưng chưa thiết kế?"
            ]},
            {"step": 2, "title": "Kiểm tra TÍNH NHẤT QUÁN (Consistency)", "description": "Rà soát xem có requirement nào mâu thuẫn nhau không.", "sub_steps": [
                "Requirement A nói 'cho phép xóa' nhưng Requirement B nói 'không được xóa'?",
                "Thuật ngữ có được dùng nhất quán không? (VD: Customer vs Client vs Khách hàng)",
                "Business Rule có xung đột với nhau không?"
            ]},
            {"step": 3, "title": "Kiểm tra TÍNH KHẢ THI (Feasibility)", "description": "Đánh giá xem requirement có khả thi về mặt kỹ thuật không.", "sub_steps": [
                "Yêu cầu 'realtime' có thực sự cần thiết không? (Nếu near-realtime 5 phút đã đủ thì rẻ hơn nhiều)",
                "Yêu cầu tích hợp bên thứ 3 có API không?",
                "Dữ liệu cần migrate có sẵn sàng không?"
            ]},
            {"step": 4, "title": "Đưa ra câu hỏi cho khách hàng", "description": "Lập danh sách câu hỏi cần hỏi khách hàng để làm rõ.", "sub_steps": [
                "Mỗi câu hỏi phải liên kết với Requirement ID cụ thể",
                "Phân loại: Phải hỏi ngay (Blocker) vs Có thể hỏi sau (Nice to know)",
                "Đề xuất lựa chọn cho khách hàng (Option A / Option B) thay vì câu hỏi mở"
            ]},
            {"step": 5, "title": "Đưa ra gợi ý bổ sung (Suggestions)", "description": "Dựa trên kinh nghiệm, đề xuất các yêu cầu mà khách hàng có thể chưa nghĩ tới.", "sub_steps": [
                "Gợi ý tính năng nâng cao (Nice-to-have)",
                "Gợi ý cải thiện UX",
                "Gợi ý về bảo mật, audit, logging"
            ]}
        ],
        "outputs_detail": [
            {"name": "Review Report", "format": "Markdown Document", "template": "# Requirement Review Report\n\n## 1. Tổng quan\n- Số lượng Requirement đã review: [N]\n- Số lượng Issue phát hiện: [N]\n- Số lượng câu hỏi cần hỏi khách: [N]\n\n## 2. Issues Found\n| # | Requirement ID | Loại Issue | Mô tả | Severity |\n|---|---|---|---|---|\n| 1 | FR-015 | Missing Validation | Chưa validate email format | Medium |\n| 2 | FR-022 | Missing Permission | Ai được xóa đơn hàng? | High |\n\n## 3. Questions for Client\n| # | Requirement ID | Câu hỏi | Gợi ý |\n|---|---|---|---|\n| 1 | BR-003 | Hàng hết HSD xử lý thế nào? | Option A: Tự động chặn xuất. Option B: Cảnh báo nhưng vẫn cho xuất. |\n\n## 4. Suggestions\n| # | Mô tả | Lý do |\n|---|---|---|\n| 1 | Thêm Audit Log cho mọi thao tác xóa | Truy vết khi có sự cố |"}
        ],
        "sub_skills": ["Completeness Check", "Consistency Check", "Feasibility Assessment", "Question Formulation"],
        "business_rules": [
            "BR-REV-01: Mỗi Requirement phải được review ít nhất 1 lần trước khi chốt.",
            "BR-REV-02: Issue severity High phải được giải quyết trước khi bàn giao cho Dev.",
            "BR-REV-03: Mọi câu hỏi Blocker phải được trả lời trước khi bắt đầu Sprint."
        ],
        "edge_cases": [
            "Khách hàng không trả lời câu hỏi → Ghi nhận assumption và tiến hành",
            "Requirement mâu thuẫn giữa 2 phòng ban → Escalate lên Sponsor"
        ],
        "checklist": [
            "Đã kiểm tra Missing Business Rule?",
            "Đã kiểm tra Missing Exception?",
            "Đã kiểm tra Missing Validation?",
            "Đã kiểm tra Missing Permission?",
            "Đã kiểm tra Missing UI?",
            "Đã kiểm tra Missing API?",
            "Đã kiểm tra Missing Database?",
            "Đã kiểm tra Missing Workflow?",
            "Đã kiểm tra Missing Report?",
            "Đã kiểm tra Missing Notification?",
            "Đã kiểm tra Consistency (không mâu thuẫn)?",
            "Đã đặt câu hỏi cho từng điểm chưa rõ?"
        ],
        "example": "Xem Review Report template trong Outputs.",
        "related_skills": ["Write BRD", "Write SRS", "Gap Analysis", "Impact Analysis"],
        "quality_criteria": ["Phải kiểm tra đủ 10 khía cạnh trong Completeness Check", "Phải có danh sách câu hỏi cụ thể", "Issues phải có Severity"],
        "estimated_effort": "1-2 ngày / tài liệu",
        "prompt_role": "Senior Business Analyst kiêm Quality Assurance Analyst, chuyên review tài liệu yêu cầu.",
        "prompt_task": "Review toàn diện tài liệu yêu cầu, đảm bảo không bỏ sót bất kỳ khía cạnh nào.",
        "prompt_context": "Bạn nhận được một bộ tài liệu yêu cầu và cần kiểm tra tính đầy đủ trước khi chốt scope.",
        "prompt_rules": [
            "PHẢI kiểm tra đủ 10 khía cạnh: Business Rule, Exception, Validation, Permission, UI, API, Database, Workflow, Report, Notification.",
            "PHẢI đưa ra câu hỏi CỤ THỂ cho khách hàng (không chung chung).",
            "PHẢI phân loại Issue theo Severity: High / Medium / Low.",
            "PHẢI đề xuất gợi ý bổ sung dựa trên kinh nghiệm.",
            "Output PHẢI theo format Review Report template."
        ],
        "prompt_example": ""
    },
    # ================================================================
    # 03-Modeling / Thiết kế module
    # ================================================================
    {
        "path": "03-Modeling/Architecture",
        "name": "Thiết kế module",
        "level": "Level 3 - Architecture Skill",
        "domain": "Architecture",
        "tags": ["Architecture", "Module", "Design", "System"],
        "purpose": "Thiết kế kiến trúc module cho hệ thống doanh nghiệp, bao gồm phân rã module, thiết kế menu, phân quyền (RBAC), workflow, database schema, API endpoints, danh sách màn hình và đảm bảo không thiếu bất kỳ thành phần nào nhờ checklist toàn diện.",
        "when_to_use": "Sử dụng khi bắt đầu giai đoạn thiết kế kiến trúc tổng thể (High-Level Design) cho một module mới.",
        "prerequisites": ["Đã hoàn thành BRD/SRS"],
        "inputs_detail": [
            {"name": "Business Requirements", "description": "Danh sách yêu cầu nghiệp vụ đã duyệt.", "required": True, "example": "Module WMS: 35 Functional Requirements, 8 Non-Functional Requirements."},
            {"name": "Domain Knowledge", "description": "Kiến thức chuyên ngành liên quan.", "required": True, "example": "Kho vận: Inbound, Outbound, Inventory, Cycle Count, Lot/Batch management."}
        ],
        "process_detail": [
            {"step": 1, "title": "Phân rã Module (Module Decomposition)", "description": "Chia nhỏ module lớn thành các sub-module.", "sub_steps": [
                "Nhóm các Requirement có liên quan thành Sub-module",
                "Ví dụ Module WMS: Sub-module Inbound, Outbound, Inventory, Master Data",
                "Mỗi Sub-module phải độc lập về mặt logic"
            ]},
            {"step": 2, "title": "Thiết kế Menu & Navigation", "description": "Cấu trúc menu cho module.", "sub_steps": [
                "Menu Level 1: Tên module (VD: Quản lý Kho)",
                "Menu Level 2: Sub-module (Nhập kho, Xuất kho, Tồn kho, Kiểm kê)",
                "Menu Level 3: Chức năng con (Tạo phiếu nhập, Danh sách phiếu nhập, Báo cáo nhập)"
            ]},
            {"step": 3, "title": "Thiết kế Permission Matrix", "description": "Ma trận phân quyền RBAC.", "sub_steps": [
                "Xác định Roles: Admin, Manager, Operator, Viewer",
                "Mapping Role vs Feature vs Action (View/Create/Edit/Delete/Approve)",
                "Xác định data-level permission (Chỉ thấy dữ liệu của mình / của phòng ban / toàn bộ)"
            ]},
            {"step": 4, "title": "Thiết kế Workflow", "description": "Các luồng phê duyệt và trạng thái.", "sub_steps": [
                "State Machine: Draft → Submitted → Approved → Done",
                "Ai có quyền Approve? Điều kiện gì?",
                "Có cho phép Reject / Return to Draft không?"
            ]},
            {"step": 5, "title": "Thiết kế Database Schema", "description": "Xác định các bảng dữ liệu chính.", "sub_steps": [
                "Entity List: Các bảng cần tạo",
                "Relationship: 1-1, 1-N, N-N",
                "Key fields: PK, FK, Unique, Index"
            ]},
            {"step": 6, "title": "Thiết kế API Endpoints", "description": "Danh sách API cho Front-end gọi.", "sub_steps": [
                "CRUD APIs cho mỗi Entity",
                "Workflow APIs (Submit, Approve, Reject)",
                "Report/Export APIs"
            ]},
            {"step": 7, "title": "Danh sách Screens (Wireframe)", "description": "Liệt kê tất cả các màn hình cần thiết kế.", "sub_steps": [
                "List Page (Danh sách) cho mỗi Entity",
                "Detail/Form Page cho Create/Edit",
                "Dashboard Page",
                "Report Page"
            ]}
        ],
        "outputs_detail": [
            {"name": "Module Blueprint", "format": "Markdown Document bao gồm tất cả phần trên", "template": ""},
            {"name": "Permission Matrix", "format": "Markdown Table", "template": "| Chức năng | Admin | Manager | Operator | Viewer |\n|---|---|---|---|---|\n| Xem phiếu nhập | ✅ | ✅ | ✅ | ✅ |\n| Tạo phiếu nhập | ✅ | ✅ | ✅ | ❌ |\n| Duyệt phiếu nhập | ✅ | ✅ | ❌ | ❌ |\n| Xóa phiếu nhập | ✅ | ❌ | ❌ | ❌ |"}
        ],
        "sub_skills": ["Module Decomposition", "Permission Matrix Design", "Workflow Design", "Screen Listing"],
        "business_rules": [
            "BR-MOD-01: Mỗi module phải có Dashboard riêng.",
            "BR-MOD-02: Mỗi danh sách (List) phải có Search, Filter, Pagination.",
            "BR-MOD-03: Mọi thao tác quan trọng phải có Audit Log."
        ],
        "edge_cases": [
            "Module cần tích hợp với module khác → Xác định rõ Integration Points",
            "Yêu cầu Multi-tenant → Mỗi tenant thấy dữ liệu riêng"
        ],
        "checklist": [
            "Có Dashboard chưa?",
            "Có CRUD cho mỗi entity chưa?",
            "Có Import (Excel/CSV) chưa?",
            "Có Export (Excel/PDF) chưa?",
            "Có Approval workflow chưa?",
            "Có Audit Log chưa?",
            "Có Notification (Email/In-app) chưa?",
            "Có Search chưa?",
            "Có Filter chưa?",
            "Có Pagination chưa?",
            "Có Permission matrix chưa?",
            "Có Report chưa?",
            "Có Audit Trail chưa?",
            "Có Multi-language chưa (nếu cần)?",
            "Có Soft Delete chưa?"
        ],
        "example": "Xem Permission Matrix template.",
        "related_skills": ["Thiết kế ERD", "Thiết kế API Contract", "Thiết kế Dashboard"],
        "quality_criteria": ["Phải đáp ứng đủ 15 items trong Checklist", "Phải có Permission Matrix", "Phải có danh sách Screens"],
        "estimated_effort": "5-10 ngày",
        "prompt_role": "Senior Solution Architect / Senior BA.",
        "prompt_task": "Thiết kế module toàn diện cho hệ thống doanh nghiệp.",
        "prompt_context": "Doanh nghiệp cần thiết kế kiến trúc chi tiết cho một module mới.",
        "prompt_rules": [
            "PHẢI kiểm tra đủ 15 items trong Checklist (Dashboard, CRUD, Import, Export, Approval, Log, Notification, Search, Filter, Pagination, Permission, Report, Audit, Multi-lang, Soft Delete).",
            "PHẢI có Permission Matrix dạng bảng.",
            "PHẢI liệt kê tất cả Screens cần thiết.",
            "PHẢI thiết kế Workflow (State Machine) cho các entity có trạng thái.",
            "PHẢI liệt kê API Endpoints.",
            "Output PHẢI bao gồm: Module Blueprint, Menu Structure, Permission Matrix, Entity List, Screen List, API List."
        ],
        "prompt_example": ""
    },
    # ================================================================
    # 09-BA-Agent / Gap Analysis
    # ================================================================
    {
        "path": "09-BA-Agent/Thinking Skills",
        "name": "Gap Analysis",
        "level": "Level 4 - Thinking Skill",
        "domain": "Thinking",
        "tags": ["Thinking", "Analysis", "Gap", "As-Is", "To-Be"],
        "purpose": "Phân tích khoảng cách giữa trạng thái hiện tại (As-Is) và trạng thái mong muốn (To-Be), sau đó đề xuất kế hoạch hành động (Action Plan) để thu hẹp khoảng cách, phân theo 3 nhóm: Business Process, Technology/System, và People/Organization.",
        "when_to_use": "Sử dụng khi:\n- Chuyển đổi từ hệ thống cũ sang mới.\n- Cải thiện quy trình nghiệp vụ hiện tại.\n- Đánh giá sản phẩm hiện có so với yêu cầu mới.",
        "prerequisites": ["Hiểu quy trình hiện tại (As-Is)", "Hiểu mục tiêu (To-Be)"],
        "inputs_detail": [
            {"name": "Mô tả trạng thái hiện tại (As-Is)", "description": "Quy trình, hệ thống, con người hiện tại đang hoạt động ra sao.", "required": True, "example": "Hiện tại: Kho quản lý bằng Excel, kiểm kê thủ công, không có barcode, mỗi lần kiểm kê mất 2 ngày."},
            {"name": "Mục tiêu mong muốn (To-Be)", "description": "Trạng thái lý tưởng sau khi cải thiện.", "required": True, "example": "Mong muốn: Hệ thống WMS quét barcode, kiểm kê Cycle Count hàng ngày, sai lệch tồn kho < 1%."}
        ],
        "process_detail": [
            {"step": 1, "title": "Mô tả chi tiết As-Is", "description": "Vẽ sơ đồ và mô tả quy trình hiện tại.", "sub_steps": [
                "Vẽ luồng As-Is dưới dạng BPMN hoặc Flowchart",
                "Ghi nhận Pain Points (Điểm đau): Chậm, sai sót, tốn nhân lực",
                "Ghi nhận Workarounds (Cách chữa cháy) hiện tại",
                "Phỏng vấn người dùng: Điều gì khiến bạn khó chịu nhất?"
            ]},
            {"step": 2, "title": "Mô tả chi tiết To-Be", "description": "Vẽ sơ đồ và mô tả trạng thái mong muốn.", "sub_steps": [
                "Vẽ luồng To-Be lý tưởng",
                "Xác định các KPI đo lường mục tiêu",
                "Best Practices từ ngành tham khảo"
            ]},
            {"step": 3, "title": "Xác định Gaps (Khoảng cách)", "description": "So sánh As-Is vs To-Be và liệt kê các điểm khác biệt.", "sub_steps": [
                "Business Process Gaps: Quy trình nào cần thay đổi?",
                "Technology/System Gaps: Hệ thống nào cần xây mới/nâng cấp?",
                "People/Organization Gaps: Nhân sự nào cần đào tạo? Cần tuyển mới?",
                "Data Gaps: Dữ liệu nào thiếu hoặc không đúng format?"
            ]},
            {"step": 4, "title": "Lập Action Plan", "description": "Đề xuất giải pháp thu hẹp từng Gap.", "sub_steps": [
                "Mỗi Gap → 1 hoặc nhiều Action Items",
                "Mỗi Action Item có: Owner, Timeline, Priority, Estimated Cost",
                "Sắp xếp theo Quick Wins (Dễ làm, hiệu quả cao) trước"
            ]}
        ],
        "outputs_detail": [
            {"name": "Gap Analysis Report", "format": "Markdown Table", "template": "| # | Nhóm | As-Is | To-Be | Gap | Action | Priority | Owner |\n|---|---|---|---|---|---|---|---|\n| 1 | Process | Kiểm kê bằng tay 2 ngày | Cycle Count barcode 2h | Không có barcode | Triển khai hệ thống barcode | High | IT |\n| 2 | System | Quản lý kho bằng Excel | WMS chuyên dụng | Không có phần mềm | Mua/Xây WMS | High | PM |\n| 3 | People | Nhân viên kho không biết dùng máy tính | Nhân viên sử dụng thành thạo PDA | Thiếu kỹ năng | Đào tạo 2 tuần | Medium | HR |"}
        ],
        "sub_skills": ["As-Is Process Mapping", "To-Be Vision Design", "Action Plan Creation"],
        "business_rules": [
            "BR-GAP-01: Gap phải được chia thành 3 nhóm: Process, System, People.",
            "BR-GAP-02: Mỗi Gap phải có Action Item cụ thể.",
            "BR-GAP-03: Action Plan phải có Owner và Timeline."
        ],
        "edge_cases": [
            "As-Is quá hỗn loạn, không ai mô tả được chính xác → Quan sát thực tế (Observation)",
            "To-Be quá lý tưởng, không khả thi → Chia thành To-Be Phase 1 (khả thi) + To-Be Phase 2 (lý tưởng)"
        ],
        "checklist": [
            "Đã vẽ As-Is Process?",
            "Đã vẽ To-Be Process?",
            "Đã liệt kê đủ Gaps theo 3 nhóm (Process, System, People)?",
            "Mỗi Gap có Action Item?",
            "Action Plan có Owner và Timeline?",
            "Đã đánh giá rủi ro khi thay đổi?"
        ],
        "example": "Xem Gap Analysis Report template trong Outputs.",
        "related_skills": ["Root Cause Analysis", "Impact Analysis", "Risk Analysis"],
        "quality_criteria": ["Phải chia Gap thành 3 nhóm", "Phải có Action Plan", "Action Plan phải có Owner"],
        "estimated_effort": "3-5 ngày",
        "prompt_role": "Senior Business Analyst / Transformation Consultant.",
        "prompt_task": "Thực hiện Gap Analysis toàn diện giữa As-Is và To-Be.",
        "prompt_context": "Doanh nghiệp đang trong giai đoạn chuyển đổi số hoặc cải tiến quy trình.",
        "prompt_rules": [
            "PHẢI chia Gaps thành 3 nhóm: Business Process, Technology/System, People/Organization.",
            "PHẢI có As-Is và To-Be rõ ràng.",
            "PHẢI có Action Plan với Owner, Timeline, Priority.",
            "PHẢI đánh giá rủi ro cho mỗi thay đổi lớn.",
            "Output PHẢI dùng Markdown Table format."
        ],
        "prompt_example": ""
    },
    # ================================================================
    # 09-BA-Agent / Root Cause Analysis
    # ================================================================
    {
        "path": "09-BA-Agent/Thinking Skills",
        "name": "Root Cause Analysis",
        "level": "Level 4 - Thinking Skill",
        "domain": "Thinking",
        "tags": ["Thinking", "RCA", "5 Whys", "Fishbone", "Problem Solving"],
        "purpose": "Phân tích nguyên nhân gốc rễ của một vấn đề kinh doanh hoặc lỗi hệ thống bằng các kỹ thuật chuyên nghiệp (5 Whys, Fishbone Diagram) để đề xuất giải pháp triệt để thay vì chỉ xử lý triệu chứng.",
        "when_to_use": "Sử dụng khi phát hiện vấn đề lặp đi lặp lại hoặc lỗi hệ thống nghiêm trọng cần tìm ra nguyên nhân sâu xa.",
        "prerequisites": ["Nắm rõ vấn đề cần phân tích"],
        "inputs_detail": [
            {"name": "Problem Statement", "description": "Mô tả vấn đề cụ thể, đo lường được.", "required": True, "example": "Tỷ lệ hàng giao sai cho khách hàng tăng từ 1% lên 5% trong 3 tháng gần đây."},
            {"name": "Dữ liệu liên quan", "description": "Số liệu, log, báo cáo để phân tích.", "required": False, "example": "Log đơn hàng bị trả lại, Danh sách ca làm việc, Tỷ lệ lỗi theo sản phẩm"}
        ],
        "process_detail": [
            {"step": 1, "title": "Xác định vấn đề (Define Problem)", "description": "Mô tả vấn đề một cách cụ thể và đo lường được.", "sub_steps": [
                "Vấn đề là gì? (What happened?)",
                "Xảy ra ở đâu? (Where?)",
                "Xảy ra khi nào? (When? Từ bao giờ?)",
                "Ảnh hưởng bao nhiêu? (How much/many?)",
                "Ai bị ảnh hưởng? (Who?)"
            ]},
            {"step": 2, "title": "Thu thập dữ liệu", "description": "Gom dữ liệu thực tế để phân tích.", "sub_steps": [
                "Phỏng vấn người liên quan",
                "Xem log hệ thống",
                "Phân tích xu hướng (Trend analysis)",
                "Đi xuống hiện trường quan sát (Gemba Walk)"
            ]},
            {"step": 3, "title": "Phân tích bằng 5 Whys", "description": "Hỏi 'Tại sao?' liên tiếp 5 lần để đào sâu đến gốc rễ.", "sub_steps": [
                "Why 1: Tại sao hàng giao sai? → Vì nhân viên Picking lấy nhầm hàng.",
                "Why 2: Tại sao lấy nhầm? → Vì không quét barcode, dùng mắt tìm.",
                "Why 3: Tại sao không quét barcode? → Vì máy PDA hết pin.",
                "Why 4: Tại sao PDA hết pin? → Vì chỉ có 5 PDA cho 15 nhân viên.",
                "Why 5: Tại sao thiếu PDA? → Vì chưa được duyệt ngân sách mua thêm.",
                "→ Root Cause: Thiếu thiết bị PDA + Quy trình không bắt buộc scan barcode."
            ]},
            {"step": 4, "title": "Phân tích bằng Fishbone (Ishikawa)", "description": "Sử dụng sơ đồ xương cá để phân loại nguyên nhân.", "sub_steps": [
                "Man (Con người): Thiếu đào tạo, thiếu nhân lực",
                "Machine (Máy móc): Thiếu PDA, máy cũ",
                "Method (Phương pháp): Quy trình chưa bắt buộc scan",
                "Material (Vật liệu): Nhãn hàng bị mờ, khó đọc",
                "Measurement (Đo lường): Không có KPI theo dõi tỷ lệ lỗi",
                "Mother Nature (Môi trường): Kho tối, chật hẹp"
            ]},
            {"step": 5, "title": "Đề xuất giải pháp & Hành động", "description": "Đưa ra giải pháp cho Root Cause.", "sub_steps": [
                "Corrective Action: Sửa ngay (Mua thêm PDA, ép scan barcode)",
                "Preventive Action: Ngăn tái diễn (SOP mới, audit hàng tuần)",
                "Verification: Cách kiểm tra giải pháp có hiệu quả (Theo dõi tỷ lệ lỗi 30 ngày)"
            ]}
        ],
        "outputs_detail": [
            {"name": "RCA Report", "format": "Markdown Document", "template": "# Root Cause Analysis Report\n\n## Problem Statement\n[Mô tả vấn đề cụ thể...]\n\n## 5 Whys Analysis\n| # | Question | Answer |\n|---|---|---|\n| 1 | Tại sao...? | Vì... |\n| 2 | Tại sao...? | Vì... |\n| 3 | Tại sao...? | Vì... |\n| 4 | Tại sao...? | Vì... |\n| 5 | Tại sao...? | Vì... |\n\n**Root Cause:** [Nguyên nhân gốc rễ]\n\n## Fishbone Diagram (6M)\n| Category | Possible Causes |\n|---|---|\n| Man | ... |\n| Machine | ... |\n| Method | ... |\n| Material | ... |\n| Measurement | ... |\n| Environment | ... |\n\n## Action Plan\n| # | Action | Type | Owner | Deadline |\n|---|---|---|---|---|\n| 1 | Mua 10 PDA | Corrective | IT | 2 tuần |\n| 2 | Cập nhật SOP bắt buộc scan | Preventive | QC Manager | 1 tuần |"}
        ],
        "sub_skills": ["5 Whys Technique", "Fishbone Diagram", "Corrective/Preventive Action"],
        "business_rules": [
            "BR-RCA-01: Phải hỏi ít nhất 5 lần TẠI SAO.",
            "BR-RCA-02: Root Cause phải là nguyên nhân có thể hành động được (Actionable).",
            "BR-RCA-03: Giải pháp phải bao gồm cả Corrective (Sửa ngay) và Preventive (Ngăn tái diễn)."
        ],
        "edge_cases": [
            "Root cause nằm ngoài tầm kiểm soát (VD: Luật pháp) → Ghi nhận và đề xuất workaround",
            "Nhiều Root Cause đồng thời → Xử lý tất cả, ưu tiên cause có ảnh hưởng lớn nhất"
        ],
        "checklist": [
            "Vấn đề đã được mô tả cụ thể, đo lường được?",
            "Đã thu thập đủ dữ liệu?",
            "Đã hỏi ít nhất 5 lần Tại sao?",
            "Đã sử dụng Fishbone 6M?",
            "Root Cause đã xác định rõ?",
            "Giải pháp có cả Corrective và Preventive?",
            "Có cách kiểm tra hiệu quả giải pháp (Verification)?"
        ],
        "example": "Xem ví dụ 5 Whys trong Process section.",
        "related_skills": ["Gap Analysis", "Impact Analysis", "Risk Analysis", "Phân tích OEE"],
        "quality_criteria": ["Phải có 5 Whys", "Phải có Fishbone 6M", "Phải có Action Plan với Owner"],
        "estimated_effort": "1-3 ngày",
        "prompt_role": "Senior Problem-Solving Analyst / Continuous Improvement Specialist.",
        "prompt_task": "Phân tích nguyên nhân gốc rễ của một vấn đề.",
        "prompt_context": "Doanh nghiệp gặp phải vấn đề lặp đi lặp lại và cần tìm nguyên nhân triệt để.",
        "prompt_rules": [
            "PHẢI sử dụng kỹ thuật 5 Whys, trình bày dưới dạng bảng hỏi - đáp.",
            "PHẢI sử dụng Fishbone 6M để phân loại nguyên nhân.",
            "Root Cause PHẢI actionable (có thể hành động được).",
            "PHẢI có Corrective + Preventive Actions.",
            "Output PHẢI theo format RCA Report."
        ],
        "prompt_example": ""
    }
]

if __name__ == "__main__":
    print("=== Expanding: Requirement + Modeling + Thinking Skills ===")
    run(skills)
