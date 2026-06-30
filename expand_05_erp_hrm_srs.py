import sys
sys.path.insert(0, r"e:\BA Skill Library")
from skill_generator import run

skills = [
    # ================================================================
    # ERP - Kế toán công nợ
    # ================================================================
    {
        "path": "01-Business-Domain/ERP",
        "name": "Phân tích Kế toán công nợ",
        "level": "Level 2 - Business Skill",
        "domain": "ERP",
        "tags": ["ERP", "AR", "AP", "Receivable", "Payable", "Accounting"],
        "purpose": "Phân tích toàn diện luồng quản lý công nợ phải thu (Accounts Receivable - AR) và công nợ phải trả (Accounts Payable - AP), bao gồm hạn mức tín dụng (Credit Limit), tuổi nợ (Aging), đối chiếu công nợ và xử lý xóa nợ (Write-off).",
        "when_to_use": "Sử dụng khi xây dựng module Kế toán cho ERP hoặc tích hợp CRM/WMS với Kế toán.",
        "prerequisites": ["Hiểu cơ bản về kế toán doanh nghiệp", "Đã phân tích Procurement"],
        "inputs_detail": [
            {"name": "Chính sách tín dụng (Credit Policy)", "description": "Quy định về hạn mức nợ và thời hạn thanh toán cho khách hàng.", "required": True, "example": "Khách hàng hạng A: Credit Limit = 500tr, Payment Term = Net 30. Khách hàng hạng B: Credit Limit = 200tr, Payment Term = Net 15."},
            {"name": "Hóa đơn (Invoice)", "description": "Danh sách hóa đơn phát sinh từ Bán hàng hoặc Mua hàng.", "required": True, "example": "INV-001: Khách ABC, Giá trị 100tr, Ngày xuất 01/06, Hạn thanh toán 30/06."},
            {"name": "Quy tắc nhắc nợ (Dunning Rules)", "description": "Kịch bản nhắc nợ theo thời gian quá hạn.", "required": False, "example": "Quá hạn 7 ngày → Email nhắc. 15 ngày → Gọi điện. 30 ngày → Thư cảnh cáo. 60 ngày → Chặn bán hàng."}
        ],
        "process_detail": [
            {"step": 1, "title": "Ghi nhận phát sinh công nợ", "description": "Tạo bản ghi công nợ khi có hóa đơn bán hàng (AR) hoặc hóa đơn mua hàng (AP).", "sub_steps": [
                "AR: Khi xuất hóa đơn bán hàng → Tự động tạo bản ghi Phải Thu liên kết với Invoice + SO",
                "AP: Khi nhận hóa đơn NCC (đã qua 3-Way Matching) → Tự động tạo bản ghi Phải Trả liên kết với Invoice + PO + GRN",
                "Kiểm tra Credit Limit: Nếu tổng nợ hiện tại + đơn mới > Credit Limit → Block đơn hàng, cần phê duyệt đặc biệt"
            ]},
            {"step": 2, "title": "Theo dõi tuổi nợ (Aging Analysis)", "description": "Phân loại công nợ theo thời gian quá hạn.", "sub_steps": [
                "Bucket 1: Chưa đến hạn (Current)",
                "Bucket 2: Quá hạn 1-30 ngày",
                "Bucket 3: Quá hạn 31-60 ngày",
                "Bucket 4: Quá hạn 61-90 ngày",
                "Bucket 5: Quá hạn > 90 ngày (Nợ khó đòi)",
                "Dashboard: Biểu đồ Aging theo khách hàng, theo khu vực"
            ]},
            {"step": 3, "title": "Nhắc nợ tự động (Dunning)", "description": "Gửi thông báo nhắc nợ theo kịch bản.", "sub_steps": [
                "Level 1 (Quá hạn 7 ngày): Email nhắc nhở nhẹ nhàng",
                "Level 2 (Quá hạn 15 ngày): Gọi điện thoại + Email",
                "Level 3 (Quá hạn 30 ngày): Thư cảnh cáo chính thức",
                "Level 4 (Quá hạn 60 ngày): Chặn bán hàng (Block Sales Order)",
                "Level 5 (Quá hạn 90 ngày): Chuyển cho bộ phận Pháp lý"
            ]},
            {"step": 4, "title": "Đối chiếu công nợ (Reconciliation)", "description": "Đối chiếu số liệu giữa Sổ công nợ và Sổ ngân hàng/Sổ cái.", "sub_steps": [
                "Khớp thanh toán (Payment Matching): Khi nhận tiền → Khớp với Invoice nào?",
                "Hỗ trợ khớp tự động (Auto-matching) theo số Invoice trên mã giao dịch ngân hàng",
                "Xử lý thanh toán dư (Overpayment): Trả lại hay giữ Credit Memo?",
                "Xử lý thanh toán thiếu (Underpayment): Tạo Debit Note hay chờ?",
                "Đối chiếu cuối kỳ: Gửi Statement of Account cho khách ký xác nhận"
            ]},
            {"step": 5, "title": "Xóa nợ và trích lập dự phòng (Write-off & Provision)", "description": "Xử lý nợ không thể thu hồi.", "sub_steps": [
                "Nợ quá hạn > 12 tháng: Trích lập dự phòng (Provision) 100%",
                "Nợ xác nhận không thu được: Lập hồ sơ xóa nợ (Write-off)",
                "Phê duyệt xóa nợ: Kế toán trưởng → Giám đốc Tài chính → CEO (tùy giá trị)",
                "Hạch toán kế toán: Nợ TK Chi phí / Có TK Phải thu"
            ]}
        ],
        "outputs_detail": [
            {"name": "Báo cáo Aging (Tuổi nợ)", "format": "Markdown Table", "template": "| Khách hàng | Current | 1-30 ngày | 31-60 ngày | 61-90 ngày | >90 ngày | Tổng |\n|---|---|---|---|---|---|---|\n| ABC Corp | 100tr | 50tr | 20tr | 0 | 0 | 170tr |\n| XYZ Ltd | 0 | 0 | 30tr | 45tr | 80tr | 155tr |"},
            {"name": "Dunning Schedule", "format": "Markdown Table", "template": "| Level | Quá hạn | Hành động | Người thực hiện | Kênh |\n|---|---|---|---|---|\n| 1 | 7 ngày | Nhắc nhở | Hệ thống tự động | Email |\n| 2 | 15 ngày | Gọi điện | Kế toán | Phone + Email |\n| 3 | 30 ngày | Cảnh cáo | Kế toán trưởng | Thư chính thức |\n| 4 | 60 ngày | Chặn bán | Hệ thống tự động | Block SO |\n| 5 | 90 ngày | Pháp lý | Pháp chế | Công văn |"},
            {"name": "Cấu trúc dữ liệu AR/AP", "format": "Markdown Table", "template": "| Trường | Kiểu | Mô tả |\n|---|---|---|\n| receivable_id | INT (PK) | Mã công nợ |\n| customer_id | INT (FK) | Khách hàng |\n| invoice_id | INT (FK) | Hóa đơn |\n| amount | DECIMAL | Số tiền |\n| due_date | DATE | Ngày đến hạn |\n| paid_amount | DECIMAL | Đã thanh toán |\n| balance | DECIMAL | Còn lại |\n| status | ENUM | Open/Partial/Paid/Overdue/WriteOff |"}
        ],
        "sub_skills": ["Thiết kế Credit Limit Policy", "Thiết kế Aging Report", "Thiết kế Dunning Automation", "Thiết kế Payment Matching"],
        "business_rules": [
            "BR-FIN-AR-01: Tổng nợ hiện tại + Đơn hàng mới > Credit Limit → Block Sales Order.",
            "BR-FIN-AR-02: Khách hàng quá hạn > 60 ngày tự động bị chặn bán hàng.",
            "BR-FIN-AR-03: Write-off nợ > 50 triệu phải có phê duyệt của CFO.",
            "BR-FIN-AR-04: Nợ quá hạn > 6 tháng phải trích lập dự phòng 50%, > 12 tháng = 100%.",
            "BR-FIN-AP-05: Không thanh toán cho NCC nếu Invoice chưa qua 3-Way Matching."
        ],
        "edge_cases": [
            "Khách thanh toán bằng tiền mặt nhưng không ghi số Invoice → Xử lý Unidentified Payment",
            "Khách thanh toán gộp nhiều Invoice trong 1 lần chuyển khoản → Cần tách (Split Payment)",
            "NCC gửi Invoice trùng → Cần phát hiện Duplicate Invoice",
            "Tỷ giá thay đổi giữa ngày xuất Invoice và ngày thanh toán → Xử lý chênh lệch tỷ giá (Exchange Rate Difference)"
        ],
        "checklist": [
            "Đã thiết kế Credit Limit cho khách hàng",
            "Đã có Aging Report (5 Buckets)",
            "Đã thiết kế Dunning tự động theo cấp",
            "Đã có luồng đối chiếu công nợ (Reconciliation)",
            "Đã xử lý Payment Matching (tự động + thủ công)",
            "Đã có luồng Write-off với phê duyệt nhiều cấp",
            "Đã xử lý Overpayment / Underpayment",
            "Đã có Statement of Account gửi khách hàng cuối kỳ"
        ],
        "example": "Xem Aging Report và Dunning Schedule trong phần Outputs.",
        "related_skills": ["Phân tích Procurement", "Phân tích Opportunity"],
        "quality_criteria": ["Phải có Aging Analysis 5 Buckets", "Phải có Dunning tự động", "Phải có Credit Limit check", "Phải có Write-off workflow"],
        "estimated_effort": "5-7 ngày",
        "prompt_role": "Senior Finance/Accounting Analyst chuyên về Accounts Receivable & Payable trong hệ thống ERP.",
        "prompt_task": "Phân tích và thiết kế quy trình quản lý công nợ phải thu/phải trả toàn diện.",
        "prompt_context": "Doanh nghiệp cần số hóa quy trình theo dõi công nợ, chủ động nhắc nợ và kiểm soát rủi ro tín dụng khách hàng.",
        "prompt_rules": [
            "PHẢI có Credit Limit check trước khi cho phép bán hàng.",
            "PHẢI có Aging Report với 5 Buckets (Current, 1-30, 31-60, 61-90, >90).",
            "PHẢI có Dunning tự động theo cấp.",
            "PHẢI có luồng Write-off với phê duyệt nhiều cấp.",
            "PHẢI xử lý Payment Matching.",
            "Output PHẢI bao gồm Aging Table, Dunning Schedule, và Data Model."
        ],
        "prompt_example": ""
    },
    # ================================================================
    # HRM - Payroll
    # ================================================================
    {
        "path": "01-Business-Domain/HRM",
        "name": "Phân tích Payroll",
        "level": "Level 2 - Business Skill",
        "domain": "HRM",
        "tags": ["HRM", "Payroll", "Salary", "Tax", "BHXH"],
        "purpose": "Phân tích toàn diện luồng tính lương nhân viên, từ thu thập dữ liệu công đến ra bảng lương cuối cùng, bao gồm tính lương cơ bản, phụ cấp, thưởng, khấu trừ thuế TNCN, BHXH/BHYT/BHTN, và quy trình duyệt + phát lương.",
        "when_to_use": "Sử dụng khi xây dựng module Payroll cho hệ thống HRM.",
        "prerequisites": ["Đã phân tích Chấm công", "Hiểu Luật Thuế TNCN và BHXH Việt Nam"],
        "inputs_detail": [
            {"name": "Bảng công đã duyệt", "description": "Dữ liệu chấm công tổng hợp cuối tháng.", "required": True, "example": "NV Nguyễn Văn A: 22 ngày đi làm, 8 giờ OT ngày thường, 4 giờ OT ngày nghỉ."},
            {"name": "Cấu trúc lương", "description": "Các thành phần cấu thành thu nhập.", "required": True, "example": "Lương cơ bản: 15tr. Phụ cấp ăn: 730k. Phụ cấp xăng: 500k. Phụ cấp điện thoại: 300k."},
            {"name": "Bảng thuế TNCN & BHXH", "description": "Biểu thuế lũy tiến và tỷ lệ đóng BHXH.", "required": True, "example": "Thuế TNCN: 0-5tr = 5%, 5-10tr = 10%, 10-18tr = 15%... BHXH: NV đóng 10.5%, DN đóng 21.5%."}
        ],
        "process_detail": [
            {"step": 1, "title": "Thu thập dữ liệu đầu vào", "description": "Gom tất cả dữ liệu cần thiết cho tính lương.", "sub_steps": [
                "Bảng công đã duyệt (từ module Chấm công)",
                "Dữ liệu OT đã duyệt",
                "Phụ cấp đặc biệt tháng này (Thưởng dự án, Hoa hồng Sales...)",
                "Khấu trừ đặc biệt (Tạm ứng lương, Phạt, Đền bù...)",
                "Thay đổi nhân sự: Nhân viên mới (tính theo ngày thực tế), Nhân viên nghỉ việc"
            ]},
            {"step": 2, "title": "Tính lương Gross (Tổng thu nhập)", "description": "Tính toàn bộ thu nhập trước thuế.", "sub_steps": [
                "Lương cơ bản theo ngày: (Lương tháng / 26 ngày) × Số ngày đi làm",
                "Lương OT: Ngày thường × 150%, Ngày nghỉ × 200%, Ngày lễ × 300%",
                "Phụ cấp cố định: Ăn trưa, Xăng xe, Điện thoại, Chức vụ",
                "Thu nhập không thường xuyên: Thưởng, Hoa hồng, Phúc lợi",
                "Gross Salary = Lương cơ bản + OT + Phụ cấp + Thưởng"
            ]},
            {"step": 3, "title": "Tính khấu trừ (Deductions)", "description": "Tính các khoản phải trừ theo luật.", "sub_steps": [
                "BHXH (8%): Tính trên mức lương đóng BH (có mức trần = 20 × lương cơ sở)",
                "BHYT (1.5%): Tính trên mức lương đóng BH",
                "BHTN (1%): Tính trên mức lương đóng BH",
                "Tổng BH nhân viên đóng = 10.5% × Lương đóng BH",
                "Thuế TNCN: Thu nhập chịu thuế = Gross - BH - Giảm trừ bản thân (11tr) - Giảm trừ người phụ thuộc (4.4tr/người)",
                "Áp biểu thuế lũy tiến từng phần (7 bậc: 5%, 10%, 15%, 20%, 25%, 30%, 35%)",
                "Khấu trừ khác: Tạm ứng, Phạt, Hoàn ứng công tác"
            ]},
            {"step": 4, "title": "Tính lương Net (Thực nhận)", "description": "Tính số tiền nhân viên thực nhận.", "sub_steps": [
                "Net Salary = Gross Salary - BHXH/BHYT/BHTN - Thuế TNCN - Khấu trừ khác",
                "Kiểm tra: Net Salary > 0 (Nếu < 0 → Cảnh báo bất thường)",
                "Làm tròn đến hàng nghìn đồng"
            ]},
            {"step": 5, "title": "Duyệt và Phát lương", "description": "Luồng phê duyệt và thanh toán.", "sub_steps": [
                "HR tạo bảng lương → Kế toán trưởng review → Giám đốc phê duyệt",
                "Sau khi duyệt: Tạo file chuyển khoản hàng loạt (Bank Transfer File)",
                "In phiếu lương (Payslip) gửi cho từng nhân viên",
                "Lock bảng lương (không cho chỉnh sửa) sau khi phát lương",
                "Lưu trữ hồ sơ lương ít nhất 5 năm theo quy định"
            ]}
        ],
        "outputs_detail": [
            {"name": "Bảng lương chi tiết", "format": "Markdown Table", "template": "| Mục | Công thức | NV Nguyễn Văn A |\n|---|---|---|\n| Lương cơ bản | 15tr / 26 × 22 ngày | 12,692,308 |\n| OT ngày thường | (15tr/26/8) × 8h × 150% | 865,385 |\n| OT ngày nghỉ | (15tr/26/8) × 4h × 200% | 576,923 |\n| Phụ cấp ăn | Cố định | 730,000 |\n| Phụ cấp xăng | Cố định | 500,000 |\n| **Gross** | | **15,364,616** |\n| BHXH (8%) | 15tr × 8% | -1,200,000 |\n| BHYT (1.5%) | 15tr × 1.5% | -225,000 |\n| BHTN (1%) | 15tr × 1% | -150,000 |\n| Giảm trừ bản thân | | -11,000,000 |\n| Thu nhập chịu thuế | 15,364,616 - 1,575,000 - 11,000,000 | 2,789,616 |\n| Thuế TNCN (5%) | 2,789,616 × 5% | -139,481 |\n| **Net Salary** | | **13,650,135** |"},
            {"name": "Payslip Template", "format": "Markdown", "template": "# PHIẾU LƯƠNG THÁNG [MM/YYYY]\n\n**Nhân viên:** [Tên]\n**Mã NV:** [Mã]\n**Phòng ban:** [PB]\n\n| Thu nhập | Số tiền | Khấu trừ | Số tiền |\n|---|---|---|---|\n| Lương cơ bản | xxx | BHXH | xxx |\n| OT | xxx | BHYT | xxx |\n| Phụ cấp | xxx | BHTN | xxx |\n| Thưởng | xxx | Thuế TNCN | xxx |\n| **Tổng thu nhập** | **xxx** | **Tổng khấu trừ** | **xxx** |\n\n**THỰC NHẬN: xxx VNĐ**"}
        ],
        "sub_skills": ["Tính OT theo Luật LĐ", "Tính Thuế TNCN lũy tiến", "Tính BHXH/BHYT/BHTN", "Thiết kế Payslip"],
        "business_rules": [
            "BR-HRM-PAY-01: Lương OT ngày thường = 150%, ngày nghỉ = 200%, ngày lễ = 300%.",
            "BR-HRM-PAY-02: Thuế TNCN tính theo biểu lũy tiến từng phần 7 bậc.",
            "BR-HRM-PAY-03: Mức lương đóng BHXH không vượt quá 20 × lương cơ sở (hiện tại 1,800,000 × 20 = 36,000,000).",
            "BR-HRM-PAY-04: Giảm trừ bản thân = 11,000,000 VNĐ/tháng. Giảm trừ người phụ thuộc = 4,400,000/người/tháng.",
            "BR-HRM-PAY-05: Bảng lương phải được duyệt bởi ít nhất 2 cấp trước khi phát lương."
        ],
        "edge_cases": [
            "Nhân viên vào giữa tháng → Tính lương pro-rata theo ngày thực tế",
            "Nhân viên nghỉ thai sản → Hưởng BHXH thay vì lương công ty",
            "Nhân viên có thu nhập từ nhiều nơi → Quyết toán thuế cuối năm",
            "Thay đổi mức lương giữa tháng → Chia 2 giai đoạn tính lương"
        ],
        "checklist": [
            "Đã tính lương cơ bản theo ngày công thực tế",
            "Đã tính OT đúng hệ số (150%, 200%, 300%)",
            "Đã trừ BHXH/BHYT/BHTN đúng tỷ lệ",
            "Đã tính thuế TNCN theo biểu lũy tiến",
            "Đã áp dụng giảm trừ bản thân + người phụ thuộc",
            "Đã có luồng duyệt bảng lương",
            "Đã thiết kế Payslip template",
            "Đã có file chuyển khoản hàng loạt cho ngân hàng",
            "Đã lock bảng lương sau khi phát"
        ],
        "example": "Xem Bảng lương chi tiết và Payslip Template trong Outputs.",
        "related_skills": ["Phân tích Chấm công", "Phân tích KPI và Đánh giá"],
        "quality_criteria": ["Phải đúng công thức OT", "Phải đúng biểu thuế TNCN VN", "Phải đúng tỷ lệ BHXH", "Phải có Payslip"],
        "estimated_effort": "5-7 ngày",
        "prompt_role": "Senior HR/Payroll Analyst am hiểu Luật Lao động và Luật Thuế TNCN Việt Nam.",
        "prompt_task": "Phân tích và thiết kế quy trình tính lương toàn diện cho doanh nghiệp Việt Nam.",
        "prompt_context": "Doanh nghiệp Việt Nam cần hệ thống tính lương tự động tuân thủ pháp luật.",
        "prompt_rules": [
            "PHẢI tuân thủ Luật Lao động VN về hệ số OT (150%, 200%, 300%).",
            "PHẢI đúng biểu thuế TNCN lũy tiến 7 bậc.",
            "PHẢI đúng tỷ lệ BHXH (NV: 10.5%, DN: 21.5%).",
            "PHẢI có giảm trừ bản thân (11tr) và người phụ thuộc (4.4tr).",
            "PHẢI có Payslip template.",
            "Output PHẢI bao gồm bảng tính lương mẫu với số liệu cụ thể."
        ],
        "prompt_example": ""
    },
    # ================================================================
    # HRM - Tuyển dụng
    # ================================================================
    {
        "path": "01-Business-Domain/HRM",
        "name": "Phân tích Tuyển dụng",
        "level": "Level 2 - Business Skill",
        "domain": "HRM",
        "tags": ["HRM", "Recruitment", "ATS", "Hiring"],
        "purpose": "Phân tích toàn diện quy trình Applicant Tracking System (ATS), từ tạo yêu cầu tuyển dụng (Job Requisition) đến Onboarding nhân viên mới, bao gồm quản lý Pipeline ứng viên, đánh giá phỏng vấn, và Talent Pool.",
        "when_to_use": "Sử dụng khi xây dựng module Tuyển dụng cho HRM.",
        "prerequisites": ["Hiểu quy trình tuyển dụng doanh nghiệp"],
        "inputs_detail": [
            {"name": "Yêu cầu tuyển dụng (Job Requisition)", "description": "Phiếu đề xuất tuyển dụng từ trưởng phòng.", "required": True, "example": "Phòng IT đề xuất tuyển 2 Backend Developer, mức lương 20-30tr, kinh nghiệm 3 năm Java."},
            {"name": "Kênh tuyển dụng", "description": "Các kênh đăng tin tuyển dụng.", "required": True, "example": "VietnamWorks, LinkedIn, TopDev, Facebook Groups, Website công ty, Headhunter"},
            {"name": "Quy trình phỏng vấn", "description": "Các vòng phỏng vấn và tiêu chí.", "required": True, "example": "Vòng 1: HR screening (Phone). Vòng 2: Technical Test. Vòng 3: Interview with Manager. Vòng 4: Culture Fit with CEO."}
        ],
        "process_detail": [
            {"step": 1, "title": "Tạo & Duyệt Yêu cầu tuyển dụng", "description": "Trưởng phòng tạo JR, gửi HR duyệt.", "sub_steps": [
                "Điền thông tin: Vị trí, Số lượng, Mức lương, Mô tả công việc (JD), Tiêu chí",
                "HR review: Kiểm tra ngân sách headcount, mức lương thị trường",
                "Phê duyệt: Manager → HR Director → CEO (nếu cấp cao)",
                "JR được duyệt → HR bắt đầu đăng tuyển"
            ]},
            {"step": 2, "title": "Đăng tuyển & Thu nhận CV", "description": "Đăng tin và thu thập hồ sơ ứng viên.", "sub_steps": [
                "Đăng trên nhiều kênh đồng thời",
                "Nhận CV qua Email/Portal → Tự động tạo bản ghi Applicant trong hệ thống",
                "Parse CV tự động (Extract tên, SĐT, Email, Kinh nghiệm)",
                "Gửi email xác nhận đã nhận CV cho ứng viên"
            ]},
            {"step": 3, "title": "Sàng lọc (Screening)", "description": "Lọc hồ sơ phù hợp.", "sub_steps": [
                "HR review CV: Khớp JD? Kinh nghiệm đủ? Mức lương phù hợp?",
                "Trạng thái: Shortlisted (Vào vòng trong) / Rejected (Loại) / KIP (Giữ lại cho vị trí khác)",
                "Gọi điện screening: Xác nhận thông tin, mức lương kỳ vọng, khả năng onboard"
            ]},
            {"step": 4, "title": "Phỏng vấn nhiều vòng", "description": "Tiến hành phỏng vấn và đánh giá.", "sub_steps": [
                "Mỗi vòng có Scorecard riêng (Tiêu chí + Thang điểm 1-5)",
                "Interviewer nhập nhận xét và điểm vào hệ thống",
                "Sau mỗi vòng: Pass / Fail / On Hold",
                "Hệ thống gửi email hẹn lịch tự động (tích hợp Google Calendar)"
            ]},
            {"step": 5, "title": "Offer & Onboarding", "description": "Đưa ra lời mời và hoàn tất thủ tục.", "sub_steps": [
                "HR tạo Offer Letter với điều khoản (Lương, Benefits, Ngày bắt đầu)",
                "Gửi Offer → Ứng viên Accept / Negotiate / Reject",
                "Accept → Tạo hồ sơ Employee (chuyển từ Applicant sang Employee)",
                "Chuẩn bị Onboarding: Laptop, Email, Seat, Training plan",
                "Ứng viên Reject → Gửi cho backup candidate"
            ]}
        ],
        "outputs_detail": [
            {"name": "Hiring Pipeline", "format": "Mermaid Flowchart", "template": "graph LR\n    A[JR Created] --> B[Approved]\n    B --> C[Job Posted]\n    C --> D[CVs Received]\n    D --> E[Screening]\n    E --> F[Interview Round 1-N]\n    F --> G[Offer]\n    G --> H[Onboarded]"},
            {"name": "Interview Scorecard", "format": "Markdown Table", "template": "| Tiêu chí | Trọng số | Điểm (1-5) | Ghi chú |\n|---|---|---|---|\n| Kỹ năng chuyên môn | 40% | | |\n| Kinh nghiệm liên quan | 25% | | |\n| Communication | 15% | | |\n| Culture Fit | 10% | | |\n| Motivation | 10% | | |\n| **Tổng điểm (Weighted)** | **100%** | | |"}
        ],
        "sub_skills": ["Thiết kế JD Template", "Thiết kế Interview Scorecard", "Thiết kế Talent Pool", "Thiết kế Onboarding Checklist"],
        "business_rules": [
            "BR-HRM-REC-01: Mọi tuyển dụng phải có Job Requisition được duyệt.",
            "BR-HRM-REC-02: Ứng viên bị Reject phải được giữ trong Talent Pool ít nhất 12 tháng.",
            "BR-HRM-REC-03: Offer Letter phải được HR Director duyệt trước khi gửi.",
            "BR-HRM-REC-04: Mỗi vòng phỏng vấn phải có Scorecard với tiêu chí rõ ràng."
        ],
        "edge_cases": [
            "Ứng viên accept Offer nhưng không đến ngày đầu tiên (No-show) → Activate backup",
            "Hiring Manager muốn tuyển vượt headcount → Cần phê duyệt đặc biệt",
            "Ứng viên nội bộ (Internal Transfer) → Quy trình riêng, ưu tiên"
        ],
        "checklist": [
            "Đã thiết kế luồng Job Requisition + Approval",
            "Đã tích hợp đa kênh tuyển dụng",
            "Đã có Parse CV tự động",
            "Đã thiết kế Interview Scorecard",
            "Đã có Talent Pool cho ứng viên tiềm năng",
            "Đã thiết kế Offer Letter workflow",
            "Đã có Onboarding Checklist",
            "Đã có Dashboard: Time-to-Hire, Source Effectiveness, Offer Accept Rate"
        ],
        "example": "Xem Interview Scorecard và Hiring Pipeline trong Outputs.",
        "related_skills": ["Phân tích KPI và Đánh giá", "Phân tích Chấm công"],
        "quality_criteria": ["Phải có Job Requisition workflow", "Phải có Interview Scorecard", "Phải có Talent Pool"],
        "estimated_effort": "5-7 ngày",
        "prompt_role": "Senior HR Analyst chuyên về Talent Acquisition.",
        "prompt_task": "Phân tích và thiết kế hệ thống ATS toàn diện.",
        "prompt_context": "Doanh nghiệp cần hệ thống tuyển dụng chuyên nghiệp thay vì quản lý bằng Excel.",
        "prompt_rules": [
            "PHẢI có Job Requisition approval trước khi đăng tuyển.",
            "PHẢI có Interview Scorecard với tiêu chí và trọng số.",
            "PHẢI có Talent Pool.",
            "PHẢI có Onboarding Checklist.",
            "Output PHẢI bao gồm Hiring Pipeline, Scorecard Template, và Data Model."
        ],
        "prompt_example": ""
    },
    # ================================================================
    # Requirement - Write SRS
    # ================================================================
    {
        "path": "02-Requirement/SRS",
        "name": "Write SRS",
        "level": "Level 1 - Basic Skill",
        "domain": "Requirement",
        "tags": ["Requirement", "SRS", "Document", "Functional", "Non-Functional"],
        "purpose": "Soạn thảo Software Requirements Specification (SRS) chi tiết mức độ team Dev có thể code được ngay, bao gồm đặc tả chức năng (Functional), phi chức năng (Non-Functional), giao diện, API, và ràng buộc hệ thống.",
        "when_to_use": "Sử dụng sau khi BRD đã được duyệt, cần chuyển yêu cầu nghiệp vụ thành đặc tả kỹ thuật chi tiết.",
        "prerequisites": ["Đã hoàn thành BRD", "Đã viết User Stories"],
        "inputs_detail": [
            {"name": "BRD đã duyệt", "description": "Tài liệu yêu cầu nghiệp vụ cấp cao.", "required": True, "example": "BRD v1.0 Module WMS với 35 Business Requirements."},
            {"name": "User Stories", "description": "Danh sách User Stories đã viết.", "required": True, "example": "45 User Stories đã estimate Story Points."},
            {"name": "Wireframes / Mockups", "description": "Bản thiết kế giao diện sơ bộ.", "required": False, "example": "Figma mockups cho 15 màn hình chính."}
        ],
        "process_detail": [
            {"step": 1, "title": "Mô tả tổng quan hệ thống", "description": "Giới thiệu mục đích, phạm vi và kiến trúc tổng thể.", "sub_steps": [
                "Mục đích hệ thống",
                "Phạm vi (In-scope / Out-of-scope)",
                "Kiến trúc tổng quan (Client-Server, Microservices...)",
                "Công nghệ sử dụng (Tech Stack)",
                "Danh sách User Roles"
            ]},
            {"step": 2, "title": "Đặc tả chức năng (Functional Requirements)", "description": "Mô tả chi tiết từng chức năng hệ thống.", "sub_steps": [
                "Mỗi FR có ID duy nhất: FR-WMS-001, FR-WMS-002...",
                "Mô tả: Hệ thống phải [làm gì] khi [điều kiện]",
                "Input: User nhập gì? Từ đâu?",
                "Processing: Hệ thống xử lý như thế nào? Business Rules?",
                "Output: Hệ thống hiển thị/lưu/gửi gì?",
                "Validation Rules: Trường nào bắt buộc? Format? Min/Max?",
                "Error Handling: Thông báo lỗi gì khi nhập sai?",
                "Security: Ai được dùng tính năng này?"
            ]},
            {"step": 3, "title": "Đặc tả phi chức năng (Non-Functional Requirements)", "description": "Mô tả các yêu cầu chất lượng hệ thống.", "sub_steps": [
                "Performance: Response time < 2s cho 95% requests. Hỗ trợ 500 CCU.",
                "Security: Encrypt mật khẩu bcrypt, JWT Token expire 24h, OWASP Top 10",
                "Availability: Uptime 99.5% (Tối đa 43.8 giờ downtime/năm)",
                "Scalability: Horizontal scaling khi CCU > 1000",
                "Backup: Daily backup, Retention 30 ngày",
                "Compatibility: Chrome 90+, Firefox 85+, Edge, Safari. Mobile responsive"
            ]},
            {"step": 4, "title": "Đặc tả giao diện (Interface Requirements)", "description": "Mô tả các giao diện tích hợp.", "sub_steps": [
                "User Interface: Responsive Web, Mobile App (nếu có)",
                "API Interface: RESTful API, Authentication method",
                "Hardware Interface: Máy quét barcode, Máy in, Máy chấm công",
                "Software Interface: Tích hợp ERP, Tích hợp Email, Tích hợp SMS Gateway"
            ]},
            {"step": 5, "title": "Data Model", "description": "Mô tả cấu trúc dữ liệu.", "sub_steps": [
                "ERD tổng quan",
                "Data Dictionary cho các bảng chính",
                "Quy ước đặt tên (Naming Convention)"
            ]}
        ],
        "outputs_detail": [
            {"name": "Tài liệu SRS", "format": "Markdown Document", "template": "# Software Requirements Specification (SRS)\n\n## 1. Introduction\n### 1.1. Purpose\n### 1.2. Scope\n### 1.3. Definitions & Acronyms\n### 1.4. References\n\n## 2. Overall Description\n### 2.1. Product Perspective\n### 2.2. User Classes and Characteristics\n### 2.3. Operating Environment\n### 2.4. Assumptions and Dependencies\n\n## 3. System Features (Functional Requirements)\n### 3.1. [Module Name]\n#### FR-001: [Feature Name]\n- **Description:** Hệ thống phải...\n- **Input:** ...\n- **Processing:** ...\n- **Output:** ...\n- **Validation:** ...\n- **Error Handling:** ...\n- **Permission:** ...\n- **Priority:** Must/Should/Could\n\n## 4. Non-Functional Requirements\n### 4.1. Performance\n### 4.2. Security\n### 4.3. Availability\n### 4.4. Scalability\n\n## 5. Interface Requirements\n### 5.1. User Interfaces\n### 5.2. API Interfaces\n### 5.3. Hardware Interfaces\n\n## 6. Data Requirements\n### 6.1. ERD\n### 6.2. Data Dictionary\n\n## 7. Appendix"}
        ],
        "sub_skills": ["Viết Functional Requirements chi tiết", "Viết Non-Functional Requirements", "Thiết kế Data Model", "Viết Validation Rules"],
        "business_rules": [
            "BR-SRS-01: Mỗi Functional Requirement phải có ID, Input, Processing, Output, Validation.",
            "BR-SRS-02: Non-Functional Requirements phải có thể đo lường được (Measurable).",
            "BR-SRS-03: SRS phải cover Error Handling cho mỗi chức năng.",
            "BR-SRS-04: SRS phải có Traceability ngược về BRD (Mỗi FR link về BR tương ứng)."
        ],
        "edge_cases": [
            "Yêu cầu quá phức tạp để viết SRS → Chia thành nhiều tài liệu SRS theo module",
            "Wireframe chưa có → Mô tả bằng lời, bổ sung sau"
        ],
        "checklist": [
            "Có đủ FR cho mỗi User Story?",
            "Mỗi FR có Input/Processing/Output/Validation/Error?",
            "Có NFR (Performance, Security, Availability)?",
            "NFR có đo lường được không (không dùng từ 'nhanh', 'tốt')?",
            "Có Data Model (ERD + Data Dictionary)?",
            "Có Interface Requirements (API, Hardware)?",
            "SRS có trace ngược về BRD không?"
        ],
        "example": "Xem SRS Template trong Outputs.",
        "related_skills": ["Write BRD", "Write User Story", "Thiết kế ERD", "Create Data Dictionary"],
        "quality_criteria": ["Mỗi FR phải có đủ 7 phần", "NFR phải measurable", "Phải có Data Model"],
        "estimated_effort": "7-14 ngày",
        "prompt_role": "Senior Business Analyst chuyên soạn thảo SRS cho các dự án phần mềm doanh nghiệp quy mô lớn.",
        "prompt_task": "Soạn thảo SRS chi tiết đến mức team Dev có thể code được ngay.",
        "prompt_context": "Dự án đang ở giai đoạn Detail Design, cần SRS chi tiết để Dev estimate và implement.",
        "prompt_rules": [
            "Mỗi Functional Requirement PHẢI có: ID, Description, Input, Processing, Output, Validation, Error Handling, Permission.",
            "Non-Functional Requirements PHẢI measurable (VD: 'Response time < 2 giây' thay vì 'Nhanh').",
            "PHẢI có Error Handling cho MỌI chức năng.",
            "PHẢI có Data Model (ERD + Data Dictionary).",
            "PHẢI có Traceability về BRD.",
            "Output PHẢI theo đúng template SRS chuẩn IEEE 830."
        ],
        "prompt_example": ""
    }
]

if __name__ == "__main__":
    print("=== Expanding: ERP(Kế toán) + HRM(Payroll, Tuyển dụng) + SRS ===")
    run(skills)
