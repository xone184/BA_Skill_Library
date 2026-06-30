import sys
sys.path.insert(0, r"e:\BA Skill Library")
from skill_generator import run

skills = [
    # ================================================================
    # MES - Production Order
    # ================================================================
    {
        "path": "01-Business-Domain/MES",
        "name": "Phân tích Production Order",
        "level": "Level 2 - Business Skill",
        "domain": "MES",
        "tags": ["MES", "Production", "Manufacturing", "Work Order", "BOM"],
        "purpose": "Phân tích toàn diện quy trình tạo và quản lý lệnh sản xuất (Production Order / Work Order), từ khi nhận kế hoạch sản xuất đến khi thành phẩm nhập kho, bao gồm kiểm tra vật tư (Material Availability), định mức sản xuất (Routing/BOM), theo dõi tiến độ theo thời gian thực và xử lý phế phẩm (Scrap).",
        "when_to_use": "Sử dụng khi xây dựng hệ thống MES cho nhà máy sản xuất, từ nhà máy thực phẩm, cơ khí đến điện tử.",
        "prerequisites": ["Hiểu BOM (Bill of Materials)", "Hiểu Routing (Định mức công đoạn)"],
        "inputs_detail": [
            {"name": "Kế hoạch sản xuất (Production Plan)", "description": "Số lượng thành phẩm cần sản xuất theo ngày/tuần/tháng.", "required": True, "example": "Sản xuất 5000 chai nước suối 500ml trong tuần 28, chia 3 ca/ngày."},
            {"name": "BOM (Bill of Materials)", "description": "Danh sách nguyên vật liệu cần cho 1 đơn vị thành phẩm.", "required": True, "example": "1 chai nước suối 500ml = 1 vỏ chai PET + 1 nắp + 500ml nước + 1 nhãn dán"},
            {"name": "Routing (Định mức công đoạn)", "description": "Các bước sản xuất và thời gian tiêu chuẩn.", "required": True, "example": "Công đoạn 1: Thổi chai (5s/chai) → Công đoạn 2: Rót nước (3s) → Công đoạn 3: Đóng nắp (2s) → Công đoạn 4: Dán nhãn (2s) → Công đoạn 5: Đóng thùng (10s/12 chai)"}
        ],
        "process_detail": [
            {"step": 1, "title": "Tiếp nhận kế hoạch & Tạo Work Order", "description": "Chuyển kế hoạch sản xuất thành các Work Order cụ thể.", "sub_steps": [
                "Phân tách kế hoạch thành WO theo ngày/ca/máy",
                "Tính toán số lượng NVL cần dựa trên BOM (Bill of Materials Explosion)",
                "Kiểm tra tồn kho NVL (Material Availability Check)",
                "Nếu thiếu NVL → Tạo yêu cầu mua hàng (Purchase Requisition) hoặc chờ",
                "Gán WO cho dây chuyền/máy cụ thể"
            ]},
            {"step": 2, "title": "Phát lệnh sản xuất (Release WO)", "description": "Xác nhận NVL đủ và phát lệnh xuống xưởng.", "sub_steps": [
                "Trạng thái WO: Planned → Released",
                "In phiếu lệnh sản xuất cho Quản đốc",
                "Xuất NVL từ kho sang dây chuyền (Material Issue)",
                "Ghi nhận thời gian bắt đầu sản xuất"
            ]},
            {"step": 3, "title": "Theo dõi tiến độ (Production Tracking)", "description": "Ghi nhận số lượng sản xuất theo thời gian thực.", "sub_steps": [
                "Nhân viên quét barcode hoặc hệ thống IoT tự động đếm sản phẩm tại mỗi công đoạn",
                "Dashboard hiển thị: Kế hoạch vs Thực tế (Planned vs Actual)",
                "Ghi nhận thời gian dừng máy (Downtime) và lý do",
                "Ghi nhận phế phẩm (Scrap/Reject) và lý do",
                "Cảnh báo nếu sản lượng thực tế < 80% kế hoạch"
            ]},
            {"step": 4, "title": "Kiểm tra chất lượng (QC)", "description": "QC kiểm tra thành phẩm trước khi nhập kho.", "sub_steps": [
                "Lấy mẫu theo tỷ lệ quy định (AQL Sampling)",
                "Kiểm tra các chỉ tiêu: Ngoại quan, Kích thước, Trọng lượng, Chức năng",
                "Pass → Chuyển sang nhập kho thành phẩm",
                "Fail → Rework (Sửa chữa) hoặc Scrap (Tiêu hủy)"
            ]},
            {"step": 5, "title": "Hoàn thành & Nhập kho thành phẩm", "description": "Đóng Work Order và nhập hàng vào kho thành phẩm.", "sub_steps": [
                "Ghi nhận số lượng thực sản xuất (Good Qty + Scrap Qty)",
                "Trả NVL dư về kho (Material Return)",
                "Tính chi phí sản xuất thực tế (Actual Cost vs Standard Cost)",
                "Tạo phiếu nhập kho thành phẩm (Finished Goods Receipt)",
                "Trạng thái WO: Released → Completed"
            ]}
        ],
        "outputs_detail": [
            {"name": "Luồng Production Order", "format": "Mermaid Flowchart", "template": "graph TD\n    A[Nhận kế hoạch] --> B[Tạo Work Order]\n    B --> C{NVL đủ?}\n    C -->|Có| D[Release WO]\n    C -->|Không| E[Tạo PR mua NVL]\n    E --> C\n    D --> F[Xuất NVL cho sản xuất]\n    F --> G[Sản xuất & Tracking]\n    G --> H[QC kiểm tra]\n    H -->|Pass| I[Nhập kho thành phẩm]\n    H -->|Fail| J[Rework / Scrap]\n    I --> K[Đóng WO]"},
            {"name": "Cấu trúc dữ liệu Work Order", "format": "Markdown Table", "template": "| Trường | Kiểu | Mô tả |\n|---|---|---|\n| wo_id | INT (PK) | Mã lệnh SX |\n| product_id | INT (FK) | Thành phẩm |\n| planned_qty | DECIMAL | SL kế hoạch |\n| actual_qty | DECIMAL | SL thực tế |\n| scrap_qty | DECIMAL | SL phế phẩm |\n| start_date | DATETIME | Ngày bắt đầu |\n| end_date | DATETIME | Ngày kết thúc |\n| status | ENUM | Planned/Released/In Progress/Completed |\n| machine_id | INT (FK) | Máy/Dây chuyền |\n| shift | ENUM | Ca 1/2/3 |"},
            {"name": "BOM Explosion", "format": "Markdown Table", "template": "| NVL | Đơn vị | Qty/TP | WO Qty | Tổng NVL cần | Tồn kho | Thiếu |\n|---|---|---|---|---|---|---|\n| Vỏ chai PET | Cái | 1 | 5000 | 5000 | 6000 | 0 |\n| Nắp chai | Cái | 1 | 5000 | 5000 | 4500 | 500 |"}
        ],
        "sub_skills": ["Thiết kế BOM Structure", "Thiết kế Routing", "Thiết kế Production Dashboard", "Thiết kế Scrap Management"],
        "business_rules": [
            "BR-MES-WO-01: Không được Release WO nếu NVL không đủ.",
            "BR-MES-WO-02: Scrap Rate > 5% phải có điều tra nguyên nhân.",
            "BR-MES-WO-03: WO phải ghi nhận chính xác ca làm việc và máy sản xuất.",
            "BR-MES-WO-04: NVL dư sau khi hoàn thành WO phải được trả về kho.",
            "BR-MES-WO-05: Chi phí thực tế chênh lệch > 10% so với Standard Cost phải báo cáo cho Kế toán."
        ],
        "edge_cases": [
            "Máy hỏng giữa chừng → Chuyển WO sang máy khác hay chờ sửa?",
            "NVL nhận từ NCC không đạt QC → WO phải chờ hay dùng NVL thay thế?",
            "Khách hàng đột ngột thay đổi số lượng → Điều chỉnh WO mid-production"
        ],
        "checklist": [
            "Đã thiết kế BOM đa cấp (Multi-level BOM)",
            "Đã có Material Availability Check trước khi Release",
            "Đã theo dõi sản lượng realtime (IoT/Manual)",
            "Đã ghi nhận Downtime với lý do",
            "Đã ghi nhận Scrap với lý do",
            "Đã tích hợp QC tại cuối dây chuyền",
            "Đã tính toán Actual Cost vs Standard Cost",
            "Đã có Dashboard: Planned vs Actual"
        ],
        "example": "Xem Process section.",
        "related_skills": ["Phân tích OEE", "Phân tích Quality Control", "Phân tích Inbound Flow"],
        "quality_criteria": ["Phải có BOM Explosion", "Phải có Material Availability Check", "Phải ghi nhận Scrap"],
        "estimated_effort": "7-10 ngày",
        "prompt_role": "Senior MES Consultant với kinh nghiệm triển khai hệ thống điều hành sản xuất cho nhà máy.",
        "prompt_task": "Phân tích và thiết kế quy trình Production Order toàn diện.",
        "prompt_context": "Nhà máy sản xuất cần số hóa quy trình từ kế hoạch đến thành phẩm.",
        "prompt_rules": [
            "PHẢI có BOM Explosion và Material Availability Check.",
            "PHẢI ghi nhận Downtime và Scrap với lý do.",
            "PHẢI có Production Dashboard realtime.",
            "PHẢI tính Actual Cost.",
            "Output PHẢI bao gồm BPMN, BOM Table, WO Data Model."
        ],
        "prompt_example": ""
    },
    # ================================================================
    # MES - OEE
    # ================================================================
    {
        "path": "01-Business-Domain/MES",
        "name": "Phân tích OEE",
        "level": "Level 2 - Business Skill",
        "domain": "MES",
        "tags": ["MES", "OEE", "KPI", "Downtime", "Performance"],
        "purpose": "Đo lường và phân tích hiệu quả thiết bị tổng thể (Overall Equipment Effectiveness), xác định 6 tổn thất lớn (Six Big Losses) và đề xuất giải pháp cải thiện.",
        "when_to_use": "Sử dụng khi nhà máy cần đo lường hiệu suất máy móc và tìm cách cải thiện sản lượng.",
        "prerequisites": ["Đã phân tích Production Order", "Hiểu các loại Downtime"],
        "inputs_detail": [
            {"name": "Dữ liệu máy móc (Machine Data)", "description": "Thời gian chạy, thời gian dừng, lý do dừng.", "required": True, "example": "Máy CNC-01: Tổng thời gian ca = 480p, Planned Downtime (nghỉ trưa) = 30p, Unplanned Downtime (hỏng máy) = 45p"},
            {"name": "Dữ liệu sản xuất", "description": "Số lượng sản phẩm sản xuất và Cycle Time.", "required": True, "example": "Sản lượng = 350 sản phẩm, Cycle Time lý thuyết = 1p/sp, Cycle Time thực tế = 1.2p/sp"},
            {"name": "Dữ liệu chất lượng", "description": "Số lượng hàng tốt và hàng lỗi.", "required": True, "example": "Hàng tốt = 340, Hàng lỗi = 10"}
        ],
        "process_detail": [
            {"step": 1, "title": "Thu thập dữ liệu 3 yếu tố", "description": "Thu thập Availability, Performance, Quality.", "sub_steps": [
                "Availability = (Planned Production Time - Unplanned Downtime) / Planned Production Time",
                "Planned Production Time = Total Time - Planned Downtime (nghỉ trưa, bảo trì kế hoạch)",
                "Performance = (Ideal Cycle Time × Total Pieces) / Operating Time",
                "Quality = Good Pieces / Total Pieces"
            ]},
            {"step": 2, "title": "Tính toán OEE", "description": "OEE = Availability × Performance × Quality.", "sub_steps": [
                "Ví dụ: Availability = 90%, Performance = 85%, Quality = 97%",
                "OEE = 0.90 × 0.85 × 0.97 = 74.2%",
                "World-class OEE = 85%. Trung bình = 60%. Dưới 40% = Cần cải thiện gấp."
            ]},
            {"step": 3, "title": "Phân tích 6 tổn thất lớn (Six Big Losses)", "description": "Xác định nguyên nhân gây giảm OEE.", "sub_steps": [
                "Availability Losses: (1) Breakdowns (Hỏng máy), (2) Setup/Changeover (Chuyển đổi sản phẩm)",
                "Performance Losses: (3) Small Stops (Dừng ngắn), (4) Reduced Speed (Chạy chậm)",
                "Quality Losses: (5) Startup Rejects (Lỗi khởi động), (6) Production Rejects (Lỗi sản xuất)"
            ]},
            {"step": 4, "title": "Đề xuất cải thiện", "description": "Dựa trên phân tích Six Big Losses, đề xuất giải pháp.", "sub_steps": [
                "Availability thấp → Tăng cường bảo trì phòng ngừa (Preventive Maintenance)",
                "Performance thấp → Rà soát Cycle Time, kiểm tra máy chạy không đúng tốc độ",
                "Quality thấp → Cải thiện quy trình QC, đào tạo Operator"
            ]}
        ],
        "outputs_detail": [
            {"name": "Bảng tính OEE", "format": "Markdown Table", "template": "| Yếu tố | Công thức | Giá trị | Ghi chú |\n|---|---|---|---|\n| Planned Production Time | 480p - 30p (nghỉ) | 450p | |\n| Operating Time | 450p - 45p (hỏng máy) | 405p | |\n| Availability | 405/450 | 90% | |\n| Ideal Cycle Time | | 1p/sp | |\n| Total Pieces | | 350 sp | |\n| Performance | (1 × 350)/405 | 86.4% | |\n| Good Pieces | | 340 sp | |\n| Quality | 340/350 | 97.1% | |\n| **OEE** | 90% × 86.4% × 97.1% | **75.5%** | Target: 85% |"},
            {"name": "Dashboard OEE", "format": "Mô tả chi tiết", "template": "Dashboard cần có:\n- Gauge chart hiển thị OEE tổng\n- Bar chart so sánh OEE theo máy\n- Trend line OEE theo tuần/tháng\n- Pareto chart: Top 5 lý do Downtime\n- Breakdown: Availability / Performance / Quality"}
        ],
        "sub_skills": ["Thiết kế Downtime Tracking", "Thiết kế OEE Dashboard", "Six Big Losses Analysis"],
        "business_rules": [
            "BR-MES-OEE-01: Chỉ sử dụng công thức chuẩn OEE = Availability × Performance × Quality.",
            "BR-MES-OEE-02: Planned Downtime (nghỉ trưa, bảo trì kế hoạch) KHÔNG tính vào mất Availability.",
            "BR-MES-OEE-03: Setup/Changeover time phải được ghi nhận riêng, không gộp vào Breakdown.",
            "BR-MES-OEE-04: OEE phải được tính cho từng máy, từng ca, từng sản phẩm."
        ],
        "edge_cases": [
            "Máy chạy nhưng không có hàng để sản xuất (Starving) → Tính vào mất gì?",
            "Máy chạy nhưng không có người vận hành → Tính Availability hay Performance?",
            "Sản phẩm Rework (sửa lại) thành tốt → Tính vào Good hay Reject?"
        ],
        "checklist": [
            "Đã thu thập đủ 3 yếu tố: Availability, Performance, Quality",
            "Đã phân biệt Planned vs Unplanned Downtime",
            "Đã phân tích Six Big Losses",
            "Đã thiết kế Dashboard OEE",
            "Đã có Pareto chart cho Downtime reasons",
            "Đã so sánh OEE theo máy/ca/sản phẩm",
            "Đã đề xuất giải pháp cải thiện"
        ],
        "example": "Xem Bảng tính OEE trong Outputs.",
        "related_skills": ["Phân tích Production Order", "Phân tích Quality Control", "Root Cause Analysis"],
        "quality_criteria": ["Phải đúng công thức OEE", "Phải có Six Big Losses", "Phải có Dashboard design"],
        "estimated_effort": "3-5 ngày",
        "prompt_role": "Senior MES/OEE Analyst chuyên về đo lường hiệu suất nhà máy.",
        "prompt_task": "Phân tích OEE và đề xuất giải pháp cải thiện.",
        "prompt_context": "Nhà máy cần đo lường và nâng cao hiệu suất thiết bị.",
        "prompt_rules": [
            "PHẢI sử dụng công thức chuẩn OEE = A × P × Q.",
            "PHẢI phân biệt Planned và Unplanned Downtime.",
            "PHẢI liệt kê Six Big Losses.",
            "PHẢI thiết kế OEE Dashboard với Gauge, Bar, Trend, Pareto.",
            "PHẢI đề xuất giải pháp cụ thể cho từng yếu tố thấp."
        ],
        "prompt_example": ""
    },
    # ================================================================
    # MES - Quality Control
    # ================================================================
    {
        "path": "01-Business-Domain/MES",
        "name": "Phân tích Quality Control",
        "level": "Level 2 - Business Skill",
        "domain": "MES",
        "tags": ["MES", "QC", "QA", "Quality", "Inspection"],
        "purpose": "Phân tích toàn diện quy trình quản lý chất lượng trong sản xuất, từ IQC (Incoming), PQC (Process), OQC (Outgoing), bao gồm tiêu chuẩn lấy mẫu (AQL), xử lý hàng lỗi (Rework/Scrap) và truy xuất nguồn gốc (Traceability).",
        "when_to_use": "Sử dụng khi nhà máy cần hệ thống QC chuyên nghiệp.",
        "prerequisites": ["Đã phân tích Production Order"],
        "inputs_detail": [
            {"name": "Tiêu chuẩn chất lượng (Quality Standards)", "description": "Các chỉ tiêu kiểm tra cho từng sản phẩm.", "required": True, "example": "Chai nước: Dung tích 500ml ± 5ml, Nắp đóng chặt (lực xoay > 2Nm), Nhãn dán ngay ngắn"},
            {"name": "AQL Level (Acceptable Quality Level)", "description": "Tỷ lệ lỗi chấp nhận được.", "required": True, "example": "AQL = 1.0 (Major), AQL = 2.5 (Minor)"},
            {"name": "Quy trình sản xuất", "description": "Các công đoạn cần kiểm tra.", "required": True, "example": "IQC: Kiểm NVL đầu vào. PQC: Kiểm tại mỗi công đoạn. OQC: Kiểm thành phẩm trước khi nhập kho."}
        ],
        "process_detail": [
            {"step": 1, "title": "IQC - Kiểm tra NVL đầu vào (Incoming QC)", "description": "Kiểm tra chất lượng nguyên vật liệu từ NCC trước khi đưa vào sản xuất.", "sub_steps": [
                "Lấy mẫu theo AQL (VD: Lô 1000 chai → Kiểm 80 chai)",
                "Kiểm tra ngoại quan, kích thước, chức năng",
                "Pass → Nhận hàng. Fail → Reject hoặc Nhận có điều kiện",
                "Ghi nhận kết quả QC vào hồ sơ NCC (Vendor Scorecard)"
            ]},
            {"step": 2, "title": "PQC - Kiểm tra trong quá trình (Process QC)", "description": "Kiểm tra tại các công đoạn sản xuất then chốt.", "sub_steps": [
                "Kiểm tra đầu ca (First Piece Inspection)",
                "Kiểm tra định kỳ (Hourly/Per Batch)",
                "Kiểm tra khi chuyển đổi sản phẩm (Changeover Inspection)",
                "Nếu phát hiện lỗi → Dừng dây chuyền (Stop the Line) nếu Critical"
            ]},
            {"step": 3, "title": "OQC - Kiểm tra thành phẩm (Outgoing QC)", "description": "Kiểm tra lô thành phẩm trước khi nhập kho hoặc xuất cho khách.", "sub_steps": [
                "Lấy mẫu theo AQL",
                "Kiểm tra đầy đủ tiêu chí",
                "Pass → Nhập kho thành phẩm",
                "Fail → Giữ lại (Hold) để điều tra"
            ]},
            {"step": 4, "title": "Xử lý hàng lỗi (NCR - Non-Conformance Report)", "description": "Quy trình khi phát hiện sản phẩm không đạt.", "sub_steps": [
                "Tạo NCR (Non-Conformance Report) mô tả lỗi chi tiết",
                "Phân loại: Rework (Sửa lại), Scrap (Tiêu hủy), Downgrade (Hạ cấp)",
                "Rework → Sửa → QC lại → Nếu Pass thì nhập kho",
                "Scrap → Ghi nhận tiêu hủy, tính vào chi phí",
                "Truy tìm nguyên nhân gốc (Root Cause) để ngăn tái diễn"
            ]}
        ],
        "outputs_detail": [
            {"name": "Quy trình QC (BPMN)", "format": "Mermaid Flowchart", "template": ""},
            {"name": "Ma trận tiêu chí QC", "format": "Markdown Table", "template": "| Giai đoạn | Đối tượng | Tiêu chí | Phương pháp | AQL |\n|---|---|---|---|---|\n| IQC | Vỏ chai PET | Kích thước, Độ trong | Đo + Visual | 1.0 |\n| PQC | Chai đã rót | Dung tích ± 5ml | Cân | - |\n| OQC | Thành phẩm | Toàn bộ | Lấy mẫu | 2.5 |"}
        ],
        "sub_skills": ["Thiết kế AQL Sampling Plan", "Thiết kế NCR Workflow", "Thiết kế Vendor Scorecard", "Thiết kế Traceability"],
        "business_rules": [
            "BR-MES-QC-01: Mọi lô hàng phải qua QC trước khi nhập kho thành phẩm.",
            "BR-MES-QC-02: Lỗi Critical phải dừng dây chuyền ngay lập tức.",
            "BR-MES-QC-03: Hàng Rework chỉ được phép Rework tối đa 1 lần.",
            "BR-MES-QC-04: NCR phải được điều tra Root Cause trong 48 giờ.",
            "BR-MES-QC-05: NCC có tỷ lệ lỗi IQC > 5% phải đánh giá lại hợp đồng."
        ],
        "edge_cases": [
            "Hàng Rework lại fail lần 2 → Bắt buộc Scrap",
            "Lỗi chỉ phát hiện khi hàng đã giao cho khách → Recall (Thu hồi)",
            "QC không đồng ý nhưng Production ép xuất hàng → Escalation"
        ],
        "checklist": [
            "Đã thiết kế IQC, PQC, OQC",
            "Đã có AQL Sampling Plan",
            "Đã có NCR Workflow",
            "Đã có luồng Rework và giới hạn số lần",
            "Đã có Traceability (Truy xuất lô sản phẩm)",
            "Đã tích hợp kết quả QC với OEE (Quality factor)"
        ],
        "example": "Xem Process section.",
        "related_skills": ["Phân tích Production Order", "Phân tích OEE", "Root Cause Analysis"],
        "quality_criteria": ["Phải có IQC/PQC/OQC", "Phải có AQL", "Phải có NCR workflow"],
        "estimated_effort": "5-7 ngày",
        "prompt_role": "Senior QA/QC Analyst chuyên về quản lý chất lượng sản xuất.",
        "prompt_task": "Phân tích và thiết kế quy trình QC toàn diện cho nhà máy.",
        "prompt_context": "Nhà máy cần hệ thống QC số hóa để đảm bảo chất lượng sản phẩm.",
        "prompt_rules": [
            "PHẢI bao gồm 3 giai đoạn: IQC, PQC, OQC.",
            "PHẢI có AQL Sampling Plan.",
            "PHẢI có NCR workflow với Rework/Scrap.",
            "PHẢI có truy xuất nguồn gốc (Traceability)."
        ],
        "prompt_example": ""
    },
    # ================================================================
    # ERP - Procurement
    # ================================================================
    {
        "path": "01-Business-Domain/ERP",
        "name": "Phân tích Procurement",
        "level": "Level 2 - Business Skill",
        "domain": "ERP",
        "tags": ["ERP", "Procurement", "Purchase", "P2P"],
        "purpose": "Phân tích toàn diện quy trình mua hàng (Procure-to-Pay / P2P), từ yêu cầu mua hàng (PR) đến thanh toán cho NCC, bao gồm luồng phê duyệt nhiều cấp, so sánh báo giá NCC, quản lý hợp đồng mua và đánh giá NCC.",
        "when_to_use": "Sử dụng khi xây dựng module Mua hàng cho ERP.",
        "prerequisites": ["Hiểu quy trình mua hàng doanh nghiệp"],
        "inputs_detail": [
            {"name": "Yêu cầu mua hàng (Purchase Requisition - PR)", "description": "Phiếu đề xuất mua hàng từ các phòng ban.", "required": True, "example": "PR-001: Phòng IT đề xuất mua 10 laptop Dell Latitude 5540, ngân sách 250 triệu."},
            {"name": "Danh sách NCC (Vendor List)", "description": "Danh sách nhà cung cấp đã được phê duyệt.", "required": True, "example": "NCC A (Phân phối Dell), NCC B (Tổng đại lý), NCC C (Amazon)"},
            {"name": "Ma trận phê duyệt", "description": "Ai duyệt PR/PO ở mức nào.", "required": True, "example": "< 10tr: Trưởng phòng. 10-100tr: Giám đốc. > 100tr: CEO."}
        ],
        "process_detail": [
            {"step": 1, "title": "Tạo & Duyệt PR", "description": "Nhân viên tạo yêu cầu mua hàng, gửi duyệt theo cấp.", "sub_steps": [
                "Nhân viên tạo PR với mô tả hàng, số lượng, ngân sách",
                "Hệ thống tự động xác định cấp duyệt dựa trên tổng tiền",
                "Người duyệt: Approve / Reject / Request More Info",
                "PR được duyệt → Chuyển sang Bộ phận Mua hàng"
            ]},
            {"step": 2, "title": "Lấy báo giá & So sánh (RFQ)", "description": "Gửi yêu cầu báo giá cho nhiều NCC và so sánh.", "sub_steps": [
                "Gửi RFQ (Request for Quotation) cho ít nhất 3 NCC",
                "Nhận báo giá, nhập vào hệ thống",
                "So sánh trên: Giá, Thời gian giao, Điều kiện thanh toán, Bảo hành",
                "Chọn NCC tốt nhất"
            ]},
            {"step": 3, "title": "Tạo & Duyệt PO", "description": "Tạo Purchase Order và gửi cho NCC.", "sub_steps": [
                "Tạo PO từ PR đã duyệt + Báo giá đã chọn",
                "PO qua luồng phê duyệt (tương tự PR nhưng có thể cấp cao hơn)",
                "PO được duyệt → Gửi cho NCC (Email/EDI)",
                "NCC xác nhận (PO Confirmation)"
            ]},
            {"step": 4, "title": "Nhận hàng & Đối chiếu", "description": "Nhận hàng và đối chiếu 3 bên (3-Way Matching).", "sub_steps": [
                "Nhận hàng → Tạo GRN (liên kết với PO)",
                "3-Way Matching: PO (đã đặt) vs GRN (đã nhận) vs Invoice (hóa đơn NCC)",
                "Nếu khớp → Duyệt thanh toán",
                "Nếu không khớp → Giữ lại (Hold) để điều tra"
            ]},
            {"step": 5, "title": "Thanh toán (Payment)", "description": "Thanh toán cho NCC theo điều kiện hợp đồng.", "sub_steps": [
                "Kế toán duyệt Invoice",
                "Lên lịch thanh toán (Payment Schedule)",
                "Thanh toán (Bank Transfer / LC / Cash)",
                "Cập nhật công nợ NCC"
            ]}
        ],
        "outputs_detail": [
            {"name": "Luồng P2P (BPMN)", "format": "Mermaid Flowchart", "template": ""},
            {"name": "Ma trận phê duyệt", "format": "Markdown Table", "template": "| Giá trị | PR Approver | PO Approver |\n|---|---|---|\n| < 10 triệu | Trưởng phòng | Trưởng phòng Mua |\n| 10 - 100 triệu | Giám đốc | Giám đốc |\n| > 100 triệu | CEO | CEO |"},
            {"name": "Bảng so sánh báo giá", "format": "Markdown Table", "template": "| Tiêu chí | NCC A | NCC B | NCC C |\n|---|---|---|---|\n| Đơn giá | 25tr | 24tr | 26tr |\n| Giao hàng | 3 ngày | 7 ngày | 2 ngày |\n| Thanh toán | 30 ngày | 45 ngày | COD |\n| Bảo hành | 12 tháng | 24 tháng | 12 tháng |"}
        ],
        "sub_skills": ["Thiết kế Approval Workflow", "Thiết kế RFQ Process", "Thiết kế 3-Way Matching", "Thiết kế Vendor Evaluation"],
        "business_rules": [
            "BR-ERP-PO-01: PO > 50 triệu bắt buộc phải có ít nhất 3 báo giá.",
            "BR-ERP-PO-02: 3-Way Matching chênh lệch > 2% phải Hold Invoice.",
            "BR-ERP-PO-03: NCC mới phải qua quy trình Vendor Onboarding trước khi tạo PO.",
            "BR-ERP-PO-04: PR quá 7 ngày chưa duyệt phải escalate lên cấp trên."
        ],
        "edge_cases": [
            "NCC giao hàng trước khi PO được duyệt → Xử lý Retrospective PO?",
            "Cần mua khẩn cấp (Emergency Purchase) → Bỏ qua RFQ được không?",
            "NCC phá sản giữa chừng → Chuyển sang NCC backup"
        ],
        "checklist": [
            "Đã thiết kế luồng PR → RFQ → PO → GRN → Invoice → Payment",
            "Đã có ma trận phê duyệt theo giá trị",
            "Đã có 3-Way Matching",
            "Đã có quy trình đánh giá NCC (Vendor Scorecard)",
            "Đã có Emergency Purchase procedure"
        ],
        "example": "Xem Process section.",
        "related_skills": ["Phân tích Inbound Flow", "Phân tích Kế toán công nợ"],
        "quality_criteria": ["Phải có Approval Matrix", "Phải có 3-Way Matching", "Phải có RFQ comparison"],
        "estimated_effort": "5-7 ngày",
        "prompt_role": "Senior ERP/Procurement Analyst.",
        "prompt_task": "Phân tích và thiết kế quy trình Procure-to-Pay.",
        "prompt_context": "Doanh nghiệp cần quản lý mua hàng chặt chẽ, chống thất thoát.",
        "prompt_rules": [
            "PHẢI bao gồm luồng PR → RFQ → PO → GRN → Invoice → Payment.",
            "PHẢI có ma trận phê duyệt nhiều cấp.",
            "PHẢI có 3-Way Matching.",
            "PHẢI có so sánh báo giá ít nhất 3 NCC."
        ],
        "prompt_example": ""
    },
    # ================================================================
    # HRM - Chấm công
    # ================================================================
    {
        "path": "01-Business-Domain/HRM",
        "name": "Phân tích Chấm công",
        "level": "Level 2 - Business Skill",
        "domain": "HRM",
        "tags": ["HRM", "Attendance", "Time", "Shift", "Leave"],
        "purpose": "Phân tích toàn diện quy trình quản lý thời gian làm việc (Time & Attendance), bao gồm thiết lập ca làm việc (Shift), tích hợp máy chấm công, xử lý đi trễ/về sớm/vắng mặt, quản lý nghỉ phép (Leave Management) và tính làm thêm giờ (OT).",
        "when_to_use": "Sử dụng khi xây dựng module Chấm công cho HRM.",
        "prerequisites": ["Hiểu Luật Lao động Việt Nam về giờ làm việc và OT"],
        "inputs_detail": [
            {"name": "Cấu trúc ca làm việc", "description": "Giờ vào/ra của các ca.", "required": True, "example": "Ca Hành chính: 08:00-17:00 (nghỉ trưa 12:00-13:00). Ca 1: 06:00-14:00. Ca 2: 14:00-22:00. Ca 3: 22:00-06:00."},
            {"name": "Dữ liệu máy chấm công", "description": "Log vào/ra từ máy vân tay, thẻ từ, Face ID.", "required": True, "example": "Employee ID: E001, Check-in: 07:58, Check-out: 17:05, Machine: Cổng chính"},
            {"name": "Chính sách nghỉ phép", "description": "Số ngày phép/năm, điều kiện nghỉ.", "required": True, "example": "12 ngày phép năm (sau 12 tháng). Nghỉ ốm: Theo sổ BHXH. Nghỉ không lương: Tối đa 5 ngày/năm."}
        ],
        "process_detail": [
            {"step": 1, "title": "Thiết lập Master Data", "description": "Cấu hình ca làm việc, lịch công ty, ngày lễ.", "sub_steps": [
                "Tạo các Shift với giờ vào/ra chính xác",
                "Cấu hình Tolerance (VD: Trễ ≤ 5 phút vẫn tính đúng giờ)",
                "Cấu hình ngày lễ, ngày nghỉ bù",
                "Gán ca cho từng nhân viên (Fixed Shift hoặc Rotating Shift)"
            ]},
            {"step": 2, "title": "Thu thập & Xử lý dữ liệu chấm công", "description": "Đồng bộ dữ liệu từ máy chấm công về hệ thống.", "sub_steps": [
                "API/File sync từ máy chấm công mỗi 5-15 phút",
                "Ghép cặp Check-in / Check-out (Matching)",
                "Phát hiện bất thường: Chỉ có Check-in không có Check-out, hoặc ngược lại",
                "Tự động tính giờ làm việc thực tế",
                "So sánh với ca đã gán → Tính Trễ / Sớm / Vắng"
            ]},
            {"step": 3, "title": "Quản lý nghỉ phép (Leave Management)", "description": "Quy trình đăng ký và phê duyệt nghỉ phép.", "sub_steps": [
                "Nhân viên tạo đơn nghỉ phép trên hệ thống (Loại phép, Ngày, Lý do)",
                "Quản lý duyệt → Trừ phép còn lại",
                "Đối soát với dữ liệu chấm công: Vắng mặt nhưng chưa có đơn → Cảnh báo",
                "Hệ thống hiển thị số ngày phép còn lại realtime"
            ]},
            {"step": 4, "title": "Tính OT (Overtime)", "description": "Ghi nhận và phê duyệt làm thêm giờ.", "sub_steps": [
                "Đăng ký OT trước (Pre-approved) hoặc hệ thống tự phát hiện giờ dư",
                "OT ngày thường: x150%. OT ngày nghỉ: x200%. OT ngày lễ: x300%",
                "Giới hạn OT: Không quá 40h/tháng (theo Luật LĐ VN)",
                "Manager duyệt OT → Chuyển sang Payroll"
            ]},
            {"step": 5, "title": "Tổng hợp bảng công", "description": "Tạo bảng công tổng hợp cuối tháng.", "sub_steps": [
                "Tổng hợp: Số ngày đi làm, Số ngày nghỉ phép, Số ngày vắng, Số giờ OT",
                "Quản lý xác nhận bảng công cho từng nhân viên",
                "HR duyệt bảng công tổng → Chuyển cho Payroll",
                "Lock bảng công (không cho sửa) sau khi duyệt"
            ]}
        ],
        "outputs_detail": [
            {"name": "Bảng công mẫu", "format": "Markdown Table", "template": "| Nhân viên | Ngày đi làm | Trễ (lần) | Vắng KP | Phép năm | OT (giờ) | Ghi chú |\n|---|---|---|---|---|---|---|\n| Nguyễn Văn A | 22 | 2 | 0 | 1 | 8 | |\n| Trần Thị B | 20 | 0 | 1 | 2 | 12 | Vắng ngày 15 chưa có đơn |"}
        ],
        "sub_skills": ["Thiết kế Shift Management", "Thiết kế Leave Management", "Thiết kế OT Calculation", "Thiết kế Attendance Dashboard"],
        "business_rules": [
            "BR-HRM-ATT-01: Trễ ≤ 5 phút không tính phạt. Trễ > 5 phút tính nửa công sáng.",
            "BR-HRM-ATT-02: Vắng không phép (Absent without Leave) > 3 ngày/tháng → Cảnh cáo.",
            "BR-HRM-ATT-03: OT phải được đăng ký/duyệt trước, không chấp nhận OT tự phát.",
            "BR-HRM-ATT-04: Bảng công phải được Lock sau ngày 5 của tháng tiếp theo.",
            "BR-HRM-ATT-05: Nhân viên Ca đêm (22:00-06:00) được phụ cấp đêm 30%."
        ],
        "edge_cases": [
            "Máy chấm công hỏng → Cho phép chấm công thủ công (Manual Attendance)",
            "Nhân viên đi công tác không thể chấm công → Xử lý Business Trip Attendance",
            "Làm việc từ xa (WFH) → Chấm công bằng gì?",
            "Nhân viên quẹt thẻ hộ người khác → Gian lận chấm công (Buddy Punching)"
        ],
        "checklist": [
            "Đã thiết kế cấu trúc Ca làm việc (Shift)",
            "Đã tích hợp máy chấm công (API/File)",
            "Đã xử lý ghép cặp Check-in/Check-out",
            "Đã có quy tắc tính Trễ/Sớm/Vắng",
            "Đã thiết kế Leave Management (Đăng ký, Duyệt, Trừ phép)",
            "Đã thiết kế OT Registration & Approval",
            "Đã tổng hợp bảng công cuối tháng",
            "Đã có chống gian lận chấm công"
        ],
        "example": "Xem bảng công mẫu trong Outputs.",
        "related_skills": ["Phân tích Payroll", "Phân tích KPI và Đánh giá"],
        "quality_criteria": ["Phải có Shift management", "Phải tính OT theo Luật LĐ VN", "Phải có Leave Management"],
        "estimated_effort": "5-7 ngày",
        "prompt_role": "Senior HRM Analyst chuyên về Time & Attendance.",
        "prompt_task": "Phân tích và thiết kế hệ thống chấm công toàn diện.",
        "prompt_context": "Doanh nghiệp có nhiều ca làm việc, cần số hóa chấm công.",
        "prompt_rules": [
            "PHẢI tuân thủ Luật Lao động Việt Nam về OT (x150%, x200%, x300%, giới hạn 40h/tháng).",
            "PHẢI có Leave Management.",
            "PHẢI xử lý máy chấm công hỏng (Manual fallback).",
            "PHẢI có bảng công tổng hợp cuối tháng."
        ],
        "prompt_example": ""
    }
]

if __name__ == "__main__":
    print("=== Expanding Business Domain: MES + ERP + HRM Skills ===")
    run(skills)
