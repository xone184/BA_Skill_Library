import sys
sys.path.insert(0, r"e:\BA Skill Library")
from skill_generator import run

skills = [
    # ================================================================
    # CRM - Lead Management
    # ================================================================
    {
        "path": "01-Business-Domain/CRM",
        "name": "Phân tích Lead Management",
        "level": "Level 2 - Business Skill",
        "domain": "CRM",
        "tags": ["CRM", "Lead", "Sales", "Marketing"],
        "purpose": "Phân tích toàn diện quy trình quản lý khách hàng tiềm năng (Lead), từ lúc tiếp nhận thông tin đến khi chuyển đổi thành cơ hội bán hàng (Opportunity), bao gồm quy tắc chấm điểm (Scoring), phân bổ (Routing) và chống trùng lặp (Deduplication).",
        "when_to_use": "Sử dụng khi:\n- Doanh nghiệp cần xây dựng hệ thống CRM mới có module quản lý Lead.\n- Muốn cải thiện tỷ lệ chuyển đổi Lead thành khách hàng.\n- Cần tích hợp nhiều kênh Marketing (Website, Facebook, Zalo, Google Ads) vào một hệ thống duy nhất.",
        "prerequisites": ["Hiểu cơ bản về Sales Funnel", "Biết quy trình bán hàng của doanh nghiệp"],
        "inputs_detail": [
            {"name": "Nguồn Lead (Lead Sources)", "description": "Danh sách tất cả các kênh mà doanh nghiệp thu thập khách hàng tiềm năng.", "required": True, "example": "Website form, Facebook Ads, Zalo OA, Giới thiệu, Sự kiện, Cold Call"},
            {"name": "Trạng thái Lead (Lead Status)", "description": "Các giai đoạn mà một Lead sẽ trải qua trong vòng đời.", "required": True, "example": "New → Contacted → Qualified → Converted / Disqualified"},
            {"name": "Tiêu chí chấm điểm (Scoring Criteria)", "description": "Các yếu tố để chấm điểm mức độ tiềm năng của Lead.", "required": False, "example": "Ngân sách > 100tr = +20 điểm, Đã xem demo = +30 điểm, Không trả lời 3 ngày = -10 điểm"},
            {"name": "Kênh Marketing", "description": "Các kênh quảng cáo đang chạy để tracking nguồn Lead.", "required": False, "example": "Google Ads, Facebook, SEO, Email Marketing"}
        ],
        "process_detail": [
            {"step": 1, "title": "Thu thập và Ghi nhận Lead", "description": "Phân tích tất cả các điểm chạm (Touchpoints) mà khách hàng tiềm năng có thể liên hệ với doanh nghiệp. Đảm bảo mọi kênh đều tự động tạo Lead trong hệ thống.", "sub_steps": [
                "Liệt kê toàn bộ kênh thu thập Lead (Online & Offline)",
                "Xác định trường dữ liệu bắt buộc khi tạo Lead (Họ tên, SĐT, Email, Nguồn)",
                "Thiết kế rule tự động tạo Lead từ Web form, Landing page, Chatbot",
                "Quy định cách nhập Lead thủ công (Import Excel, Nhập tay)"
            ]},
            {"step": 2, "title": "Chống trùng lặp (Deduplication)", "description": "Thiết kế quy tắc phát hiện và xử lý Lead trùng lặp để đảm bảo dữ liệu sạch.", "sub_steps": [
                "Xác định trường khóa chống trùng (SĐT, Email, hoặc cả hai)",
                "Khi phát hiện trùng: Merge (Gộp), Block (Chặn tạo mới), hay Alert (Cảnh báo)?",
                "Quy tắc ưu tiên dữ liệu khi Merge (Giữ bản gốc hay bản mới hơn?)"
            ]},
            {"step": 3, "title": "Chấm điểm Lead (Lead Scoring)", "description": "Thiết kế hệ thống scoring tự động để xếp hạng mức độ tiềm năng.", "sub_steps": [
                "Scoring theo hồ sơ (Demographic): Ngành nghề, Quy mô, Vị trí",
                "Scoring theo hành vi (Behavioral): Xem trang báo giá, Tải tài liệu, Đăng ký demo",
                "Xác định ngưỡng (Threshold): Bao nhiêu điểm thì chuyển thành MQL (Marketing Qualified Lead)?",
                "Bao nhiêu điểm thì chuyển thành SQL (Sales Qualified Lead)?"
            ]},
            {"step": 4, "title": "Phân bổ Lead (Lead Routing)", "description": "Thiết kế quy tắc tự động gán Lead cho nhân viên kinh doanh phù hợp.", "sub_steps": [
                "Phân bổ theo khu vực địa lý (Territory)",
                "Phân bổ theo ngành (Industry Vertical)",
                "Phân bổ Round-robin (Lần lượt công bằng)",
                "Phân bổ theo Workload (Ai có ít Lead nhất thì nhận)"
            ]},
            {"step": 5, "title": "Nuôi dưỡng Lead (Lead Nurturing)", "description": "Thiết kế quy trình chăm sóc Lead chưa sẵn sàng mua.", "sub_steps": [
                "Email tự động theo chuỗi (Drip Campaign)",
                "Nhắc việc gọi lại cho Sales (Follow-up Reminder)",
                "Gửi nội dung giáo dục (Content Marketing)"
            ]},
            {"step": 6, "title": "Chuyển đổi Lead (Lead Conversion)", "description": "Thiết kế quy trình chuyển Lead thành Account + Contact + Opportunity.", "sub_steps": [
                "Dữ liệu Lead nào map sang Account? (Tên công ty, Địa chỉ)",
                "Dữ liệu Lead nào map sang Contact? (Tên người, SĐT, Email)",
                "Tự động tạo Opportunity kèm theo hay không?",
                "Lead sau khi convert thì xóa hay giữ lại để truy vết?"
            ]}
        ],
        "outputs_detail": [
            {"name": "Quy trình Lead Lifecycle (BPMN)", "format": "Sơ đồ BPMN hoặc Mermaid Flowchart", "template": "graph TD\n    A[Tiếp nhận Lead] --> B{Trùng lặp?}\n    B -->|Có| C[Merge/Alert]\n    B -->|Không| D[Lead Scoring]\n    D --> E{Score >= Threshold?}\n    E -->|Có| F[Assign to Sales]\n    E -->|Không| G[Nurturing Campaign]\n    F --> H[Contact & Qualify]\n    H --> I{Qualified?}\n    I -->|Có| J[Convert to Opportunity]\n    I -->|Không| K[Disqualified]"},
            {"name": "Cấu trúc dữ liệu Lead", "format": "Markdown Table", "template": "| Tên trường | Kiểu dữ liệu | Bắt buộc | Mô tả |\n|---|---|---|---|\n| lead_id | INT (PK) | Có | Mã Lead tự tăng |\n| full_name | VARCHAR(200) | Có | Họ và tên |\n| phone | VARCHAR(20) | Có | Số điện thoại |\n| email | VARCHAR(100) | Không | Email |\n| source | ENUM | Có | Nguồn Lead |\n| status | ENUM | Có | Trạng thái Lead |\n| score | INT | Không | Điểm Lead |\n| assigned_to | INT (FK) | Không | Nhân viên phụ trách |\n| created_at | DATETIME | Có | Ngày tạo |"},
            {"name": "Ma trận Lead Scoring", "format": "Markdown Table", "template": "| Tiêu chí | Điều kiện | Điểm |\n|---|---|---|\n| Ngành nghề | Sản xuất, Bán lẻ | +20 |\n| Quy mô | > 100 nhân viên | +15 |\n| Đã xem Demo | Có | +30 |\n| Không phản hồi | > 7 ngày | -15 |"}
        ],
        "sub_skills": ["Thiết kế Lead Scoring Model", "Thiết kế Deduplication Rules", "Thiết kế Lead Routing Rules", "Thiết kế Nurturing Campaign"],
        "business_rules": [
            "BR-CRM-LEAD-01: Mỗi Lead bắt buộc phải có ít nhất SĐT hoặc Email.",
            "BR-CRM-LEAD-02: Lead mới tạo phải được gán cho Sales trong vòng 24 giờ.",
            "BR-CRM-LEAD-03: Lead không có tương tác sau 90 ngày sẽ tự động chuyển sang trạng thái 'Dormant'.",
            "BR-CRM-LEAD-04: Không cho phép tạo Lead trùng SĐT với Lead đang ở trạng thái Active.",
            "BR-CRM-LEAD-05: Lead Score phải được tính lại mỗi khi có hành vi mới."
        ],
        "edge_cases": [
            "Lead có cả SĐT cá nhân và SĐT công ty → Chọn SĐT nào làm khóa chống trùng?",
            "Một người nhưng đại diện cho nhiều công ty → Tạo nhiều Lead hay gộp?",
            "Lead đã Disqualified quay lại hỏi mua → Mở lại Lead cũ hay tạo mới?",
            "Lead từ đối thủ cạnh tranh giả mạo khách hàng → Cần rule phát hiện.",
            "Import 10.000 Lead từ Excel cùng lúc → Xử lý trùng lặp hàng loạt ra sao?"
        ],
        "checklist": [
            "Đã xác định đủ tất cả nguồn Lead (Online + Offline)",
            "Đã thiết kế quy tắc chống trùng lặp (Deduplication)",
            "Đã thiết kế mô hình Lead Scoring",
            "Đã thiết kế quy tắc phân bổ Lead (Routing)",
            "Đã thiết kế luồng Nurturing cho Lead chưa qualified",
            "Đã thiết kế quy trình Convert Lead → Account/Contact/Opportunity",
            "Đã xác định SLA phản hồi Lead (ví dụ: < 24 giờ)",
            "Đã thiết kế Dashboard theo dõi Lead (Số lượng, Tỷ lệ chuyển đổi, Nguồn hiệu quả nhất)",
            "Đã thiết kế cảnh báo (Notification) cho Sales khi có Lead mới",
            "Đã thiết kế báo cáo ROI theo kênh Marketing"
        ],
        "example": """### Ví dụ: Công ty ABC (Phần mềm ERP) muốn xây dựng module Lead Management

**Input từ khách hàng:**
- Nguồn Lead: Website (40%), Facebook Ads (30%), Giới thiệu (20%), Sự kiện (10%)
- Đội Sales: 10 người, chia theo 3 khu vực (Bắc, Trung, Nam)
- Mục tiêu: Tăng tỷ lệ chuyển đổi từ 5% lên 15%

**Output của BA:**
1. Lead Lifecycle gồm 6 trạng thái: New → Contacted → Qualified → Proposal → Won / Lost
2. Scoring Model: Website form = +10, Download brochure = +20, Request demo = +40, Budget > 500tr = +30
3. Routing: Lead Bắc → Team A, Lead Trung → Team B, Lead Nam → Team C
4. SLA: Lead mới phải được gọi trong vòng 4 giờ làm việc
5. Dedup: Trùng SĐT → Alert cho Sales, Trùng Email → Auto-merge""",
        "related_skills": ["Phân tích Opportunity", "Phân tích Customer Support", "Phân tích Loyalty Program"],
        "quality_criteria": [
            "Quy trình Lead phải có ít nhất 4 trạng thái rõ ràng",
            "Phải có quy tắc chống trùng lặp cụ thể",
            "Phải có mô hình Scoring với ít nhất 5 tiêu chí",
            "Phải có SLA phản hồi Lead rõ ràng",
            "Phải có ít nhất 3 Business Rules đánh số ID"
        ],
        "estimated_effort": "3-5 ngày phân tích",
        "prompt_role": "Senior CRM Business Analyst với 10+ năm kinh nghiệm triển khai Salesforce, HubSpot, Zoho CRM cho các doanh nghiệp vừa và lớn tại Việt Nam.",
        "prompt_task": "Phân tích toàn diện quy trình Lead Management cho doanh nghiệp, đảm bảo không bỏ sót bất kỳ khía cạnh nào từ thu thập, chấm điểm, phân bổ đến chuyển đổi.",
        "prompt_context": "Bạn đang làm việc với một doanh nghiệp Việt Nam muốn xây dựng hoặc cải thiện hệ thống CRM. Doanh nghiệp có thể chưa có CRM hoặc đang dùng Excel để quản lý Lead.",
        "prompt_rules": [
            "PHẢI hỏi rõ nguồn Lead trước khi bắt đầu phân tích.",
            "PHẢI thiết kế quy tắc chống trùng lặp dữ liệu.",
            "PHẢI có mô hình Lead Scoring với tiêu chí rõ ràng và có thể đo lường.",
            "PHẢI đảm bảo luồng chuyển đổi từ Lead → Account/Contact/Opportunity rõ ràng.",
            "KHÔNG ĐƯỢC bỏ qua luồng xử lý Lead bị Disqualified.",
            "KHÔNG ĐƯỢC thiết kế quá 8 trạng thái Lead (Gây phức tạp cho Sales).",
            "Output PHẢI bao gồm sơ đồ BPMN/Flowchart, bảng cấu trúc dữ liệu, và bảng Scoring."
        ],
        "prompt_example": """**User hỏi:** "Giúp tôi phân tích Lead Management cho công ty bán thiết bị y tế, có 5 sales."

**AI trả lời (Tóm tắt):**
1. Nguồn Lead: Website, Triển lãm y tế, Bệnh viện giới thiệu, Tele-sales
2. Trạng thái: New → Contacted → Demo Scheduled → Proposal Sent → Won/Lost
3. Scoring: Bệnh viện lớn (+40), Phòng khám tư (+20), Đã xem demo (+30), Ngân sách > 1 tỷ (+50)
4. Routing: Round-robin vì 5 sales cùng khu vực
5. Dedup: Trùng SĐT bệnh viện → Alert, Trùng tên bác sĩ → Merge vào Lead cũ
6. Dashboard: Số Lead mới/tuần, Conversion Rate, Lead theo nguồn, Lead aging (quá hạn chưa xử lý)"""
    },
    # ================================================================
    # CRM - Opportunity
    # ================================================================
    {
        "path": "01-Business-Domain/CRM",
        "name": "Phân tích Opportunity",
        "level": "Level 2 - Business Skill",
        "domain": "CRM",
        "tags": ["CRM", "Sales", "Pipeline", "Forecasting"],
        "purpose": "Phân tích toàn diện luồng cơ hội bán hàng (Opportunity/Deal) từ khi Lead chuyển đổi đến khi ký hợp đồng hoặc mất cơ hội, bao gồm các giai đoạn (Stages), tỷ lệ thắng (Win Probability), dự báo doanh thu (Revenue Forecasting) và quy trình phê duyệt báo giá.",
        "when_to_use": "Sử dụng khi:\n- Xây dựng module Sales Pipeline cho hệ thống CRM.\n- Doanh nghiệp cần dự báo doanh thu chính xác hơn.\n- Cần thiết kế luồng phê duyệt báo giá/chiết khấu nhiều cấp.",
        "prerequisites": ["Đã hoàn thành Phân tích Lead Management", "Hiểu quy trình bán hàng B2B/B2C"],
        "inputs_detail": [
            {"name": "Giai đoạn bán hàng (Sales Stages)", "description": "Các bước trong quy trình bán hàng từ lúc có cơ hội đến khi chốt.", "required": True, "example": "Qualification → Needs Analysis → Proposal → Negotiation → Closed Won/Lost"},
            {"name": "Sản phẩm/Dịch vụ", "description": "Danh mục sản phẩm bán kèm giá.", "required": True, "example": "Phần mềm ERP = 500tr, Module WMS = 200tr, Tùy chỉnh = 100tr/ngày"},
            {"name": "Ma trận phê duyệt chiết khấu", "description": "Ai được duyệt chiết khấu bao nhiêu %.", "required": False, "example": "Sales: ≤5%, Manager: ≤15%, Director: ≤30%"}
        ],
        "process_detail": [
            {"step": 1, "title": "Định nghĩa Sales Stages", "description": "Thiết kế các giai đoạn trong Sales Pipeline. Mỗi giai đoạn phải có tiêu chí vào (Entry Criteria) và tỷ lệ thắng tham khảo.", "sub_steps": [
                "Liệt kê tối đa 6-8 Stages (Ít hơn = Sales dễ dùng hơn)",
                "Mỗi Stage phải có Entry Criteria rõ ràng (VD: Đã gửi Proposal → mới được chuyển sang Negotiation)",
                "Gán Probability % cho mỗi Stage (VD: Qualification = 10%, Proposal = 50%, Negotiation = 75%)",
                "Xác định Stage nào bắt buộc (Mandatory) và Stage nào có thể bỏ qua (Optional)"
            ]},
            {"step": 2, "title": "Thiết kế Cấu trúc Opportunity", "description": "Xác định các trường dữ liệu cần thiết trên bản ghi Opportunity.", "sub_steps": [
                "Trường bắt buộc: Tên Opportunity, Account, Amount, Close Date, Stage, Owner",
                "Trường bổ sung: Nguồn (Source), Đối thủ (Competitor), Next Step, Ghi chú",
                "Opportunity Products: Cho phép thêm nhiều sản phẩm vào 1 Opportunity",
                "Lịch sử thay đổi Stage (Stage History) để theo dõi tốc độ di chuyển"
            ]},
            {"step": 3, "title": "Thiết kế luồng Quotation", "description": "Quy trình tạo và phê duyệt báo giá.", "sub_steps": [
                "Tạo Quotation từ Opportunity (Kéo sản phẩm, đơn giá, số lượng)",
                "Áp dụng chiết khấu và kiểm tra ngưỡng phê duyệt",
                "Luồng duyệt: Sales tạo → Manager duyệt → Gửi khách hàng",
                "Cho phép tạo nhiều phiên bản Quotation (v1, v2, v3)"
            ]},
            {"step": 4, "title": "Thiết kế Revenue Forecasting", "description": "Xây dựng cơ chế dự báo doanh thu.", "sub_steps": [
                "Forecast = Tổng(Amount × Probability) của tất cả Opportunity",
                "Chia Forecast theo tháng/quý/năm",
                "Forecast Category: Pipeline, Best Case, Commit, Closed",
                "Dashboard hiển thị Target vs Actual vs Forecast"
            ]},
            {"step": 5, "title": "Xử lý Closed Lost", "description": "Thiết kế quy trình khi mất cơ hội.", "sub_steps": [
                "Bắt buộc nhập Lost Reason (Giá cao, Đối thủ, Không có ngân sách, Timing)",
                "Bắt buộc nhập Competitor nếu lý do là Đối thủ",
                "Tự động tạo Reminder 6 tháng sau để re-engage"
            ]}
        ],
        "outputs_detail": [
            {"name": "Sales Pipeline Design", "format": "Markdown Table + BPMN", "template": "| Stage | Entry Criteria | Probability | Activities |\n|---|---|---|---|\n| Qualification | Lead converted | 10% | Xác nhận nhu cầu, ngân sách |\n| Needs Analysis | Khách xác nhận quan tâm | 25% | Demo, khảo sát chi tiết |\n| Proposal | Đã hiểu rõ scope | 50% | Gửi báo giá |\n| Negotiation | Khách đồng ý về scope | 75% | Thương lượng giá, hợp đồng |\n| Closed Won | Ký hợp đồng | 100% | Bàn giao cho triển khai |\n| Closed Lost | Khách từ chối | 0% | Ghi nhận lý do |"},
            {"name": "Cấu trúc dữ liệu Opportunity", "format": "Markdown Table", "template": "| Trường | Kiểu | Bắt buộc | Mô tả |\n|---|---|---|---|\n| opp_id | INT (PK) | Có | Mã cơ hội |\n| opp_name | VARCHAR(200) | Có | Tên cơ hội |\n| account_id | INT (FK) | Có | Khách hàng |\n| amount | DECIMAL | Có | Giá trị |\n| close_date | DATE | Có | Ngày dự kiến chốt |\n| stage | ENUM | Có | Giai đoạn |\n| probability | INT | Có | % thắng |\n| lost_reason | ENUM | Không | Lý do thua |"}
        ],
        "sub_skills": ["Thiết kế Sales Pipeline", "Thiết kế Quotation Approval", "Thiết kế Revenue Forecasting", "Phân tích Lost Reason"],
        "business_rules": [
            "BR-CRM-OPP-01: Opportunity bắt buộc phải liên kết với Account.",
            "BR-CRM-OPP-02: Khi chuyển sang Closed Lost, phải nhập Lost Reason.",
            "BR-CRM-OPP-03: Chiết khấu > 5% phải qua Manager duyệt, > 15% phải qua Director.",
            "BR-CRM-OPP-04: Close Date không được là ngày trong quá khứ.",
            "BR-CRM-OPP-05: Probability % tự động theo Stage nhưng Sales có thể override."
        ],
        "edge_cases": [
            "Opportunity đã Closed Won nhưng khách hàng hủy hợp đồng → Rollback hay tạo mới?",
            "Một Account có nhiều Opportunity cùng lúc → Hiển thị tổng giá trị ra sao?",
            "Sales nghỉ việc → Opportunity chuyển cho ai?",
            "Opportunity kéo dài > 6 tháng không chuyển Stage → Cảnh báo Stale Deal"
        ],
        "checklist": [
            "Đã định nghĩa đủ Sales Stages với Entry Criteria",
            "Đã gán Probability % cho mỗi Stage",
            "Đã thiết kế luồng phê duyệt chiết khấu (Discount Approval)",
            "Đã bắt buộc nhập Lost Reason khi đóng cơ hội",
            "Đã thiết kế Forecasting Dashboard",
            "Đã có cơ chế cảnh báo Stale Deal (Deal quá lâu không chuyển Stage)",
            "Đã có quy trình re-assign khi Sales nghỉ việc",
            "Đã tích hợp với module Quotation/Contract"
        ],
        "example": "Xem mô tả trong phần Process.",
        "related_skills": ["Phân tích Lead Management", "Thiết kế API Contract", "Write BRD"],
        "quality_criteria": ["Sales Pipeline phải có 5-8 Stages", "Mỗi Stage phải có Entry Criteria", "Phải có Lost Reason bắt buộc", "Phải có Forecasting logic"],
        "estimated_effort": "3-5 ngày",
        "prompt_role": "Senior CRM Business Analyst chuyên về Sales Process Optimization.",
        "prompt_task": "Phân tích và thiết kế luồng Opportunity Management hoàn chỉnh.",
        "prompt_context": "Doanh nghiệp cần xây dựng hệ thống quản lý Pipeline bán hàng để theo dõi cơ hội và dự báo doanh thu.",
        "prompt_rules": [
            "PHẢI có ít nhất 5 Sales Stages với Probability % rõ ràng.",
            "PHẢI có Lost Reason bắt buộc khi Closed Lost.",
            "PHẢI có luồng phê duyệt chiết khấu nhiều cấp.",
            "PHẢI có Revenue Forecasting logic.",
            "Output PHẢI bao gồm Sales Pipeline Table, Data Model, và BPMN."
        ],
        "prompt_example": ""
    },
    # ================================================================
    # CRM - Customer Support
    # ================================================================
    {
        "path": "01-Business-Domain/CRM",
        "name": "Phân tích Customer Support",
        "level": "Level 2 - Business Skill",
        "domain": "CRM",
        "tags": ["CRM", "Support", "Ticket", "SLA", "Helpdesk"],
        "purpose": "Phân tích toàn diện quy trình tiếp nhận và xử lý yêu cầu hỗ trợ khách hàng (Ticket Management), bao gồm phân loại ticket, escalation tự động, theo dõi SLA, đo lường CSAT/NPS và thiết kế Knowledge Base.",
        "when_to_use": "Sử dụng khi:\n- Xây dựng module Customer Support / Helpdesk cho CRM.\n- Doanh nghiệp cần quản lý yêu cầu hỗ trợ từ nhiều kênh (Email, Chat, Call, Social Media).\n- Cần thiết kế SLA tự động và cảnh báo vi phạm.",
        "prerequisites": ["Hiểu các kênh liên hệ khách hàng", "Biết SLA là gì"],
        "inputs_detail": [
            {"name": "Kênh tiếp nhận (Support Channels)", "description": "Tất cả các kênh mà khách hàng có thể gửi yêu cầu hỗ trợ.", "required": True, "example": "Email, Hotline, Live Chat, Facebook Messenger, Zalo, Cổng tự phục vụ (Portal)"},
            {"name": "Hợp đồng SLA (Service Level Agreement)", "description": "Cam kết thời gian phản hồi và xử lý cho từng loại yêu cầu.", "required": True, "example": "Critical: Phản hồi 1h / Giải quyết 4h. High: 4h / 8h. Medium: 8h / 24h. Low: 24h / 72h."},
            {"name": "Cấu trúc đội hỗ trợ (Support Tiers)", "description": "Phân cấp đội ngũ xử lý theo mức độ chuyên môn.", "required": True, "example": "Tier 1: Agent tổng đài (FAQ). Tier 2: Chuyên viên kỹ thuật. Tier 3: Dev/Vendor."}
        ],
        "process_detail": [
            {"step": 1, "title": "Tiếp nhận & Tạo Ticket", "description": "Thiết kế cách hệ thống tiếp nhận yêu cầu từ mọi kênh và tạo Ticket tự động.", "sub_steps": [
                "Email gửi vào support@company.com → Tự động tạo Ticket",
                "Chat/Call → Agent tạo Ticket thủ công hoặc hệ thống tự động",
                "Portal → Khách hàng tự tạo Ticket và theo dõi trạng thái",
                "Social Media → Tích hợp chuyển thành Ticket"
            ]},
            {"step": 2, "title": "Phân loại & Ưu tiên (Categorization & Priority)", "description": "Thiết kế quy tắc phân loại ticket tự động và thủ công.", "sub_steps": [
                "Phân loại theo Type: Bug, Feature Request, Question, Complaint",
                "Phân loại theo Module: CRM, WMS, MES, Kế toán",
                "Xác định Priority: Critical / High / Medium / Low",
                "Auto-priority: Keyword 'khẩn cấp', 'không hoạt động' → Tự động đặt Critical"
            ]},
            {"step": 3, "title": "Routing & Assignment", "description": "Phân bổ ticket cho đúng người xử lý.", "sub_steps": [
                "Round-robin trong Tier 1",
                "Skill-based routing: Ticket về WMS → Gán cho agent chuyên WMS",
                "VIP routing: Khách hàng hạng Gold/Platinum → Ưu tiên xử lý trước"
            ]},
            {"step": 4, "title": "Xử lý & Escalation", "description": "Quy trình xử lý và leo thang ticket.", "sub_steps": [
                "Tier 1 xử lý FAQ, hướng dẫn cơ bản",
                "Nếu không giải quyết được trong SLA → Escalate lên Tier 2",
                "Tier 2 xử lý vấn đề kỹ thuật, cấu hình",
                "Tier 3 xử lý bug, lỗi hệ thống, cần sửa code",
                "Auto-escalation: Ticket quá SLA tự động leo thang + gửi email cảnh báo cho Manager"
            ]},
            {"step": 5, "title": "Đóng Ticket & Đo lường", "description": "Quy trình đóng ticket và thu thập phản hồi.", "sub_steps": [
                "Agent đóng ticket → Gửi khảo sát CSAT cho khách hàng",
                "Khách hàng xác nhận hoặc mở lại ticket nếu chưa hài lòng",
                "Tự động đóng ticket sau 7 ngày nếu khách không phản hồi",
                "Đo lường: First Response Time, Resolution Time, CSAT Score, Ticket Volume"
            ]}
        ],
        "outputs_detail": [
            {"name": "Quy trình quản lý Ticket (BPMN)", "format": "Mermaid Flowchart", "template": ""},
            {"name": "Ma trận SLA", "format": "Markdown Table", "template": "| Priority | First Response | Resolution | Escalation |\n|---|---|---|---|\n| Critical | 1 giờ | 4 giờ | Auto → Tier 2 sau 2h |\n| High | 4 giờ | 8 giờ | Auto → Tier 2 sau 6h |\n| Medium | 8 giờ | 24 giờ | Alert Manager sau 20h |\n| Low | 24 giờ | 72 giờ | Không auto-escalate |"},
            {"name": "Ma trận phân quyền (Tier Matrix)", "format": "Markdown Table", "template": "| Loại vấn đề | Tier 1 | Tier 2 | Tier 3 |\n|---|---|---|---|\n| Hướng dẫn sử dụng | ✅ | | |\n| Reset mật khẩu | ✅ | | |\n| Lỗi cấu hình | | ✅ | |\n| Bug phần mềm | | | ✅ |\n| Yêu cầu tùy chỉnh | | | ✅ |"}
        ],
        "sub_skills": ["Thiết kế SLA Matrix", "Thiết kế Escalation Rules", "Thiết kế Knowledge Base", "Thiết kế CSAT Survey"],
        "business_rules": [
            "BR-SUP-01: Mọi yêu cầu từ khách hàng phải tạo Ticket, không xử lý ngoài hệ thống.",
            "BR-SUP-02: Ticket Critical phải được phản hồi trong vòng 1 giờ làm việc.",
            "BR-SUP-03: Ticket quá SLA phải tự động escalate và gửi cảnh báo.",
            "BR-SUP-04: Không được phép đóng Ticket nếu chưa có phản hồi từ khách hàng.",
            "BR-SUP-05: Mỗi Ticket đóng phải gửi khảo sát CSAT."
        ],
        "edge_cases": [
            "Khách hàng gửi cùng 1 vấn đề qua Email + Chat → Tạo 1 hay 2 Ticket? (Merge)",
            "Ticket thuộc về nhiều module → Assign cho ai?",
            "Agent nghỉ phép → Ticket đang xử lý dở chuyển cho ai?",
            "Khách hàng spam Ticket → Cần rate limiting"
        ],
        "checklist": [
            "Đã xác định tất cả kênh tiếp nhận (Omnichannel)",
            "Đã thiết kế ma trận SLA với 4 mức Priority",
            "Đã thiết kế luồng Escalation tự động",
            "Đã thiết kế Tier 1/2/3 với phân quyền rõ ràng",
            "Đã có cơ chế Merge Ticket trùng lặp",
            "Đã thiết kế CSAT Survey sau khi đóng Ticket",
            "Đã có Dashboard theo dõi (Ticket Volume, SLA Compliance, CSAT)",
            "Đã thiết kế Knowledge Base cho self-service"
        ],
        "example": "Xem Process section.",
        "related_skills": ["Phân tích Lead Management", "Phân tích Loyalty Program"],
        "quality_criteria": ["Phải có SLA Matrix rõ ràng", "Phải có Escalation rules", "Phải có CSAT measurement"],
        "estimated_effort": "3-5 ngày",
        "prompt_role": "Senior Customer Support Analyst chuyên thiết kế hệ thống Helpdesk/Ticketing.",
        "prompt_task": "Phân tích và thiết kế quy trình Customer Support toàn diện.",
        "prompt_context": "Doanh nghiệp cần hệ thống quản lý yêu cầu hỗ trợ từ khách hàng đa kênh.",
        "prompt_rules": [
            "PHẢI có SLA Matrix cho 4 mức Priority.",
            "PHẢI có luồng Escalation tự động khi quá SLA.",
            "PHẢI có phân cấp Tier 1/2/3.",
            "PHẢI có CSAT Survey.",
            "KHÔNG ĐƯỢC để Agent xử lý ngoài hệ thống."
        ],
        "prompt_example": ""
    },
    # ================================================================
    # CRM - Loyalty Program
    # ================================================================
    {
        "path": "01-Business-Domain/CRM",
        "name": "Phân tích Loyalty Program",
        "level": "Level 2 - Business Skill",
        "domain": "CRM",
        "tags": ["CRM", "Loyalty", "Points", "Membership"],
        "purpose": "Phân tích hệ thống điểm thưởng và khách hàng thân thiết (Loyalty Program), bao gồm cơ chế tích điểm, cấu trúc hạng thành viên (Tier), quy đổi điểm, xử lý gian lận và tích hợp với POS/E-commerce.",
        "when_to_use": "Sử dụng khi doanh nghiệp bán lẻ, F&B, hoặc dịch vụ muốn xây dựng chương trình khách hàng thân thiết.",
        "prerequisites": ["Hiểu mô hình kinh doanh B2C", "Biết quy trình bán hàng"],
        "inputs_detail": [
            {"name": "Chính sách tích điểm", "description": "Quy tắc quy đổi chi tiêu thành điểm thưởng.", "required": True, "example": "Chi 10.000 VNĐ = 1 điểm. Mua ngày sinh nhật = x2 điểm."},
            {"name": "Cấu trúc hạng thành viên (Tier)", "description": "Các mức thành viên và điều kiện thăng/giáng hạng.", "required": True, "example": "Bạc (0-499 điểm), Vàng (500-1499), Kim Cương (1500+)"},
            {"name": "Danh mục quà đổi (Reward Catalog)", "description": "Những gì khách hàng có thể dùng điểm để đổi.", "required": True, "example": "Voucher giảm 50k = 100 điểm, Sản phẩm miễn phí = 500 điểm"}
        ],
        "process_detail": [
            {"step": 1, "title": "Thiết kế cơ chế Tích điểm (Earn)", "description": "Xây dựng quy tắc quy đổi chi tiêu thành điểm.", "sub_steps": [
                "Tỷ lệ quy đổi cơ bản (Base rate)",
                "Bonus multiplier theo hạng thành viên (VD: Kim Cương x3)",
                "Bonus theo sự kiện (Sinh nhật, Lễ tết x2)",
                "Bonus theo sản phẩm/danh mục (Hàng mới x1.5)",
                "Điểm có thời hạn hay vĩnh viễn?"
            ]},
            {"step": 2, "title": "Thiết kế cấu trúc Hạng (Tier)", "description": "Định nghĩa các hạng thành viên.", "sub_steps": [
                "Điều kiện lên hạng (Tổng chi tiêu / Tổng điểm trong 12 tháng)",
                "Chu kỳ đánh giá hạng (Hàng năm / Hàng quý)",
                "Quyền lợi mỗi hạng (Chiết khấu, Quà tặng, Ưu tiên)",
                "Quy tắc giáng hạng (Downgrade)"
            ]},
            {"step": 3, "title": "Thiết kế cơ chế Đổi điểm (Redeem)", "description": "Quy trình sử dụng điểm.", "sub_steps": [
                "Đổi điểm lấy Voucher giảm giá",
                "Đổi điểm lấy sản phẩm miễn phí",
                "Thanh toán bằng điểm (Partial/Full)",
                "Tặng điểm cho người thân"
            ]},
            {"step": 4, "title": "Xử lý hoàn trả & Gian lận (Return & Fraud)", "description": "Quy tắc trừ điểm khi hoàn trả và phát hiện gian lận.", "sub_steps": [
                "Hoàn hàng → Trừ lại số điểm tương ứng đã cộng",
                "Phát hiện giao dịch bất thường (Mua rồi trả ngay để lấy điểm)",
                "Giới hạn số lần đổi điểm/ngày",
                "Block tài khoản nghi ngờ gian lận"
            ]}
        ],
        "outputs_detail": [
            {"name": "Bảng cấu trúc Tier", "format": "Markdown Table", "template": "| Hạng | Điều kiện | Chiết khấu | Multiplier | Quyền lợi đặc biệt |\n|---|---|---|---|---|\n| Bạc | 0 - 499 điểm | 0% | x1 | Tích điểm cơ bản |\n| Vàng | 500 - 1499 | 5% | x1.5 | Quà sinh nhật |\n| Kim Cương | 1500+ | 10% | x2 | Ưu tiên hỗ trợ, Sự kiện VIP |"},
            {"name": "Luật Tích/Trừ điểm", "format": "Markdown Table", "template": "| Sự kiện | Điểm | Ghi chú |\n|---|---|---|\n| Chi 10.000 VNĐ | +1 | Base rate |\n| Mua ngày sinh nhật | x2 | Bonus |\n| Hoàn hàng | -N | Trừ lại đúng số điểm đã cộng |\n| Điểm quá hạn 12 tháng | -All | Hết hạn |"}
        ],
        "sub_skills": ["Thiết kế Point Earning Rules", "Thiết kế Tier Structure", "Thiết kế Redemption Flow", "Anti-fraud Logic"],
        "business_rules": [
            "BR-LOY-01: Điểm chỉ được cộng sau khi giao dịch hoàn tất (không tính đơn hủy).",
            "BR-LOY-02: Hoàn hàng bắt buộc phải trừ lại điểm đã cộng cho giao dịch đó.",
            "BR-LOY-03: Điểm thưởng hết hạn sau 12 tháng nếu không sử dụng.",
            "BR-LOY-04: Tài khoản bị nghi ngờ gian lận sẽ bị đóng băng điểm.",
            "BR-LOY-05: Điểm không được chuyển nhượng giữa các tài khoản (trừ gói Gia đình)."
        ],
        "edge_cases": [
            "Khách hàng hoàn trả nhưng đã dùng điểm đó để đổi quà rồi → Xử lý sao?",
            "Hệ thống lỗi cộng nhầm điểm hàng loạt → Rollback procedure?",
            "Khách tạo nhiều tài khoản để lấy ưu đãi thành viên mới → Anti-fraud?"
        ],
        "checklist": [
            "Đã thiết kế tỷ lệ quy đổi (Earn rate) rõ ràng",
            "Đã thiết kế cấu trúc Tier với điều kiện lên/xuống hạng",
            "Đã có cơ chế đổi điểm (Redeem) đa dạng",
            "Đã xử lý trường hợp hoàn hàng (Trừ điểm)",
            "Đã có cơ chế chống gian lận (Anti-fraud)",
            "Đã có thời hạn điểm (Expiration)",
            "Đã tích hợp với POS/E-commerce"
        ],
        "example": "Xem Process section.",
        "related_skills": ["Phân tích Lead Management", "Phân tích Bán hàng tại quầy (POS)"],
        "quality_criteria": ["Phải có Tier Structure", "Phải xử lý Return refund points", "Phải có anti-fraud"],
        "estimated_effort": "3-4 ngày",
        "prompt_role": "Senior Loyalty Program Analyst.",
        "prompt_task": "Thiết kế chương trình khách hàng thân thiết.",
        "prompt_context": "Doanh nghiệp bán lẻ/F&B cần hệ thống tích điểm và thành viên.",
        "prompt_rules": [
            "PHẢI có cơ chế trừ điểm khi hoàn trả.",
            "PHẢI có thời hạn điểm (Expiration).",
            "PHẢI có cơ chế phát hiện gian lận.",
            "PHẢI có tối thiểu 3 hạng thành viên."
        ],
        "prompt_example": ""
    }
]

if __name__ == "__main__":
    print("=== Expanding Business Domain: CRM Skills ===")
    run(skills)
