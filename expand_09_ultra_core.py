import sys
sys.path.insert(0, r"e:\BA Skill Library")
from skill_generator import run

skills = [
    # ================================================================
    # Ultra Deep: Use Case Analysis
    # ================================================================
    {
        "path": "02-Requirement/Use Case",
        "name": "Phân tích Use Case",
        "level": "Level 2 - Business Skill",
        "domain": "Requirement",
        "tags": ["Requirement", "Use Case", "UML", "Flow", "Alternate Flow", "Exception", "Micro-tasking"],
        "purpose": "Đặc tả siêu chi tiết sự tương tác giữa Người dùng (Actor) và Hệ thống (System) thông qua Use Case Specification. Kỹ năng này cung cấp sức mạnh để phân rã luồng chính (Basic Flow), luồng rẽ nhánh hợp lệ (Alternate Flow), luồng lỗi (Exception Flow). Đặc biệt hỗ trợ Micro-tasking (bóc tách 1 luồng nhỏ).",
        "when_to_use": "Sử dụng khi cần đặc tả yêu cầu chức năng một cách chi tiết theo góc nhìn tương tác người-máy. Rất hiệu quả khi User yêu cầu AI 'chỉ làm 1 phần nhỏ' (Micro-tasking).",
        "prerequisites": ["Đã xác định được các Actor trong hệ thống"],
        "inputs_detail": [
            {"name": "Mô tả tính năng", "description": "Mô tả ngắn gọn về tính năng cần phân tích.", "required": True, "example": "Tính năng Đăng nhập bằng Số điện thoại."},
            {"name": "Lệnh Micro-tasking (Tùy chọn)", "description": "Lệnh yêu cầu AI chỉ thực thi 1 phần của Use Case.", "required": False, "example": "Chỉ viết Exception Flows cho luồng gửi OTP."}
        ],
        "process_detail": [
            {"step": 1, "title": "Xác định Use Case Profile", "description": "Thông tin cơ bản của Use Case.", "sub_steps": [
                "Actor (Ai thực hiện?)",
                "Pre-conditions (Điều kiện tiên quyết trước khi bắt đầu? VD: Đã mở app, chưa login)",
                "Post-conditions (Trạng thái hệ thống sau khi UC thành công? VD: Bảng Session tạo record mới)",
                "Includes / Extends (Có gọi Use Case khác không? VD: Include UC_Send_SMS)"
            ]},
            {"step": 2, "title": "Thiết kế Basic Flow (Luồng chính/Happy Path)", "description": "Kịch bản mọi thứ diễn ra suôn sẻ.", "sub_steps": [
                "Đánh số thứ tự từng bước: 1, 2, 3...",
                "Bắt đầu bằng Actor action: 'User nhập SĐT và bấm Gửi OTP'",
                "Theo sau là System response: 'Hệ thống validate SĐT và gửi OTP qua SMS'"
            ]},
            {"step": 3, "title": "Thiết kế Alternate Flows (Luồng rẽ nhánh hợp lệ)", "description": "Luồng đi đường vòng nhưng vẫn đạt kết quả.", "sub_steps": [
                "Chỉ định rõ nhánh này tách ra từ bước nào của Basic Flow (VD: Tại bước 2, User chọn Đăng nhập bằng Mật khẩu thay vì OTP)",
                "Mô tả các bước của luồng này",
                "Quay lại bước nào của Basic Flow hoặc Kết thúc?"
            ]},
            {"step": 4, "title": "Thiết kế Exception Flows (Luồng lỗi/ngoại lệ)", "description": "Luồng gặp lỗi và không đạt kết quả.", "sub_steps": [
                "Tách ra từ bước nào? (VD: Tại bước 3, User nhập sai OTP)",
                "Hệ thống xử lý thế nào? (VD: Hiển thị lỗi 'OTP không đúng, còn 2 lần thử')",
                "Dừng Use Case hay cho User thử lại?"
            ]},
            {"step": 5, "title": "Xử lý Micro-tasking (Theo yêu cầu)", "description": "Nếu người dùng có yêu cầu cụ thể (chỉ xuất 1 luồng).", "sub_steps": [
                "Nếu User bảo 'Chỉ viết Alternate Flow' → Bỏ qua Basic/Exception Flow, chỉ sinh ra Alternate.",
                "Nếu User bảo 'Tìm lỗ hổng trong luồng này' → Áp dụng Error Guessing để tìm các ngoại lệ bị sót."
            ]}
        ],
        "outputs_detail": [
            {"name": "Use Case Specification", "format": "Markdown Table & Lists", "template": "### UC-001: Đăng nhập bằng SĐT\n\n**1. Profile**\n- **Actor:** Khách hàng\n- **Pre-condition:** Đã tải App.\n- **Post-condition:** Đăng nhập thành công, tạo Token.\n\n**2. Basic Flow**\n1. User nhập SĐT và bấm 'Lấy OTP'.\n2. System kiểm tra SĐT hợp lệ và gọi `UC_Send_SMS`.\n3. System chuyển sang màn hình nhập OTP (đếm ngược 60s).\n4. User nhập 6 số OTP.\n5. System xác thực OTP đúng, sinh JWT Token.\n6. System chuyển hướng vào Home Screen.\n\n**3. Alternate Flows**\n*3.1. Đăng nhập bằng Mật khẩu (Từ bước 1)*\n- 1a1. User click 'Dùng Mật khẩu'.\n- 1a2. System chuyển sang màn hình nhập Mật khẩu.\n- 1a3. User nhập Mật khẩu và submit. (Quay lại bước 5).\n\n**4. Exception Flows**\n*4.1. SĐT không tồn tại (Từ bước 2)*\n- 2e1. System phát hiện SĐT chưa đăng ký.\n- 2e2. System báo lỗi 'Số điện thoại chưa đăng ký'. Use Case kết thúc."}
        ],
        "sub_skills": ["Include/Extend Definition", "Micro-tasking Flow Extract", "Exception Handling Design"],
        "business_rules": [
            "BR-UC-01: Mọi bước trong Basic Flow phải rõ ràng Chủ ngữ (User làm gì / System phản hồi gì).",
            "BR-UC-02: Alternate/Exception Flow PHẢI trỏ rõ ràng nó tách ra từ bước nào của Basic Flow (VD: 3a, 2e).",
            "BR-UC-03: Exception Flow phải ghi rõ là Kết thúc Use Case hay Quay lại bước nào."
        ],
        "edge_cases": [
            "Tương tác với hệ thống ngoài (3rd Party) bị lỗi → Đưa vào Exception Flow",
            "Timeout (Quá thời gian nhập OTP) → Đưa vào Exception Flow"
        ],
        "checklist": [
            "Có Basic Flow rõ ràng (Actor-System ping pong)?",
            "Đã bóc tách Alternate Flows chưa?",
            "Đã xử lý đủ các Exception Flows (Validation, Timeout, Lỗi mạng)?",
            "Các luồng phụ có chỉ định rõ điểm bắt đầu từ Basic Flow không?",
            "Có đáp ứng đúng lệnh Micro-tasking của User không?"
        ],
        "example": "Xem Use Case Specification template trong phần Outputs.",
        "related_skills": ["Viết Test Case (Ultra)", "Write SRS (Ultra)"],
        "quality_criteria": ["Rõ ràng Actor-System", "Có Exception Flows", "Đánh số thứ tự chuẩn (1a1, 2e1)"],
        "estimated_effort": "0.5 ngày / Use Case",
        "prompt_role": "Senior Systems Analyst & UML Expert. Am hiểu sâu sắc về Use Case Specification và Exception Handling.",
        "prompt_task": "Phân tích Use Case chi tiết, tập trung đặc tả luồng rẽ nhánh và ngoại lệ. Thực hiện Micro-tasking nếu User yêu cầu.",
        "prompt_context": "Dự án yêu cầu đặc tả cực kỳ chặt chẽ về mọi tình huống tương tác để tránh Bug trong quá trình Dev.",
        "prompt_rules": [
            "PHẢI đánh số từng bước trong Basic Flow.",
            "Alternate Flow và Exception Flow PHẢI tham chiếu đến số thứ tự của bước trong Basic Flow (VD: 2a1, 3e1).",
            "PHẢI sử dụng mẫu cấu trúc: [Chủ thể] + [Hành động] (VD: System gọi API...).",
            "NẾU User đưa ra lệnh Micro-tasking (VD: 'Chỉ phân tích luồng lỗi'): PHẢI TẬP TRUNG 100% sinh ra chi tiết luồng lỗi, KHÔNG sinh thừa thông tin không được hỏi.",
            "Luôn tư duy về các Exception ngầm (Mất mạng, Quá hạn, Spam click) để bổ sung vào Exception Flow."
        ],
        "prompt_example": ""
    },
    
    # ================================================================
    # Ultra Deep: Write SRS
    # ================================================================
    {
        "path": "02-Requirement/SRS",
        "name": "Write SRS (Ultra)",
        "level": "Level 1 - Basic Skill",
        "domain": "Requirement",
        "tags": ["Requirement", "SRS", "FURPS+", "Micro-tasking", "Functional", "Non-Functional"],
        "purpose": "Soạn thảo SRS phiên bản siêu chi tiết. Cung cấp bộ công cụ mạnh mẽ để AI có thể làm Micro-tasking (Ví dụ: Chỉ sinh ra bộ Non-Functional Requirements theo chuẩn FURPS+, hoặc chỉ thiết kế Traceability Matrix) thay vì sinh ra 1 tài liệu quá dài.",
        "when_to_use": "Khi cần viết đặc tả kỹ thuật, HOẶC khi cần AI hỗ trợ bổ sung một phần bị thiếu (VD: NFR) cho một tài liệu đã có.",
        "prerequisites": ["Đã có BRD hoặc User Stories"],
        "inputs_detail": [
            {"name": "Tính năng / Module", "description": "Phạm vi cần viết SRS.", "required": True, "example": "Module Quản lý Tồn kho."},
            {"name": "Lệnh Micro-tasking (Tùy chọn)", "description": "Lệnh yêu cầu AI chỉ viết 1 phần của SRS.", "required": False, "example": "Chỉ liệt kê NFR theo mô hình FURPS+ cho module này."}
        ],
        "process_detail": [
            {"step": 1, "title": "Xử lý Micro-tasking (Quan trọng nhất)", "description": "Xác định AI cần sinh toàn bộ SRS hay chỉ một phần.", "sub_steps": [
                "Nếu User yêu cầu 'Chỉ NFR' → Chuyển thẳng sang Bước 3.",
                "Nếu User yêu cầu 'Chỉ Data Dictionary' → Chuyển thẳng sang Bước 4.",
                "Nếu không có yêu cầu đặc biệt → Sinh cấu trúc SRS tổng quan."
            ]},
            {"step": 2, "title": "Đặc tả Functional (FR)", "description": "Chi tiết chức năng hệ thống.", "sub_steps": [
                "Mỗi FR có Input, Processing logic, Output, Error Handling, Validation Rules",
                "Áp dụng Business Rules cụ thể thay vì chung chung"
            ]},
            {"step": 3, "title": "Đặc tả Non-Functional (NFR) chuẩn FURPS+", "description": "Phân tích NFR sâu theo chuẩn ngành.", "sub_steps": [
                "F (Functionality): Security, Logging, Auditing",
                "U (Usability): UI standards, Accessibility, Localization",
                "R (Reliability): Availability (99.9%), Fault tolerance, Recoverability",
                "P (Performance): Response time (<2s), Throughput (1000 TPS), Capacity",
                "S (Supportability): Maintainability, Configurable params",
                "+ (Plus): Ràng buộc phần cứng, pháp lý (GDPR)"
            ]},
            {"step": 4, "title": "Thiết lập Traceability Matrix", "description": "Liên kết Requirement.", "sub_steps": [
                "Map Business Requirement (BR) → Functional Req (FR) → Test Case (TC)"
            ]}
        ],
        "outputs_detail": [
            {"name": "FURPS+ NFR Report (Dành cho Micro-tasking)", "format": "Markdown Table", "template": "### NFR Report (FURPS+)\n\n| Nhóm (FURPS) | ID | Mô tả chi tiết | Phương pháp đo lường (Measurable) |\n|---|---|---|---|\n| **R**eliability | NFR-01 | Hệ thống phải tự động failover sang máy chủ dự phòng trong < 30s khi Crash. | Giả lập crash, đếm thời gian downtime. |\n| **P**erformance | NFR-02 | Thời gian tải trang Dashboard < 2 giây với 100,000 bản ghi dữ liệu. | Dùng JMeter test load 1000 CCU. |\n| **S**upportability| NFR-03 | Mọi tham số cấu hình (Thuế, Phí ship) phải thay đổi được trên giao diện Admin không cần restart code. | Test thay đổi giá trị và xem hiệu ứng tức thời. |"}
        ],
        "sub_skills": ["FURPS+ NFR Design", "Traceability Mapping", "Micro-tasking Document Section"],
        "business_rules": [
            "BR-SRS-U1: NFR PHẢI có phương pháp đo lường (Measurable). Không dùng từ 'Nhanh', 'Bảo mật cao'.",
            "BR-SRS-U2: Nếu có lệnh Micro-tasking, AI PHẢI loại bỏ các phần không liên quan để tránh loãng thông tin."
        ],
        "edge_cases": [
            "Hệ thống yêu cầu pháp lý đặc biệt (Health data, Financial data) → Tập trung cực sâu vào Security (F) và Plus (+)."
        ],
        "checklist": [
            "Nếu sinh NFR, đã đủ 5 khía cạnh FURPS+ chưa?",
            "Các chỉ số Performance có định lượng (giây, TPS, %) không?",
            "Đã thực hiện đúng lệnh Micro-tasking của User chưa?"
        ],
        "example": "Xem FURPS+ NFR Report trong Outputs.",
        "related_skills": ["Phân tích Use Case", "Thiết kế API Contract"],
        "quality_criteria": ["FURPS+ Coverage", "Định lượng Measurable", "Đáp ứng chính xác Micro-task"],
        "estimated_effort": "0.5-2 ngày",
        "prompt_role": "Senior Systems Engineer / Technical BA. Chuyên gia về Software Architecture và FURPS+ framework.",
        "prompt_task": "Soạn thảo SRS hoặc thực thi Micro-tasking để sinh ra các thành phần kỹ thuật chuyên sâu của SRS.",
        "prompt_context": "User cần các tài liệu đặc tả hệ thống có tính định lượng cao, đặc biệt là các yêu cầu phi chức năng (NFR).",
        "prompt_rules": [
            "LẮNG NGHE LỆNH MICRO-TASKING: Nếu User chỉ yêu cầu NFR, KHÔNG sinh FR, KHÔNG sinh Introduction. Trực tiếp sinh bảng FURPS+.",
            "NFR PHẢI dùng framework FURPS+.",
            "Mọi NFR PHẢI có cột 'Phương pháp đo lường' (Measurable metrics).",
            "KHÔNG sử dụng các tính từ định tính như: nhanh, tốt, dễ dùng, an toàn. PHẢI định lượng: < 2s, 3 clicks, 99.9% uptime, mã hóa RSA-2048."
        ],
        "prompt_example": ""
    },
    
    # ================================================================
    # Ultra Deep: Viết Test Case
    # ================================================================
    {
        "path": "06-Testing/Test Case",
        "name": "Viết Test Case (Ultra)",
        "level": "Level 2 - Business Skill",
        "domain": "Testing",
        "tags": ["Testing", "QA", "Boundary Value", "Equivalence Partitioning", "Micro-tasking", "Decision Table"],
        "purpose": "Viết Test Case ứng dụng các kỹ thuật kiểm thử phần mềm nâng cao: Phân tích giá trị biên (BVA), Phân vùng tương đương (EP), và Bảng quyết định (Decision Table). Hỗ trợ Micro-tasking cực mạnh để AI đóng vai trò như một Senior QA Engineer chuyên 'bắt bug'.",
        "when_to_use": "Sử dụng để tạo bộ test case phủ 100% case lỗi, HOẶC dùng Micro-tasking để nhờ AI phân tích các giá trị biên của một trường dữ liệu phức tạp.",
        "prerequisites": ["Đã có Functional Requirement hoặc Use Case rõ ràng"],
        "inputs_detail": [
            {"name": "Rule nghiệp vụ / Feature", "description": "Tính năng cần test.", "required": True, "example": "Ô nhập Tuổi yêu cầu >= 18 và <= 60."},
            {"name": "Lệnh Micro-tasking", "description": "Yêu cầu kỹ thuật test cụ thể.", "required": False, "example": "Chỉ sinh Test Case phân tích giá trị biên (Boundary Value) cho trường Tuổi."}
        ],
        "process_detail": [
            {"step": 1, "title": "Xử lý Micro-tasking", "description": "Xác định kỹ thuật test cần áp dụng.", "sub_steps": [
                "Nếu User yêu cầu 'Boundary Value' → Tập trung vào các mốc Min-1, Min, Min+1, Max-1, Max, Max+1.",
                "Nếu User yêu cầu 'Decision Table' → Vẽ bảng kết hợp các rule (Ví dụ: Trạng thái = Active AND Hạng = VIP → Kết quả).",
                "Nếu yêu cầu 'Equivalence' → Chia vùng dữ liệu hợp lệ (Valid) và vùng lỗi (Invalid)."
            ]},
            {"step": 2, "title": "Equivalence Partitioning (Phân vùng tương đương)", "description": "Tìm vùng dữ liệu để test.", "sub_steps": [
                "Rule: Tuổi 18-60. Vùng hợp lệ (Valid): 18-60 (Chọn đại 1 số VD: 30).",
                "Vùng không hợp lệ (Invalid 1): < 18 (Chọn đại: 10).",
                "Vùng không hợp lệ (Invalid 2): > 60 (Chọn đại: 70)."
            ]},
            {"step": 3, "title": "Boundary Value Analysis (Phân tích giá trị biên)", "description": "Tìm lỗi ở viền giới hạn.", "sub_steps": [
                "Rule: Tuổi 18-60.",
                "Biên dưới: 17 (Min-1 -> Lỗi), 18 (Min -> Pass), 19 (Min+1 -> Pass).",
                "Biên trên: 59 (Max-1 -> Pass), 60 (Max -> Pass), 61 (Max+1 -> Lỗi)."
            ]},
            {"step": 4, "title": "Error Guessing & Edge Cases", "description": "Đoán lỗi dựa trên kinh nghiệm.", "sub_steps": [
                "Dữ liệu null/empty.",
                "Dữ liệu sai định dạng (Nhập chữ vào ô số, nhập số âm).",
                "Dữ liệu chứa ký tự đặc biệt, XSS, SQL Injection (nếu field text)."
            ]},
            {"step": 5, "title": "Viết Test Case chi tiết", "description": "Đóng gói thành format Test Case chuẩn.", "sub_steps": [
                "Test Case ID, Title, Test Data, Test Steps, Expected Result, Status"
            ]}
        ],
        "outputs_detail": [
            {"name": "Boundary Value Test Cases (Micro-tasking)", "format": "Markdown Table", "template": "### Kỹ thuật áp dụng: Phân tích giá trị biên (BVA) cho Rule [Tuổi 18-60]\n\n| TC ID | Kịch bản biên | Test Data | Expected Result |\n|---|---|---|---|\n| TC-BVA-01 | Min - 1 | Tuổi = 17 | Báo lỗi 'Phải >= 18 tuổi' |\n| TC-BVA-02 | Min | Tuổi = 18 | Thành công |\n| TC-BVA-03 | Min + 1 | Tuổi = 19 | Thành công |\n| TC-BVA-04 | Max - 1 | Tuổi = 59 | Thành công |\n| TC-BVA-05 | Max | Tuổi = 60 | Thành công |\n| TC-BVA-06 | Max + 1 | Tuổi = 61 | Báo lỗi 'Phải <= 60 tuổi' |"},
            {"name": "Decision Table (Micro-tasking)", "format": "Markdown Table", "template": "### Kỹ thuật áp dụng: Decision Table cho Giảm giá\n\n| Condition / Rule | Rule 1 | Rule 2 | Rule 3 | Rule 4 |\n|---|---|---|---|---|\n| Là thẻ VIP? | Yes | Yes | No | No |\n| Đơn > 5 triệu? | Yes | No | Yes | No |\n| **Action (Giảm giá)** | **20%** | **10%** | **5%** | **0%** |"}
        ],
        "sub_skills": ["Boundary Value Analysis", "Equivalence Partitioning", "Decision Table Testing"],
        "business_rules": [
            "BR-QA-U1: Nếu có khoảng giá trị (Range), PHẢI sinh ra tối thiểu 6 Test Cases cho phần Boundary (Min-1, Min, Min+1, Max-1, Max, Max+1).",
            "BR-QA-U2: Nếu có logic kết hợp nhiều điều kiện AND/OR, PHẢI sinh ra Decision Table."
        ],
        "edge_cases": [
            "Trường dữ liệu là Date/Time → Min là Yesterday, Max là Tomorrow hoặc End of Year."
        ],
        "checklist": [
            "Đã thực hiện đúng kỹ thuật Micro-tasking User yêu cầu chưa?",
            "BVA đã đủ 6 điểm cận biên chưa?",
            "Equivalence đã có cả vùng Valid và Invalid chưa?",
            "Decision Table đã cover đủ các tổ hợp Yes/No chưa?"
        ],
        "example": "Xem các bảng kỹ thuật Test trong phần Outputs.",
        "related_skills": ["Phân tích Use Case (Ultra)", "Write SRS (Ultra)"],
        "quality_criteria": ["Cover 100% Boundary", "Cover đủ tổ hợp logic", "Trình bày trực quan dạng bảng"],
        "estimated_effort": "0.5 ngày / Feature",
        "prompt_role": "Senior Quality Assurance (QA) Automation Engineer. Chuyên gia về các kỹ thuật kiểm thử hộp đen (Black-box testing).",
        "prompt_task": "Phân tích và sinh Test Case theo các kỹ thuật kiểm thử chuyên nghiệp. Phục vụ mạnh mẽ các lệnh Micro-tasking.",
        "prompt_context": "User cần các kịch bản test 'khó', tập trung vào các case dễ sinh ra bug nhất trên hệ thống (giá trị biên, logic phức tạp).",
        "prompt_rules": [
            "NẾU User yêu cầu BVA (Boundary Value): BẮT BUỘC sinh đủ 6 test case (Min-1, Min, Min+1, Max-1, Max, Max+1).",
            "NẾU User yêu cầu Decision Table: BẮT BUỘC vẽ bảng kết hợp các điều kiện True/False (Yes/No).",
            "KHÔNG viết Test Case chung chung. Mỗi TC phải có Test Data (Dữ liệu thử nghiệm) CỤ THỂ (VD: Tuổi = 17, Giá = -1).",
            "TẬP TRUNG vào lệnh Micro-tasking: User yêu cầu bảng nào, chỉ sinh bảng đó, không sinh lan man."
        ],
        "prompt_example": ""
    }
]

if __name__ == "__main__":
    print("=== Expanding: ULTRA DEEP CORE SKILLS (Use Case, SRS, Test Case) ===")
    run(skills)
