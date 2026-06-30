import sys
sys.path.insert(0, r"e:\BA Skill Library")
from skill_generator import run

skills = [
    # ================================================================
    # UIUX - Dashboard
    # ================================================================
    {
        "path": "04-UIUX/Dashboard",
        "name": "Thiết kế Dashboard",
        "level": "Level 2 - Business Skill",
        "domain": "UIUX",
        "tags": ["UIUX", "Dashboard", "KPI", "Chart", "Report"],
        "purpose": "Thiết kế Dashboard quản trị cho hệ thống doanh nghiệp bao gồm: xác định đúng KPI cho từng vai trò (Role), chọn đúng loại biểu đồ (Chart Type), bố trí layout theo nguyên tắc Information Hierarchy, thiết kế bộ lọc (Filter) và drill-down chi tiết.",
        "when_to_use": "Sử dụng khi cần thiết kế trang Dashboard cho bất kỳ module nào (CRM, WMS, MES, HRM, Finance...).",
        "prerequisites": ["Hiểu nghiệp vụ của module cần Dashboard", "Biết các loại biểu đồ cơ bản"],
        "inputs_detail": [
            {"name": "Module & Vai trò người xem", "description": "Dashboard cho module nào và ai xem.", "required": True, "example": "Module: WMS. Người xem: Quản lý kho muốn thấy tổng quan tồn kho, hiệu suất xuất nhập, cảnh báo hết hàng."},
            {"name": "KPI / Metrics cần theo dõi", "description": "Các chỉ số quan trọng cần hiển thị.", "required": True, "example": "Số lượng xuất kho hôm nay, Tỷ lệ chính xác Picking, Top 10 SKU bán chạy, Cảnh báo hàng sắp hết."},
            {"name": "Nguồn dữ liệu", "description": "Dữ liệu lấy từ bảng/API nào.", "required": False, "example": "Bảng orders, inventory, picking_logs."}
        ],
        "process_detail": [
            {"step": 1, "title": "Xác định KPI theo vai trò", "description": "Mỗi vai trò (Role) cần những KPI khác nhau.", "sub_steps": [
                "CEO/Director: Tổng doanh thu, Lợi nhuận, So sánh kỳ trước, Dự báo",
                "Manager: Hiệu suất team, Tỷ lệ hoàn thành, Cảnh báo bất thường",
                "Operator: Tác vụ cần làm hôm nay, Trạng thái công việc đang xử lý",
                "Quy tắc: Cấp càng cao → Tổng hợp hơn. Cấp càng thấp → Chi tiết thao tác."
            ]},
            {"step": 2, "title": "Chọn đúng loại biểu đồ (Chart Type)", "description": "Mỗi loại dữ liệu phù hợp với 1 loại biểu đồ cụ thể.", "sub_steps": [
                "So sánh giá trị → Bar Chart (Doanh thu theo tháng, Tồn kho theo kho)",
                "Xu hướng theo thời gian → Line Chart (Doanh thu 12 tháng, OEE theo tuần)",
                "Tỷ lệ phần trăm → Pie/Donut Chart (Tỷ lệ Lead theo nguồn) - CHỈ dùng khi ≤ 5 phần",
                "Tiến độ → Gauge Chart (OEE %, SLA Compliance %)",
                "Bảng xếp hạng → Table / Horizontal Bar (Top 10 SKU, Top 5 Sales)",
                "Phân bố địa lý → Map Chart (Doanh thu theo vùng)",
                "Số đơn lẻ nổi bật → KPI Card / Metric Tile (Tổng đơn hàng hôm nay: 152)",
                "KHÔNG dùng 3D chart, KHÔNG dùng Pie cho > 5 categories"
            ]},
            {"step": 3, "title": "Thiết kế Layout (Bố cục)", "description": "Sắp xếp các widget theo nguyên tắc Information Hierarchy.", "sub_steps": [
                "Row 1 (Top): KPI Cards - Các chỉ số tổng quan quan trọng nhất (4-6 cards)",
                "Row 2 (Middle): Charts chính - Biểu đồ xu hướng và so sánh",
                "Row 3 (Bottom): Tables chi tiết - Danh sách cần hành động (Alerts, Tasks)",
                "Sidebar/Top: Bộ lọc (Date Range, Warehouse, Product Category...)",
                "Quy tắc: Thông tin quan trọng nhất → Góc trên bên trái (Eye Tracking F-pattern)"
            ]},
            {"step": 4, "title": "Thiết kế bộ lọc (Filters)", "description": "Cho phép người dùng lọc dữ liệu theo nhiều tiêu chí.", "sub_steps": [
                "Date Range Picker: Hôm nay, Tuần này, Tháng này, Quý này, Tùy chọn",
                "Filter theo đơn vị: Kho, Chi nhánh, Phòng ban",
                "Filter theo danh mục: Nhóm sản phẩm, Loại đơn hàng",
                "Global Filter: Áp dụng cho tất cả widget trên Dashboard",
                "Quick Filter: Preset buttons (Hôm nay, 7 ngày, 30 ngày)"
            ]},
            {"step": 5, "title": "Thiết kế Drill-down & Action", "description": "Cho phép click vào chart để xem chi tiết.", "sub_steps": [
                "Click vào Bar → Xem danh sách chi tiết đằng sau số liệu",
                "Click vào KPI Card đỏ (cảnh báo) → Xem danh sách items bất thường",
                "Click vào hàng trong Table → Mở trang chi tiết",
                "Auto-refresh: Dashboard tự cập nhật mỗi 30s-5p (tùy module)"
            ]}
        ],
        "outputs_detail": [
            {"name": "Dashboard Specification", "format": "Markdown Document", "template": "# Dashboard Specification: [Tên Module]\n\n## Target User: [Role]\n\n## KPI Cards (Row 1)\n| # | KPI | Biểu đồ | Nguồn dữ liệu | Drill-down |\n|---|---|---|---|---|\n| 1 | Tổng đơn hàng hôm nay | KPI Card (số) | orders WHERE date = today | Danh sách đơn |\n| 2 | Tỷ lệ Pick chính xác | Gauge (%) | picking_logs | Chi tiết lỗi |\n| 3 | Cảnh báo hết hàng | KPI Card (đỏ) | inventory WHERE qty < min | Danh sách SKU |\n\n## Charts (Row 2)\n| # | Tên Chart | Loại | Dữ liệu | Filter |\n|---|---|---|---|---|\n| 1 | Xu hướng xuất nhập 30 ngày | Line Chart | Nhập (xanh) + Xuất (cam) | Date range |\n| 2 | Tồn kho theo Zone | Stacked Bar | Qty by zone | Warehouse |\n\n## Tables (Row 3)\n| # | Tên | Columns | Sort | Action |\n|---|---|---|---|---|\n| 1 | Đơn hàng chờ Picking | SO#, Khách, Items, Priority | Priority DESC | Click → Pick |\n\n## Filters\n- Date Range (Default: Hôm nay)\n- Warehouse (Default: Tất cả)"},
            {"name": "Chart Type Guide", "format": "Markdown Table", "template": "| Mục đích | Chart Type | Ví dụ |\n|---|---|---|\n| Giá trị đơn lẻ | KPI Card | Tổng doanh thu: 5.2 tỷ |\n| So sánh | Bar Chart | Doanh thu theo chi nhánh |\n| Xu hướng | Line Chart | Doanh thu 12 tháng |\n| Tỷ lệ (≤5 phần) | Donut Chart | Trạng thái đơn hàng |\n| Tiến độ % | Gauge Chart | OEE = 78% |\n| Xếp hạng | Horizontal Bar | Top 10 sản phẩm |"}
        ],
        "sub_skills": ["Chọn Chart Type phù hợp", "Thiết kế KPI Cards", "Thiết kế Dashboard Layout", "Thiết kế Drill-down"],
        "business_rules": [
            "BR-DASH-01: Dashboard PHẢI load trong 3 giây hoặc ít hơn.",
            "BR-DASH-02: KHÔNG dùng Pie Chart cho > 5 categories.",
            "BR-DASH-03: KHÔNG dùng 3D chart (Gây hiểu sai dữ liệu).",
            "BR-DASH-04: KPI Card cảnh báo phải dùng màu đỏ/vàng rõ ràng.",
            "BR-DASH-05: Mỗi Dashboard phải có ít nhất 1 bộ lọc Date Range.",
            "BR-DASH-06: Dữ liệu Dashboard phải realtime hoặc near-realtime (< 5 phút)."
        ],
        "edge_cases": [
            "Không có dữ liệu (mới triển khai) → Hiển thị 'Chưa có dữ liệu' thay vì chart trống",
            "Dữ liệu quá lớn → Giới hạn Top N hoặc phân trang",
            "Người dùng có 2 Role → Dashboard nào? (Hiển thị Dashboard theo Role cao nhất)"
        ],
        "checklist": [
            "Đã xác định KPI theo vai trò (Role-based)?",
            "Đã chọn đúng Chart Type cho mỗi KPI?",
            "Đã bố trí Layout theo F-pattern (Quan trọng nhất → Góc trên trái)?",
            "Đã có bộ lọc Date Range + các filter phù hợp?",
            "Đã có Drill-down khi click vào chart?",
            "Đã có cảnh báo (Alert) bằng màu sắc?",
            "Đã có Auto-refresh?",
            "Dashboard load < 3 giây?"
        ],
        "example": "Xem Dashboard Specification template trong Outputs.",
        "related_skills": ["Thiết kế module", "Phân tích Báo cáo động", "Thiết kế Role-based UI"],
        "quality_criteria": ["KPI phải phù hợp với Role", "Chart Type phải đúng dữ liệu", "Layout phải theo F-pattern", "Phải có Drill-down"],
        "estimated_effort": "2-3 ngày / Dashboard",
        "prompt_role": "Senior UIUX/BI Analyst chuyên thiết kế Dashboard cho hệ thống doanh nghiệp. Am hiểu Data Visualization best practices.",
        "prompt_task": "Thiết kế Dashboard specification chi tiết cho module được yêu cầu.",
        "prompt_context": "Doanh nghiệp cần Dashboard quản trị cho module cụ thể.",
        "prompt_rules": [
            "PHẢI xác định KPI theo vai trò (Role) của người xem.",
            "PHẢI chọn đúng Chart Type theo bảng hướng dẫn (Bar cho so sánh, Line cho xu hướng, Gauge cho %).",
            "KHÔNG dùng Pie Chart cho > 5 categories.",
            "KHÔNG dùng 3D chart.",
            "PHẢI có bộ lọc Date Range.",
            "PHẢI có Drill-down cho mỗi widget.",
            "Layout PHẢI theo F-pattern: KPI Cards (top) → Charts (middle) → Tables (bottom).",
            "Output PHẢI theo format Dashboard Specification với bảng chi tiết từng widget."
        ],
        "prompt_example": ""
    },
    # ================================================================
    # UIUX - CRUD Screen
    # ================================================================
    {
        "path": "04-UIUX/CRUD",
        "name": "Phân tích màn hình CRUD",
        "level": "Level 2 - Business Skill",
        "domain": "UIUX",
        "tags": ["UIUX", "CRUD", "Form", "List", "Screen"],
        "purpose": "Đặc tả chi tiết bộ màn hình CRUD (Create-Read-Update-Delete) cho một entity, bao gồm: màn hình List (Search/Filter/Pagination/Bulk Actions), màn hình Create/Edit (Form Validation), màn hình Detail View, và tất cả Confirmation/Error Dialogs.",
        "when_to_use": "Sử dụng khi cần đặc tả bất kỳ màn hình quản lý entity nào trong hệ thống (Quản lý Khách hàng, Quản lý Sản phẩm, Quản lý Đơn hàng...).",
        "prerequisites": ["Đã có Data Model/ERD", "Hiểu cơ bản về UIUX"],
        "inputs_detail": [
            {"name": "Entity & Trường dữ liệu", "description": "Entity nào và có những trường nào.", "required": True, "example": "Entity: Product. Trường: product_code, name, category, unit_price, stock_qty, status, created_at."},
            {"name": "Permission Matrix", "description": "Ai được CRUD trên entity này.", "required": True, "example": "Admin: CRUD. Manager: CRU. Staff: R (chỉ xem). Guest: Không thấy."}
        ],
        "process_detail": [
            {"step": 1, "title": "Đặc tả màn hình List (Danh sách)", "description": "Thiết kế trang danh sách entity.", "sub_steps": [
                "Columns: Chọn cột nào hiển thị (KHÔNG hiển thị tất cả trường)",
                "Search: Tìm theo trường nào? (VD: Tên, Mã sản phẩm)",
                "Filters: Lọc theo trường nào? (VD: Category dropdown, Status radio, Date range)",
                "Sort: Cột nào cho sort? Default sort? (VD: Mới nhất trước)",
                "Pagination: 10/25/50 items per page. Hiển thị 'Showing 1-10 of 150'",
                "Bulk Actions: Chọn nhiều → Xóa hàng loạt, Export, Thay đổi status",
                "Row Actions: Mỗi hàng có nút: View, Edit, Delete (hoặc icon)",
                "Button 'Tạo mới' ở góc phải trên",
                "Empty State: Hiển thị gì khi chưa có dữ liệu?",
                "Export: Nút Export Excel/CSV"
            ]},
            {"step": 2, "title": "Đặc tả màn hình Create/Edit (Form)", "description": "Thiết kế form nhập liệu.", "sub_steps": [
                "Bố trí trường: 1 cột hay 2 cột? Nhóm thành Section?",
                "Mỗi trường PHẢI có: Label, Placeholder, Loại control (Input/Select/DatePicker/TextArea), Bắt buộc (*), Validation rule",
                "Trường khóa (VD: Mã sản phẩm): Auto-generate hay nhập tay? Unique?",
                "Trường Foreign Key (VD: Category): Dropdown, Searchable Select, hay Popup chọn?",
                "Trường Upload: Ảnh sản phẩm → Crop, Resize, Preview trước khi upload",
                "Nút: [Lưu] [Lưu & Tiếp tục] [Hủy]",
                "Confirm khi Hủy: 'Bạn có chắc muốn hủy? Dữ liệu chưa lưu sẽ mất.'",
                "Loading state: Nút Lưu bị disable khi đang submit"
            ]},
            {"step": 3, "title": "Đặc tả Validation Rules", "description": "Chi tiết rule kiểm tra cho từng trường.", "sub_steps": [
                "Required: 'Vui lòng nhập [tên trường]'",
                "Min/Max Length: 'Tên sản phẩm phải từ 3-200 ký tự'",
                "Format: Email (abc@xyz.com), SĐT (10 số, bắt đầu 0), Mã (chỉ chữ và số)",
                "Unique: 'Mã sản phẩm đã tồn tại, vui lòng nhập mã khác'",
                "Range: 'Giá bán phải > 0'",
                "Dependency: 'Nếu chọn Loại = Thực phẩm → Bắt buộc nhập Hạn sử dụng'",
                "Realtime validation (onBlur) vs Submit validation"
            ]},
            {"step": 4, "title": "Đặc tả Delete (Xóa)", "description": "Xử lý xóa entity.", "sub_steps": [
                "Soft Delete (Đánh dấu xóa, không xóa thật) → Khuyến khích",
                "Confirm Dialog: 'Bạn có chắc chắn muốn xóa [Tên]? Hành động này không thể hoàn tác.'",
                "Kiểm tra ràng buộc: Nếu entity có child records → 'Không thể xóa vì còn [N] đơn hàng liên quan.'",
                "Bulk Delete: Confirm 'Bạn sắp xóa [N] mục. Tiếp tục?'"
            ]},
            {"step": 5, "title": "Đặc tả Detail View (Xem chi tiết)", "description": "Thiết kế trang xem chi tiết.", "sub_steps": [
                "Hiển thị tất cả trường ở chế độ Read-only",
                "Tab layout nếu entity phức tạp (Tab Thông tin chung, Tab Lịch sử, Tab Đơn hàng liên quan)",
                "Activity Log / Audit Trail: Ai đã sửa gì, khi nào?",
                "Nút hành động: [Sửa] [Xóa] [In] [Export PDF]"
            ]}
        ],
        "outputs_detail": [
            {"name": "CRUD Screen Specification", "format": "Markdown Document", "template": "# Screen Spec: Quản lý [Entity]\n\n## 1. List Screen\n### Columns\n| # | Column | Source Field | Width | Sort | Filter |\n|---|---|---|---|---|---|\n| 1 | Mã SP | product_code | 100px | ✅ | Text search |\n| 2 | Tên SP | name | 250px | ✅ | Text search |\n| 3 | Danh mục | category.name | 150px | ✅ | Dropdown |\n| 4 | Giá bán | unit_price | 120px | ✅ | Range |\n| 5 | Trạng thái | status | 100px | | Radio |\n\n### Actions\n- [+ Tạo mới] (Góc phải trên)\n- Row: [View] [Edit] [Delete]\n- Bulk: [Delete] [Export Excel]\n\n## 2. Create/Edit Form\n| # | Field | Label | Control | Required | Validation |\n|---|---|---|---|---|---|\n| 1 | product_code | Mã SP | Text Input | ✅ | Unique, [A-Z0-9-]{3,20} |\n| 2 | name | Tên SP | Text Input | ✅ | Length 3-200 |\n| 3 | category_id | Danh mục | Searchable Select | ✅ | |\n| 4 | unit_price | Giá bán | Number Input | ✅ | > 0 |\n| 5 | image | Ảnh SP | File Upload | | JPG/PNG, max 2MB |"},
            {"name": "Validation Rules Table", "format": "Markdown Table", "template": "| Field | Rule | Error Message |\n|---|---|---|\n| product_code | Required | 'Vui lòng nhập Mã sản phẩm' |\n| product_code | Unique | 'Mã sản phẩm đã tồn tại' |\n| product_code | Pattern [A-Z0-9-] | 'Mã chỉ chứa chữ in hoa, số và dấu gạch ngang' |\n| name | Required | 'Vui lòng nhập Tên sản phẩm' |\n| name | Length 3-200 | 'Tên phải từ 3-200 ký tự' |\n| unit_price | > 0 | 'Giá bán phải lớn hơn 0' |"}
        ],
        "sub_skills": ["Thiết kế List Screen", "Thiết kế Form Screen", "Thiết kế Validation Rules", "Thiết kế Empty State & Loading State"],
        "business_rules": [
            "BR-UI-CRUD-01: Mọi màn hình List phải có Search + Filter + Pagination + Sort.",
            "BR-UI-CRUD-02: Delete bắt buộc có Confirm Dialog.",
            "BR-UI-CRUD-03: Form Validation phải chạy realtime (onBlur) cho trường Required.",
            "BR-UI-CRUD-04: Nút Submit phải disable khi đang loading.",
            "BR-UI-CRUD-05: Mọi entity phải có Audit Log (created_by, updated_by, created_at, updated_at)."
        ],
        "edge_cases": [
            "2 user cùng Edit 1 record → Optimistic Locking / Concurrency conflict",
            "Upload ảnh quá lớn → Validate file size trước khi upload",
            "Mất kết nối khi đang submit form → Retry hoặc lưu Draft local"
        ],
        "checklist": [
            "List: Có Search?", "List: Có Filter?", "List: Có Pagination?", "List: Có Sort?",
            "List: Có Export Excel?", "List: Có Bulk Actions?", "List: Có Empty State?",
            "Form: Mỗi field có Label + Control + Validation?",
            "Form: Có Confirm khi Cancel?", "Form: Nút disable khi loading?",
            "Delete: Có Confirm Dialog?", "Delete: Kiểm tra ràng buộc?",
            "Detail: Có Audit Log?"
        ],
        "example": "Xem CRUD Screen Specification template trong Outputs.",
        "related_skills": ["Thiết kế Dashboard", "Thiết kế Form", "Thiết kế module"],
        "quality_criteria": ["List phải đủ 7 thành phần", "Form phải có Validation Table", "Delete phải có Confirm"],
        "estimated_effort": "1-2 ngày / entity",
        "prompt_role": "Senior UIUX/BA Analyst chuyên đặc tả màn hình cho Web Application.",
        "prompt_task": "Đặc tả chi tiết bộ màn hình CRUD cho entity được yêu cầu.",
        "prompt_context": "Team Dev cần spec chi tiết để implement màn hình quản lý.",
        "prompt_rules": [
            "List Screen PHẢI có: Search, Filter, Sort, Pagination, Bulk Actions, Export, Empty State.",
            "Create/Edit Form PHẢI có bảng: Field, Label, Control Type, Required, Validation Rule, Error Message.",
            "Delete PHẢI có Confirm Dialog.",
            "PHẢI kiểm tra Foreign Key constraint trước khi xóa.",
            "PHẢI có Audit fields: created_by, updated_by, created_at, updated_at.",
            "Output PHẢI theo format CRUD Screen Specification."
        ],
        "prompt_example": ""
    },
    # ================================================================
    # 03-Modeling / Thiết kế ERD
    # ================================================================
    {
        "path": "03-Modeling/ERD",
        "name": "Thiết kế ERD",
        "level": "Level 2 - Business Skill",
        "domain": "Modeling",
        "tags": ["Modeling", "ERD", "Database", "Entity", "Relationship"],
        "purpose": "Thiết kế Entity-Relationship Diagram (ERD) cho hệ thống, xác định rõ các Entity (Bảng), Attributes (Cột), Primary Key, Foreign Key, Relationships (1-1, 1-N, N-N), Indexes, và Constraints. ERD phải đủ chi tiết để DBA có thể tạo database trực tiếp.",
        "when_to_use": "Sử dụng khi cần thiết kế cấu trúc database cho một module hoặc toàn bộ hệ thống.",
        "prerequisites": ["Đã hoàn thành SRS hoặc User Stories"],
        "inputs_detail": [
            {"name": "Danh sách Entity (từ SRS/User Stories)", "description": "Các đối tượng cần lưu trữ dữ liệu.", "required": True, "example": "Module WMS: product, warehouse, location, purchase_order, goods_receipt, inventory, picking_order."},
            {"name": "Business Rules", "description": "Các quy tắc ảnh hưởng đến cấu trúc dữ liệu.", "required": True, "example": "1 Product có thể nằm ở nhiều Location. 1 PO có nhiều PO Lines. 1 Warehouse có nhiều Zones, mỗi Zone có nhiều Locations."}
        ],
        "process_detail": [
            {"step": 1, "title": "Xác định Entity (Bảng)", "description": "Liệt kê tất cả các Entity cần tạo.", "sub_steps": [
                "Mỗi danh từ chính trong SRS thường là 1 Entity",
                "Phân biệt Entity chính (Master: Product, Customer) và Entity giao dịch (Transaction: Order, Invoice)",
                "Phân biệt Entity chính và bảng phụ (Lookup: Status, Category)",
                "Naming Convention: snake_case, số ít (product thay vì products)"
            ]},
            {"step": 2, "title": "Xác định Attributes (Cột)", "description": "Liệt kê tất cả trường dữ liệu cho mỗi Entity.", "sub_steps": [
                "Mỗi cột phải có: Tên, Kiểu dữ liệu, Nullable?, Default value, Mô tả",
                "Kiểu dữ liệu chuẩn: INT, BIGINT, VARCHAR(N), TEXT, DECIMAL(P,S), DATE, DATETIME, BOOLEAN, ENUM",
                "Audit Columns bắt buộc: id (PK), created_at, updated_at, created_by, updated_by, is_deleted",
                "Soft Delete: Dùng is_deleted (BOOLEAN) thay vì xóa thật"
            ]},
            {"step": 3, "title": "Xác định Relationships", "description": "Xác định quan hệ giữa các Entity.", "sub_steps": [
                "1-1 (One-to-One): user ↔ user_profile (Hiếm gặp)",
                "1-N (One-to-Many): customer → orders (1 KH có nhiều đơn hàng). FK ở bảng con (orders.customer_id)",
                "N-N (Many-to-Many): product ↔ tag → Cần bảng trung gian (product_tag)",
                "Self-referencing: employee.manager_id → employee.id (Cây tổ chức)",
                "Polymorphic: activity_log.entity_type + activity_log.entity_id (Log cho nhiều entity)"
            ]},
            {"step": 4, "title": "Thiết kế Indexes", "description": "Tối ưu hiệu suất query.", "sub_steps": [
                "Primary Key: Mọi bảng phải có PK (thường là id INT AUTO_INCREMENT)",
                "Foreign Key: Tạo Index cho mỗi FK",
                "Unique Index: Trường unique (email, product_code)",
                "Composite Index: Cho query thường xuyên (VD: (warehouse_id, product_id) trên bảng inventory)",
                "Index cho Filter/Sort: Trường thường dùng trong WHERE và ORDER BY"
            ]},
            {"step": 5, "title": "Vẽ ERD Diagram", "description": "Vẽ sơ đồ ERD dạng Mermaid hoặc công cụ khác.", "sub_steps": [
                "Sử dụng Mermaid erDiagram syntax",
                "Hiển thị: Entity name, PK/FK, Relationship lines",
                "Gom nhóm theo Module nếu ERD quá lớn"
            ]}
        ],
        "outputs_detail": [
            {"name": "ERD Diagram", "format": "Mermaid erDiagram", "template": "erDiagram\n    CUSTOMER ||--o{ ORDER : places\n    ORDER ||--|{ ORDER_LINE : contains\n    PRODUCT ||--o{ ORDER_LINE : appears_in\n    WAREHOUSE ||--|{ LOCATION : has\n    PRODUCT ||--o{ INVENTORY : stored_at\n    LOCATION ||--o{ INVENTORY : holds"},
            {"name": "Data Dictionary", "format": "Markdown Table", "template": "## Table: product\n| # | Column | Type | Nullable | Default | Constraint | Description |\n|---|---|---|---|---|---|---|\n| 1 | id | INT | No | AUTO_INCREMENT | PK | Mã sản phẩm |\n| 2 | code | VARCHAR(50) | No | | UNIQUE | Mã SP hiển thị |\n| 3 | name | VARCHAR(200) | No | | | Tên sản phẩm |\n| 4 | category_id | INT | No | | FK → category.id | Danh mục |\n| 5 | unit_price | DECIMAL(15,2) | No | 0 | CHECK > 0 | Đơn giá |\n| 6 | is_deleted | BOOLEAN | No | false | | Soft delete |\n| 7 | created_at | DATETIME | No | NOW() | | Ngày tạo |\n| 8 | updated_at | DATETIME | Yes | | | Ngày cập nhật |"}
        ],
        "sub_skills": ["Entity Identification", "Relationship Design", "Data Dictionary Creation", "Index Design"],
        "business_rules": [
            "BR-ERD-01: Mọi bảng phải có Primary Key (id INT AUTO_INCREMENT).",
            "BR-ERD-02: Mọi bảng phải có audit columns (created_at, updated_at, created_by, updated_by).",
            "BR-ERD-03: Sử dụng Soft Delete (is_deleted) thay vì xóa thật.",
            "BR-ERD-04: Naming Convention: snake_case, số ít, tiếng Anh.",
            "BR-ERD-05: FK phải có Index."
        ],
        "edge_cases": [
            "Bảng N-N với dữ liệu bổ sung → Bảng trung gian trở thành Entity riêng (VD: order_line có quantity, price)",
            "Dữ liệu lịch sử (History) → Bảng snapshot (product_price_history) hoặc Audit table"
        ],
        "checklist": [
            "Mọi bảng có PK?", "Mọi bảng có Audit columns?",
            "Đã sử dụng Soft Delete?", "FK đã tạo Index?",
            "Đã xử lý N-N bằng bảng trung gian?",
            "Naming convention nhất quán (snake_case)?",
            "Data Dictionary đầy đủ cho mỗi bảng?",
            "ERD Diagram đã vẽ đầy đủ Relationship?"
        ],
        "example": "Xem ERD và Data Dictionary trong Outputs.",
        "related_skills": ["Create Data Dictionary", "Thiết kế module", "Write SRS"],
        "quality_criteria": ["Phải có ERD Diagram", "Phải có Data Dictionary", "Mọi bảng có PK + Audit", "Phải dùng Soft Delete"],
        "estimated_effort": "3-5 ngày",
        "prompt_role": "Senior Database Architect / Data Modeler.",
        "prompt_task": "Thiết kế ERD và Data Dictionary cho module được yêu cầu.",
        "prompt_context": "Team Dev cần ERD và Data Dictionary để tạo database schema.",
        "prompt_rules": [
            "Mọi bảng PHẢI có: id (PK), created_at, updated_at, created_by, updated_by, is_deleted.",
            "PHẢI sử dụng snake_case, tiếng Anh, số ít cho tên bảng và cột.",
            "PHẢI sử dụng Soft Delete (is_deleted BOOLEAN).",
            "FK PHẢI có Index.",
            "N-N PHẢI có bảng trung gian.",
            "PHẢI cung cấp Data Dictionary cho MỌI bảng với: Column, Type, Nullable, Default, Constraint, Description.",
            "Output PHẢI bao gồm Mermaid ERD Diagram + Data Dictionary tables."
        ],
        "prompt_example": ""
    },
    # ================================================================
    # 05-Database / Create Data Dictionary
    # ================================================================
    {
        "path": "05-Database/Data Dictionary",
        "name": "Create Data Dictionary",
        "level": "Level 2 - Business Skill",
        "domain": "Database",
        "tags": ["Database", "Data Dictionary", "Documentation"],
        "purpose": "Tạo Data Dictionary toàn diện cho hệ thống, mô tả chi tiết mỗi bảng, mỗi cột, kiểu dữ liệu, ràng buộc, mối quan hệ và mô tả nghiệp vụ. Đây là tài liệu tham chiếu chính cho Dev, DBA, BA và QC.",
        "when_to_use": "Sử dụng sau khi thiết kế ERD, cần tạo tài liệu chi tiết cho database.",
        "prerequisites": ["Đã thiết kế ERD"],
        "inputs_detail": [
            {"name": "ERD Diagram", "description": "Sơ đồ Entity-Relationship đã thiết kế.", "required": True, "example": "ERD Module WMS với 12 bảng."},
            {"name": "Business Rules", "description": "Các quy tắc nghiệp vụ ảnh hưởng đến dữ liệu.", "required": True, "example": "Giá bán phải > 0. Email phải unique. Status chỉ có thể là: active, inactive, archived."}
        ],
        "process_detail": [
            {"step": 1, "title": "Liệt kê tất cả bảng", "description": "Tạo danh sách tổng quan các bảng.", "sub_steps": [
                "Phân loại: Master (Dữ liệu chủ), Transaction (Giao dịch), Lookup (Tra cứu), System (Hệ thống)",
                "Mỗi bảng có: Tên, Mô tả, Loại, Số cột dự kiến, Kích thước dự kiến"
            ]},
            {"step": 2, "title": "Chi tiết mỗi bảng", "description": "Mô tả chi tiết từng cột trong bảng.", "sub_steps": [
                "Column Name: snake_case",
                "Data Type: INT, VARCHAR(N), DECIMAL(P,S), DATETIME, BOOLEAN, TEXT, ENUM, JSON",
                "Nullable: Yes/No",
                "Default Value: AUTO_INCREMENT, NOW(), false, 0",
                "Constraint: PK, FK → table.column, UNIQUE, CHECK, INDEX",
                "Description: Mô tả nghiệp vụ bằng tiếng Việt rõ ràng",
                "Sample Data: Dữ liệu mẫu để minh họa"
            ]},
            {"step": 3, "title": "Mô tả Enum / Lookup Values", "description": "Liệt kê giá trị cho các trường ENUM.", "sub_steps": [
                "VD: status ENUM → 'active', 'inactive', 'archived'",
                "VD: priority ENUM → 'low', 'medium', 'high', 'critical'",
                "Mỗi giá trị có mô tả nghiệp vụ"
            ]},
            {"step": 4, "title": "Mô tả Indexes & Constraints", "description": "Liệt kê tất cả indexes.", "sub_steps": [
                "Primary Key Index",
                "Unique Indexes (email, code...)",
                "Foreign Key Indexes",
                "Composite Indexes cho query thường dùng",
                "Full-text Index (nếu cần search nội dung)"
            ]}
        ],
        "outputs_detail": [
            {"name": "Data Dictionary", "format": "Markdown Document (1 section per table)", "template": "# Data Dictionary: [Module Name]\n\n## Tổng quan\n| # | Table | Type | Description | Est. Rows |\n|---|---|---|---|---|\n| 1 | product | Master | Sản phẩm | 10,000 |\n| 2 | order | Transaction | Đơn hàng | 1,000,000 |\n| 3 | category | Lookup | Danh mục SP | 50 |\n\n---\n\n## Table: product\n**Mô tả:** Lưu trữ thông tin sản phẩm chính.\n**Loại:** Master Data\n\n| # | Column | Type | Null | Default | Constraint | Description | Sample |\n|---|---|---|---|---|---|---|---|\n| 1 | id | INT | No | AUTO_INC | PK | Mã sản phẩm | 1 |\n| 2 | code | VARCHAR(50) | No | | UQ, IDX | Mã hiển thị | 'PRD-001' |\n| 3 | name | VARCHAR(200) | No | | | Tên SP | 'Sữa TH 1L' |\n| 4 | category_id | INT | No | | FK→category.id, IDX | Danh mục | 3 |\n| 5 | unit_price | DECIMAL(15,2) | No | 0 | CHECK>0 | Đơn giá | 25000.00 |\n| 6 | is_deleted | BOOLEAN | No | false | | Soft delete | false |\n| 7 | created_at | DATETIME | No | NOW() | | Ngày tạo | '2024-01-15' |"}
        ],
        "sub_skills": ["Xác định Data Type", "Viết Constraint", "Ước lượng Data Volume"],
        "business_rules": [
            "BR-DD-01: Mỗi cột PHẢI có mô tả nghiệp vụ bằng tiếng Việt.",
            "BR-DD-02: Mỗi bảng PHẢI có Sample Data.",
            "BR-DD-03: ENUM values phải được liệt kê đầy đủ với mô tả.",
            "BR-DD-04: Foreign Key phải ghi rõ bảng tham chiếu (FK → table.column)."
        ],
        "edge_cases": [
            "Cột lưu JSON → Cần mô tả cấu trúc JSON bên trong",
            "Cột tính toán (Computed Column) → Ghi rõ công thức"
        ],
        "checklist": [
            "Mỗi bảng có mô tả?",
            "Mỗi cột có Data Type chính xác?",
            "Mỗi cột có Description?",
            "ENUM đã liệt kê values?",
            "FK ghi rõ bảng tham chiếu?",
            "Có Sample Data?",
            "Có ước lượng Data Volume?"
        ],
        "example": "Xem Data Dictionary template trong Outputs.",
        "related_skills": ["Thiết kế ERD", "Write SRS", "Thiết kế module"],
        "quality_criteria": ["Mỗi cột phải có Description", "ENUM phải có values", "FK phải ghi rõ target"],
        "estimated_effort": "2-3 ngày",
        "prompt_role": "Senior Data Analyst / Database Architect.",
        "prompt_task": "Tạo Data Dictionary chi tiết cho module.",
        "prompt_context": "Team cần tài liệu Data Dictionary để reference trong quá trình phát triển.",
        "prompt_rules": [
            "Mỗi bảng PHẢI có: Mô tả, Loại (Master/Transaction/Lookup).",
            "Mỗi cột PHẢI có: Type, Nullable, Default, Constraint, Description, Sample.",
            "ENUM PHẢI liệt kê values.",
            "FK PHẢI ghi rõ: FK → table.column.",
            "PHẢI có bảng tổng quan danh sách tables.",
            "Output PHẢI theo format Data Dictionary template."
        ],
        "prompt_example": ""
    }
]

if __name__ == "__main__":
    print("=== Expanding: UIUX + Modeling + Database Skills ===")
    run(skills)
