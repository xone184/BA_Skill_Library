import sys
sys.path.insert(0, r"e:\BA Skill Library")
from skill_generator import run

skills = [
    # ================================================================
    # WMS - Inbound
    # ================================================================
    {
        "path": "01-Business-Domain/WMS",
        "name": "Phân tích Inbound Flow",
        "level": "Level 2 - Business Skill",
        "domain": "WMS",
        "tags": ["WMS", "Inbound", "Receiving", "Putaway", "GRN"],
        "purpose": "Phân tích toàn diện quy trình nhập kho hàng hóa, từ lúc nhận thông báo giao hàng (ASN) đến khi hàng được cất lên kệ (Putaway), bao gồm kiểm tra chất lượng đầu vào, xử lý chênh lệch so với PO, in mã vạch/QR code và chiến lược Putaway tự động.",
        "when_to_use": "Sử dụng khi:\n- Xây dựng module Nhập kho cho hệ thống WMS.\n- Cần tối ưu hóa quy trình nhận hàng tại dock.\n- Cần thiết kế chiến lược cất hàng (Putaway Strategy) tự động.",
        "prerequisites": ["Hiểu cơ bản về quản lý kho", "Biết các loại hàng hóa (Pallet, Thùng, Lẻ)"],
        "inputs_detail": [
            {"name": "Purchase Order (PO)", "description": "Đơn đặt hàng từ module Mua hàng, chứa thông tin hàng cần nhận.", "required": True, "example": "PO-2024-001: 100 thùng Sữa TH True Milk, 50 thùng Nước ngọt Pepsi"},
            {"name": "Advance Shipping Notice (ASN)", "description": "Thông báo giao hàng trước từ nhà cung cấp.", "required": False, "example": "NCC ABC sẽ giao 100 thùng vào ngày 15/7, xe biển số 51C-12345"},
            {"name": "Sơ đồ kho (Warehouse Layout)", "description": "Bản đồ kho với các Zone, Aisle, Rack, Bin.", "required": True, "example": "Zone A: Hàng khô. Zone B: Hàng lạnh. Zone C: Hàng nguy hiểm."}
        ],
        "process_detail": [
            {"step": 1, "title": "Tiếp nhận thông báo giao hàng", "description": "Hệ thống nhận ASN từ NCC (qua API/Email/Nhập tay) và tạo lịch nhận hàng tại dock.", "sub_steps": [
                "Kiểm tra ASN có khớp với PO đang mở không",
                "Đặt lịch dock (Dock Scheduling) để tránh ùn tắc",
                "Thông báo cho bộ phận kho chuẩn bị nhân lực dỡ hàng",
                "In phiếu tiếp nhận hàng (Receiving Slip)"
            ]},
            {"step": 2, "title": "Dỡ hàng & Kiểm đếm (Unloading & Tally)", "description": "Nhân viên kho dỡ hàng và kiểm đếm số lượng thực tế so với PO.", "sub_steps": [
                "Dỡ hàng từ xe tải vào khu vực Staging (Tạm)",
                "Quét mã vạch từng thùng/pallet (hoặc đếm thủ công nếu chưa có barcode)",
                "So khớp số lượng thực nhận vs số lượng trên PO",
                "Ghi nhận chênh lệch: Thừa (Overage), Thiếu (Shortage), Hư hỏng (Damage)",
                "Chụp ảnh làm bằng chứng nếu hàng bị hư hỏng"
            ]},
            {"step": 3, "title": "Kiểm tra chất lượng đầu vào (QC Inbound)", "description": "Kiểm tra chất lượng hàng nhận theo tiêu chuẩn đã quy định.", "sub_steps": [
                "Kiểm tra hạn sử dụng (Expiry Date) cho hàng thực phẩm/dược phẩm",
                "Kiểm tra ngoại quan (Visual Inspection): Bao bì rách, ẩm ướt, biến dạng",
                "Lấy mẫu kiểm tra (Sampling) theo AQL nếu hàng sản xuất",
                "Quyết định: Accept (Nhận), Reject (Từ chối), Conditional Accept (Nhận có điều kiện)"
            ]},
            {"step": 4, "title": "Tạo phiếu nhận hàng (Goods Receipt Note - GRN)", "description": "Ghi nhận chính thức hàng đã nhập kho vào hệ thống.", "sub_steps": [
                "Tạo GRN liên kết với PO",
                "Cập nhật tồn kho (Inventory) tức thì",
                "In tem mã vạch/QR code dán lên từng Pallet/Thùng nếu NCC chưa dán",
                "Ghi nhận Lot Number, Batch Number, Serial Number (nếu có)"
            ]},
            {"step": 5, "title": "Cất hàng lên kệ (Putaway)", "description": "Di chuyển hàng từ khu vực Staging lên vị trí lưu trữ cố định trên kệ.", "sub_steps": [
                "Hệ thống gợi ý vị trí cất (Putaway Suggestion) dựa trên chiến lược",
                "Chiến lược Fixed Location: Mỗi SKU có vị trí cố định",
                "Chiến lược Random Location: Cất bất kỳ ô trống nào gần nhất",
                "Chiến lược Zone-based: Hàng nhanh (Fast-moving) → Zone gần lối ra, Hàng chậm → Zone xa",
                "Chiến lược FEFO: Hàng hết hạn sớm nhất cất ở vị trí dễ lấy nhất",
                "Nhân viên quét mã vạch tại vị trí cất để xác nhận (Putaway Confirmation)"
            ]}
        ],
        "outputs_detail": [
            {"name": "Quy trình Nhập kho (BPMN)", "format": "Mermaid Flowchart", "template": "graph TD\n    A[Nhận ASN] --> B[Đặt lịch Dock]\n    B --> C[Dỡ hàng]\n    C --> D[Kiểm đếm Tally]\n    D --> E{Chênh lệch?}\n    E -->|Không| F[QC Inbound]\n    E -->|Có| G[Ghi nhận chênh lệch & Xử lý]\n    G --> F\n    F --> H{QC Pass?}\n    H -->|Có| I[Tạo GRN + In tem]\n    H -->|Không| J[Reject / Return NCC]\n    I --> K[Putaway Suggestion]\n    K --> L[Cất hàng & Confirm]"},
            {"name": "Cấu trúc dữ liệu GRN", "format": "Markdown Table", "template": "| Trường | Kiểu | Mô tả |\n|---|---|---|\n| grn_id | INT (PK) | Mã phiếu nhận |\n| po_id | INT (FK) | Liên kết PO |\n| supplier_id | INT (FK) | Nhà cung cấp |\n| received_date | DATETIME | Ngày nhận |\n| status | ENUM | Draft/Confirmed/Cancelled |\n| total_qty_ordered | DECIMAL | SL đặt |\n| total_qty_received | DECIMAL | SL thực nhận |\n| created_by | INT (FK) | Người tạo |"},
            {"name": "Ma trận Putaway Strategy", "format": "Markdown Table", "template": "| Loại hàng | Chiến lược | Zone | Lý do |\n|---|---|---|---|\n| Fast-moving | Zone-based | A (gần dock) | Giảm di chuyển |\n| Slow-moving | Random | C (xa dock) | Tối ưu diện tích |\n| Có HSD | FEFO | B | Hết hạn sớm lấy trước |\n| Nguy hiểm | Fixed | D (riêng biệt) | An toàn |"}
        ],
        "sub_skills": ["Thiết kế Dock Scheduling", "Thiết kế QC Inbound", "Thiết kế Putaway Strategy", "Thiết kế Barcode/Label"],
        "business_rules": [
            "BR-WMS-IN-01: Không được nhập hàng nếu không có PO hoặc ASN.",
            "BR-WMS-IN-02: Hàng có HSD dưới 30% thời gian sử dụng → Từ chối nhận.",
            "BR-WMS-IN-03: Chênh lệch số lượng > 5% phải có phê duyệt của Quản lý kho.",
            "BR-WMS-IN-04: Mỗi Pallet/Thùng nhập kho phải có mã vạch trước khi Putaway.",
            "BR-WMS-IN-05: Hàng nguy hiểm (Dangerous Goods) chỉ được cất ở Zone riêng.",
            "BR-WMS-IN-06: Putaway phải hoàn thành trong vòng 4 giờ kể từ khi tạo GRN."
        ],
        "edge_cases": [
            "NCC giao hàng không có trong PO (Unexpected Delivery) → Reject hay tạo PO bổ sung?",
            "Hàng bị hư hỏng 50% → Nhận phần tốt hay reject toàn bộ?",
            "Kho hết chỗ trống → Putaway đưa đi đâu? (Overflow handling)",
            "Mất điện khi đang scan → Dữ liệu có được lưu nháp không?",
            "NCC giao sai hàng (Wrong item) → Luồng xử lý Return to Vendor"
        ],
        "checklist": [
            "Đã thiết kế luồng tiếp nhận ASN",
            "Đã thiết kế Dock Scheduling",
            "Đã có quy trình kiểm đếm (Tally) và xử lý chênh lệch",
            "Đã có QC Inbound (Kiểm tra chất lượng đầu vào)",
            "Đã thiết kế in tem mã vạch/QR code",
            "Đã thiết kế chiến lược Putaway (Fixed/Random/Zone-based/FEFO)",
            "Đã có xử lý hàng hư hỏng (Damage handling)",
            "Đã có xử lý hàng thừa/thiếu so với PO",
            "Đã quản lý Lot/Batch/Serial Number",
            "Đã có thông báo cho Kế toán khi tạo GRN thành công"
        ],
        "example": "Xem Process section để biết chi tiết luồng nhập kho end-to-end.",
        "related_skills": ["Phân tích Outbound Flow", "Phân tích Inventory Management", "Phân tích Procurement"],
        "quality_criteria": ["Phải có ít nhất 5 bước quy trình chi tiết", "Phải có Putaway Strategy", "Phải xử lý chênh lệch", "Phải có QC Inbound"],
        "estimated_effort": "5-7 ngày",
        "prompt_role": "Senior WMS Consultant với kinh nghiệm triển khai hệ thống quản lý kho cho các nhà máy sản xuất và trung tâm phân phối lớn tại Việt Nam.",
        "prompt_task": "Phân tích và thiết kế quy trình nhập kho hoàn chỉnh cho hệ thống WMS.",
        "prompt_context": "Doanh nghiệp sản xuất hoặc phân phối cần hệ thống quản lý kho chuyên nghiệp thay thế Excel.",
        "prompt_rules": [
            "PHẢI bao gồm đủ 5 bước: ASN → Tally → QC → GRN → Putaway.",
            "PHẢI thiết kế chiến lược Putaway phù hợp với loại hàng.",
            "PHẢI xử lý triệt để hàng thừa/thiếu/hư hỏng.",
            "PHẢI có mã vạch/QR cho mọi đơn vị hàng trước khi Putaway.",
            "PHẢI quản lý Lot/Batch cho hàng có HSD.",
            "Output PHẢI bao gồm BPMN, Data Model, và Putaway Strategy Matrix."
        ],
        "prompt_example": ""
    },
    # ================================================================
    # WMS - Outbound
    # ================================================================
    {
        "path": "01-Business-Domain/WMS",
        "name": "Phân tích Outbound Flow",
        "level": "Level 2 - Business Skill",
        "domain": "WMS",
        "tags": ["WMS", "Outbound", "Picking", "Packing", "Shipping"],
        "purpose": "Phân tích toàn diện quy trình xuất kho, từ lúc nhận lệnh xuất (Sales Order/Transfer Order) đến khi hàng rời kho, bao gồm các chiến lược Picking (Wave, Zone, Batch), đóng gói (Packing), kiểm tra xuất (Shipping Verification) và tích hợp đơn vị vận chuyển.",
        "when_to_use": "Sử dụng khi:\n- Xây dựng module Xuất kho cho WMS.\n- Cần tối ưu hóa năng suất nhặt hàng (Picking Productivity).\n- Cần tích hợp với các hãng vận chuyển (GHN, GHTK, Viettel Post).",
        "prerequisites": ["Đã phân tích Inbound Flow", "Hiểu nguyên tắc FIFO/FEFO/LIFO"],
        "inputs_detail": [
            {"name": "Sales Order (SO) / Transfer Order", "description": "Lệnh xuất hàng từ module Bán hàng hoặc Điều phối.", "required": True, "example": "SO-2024-500: 20 thùng Sữa TH (Lot #L001, HSD 15/12/2024), giao cho KH ABC tại HCM"},
            {"name": "Nguyên tắc xuất kho", "description": "FIFO, FEFO, LIFO hoặc theo Lot/Batch chỉ định.", "required": True, "example": "Hàng thực phẩm: FEFO (hết hạn sớm nhất xuất trước). Hàng công nghiệp: FIFO."},
            {"name": "Thông tin vận chuyển", "description": "Đơn vị vận chuyển, địa chỉ giao, thời gian cắt đơn.", "required": False, "example": "GHN, cut-off time 14:00 hàng ngày"}
        ],
        "process_detail": [
            {"step": 1, "title": "Tiếp nhận & Xác nhận lệnh xuất", "description": "Hệ thống nhận SO/Transfer Order và kiểm tra tồn kho khả dụng (Available Stock).", "sub_steps": [
                "Kiểm tra tồn kho đủ không (Available Qty >= Ordered Qty)",
                "Phân bổ tồn kho (Allocation/Reservation) để khóa hàng cho đơn này",
                "Nếu thiếu hàng: Partial shipment hay chờ đủ hàng? (Backorder handling)",
                "Tạo Wave (nhóm nhiều SO để xử lý cùng lúc) hoặc xử lý từng SO"
            ]},
            {"step": 2, "title": "Lấy hàng (Picking)", "description": "Nhân viên kho di chuyển đến vị trí trên kệ và lấy đúng số lượng hàng.", "sub_steps": [
                "Hệ thống tạo Pick List (Danh sách lấy hàng) với vị trí cụ thể (Zone-Aisle-Rack-Bin)",
                "Áp dụng FIFO/FEFO để xác định lấy Lot/Batch nào trước",
                "Chiến lược Picking:",
                "  - Discrete Picking: 1 nhân viên xử lý 1 đơn → Chính xác nhưng chậm",
                "  - Batch Picking: 1 nhân viên gom nhiều đơn → Nhanh, giảm di chuyển",
                "  - Zone Picking: Mỗi nhân viên chỉ pick trong Zone được gán → Chuyên môn hóa",
                "  - Wave Picking: Gom nhiều đơn cùng Zone/cùng hãng vận chuyển → Tối ưu nhất",
                "Nhân viên quét mã vạch tại vị trí Pick để xác nhận (Pick Confirmation)",
                "Nếu hết hàng tại vị trí Pick → Trigger Replenishment"
            ]},
            {"step": 3, "title": "Đóng gói (Packing)", "description": "Nhân viên đóng gói hàng vào thùng carton và dán nhãn vận chuyển.", "sub_steps": [
                "Kiểm tra lại số lượng & chủng loại hàng (Packing Verification)",
                "Chọn loại thùng carton phù hợp kích thước",
                "In phiếu giao hàng (Delivery Note) kèm trong thùng",
                "In nhãn vận chuyển (Shipping Label) với mã vạch tracking",
                "Cân trọng lượng thùng và ghi nhận vào hệ thống"
            ]},
            {"step": 4, "title": "Xuất hàng (Shipping)", "description": "Giao hàng cho đơn vị vận chuyển.", "sub_steps": [
                "Tập kết thùng tại khu vực Staging Outbound theo hãng vận chuyển",
                "Quét mã vạch Shipping Label khi bàn giao cho tài xế",
                "In Biên bản giao nhận (Handover Form)",
                "Cập nhật trạng thái SO: Shipped",
                "Gửi thông tin tracking cho khách hàng (Email/SMS)"
            ]}
        ],
        "outputs_detail": [
            {"name": "Quy trình Xuất kho (BPMN)", "format": "Mermaid Flowchart", "template": "graph TD\n    A[Nhận SO] --> B{Tồn kho đủ?}\n    B -->|Có| C[Allocation]\n    B -->|Không| D[Backorder / Partial]\n    C --> E[Tạo Pick List]\n    E --> F[Picking - Quét mã vạch]\n    F --> G[Packing - Đóng gói]\n    G --> H[In Shipping Label]\n    H --> I[Staging Outbound]\n    I --> J[Bàn giao cho Vận chuyển]\n    J --> K[Cập nhật Shipped]"},
            {"name": "Ma trận Picking Strategy", "format": "Markdown Table", "template": "| Chiến lược | Phù hợp khi | Ưu điểm | Nhược điểm |\n|---|---|---|---|\n| Discrete | Ít đơn, hàng giá trị cao | Chính xác cao | Chậm, di chuyển nhiều |\n| Batch | Nhiều đơn nhỏ cùng SKU | Nhanh | Cần phân loại sau pick |\n| Zone | Kho lớn, nhiều Zone | Chuyên môn hóa | Cần tổng hợp cuối |\n| Wave | Nhiều đơn cùng hãng vận chuyển | Tối ưu nhất | Phức tạp thiết lập |"},
            {"name": "Cấu trúc Pick List", "format": "Markdown Table", "template": "| SO | SKU | Tên hàng | Qty | Location | Lot | Status |\n|---|---|---|---|---|---|---|\n| SO-001 | SKU-A01 | Sữa TH 1L | 20 | A-01-03-B02 | L001 | Pending |"}
        ],
        "sub_skills": ["Thiết kế Picking Strategy", "Thiết kế Packing Station", "Thiết kế Shipping Integration", "Thiết kế Backorder Logic"],
        "business_rules": [
            "BR-WMS-OUT-01: Hàng thực phẩm bắt buộc xuất theo FEFO (hết hạn sớm lấy trước).",
            "BR-WMS-OUT-02: Không xuất hàng có HSD dưới 30 ngày cho khách hàng (trừ khi khách đồng ý).",
            "BR-WMS-OUT-03: Mỗi lần Pick phải quét mã vạch xác nhận đúng vị trí và đúng hàng.",
            "BR-WMS-OUT-04: Đơn hàng phải hoàn thành Packing trước cut-off time của hãng vận chuyển.",
            "BR-WMS-OUT-05: Partial Shipment phải được khách hàng đồng ý trước."
        ],
        "edge_cases": [
            "Hàng hết tại vị trí Pick nhưng còn tại Reserve Zone → Trigger Replenishment hay pick từ Reserve?",
            "Khách yêu cầu giao hàng theo Lot chỉ định nhưng Lot đó đã cất ở vị trí khó lấy → Xử lý sao?",
            "Nhiều SO cùng 1 SKU nhưng tồn kho chỉ đủ 1 SO → Ưu tiên SO nào? (Priority rules)",
            "Picking nhầm hàng → Luồng xử lý Return-to-Shelf",
            "Hãng vận chuyển đến trễ → Hàng đã packed nằm ở Staging quá lâu"
        ],
        "checklist": [
            "Đã kiểm tra tồn kho trước khi tạo Pick List (Allocation)",
            "Đã thiết kế chiến lược Picking phù hợp (Discrete/Batch/Zone/Wave)",
            "Đã áp dụng nguyên tắc FIFO/FEFO cho Picking",
            "Đã thiết kế Packing Station với Verification",
            "Đã tích hợp in Shipping Label",
            "Đã thiết kế xử lý Backorder (Thiếu hàng)",
            "Đã có Replenishment trigger khi vị trí Pick hết hàng",
            "Đã có luồng bàn giao cho hãng vận chuyển",
            "Đã gửi thông tin tracking cho khách hàng"
        ],
        "example": "Xem Process section.",
        "related_skills": ["Phân tích Inbound Flow", "Phân tích Inventory Management", "Phân tích Replenishment"],
        "quality_criteria": ["Phải có ít nhất 4 bước (Allocation → Pick → Pack → Ship)", "Phải có Picking Strategy Matrix", "Phải xử lý Backorder"],
        "estimated_effort": "5-7 ngày",
        "prompt_role": "Senior WMS Consultant chuyên về Outbound/Fulfillment optimization.",
        "prompt_task": "Phân tích và thiết kế quy trình xuất kho hoàn chỉnh.",
        "prompt_context": "Doanh nghiệp cần hệ thống WMS để xử lý hàng trăm đơn xuất mỗi ngày.",
        "prompt_rules": [
            "PHẢI bao gồm đủ 4 bước: Allocation → Picking → Packing → Shipping.",
            "PHẢI đề xuất Picking Strategy phù hợp với quy mô kho.",
            "PHẢI áp dụng FIFO/FEFO cho hàng có HSD.",
            "PHẢI xử lý Backorder khi thiếu hàng.",
            "Output PHẢI bao gồm BPMN, Picking Strategy Matrix, và Pick List Template."
        ],
        "prompt_example": ""
    },
    # ================================================================
    # WMS - Inventory Management
    # ================================================================
    {
        "path": "01-Business-Domain/WMS",
        "name": "Phân tích Inventory Management",
        "level": "Level 2 - Business Skill",
        "domain": "WMS",
        "tags": ["WMS", "Inventory", "Cycle Count", "Stock"],
        "purpose": "Phân tích toàn diện quy trình quản lý tồn kho, bao gồm kiểm kê (Cycle Count / Full Count), điều chỉnh tồn kho (Stock Adjustment), luân chuyển nội bộ (Internal Transfer), quản lý tồn kho tối thiểu/tối đa (Min-Max) và các báo cáo phân tích tồn kho.",
        "when_to_use": "Sử dụng khi xây dựng module Inventory cho WMS hoặc ERP.",
        "prerequisites": ["Đã phân tích Inbound/Outbound Flow"],
        "inputs_detail": [
            {"name": "Dữ liệu tồn kho hiện tại", "description": "Snapshot số lượng hàng hiện có trên hệ thống.", "required": True, "example": "SKU-A01: On-hand = 500, Allocated = 120, Available = 380"},
            {"name": "Phương pháp kiểm kê", "description": "Full Count (Kiểm kê toàn bộ) hay Cycle Count (Kiểm kê luân phiên).", "required": True, "example": "Cycle Count hàng ngày theo phân loại ABC: Loại A kiểm hàng tuần, Loại B hàng tháng, Loại C hàng quý"},
            {"name": "Ngưỡng Min-Max", "description": "Mức tồn kho tối thiểu và tối đa cho từng SKU.", "required": False, "example": "SKU-A01: Min = 100, Max = 500, Reorder Point = 200"}
        ],
        "process_detail": [
            {"step": 1, "title": "Phân loại tồn kho (ABC Analysis)", "description": "Phân loại hàng hóa theo giá trị/tần suất để ưu tiên quản lý.", "sub_steps": [
                "Loại A (20% SKU, 80% giá trị): Kiểm kê thường xuyên, quản lý chặt",
                "Loại B (30% SKU, 15% giá trị): Kiểm kê định kỳ",
                "Loại C (50% SKU, 5% giá trị): Kiểm kê ít thường xuyên",
                "Kết hợp XYZ Analysis (theo biến động nhu cầu) nếu cần"
            ]},
            {"step": 2, "title": "Kiểm kê (Counting)", "description": "Thực hiện kiểm đếm tồn kho thực tế.", "sub_steps": [
                "Cycle Count: Chọn ngẫu nhiên hoặc theo lịch một số SKU/Location để đếm mỗi ngày",
                "Full Count: Đóng kho (Freeze) và kiểm toàn bộ (thường cuối năm)",
                "Blind Count: Nhân viên đếm mà không thấy số lượng hệ thống → Giảm bias",
                "Quét mã vạch tại từng Location và nhập số lượng đếm được"
            ]},
            {"step": 3, "title": "Xử lý chênh lệch (Variance)", "description": "So sánh số đếm thực tế với số trên hệ thống.", "sub_steps": [
                "Nếu chênh lệch ≤ Tolerance (VD: ≤ 2%) → Tự động điều chỉnh",
                "Nếu chênh lệch > Tolerance → Yêu cầu đếm lại (Recount)",
                "Nếu sau Recount vẫn chênh → Quản lý kho phê duyệt Stock Adjustment",
                "Ghi nhận lý do chênh lệch (Mất mát, Hư hỏng, Lỗi nhập liệu)"
            ]},
            {"step": 4, "title": "Luân chuyển nội bộ (Internal Transfer)", "description": "Di chuyển hàng giữa các kho hoặc các Zone trong cùng kho.", "sub_steps": [
                "Tạo Transfer Order (Kho A → Kho B)",
                "Trừ tồn kho Kho A, Cộng tồn kho Kho B",
                "Hỗ trợ Transfer đang trên đường (In-Transit stock)"
            ]},
            {"step": 5, "title": "Báo cáo & Cảnh báo", "description": "Dashboard và cảnh báo tồn kho.", "sub_steps": [
                "Cảnh báo tồn kho dưới MIN (Low Stock Alert)",
                "Cảnh báo tồn kho vượt MAX (Overstock Alert)",
                "Cảnh báo hàng sắp hết hạn (Expiring Soon Alert)",
                "Báo cáo: Inventory Aging (Hàng tồn quá lâu), Turnover Rate, Stock Value"
            ]}
        ],
        "outputs_detail": [
            {"name": "Quy trình Kiểm kê (BPMN)", "format": "Mermaid Flowchart", "template": ""},
            {"name": "Bảng phân loại ABC", "format": "Markdown Table", "template": "| Loại | % SKU | % Giá trị | Tần suất kiểm kê | VD |\n|---|---|---|---|---|\n| A | 20% | 80% | Hàng tuần | Linh kiện đắt tiền |\n| B | 30% | 15% | Hàng tháng | Vật tư phổ thông |\n| C | 50% | 5% | Hàng quý | Văn phòng phẩm |"},
            {"name": "Cấu trúc dữ liệu Inventory", "format": "Markdown Table", "template": "| Trường | Kiểu | Mô tả |\n|---|---|---|\n| sku | VARCHAR | Mã hàng |\n| warehouse_id | INT (FK) | Kho |\n| location | VARCHAR | Vị trí kệ |\n| on_hand_qty | DECIMAL | Tồn thực |\n| allocated_qty | DECIMAL | Đã đặt |\n| available_qty | DECIMAL | Khả dụng |\n| lot_number | VARCHAR | Số lô |\n| expiry_date | DATE | Hạn dùng |"}
        ],
        "sub_skills": ["Thiết kế ABC Analysis", "Thiết kế Cycle Count Plan", "Thiết kế Stock Adjustment Approval", "Thiết kế Min-Max Rules"],
        "business_rules": [
            "BR-WMS-INV-01: Cycle Count phải chặn giao dịch Inbound/Outbound tại Location đang đếm.",
            "BR-WMS-INV-02: Stock Adjustment chênh lệch > 2% phải có phê duyệt Manager.",
            "BR-WMS-INV-03: Available Qty = On-hand Qty - Allocated Qty.",
            "BR-WMS-INV-04: Không cho phép Available Qty âm (Overselling).",
            "BR-WMS-INV-05: Hàng tồn > 180 ngày phải đánh giá lại giá trị (Inventory Write-down)."
        ],
        "edge_cases": [
            "Đang kiểm kê thì có hàng nhập kho → Chặn GRN hay vẫn cho phép?",
            "Tồn kho hệ thống = 100 nhưng thực tế = 0 → Nguyên nhân gì?",
            "Hàng đã Allocated cho SO nhưng SO bị hủy → Giải phóng Allocation",
            "Multi-warehouse: Tồn kho Kho A = 0 nhưng Kho B = 500 → Tự động Transfer?"
        ],
        "checklist": [
            "Đã thiết kế phân loại ABC/XYZ",
            "Đã có quy trình Cycle Count và Full Count",
            "Đã xử lý chênh lệch với Tolerance threshold",
            "Đã có luồng Stock Adjustment phê duyệt",
            "Đã quản lý Available vs On-hand vs Allocated",
            "Đã có cảnh báo Min/Max/Expiry",
            "Đã có báo cáo Inventory Aging và Turnover"
        ],
        "example": "Xem Process section.",
        "related_skills": ["Phân tích Inbound Flow", "Phân tích Outbound Flow", "Phân tích Replenishment"],
        "quality_criteria": ["Phải có ABC Analysis", "Phải có Variance handling", "Phải phân biệt On-hand/Allocated/Available"],
        "estimated_effort": "5-7 ngày",
        "prompt_role": "Senior WMS/Inventory Consultant.",
        "prompt_task": "Phân tích và thiết kế quy trình quản lý tồn kho hoàn chỉnh.",
        "prompt_context": "Doanh nghiệp cần quản lý tồn kho chính xác cho kho lớn.",
        "prompt_rules": [
            "PHẢI có ABC Analysis.",
            "PHẢI phân biệt rõ On-hand, Allocated, Available.",
            "PHẢI có quy trình Cycle Count với Blind Count option.",
            "PHẢI xử lý Variance với Tolerance threshold.",
            "Output PHẢI bao gồm BPMN, Data Model, ABC Matrix, và Alert Rules."
        ],
        "prompt_example": ""
    },
    # ================================================================
    # WMS - Cross Docking, Return, Replenishment (compact but detailed)
    # ================================================================
    {
        "path": "01-Business-Domain/WMS",
        "name": "Phân tích Cross Docking",
        "level": "Level 2 - Business Skill",
        "domain": "WMS",
        "tags": ["WMS", "Cross-docking", "Transit"],
        "purpose": "Phân tích quy trình hàng đến kho nhưng không lưu trữ mà chuyển thẳng ra cửa xuất (Cross-docking), nhằm giảm thời gian lưu kho và tăng tốc giao hàng.",
        "when_to_use": "Sử dụng khi kho trung chuyển, trung tâm phân phối cần tối ưu thời gian lưu hàng.",
        "prerequisites": ["Đã phân tích Inbound Flow", "Đã phân tích Outbound Flow"],
        "inputs_detail": [
            {"name": "ASN + SO đã match", "description": "Hàng đến từ NCC đã có sẵn đơn hàng xuất đang chờ.", "required": True, "example": "ASN từ NCC A giao 200 thùng → SO-101 cần 120 thùng, SO-102 cần 80 thùng"},
            {"name": "Loại Cross-dock", "description": "Pre-distributed (đã biết phân bổ trước) hay Post-distributed (phân bổ tại kho).", "required": True, "example": "Pre-distributed: NCC đã đóng gói sẵn theo từng đơn hàng. Post-distributed: Kho phải phân loại lại."}
        ],
        "process_detail": [
            {"step": 1, "title": "Nhận diện hàng Cross-dock", "description": "Hệ thống tự động nhận diện hàng đến có thể Cross-dock dựa trên SO đang chờ.", "sub_steps": [
                "Matching ASN items với SO items đang Pending",
                "Nếu match 100% → Full Cross-dock",
                "Nếu match một phần → Partial Cross-dock (phần dư Putaway bình thường)",
                "Flag hàng Cross-dock trên GRN để nhân viên biết"
            ]},
            {"step": 2, "title": "Phân loại tại Staging (Sorting)", "description": "Hàng được dỡ xuống khu Staging và phân theo đơn hàng.", "sub_steps": [
                "Pre-distributed: Quét mã → Chuyển thẳng ra dock xuất tương ứng",
                "Post-distributed: Mở thùng → Chia hàng theo SO → Đóng gói lại",
                "Kiểm đếm nhanh (Quick Tally) để đảm bảo số lượng đúng"
            ]},
            {"step": 3, "title": "Chuyển ra dock Outbound", "description": "Di chuyển hàng đã phân loại sang khu vực Shipping.", "sub_steps": [
                "Gán Shipping Label cho từng đơn",
                "Tập kết theo hãng vận chuyển hoặc tuyến đường",
                "Thời gian tồn tại tại Staging PHẢI < 24 giờ"
            ]}
        ],
        "outputs_detail": [
            {"name": "Quy trình Cross-dock", "format": "Mermaid Flowchart", "template": ""},
            {"name": "Ma trận loại Cross-dock", "format": "Markdown Table", "template": "| Loại | Mô tả | Phù hợp khi |\n|---|---|---|\n| Pre-distributed | NCC đã chia sẵn | NCC có hệ thống tốt |\n| Post-distributed | Kho chia tại chỗ | Nhiều đơn nhỏ |\n| Hybrid | Kết hợp cả hai | Kho trung chuyển lớn |"}
        ],
        "sub_skills": ["Thiết kế Cross-dock Detection Rules", "Thiết kế Staging Layout"],
        "business_rules": [
            "BR-WMS-XD-01: Hàng Cross-dock không được ở Staging quá 24 giờ.",
            "BR-WMS-XD-02: Chỉ cho phép Cross-dock khi có SO đang chờ match với hàng đến.",
            "BR-WMS-XD-03: Hàng Cross-dock vẫn phải được ghi nhận qua GRN (để Kế toán có chứng từ)."
        ],
        "edge_cases": [
            "SO bị hủy sau khi hàng đã dỡ xuống Staging → Putaway thay vì Cross-dock",
            "NCC giao thiếu so với ASN → Ưu tiên Cross-dock cho SO nào trước?"
        ],
        "checklist": [
            "Đã thiết kế rule tự động nhận diện hàng Cross-dock",
            "Đã phân biệt Pre-distributed vs Post-distributed",
            "Đã giới hạn thời gian hàng nằm tại Staging",
            "Đã có fallback (Putaway) khi không thể Cross-dock",
            "Đã ghi nhận GRN cho chứng từ kế toán"
        ],
        "example": "Xem Process.",
        "related_skills": ["Phân tích Inbound Flow", "Phân tích Outbound Flow"],
        "quality_criteria": ["Phải có Detection Rules", "Phải phân biệt Pre/Post-distributed"],
        "estimated_effort": "2-3 ngày",
        "prompt_role": "Senior WMS Consultant.",
        "prompt_task": "Phân tích và thiết kế quy trình Cross-docking.",
        "prompt_context": "Trung tâm phân phối cần giảm thời gian lưu hàng.",
        "prompt_rules": ["PHẢI có rule tự động nhận diện hàng Cross-dock.", "PHẢI giới hạn thời gian Staging.", "PHẢI có fallback Putaway."],
        "prompt_example": ""
    },
    {
        "path": "01-Business-Domain/WMS",
        "name": "Phân tích Return Management",
        "level": "Level 2 - Business Skill",
        "domain": "WMS",
        "tags": ["WMS", "Return", "RMA", "Reverse Logistics"],
        "purpose": "Quản lý toàn diện luồng hàng hoàn trả (RMA) từ khách hàng, bao gồm tiếp nhận yêu cầu, nhận hàng trả về, kiểm tra chất lượng (QC), phân loại xử lý (Tái nhập kho, Sửa chữa, Tiêu hủy) và hoàn tiền/đổi hàng.",
        "when_to_use": "Khi xây dựng module Return trong WMS hoặc E-commerce.",
        "prerequisites": ["Đã phân tích Inbound Flow"],
        "inputs_detail": [
            {"name": "Đơn yêu cầu hoàn trả (RMA Request)", "description": "Thông tin đơn hàng gốc, lý do trả, số lượng trả.", "required": True, "example": "RMA-001: Trả 5 thùng Sữa TH từ SO-500, lý do: Hàng bị hư hỏng trong vận chuyển."},
            {"name": "Chính sách đổi trả (Return Policy)", "description": "Điều kiện được trả, thời hạn, ai chịu phí ship.", "required": True, "example": "Được trả trong 7 ngày, hàng còn nguyên seal. Hàng khuyến mãi không được trả."}
        ],
        "process_detail": [
            {"step": 1, "title": "Tiếp nhận yêu cầu trả hàng", "description": "Xác nhận đơn hàng gốc, kiểm tra điều kiện trả hàng.", "sub_steps": [
                "Kiểm tra SO gốc còn trong thời hạn đổi trả không",
                "Kiểm tra hàng có nằm trong danh sách không được trả không",
                "Tạo RMA Number và gửi cho khách hàng"
            ]},
            {"step": 2, "title": "Nhận hàng trả về", "description": "Nhận hàng vật lý tại kho.", "sub_steps": [
                "Nhận hàng tại dock Return riêng (tách biệt với Inbound)",
                "Kiểm đếm số lượng khớp RMA",
                "Chụp ảnh hiện trạng hàng"
            ]},
            {"step": 3, "title": "QC hàng trả", "description": "Kiểm tra chất lượng và phân loại.", "sub_steps": [
                "Grade A: Hàng tốt, có thể bán lại → Tái nhập kho",
                "Grade B: Hàng có khuyết điểm nhỏ → Bán giảm giá (Refurbished)",
                "Grade C: Hàng hỏng nặng → Tiêu hủy hoặc trả NCC",
                "Nếu lỗi do NCC → Tạo Supplier Claim"
            ]},
            {"step": 4, "title": "Xử lý hoàn tiền/đổi hàng", "description": "Thực hiện hoàn tiền hoặc gửi hàng thay thế.", "sub_steps": [
                "Hoàn tiền → Cập nhật công nợ, thông báo Kế toán",
                "Đổi hàng → Tạo SO thay thế tự động",
                "Cập nhật tồn kho (Nếu tái nhập) hoặc ghi giảm (Nếu tiêu hủy)"
            ]}
        ],
        "outputs_detail": [
            {"name": "Quy trình Return (BPMN)", "format": "Mermaid Flowchart", "template": ""},
            {"name": "Ma trận phân loại hàng trả", "format": "Markdown Table", "template": "| Grade | Tình trạng | Xử lý | Ảnh hưởng tồn kho |\n|---|---|---|---|\n| A | Nguyên vẹn | Tái nhập kho | +Qty |\n| B | Khuyết điểm nhỏ | Bán giảm giá | +Qty (vùng Outlet) |\n| C | Hỏng nặng | Tiêu hủy | Write-off |"}
        ],
        "sub_skills": ["Thiết kế RMA Workflow", "Thiết kế QC Return Grading", "Thiết kế Supplier Claim"],
        "business_rules": [
            "BR-WMS-RET-01: Chỉ nhận hàng trả có RMA Number hợp lệ.",
            "BR-WMS-RET-02: Hàng trả về phải qua QC trước khi tái nhập kho.",
            "BR-WMS-RET-03: Hàng Grade C phải có biên bản tiêu hủy có chữ ký Quản lý.",
            "BR-WMS-RET-04: Hoàn tiền chỉ được xử lý sau khi QC hoàn tất."
        ],
        "edge_cases": [
            "Khách trả hàng không có trong SO gốc (gửi nhầm) → Xử lý hàng vô chủ",
            "Hàng trả bị nhiễm bẩn → Có cần cách ly không?"
        ],
        "checklist": [
            "Đã thiết kế luồng RMA Request",
            "Đã có dock riêng cho hàng trả (tách biệt Inbound)",
            "Đã có QC Grading (A/B/C)",
            "Đã xử lý hoàn tiền/đổi hàng",
            "Đã cập nhật tồn kho sau khi xử lý",
            "Đã tạo Supplier Claim khi lỗi NCC"
        ],
        "example": "Xem Process.",
        "related_skills": ["Phân tích Inbound Flow", "Phân tích Quality Control"],
        "quality_criteria": ["Phải có RMA workflow", "Phải có QC Grading", "Phải xử lý hoàn tiền"],
        "estimated_effort": "3-4 ngày",
        "prompt_role": "Senior WMS/Reverse Logistics Consultant.",
        "prompt_task": "Phân tích và thiết kế quy trình Return Management.",
        "prompt_context": "Doanh nghiệp bán lẻ/E-commerce cần quản lý hàng trả về chuyên nghiệp.",
        "prompt_rules": ["PHẢI có RMA Number.", "PHẢI có QC Grading A/B/C.", "PHẢI tách dock Return khỏi Inbound.", "PHẢI cập nhật tồn kho sau xử lý."],
        "prompt_example": ""
    },
    {
        "path": "01-Business-Domain/WMS",
        "name": "Phân tích Replenishment",
        "level": "Level 2 - Business Skill",
        "domain": "WMS",
        "tags": ["WMS", "Replenishment", "Min-Max", "Safety Stock"],
        "purpose": "Phân tích quy trình bổ sung hàng tự động từ khu vực dự trữ (Reserve) sang khu vực nhặt hàng (Picking), và từ NCC vào kho khi tồn kho chạm mức tối thiểu.",
        "when_to_use": "Khi kho lớn có tách biệt Reserve Zone và Picking Zone.",
        "prerequisites": ["Đã phân tích Inventory Management"],
        "inputs_detail": [
            {"name": "Reorder Point / Min Level", "description": "Ngưỡng tồn kho tại vị trí Picking để trigger bổ sung.", "required": True, "example": "SKU-A01 tại Zone A: Min = 20 thùng. Khi tồn Picking < 20 → Trigger Replenishment."},
            {"name": "Safety Stock", "description": "Lượng tồn kho an toàn để phòng biến động.", "required": True, "example": "Safety Stock = 50 thùng (Dựa trên Lead time NCC là 3 ngày và nhu cầu trung bình 15 thùng/ngày)"}
        ],
        "process_detail": [
            {"step": 1, "title": "Giám sát ngưỡng tồn kho", "description": "Hệ thống liên tục theo dõi Available Qty tại Picking Location.", "sub_steps": [
                "So sánh Available Qty vs Min Level theo realtime hoặc batch (mỗi giờ)",
                "Khi Available Qty < Min Level → Trigger Replenishment Task"
            ]},
            {"step": 2, "title": "Tạo lệnh bổ sung (Replenishment Task)", "description": "Hệ thống tự động tạo lệnh di chuyển hàng.", "sub_steps": [
                "Xác định nguồn: Reserve Location cùng SKU gần nhất",
                "Số lượng bổ sung = Max Level - Current Qty (Top-off) hoặc = Fixed Qty",
                "Gán cho nhân viên kho thực hiện"
            ]},
            {"step": 3, "title": "Thực hiện & Xác nhận", "description": "Nhân viên di chuyển hàng từ Reserve sang Picking.", "sub_steps": [
                "Quét mã vạch tại Reserve Location → Pick",
                "Di chuyển hàng đến Picking Location",
                "Quét mã vạch tại Picking Location → Confirm",
                "Hệ thống cập nhật Qty tại cả hai Location"
            ]}
        ],
        "outputs_detail": [
            {"name": "Replenishment Rules", "format": "Markdown Table", "template": "| SKU | Picking Location | Min | Max | Replenish Qty | Reserve Source |\n|---|---|---|---|---|---|\n| SKU-A01 | A-01-01 | 20 | 100 | 80 | R-05-03 |\n| SKU-B02 | A-02-05 | 10 | 50 | 40 | R-08-01 |"}
        ],
        "sub_skills": ["Thiết kế Min-Max Rules", "Thiết kế Safety Stock Calculation"],
        "business_rules": [
            "BR-WMS-REP-01: Replenishment phải hoàn thành trước khi hết hàng tại Picking (Prevent stockout).",
            "BR-WMS-REP-02: Ưu tiên Replenish SKU đang có SO chờ trước.",
            "BR-WMS-REP-03: Không Replenish quá Max Level."
        ],
        "edge_cases": [
            "Reserve cũng hết hàng → Trigger PO cho NCC",
            "Nhiều Picking Location cùng SKU đều cần Replenish → Ưu tiên Location nào?"
        ],
        "checklist": [
            "Đã thiết kế Min/Max cho từng SKU",
            "Đã có trigger tự động khi chạm Min",
            "Đã có logic tính Safety Stock (dựa trên Lead Time + Demand Variability)",
            "Đã có fallback khi Reserve hết hàng"
        ],
        "example": "Xem Process.",
        "related_skills": ["Phân tích Inventory Management", "Phân tích Outbound Flow"],
        "quality_criteria": ["Phải có Min/Max logic", "Phải có Safety Stock formula"],
        "estimated_effort": "2-3 ngày",
        "prompt_role": "Senior WMS Consultant.",
        "prompt_task": "Thiết kế Replenishment strategy.",
        "prompt_context": "Kho có tách biệt Reserve và Picking zone.",
        "prompt_rules": ["PHẢI có Min/Max rules.", "PHẢI có Safety Stock calculation.", "PHẢI có auto-trigger."],
        "prompt_example": ""
    }
]

if __name__ == "__main__":
    print("=== Expanding Business Domain: WMS Skills ===")
    run(skills)
