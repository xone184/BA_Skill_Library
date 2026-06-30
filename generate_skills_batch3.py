import os
import json

base_dir = r"e:\BA Skill Library\BA-Skills"

skills_data = [
    # ---------------- 01-Business-Domain / WMS (Advanced) ----------------
    {
        "path": "01-Business-Domain/WMS",
        "name": "Phân tích Cross Docking",
        "level": "Level 2 - Business Skill",
        "purpose": "Phân tích quy trình xuất/nhập nhanh (không lưu kho) để tối ưu thời gian giao hàng.",
        "inputs": ["ASN (Nhận hàng)", "SO (Đơn hàng cần giao ngay)"],
        "outputs": ["Luồng xử lý Cross-docking", "Yêu cầu chia chọn hàng (Sorting)"],
        "process": ["Nhận hàng tại cửa Inbound", "Phân loại theo đơn giao ngay", "Chuyển thẳng sang cửa Outbound", "Đóng gói & Giao đi"],
        "checklist": ["Có khu vực đệm (Staging area) đủ lớn không?", "Có hệ thống tự động nhận diện đơn cần Cross-dock không?"],
        "prompt_rules": ["Nêu bật tầm quan trọng của hệ thống quét mã vạch tốc độ cao trong khâu này."]
    },
    {
        "path": "01-Business-Domain/WMS",
        "name": "Phân tích Return Management",
        "level": "Level 2 - Business Skill",
        "purpose": "Quản lý hàng hoàn trả (RMA) từ khách hàng.",
        "inputs": ["Đơn yêu cầu hoàn trả (RMA)", "Hàng vật lý trả về"],
        "outputs": ["Quy trình Return", "Định khoản kho (Hàng lỗi / Hàng tái nhập)"],
        "process": ["Tiếp nhận yêu cầu", "Nhận hàng trả về", "Kiểm tra chất lượng (QC)", "Phân loại (Sửa chữa, Tiêu hủy, Tái lưu kho)"],
        "checklist": ["Có policy hoàn tiền (Refund) không?", "Có cập nhật lại tồn kho khả dụng ngay lập tức không?"],
        "prompt_rules": ["Luôn phải có quy trình QA kiểm định trước khi quyết định đưa hàng hoàn trả vào tồn kho bán tiếp."]
    },
    {
        "path": "01-Business-Domain/WMS",
        "name": "Phân tích Replenishment",
        "level": "Level 2 - Business Skill",
        "purpose": "Phân tích quy trình bổ sung hàng tự động (Replenishment).",
        "inputs": ["Điểm đặt hàng lại (Reorder Point)", "Tồn kho an toàn (Safety Stock)"],
        "outputs": ["Luật tạo yêu cầu bổ sung hàng", "Quy trình chuyển hàng từ Kho dự trữ sang Kho nhặt hàng"],
        "process": ["Theo dõi ngưỡng tồn kho", "Tạo lệnh bổ sung khi chạm mức MIN", "Di chuyển hàng từ Reserve sang Picking area"],
        "checklist": ["Có tính thời gian giao hàng (Lead time) của NCC không?", "Có cảnh báo khan hiếm hàng không?"],
        "prompt_rules": ["Công thức Reorder Point phải bao gồm Lead Time Demand + Safety Stock."]
    },
    # ---------------- 01-Business-Domain / CRM (Advanced) ----------------
    {
        "path": "01-Business-Domain/CRM",
        "name": "Phân tích Customer Support",
        "level": "Level 2 - Business Skill",
        "purpose": "Quản lý luồng tiếp nhận và xử lý yêu cầu hỗ trợ khách hàng (Ticket Management).",
        "inputs": ["Yêu cầu khách hàng (Email, Call, Chat)", "Hợp đồng SLA"],
        "outputs": ["Quy trình quản lý Ticket", "Ma trận phân quyền giải quyết (Tier 1, 2, 3)"],
        "process": ["Tiếp nhận Ticket", "Phân loại & Gán ưu tiên (Routing)", "Xử lý", "Đóng Ticket & Đánh giá CSAT"],
        "checklist": ["Có hệ thống cảnh báo vi phạm SLA không?", "Có tính năng gộp các ticket trùng lặp (Merge) không?"],
        "prompt_rules": ["Thiết kế phải đảm bảo SLA (Service Level Agreement) luôn được theo dõi realtime."]
    },
    {
        "path": "01-Business-Domain/CRM",
        "name": "Phân tích Loyalty Program",
        "level": "Level 2 - Business Skill",
        "purpose": "Phân tích hệ thống điểm thưởng và khách hàng thân thiết.",
        "inputs": ["Lịch sử mua hàng", "Chính sách hạng thành viên"],
        "outputs": ["Luật cộng/trừ điểm", "Cấu trúc hạng (Tier: Bạc, Vàng, Kim Cương)"],
        "process": ["Ghi nhận giao dịch", "Quy đổi doanh thu sang Điểm", "Nâng/Hạ hạng thành viên", "Xử lý đổi điểm lấy quà (Redeem)"],
        "checklist": ["Có luật hết hạn điểm (Point Expiration) không?", "Có chặn trường hợp gian lận điểm (Fraud) không?"],
        "prompt_rules": ["Rất lưu ý vòng lặp trả hàng (hoàn tiền) thì điểm thưởng tương ứng cũng phải bị trừ."]
    },
    # ---------------- 01-Business-Domain / HRM (Advanced) ----------------
    {
        "path": "01-Business-Domain/HRM",
        "name": "Phân tích Tuyển dụng",
        "level": "Level 2 - Business Skill",
        "purpose": "Phân tích quy trình Applicant Tracking System (ATS).",
        "inputs": ["Yêu cầu tuyển dụng (Job Requisition)", "CV Ứng viên"],
        "outputs": ["Luồng tuyển dụng (Hiring Pipeline)", "Màn hình quản lý Ứng viên"],
        "process": ["Đăng tuyển", "Lọc CV", "Phỏng vấn các vòng", "Đưa ra Offer", "Onboarding"],
        "checklist": ["Có tạo Talent Pool (Nguồn CV dự trữ) không?", "Có tích hợp gửi email tự động (Hẹn lịch, Cảm ơn) không?"],
        "prompt_rules": ["Luôn có trạng thái 'Blacklist' hoặc 'KIP' (Keep In Pool) cho các ứng viên chưa đạt."]
    },
    {
        "path": "01-Business-Domain/HRM",
        "name": "Phân tích KPI và Đánh giá",
        "level": "Level 2 - Business Skill",
        "purpose": "Thiết kế hệ thống đánh giá hiệu suất nhân sự (Performance Review).",
        "inputs": ["Tiêu chí đánh giá", "Mục tiêu công ty/phòng ban"],
        "outputs": ["Quy trình Review 360 độ", "Biểu mẫu đánh giá"],
        "process": ["Thiết lập mục tiêu đầu kỳ", "Tự đánh giá (Self-review)", "Quản lý đánh giá", "Họp 1-1", "Phê duyệt kết quả cuối"],
        "checklist": ["Có công thức tính điểm trọng số không?", "Có luồng khiếu nại kết quả không?"],
        "prompt_rules": ["Gợi ý áp dụng khung OKR thay vì chỉ dùng KPI truyền thống để tăng tính linh hoạt."]
    },
    # ---------------- 02-Requirement (Advanced) ----------------
    {
        "path": "02-Requirement/Use Case",
        "name": "Phân tích Use Case",
        "level": "Level 1 - Basic Skill",
        "purpose": "Xác định và phân tích các Use Case hệ thống.",
        "inputs": ["Yêu cầu người dùng", "Danh sách Actor"],
        "outputs": ["Danh sách Use Case", "Sơ đồ Use Case Diagram (UML)"],
        "process": ["Xác định Actor chính/phụ", "Xác định mục tiêu tương tác", "Liệt kê các Use Case", "Vẽ sơ đồ tổng quan"],
        "checklist": ["Có phân biệt rõ include và extend không?", "Actor có bao gồm 'Hệ thống ngoại vi' không?"],
        "prompt_rules": ["Luôn nhớ 'System Timer' (Hệ thống chạy ngầm định kỳ) cũng là một Actor hợp lệ."]
    },
    {
        "path": "02-Requirement/Use Case",
        "name": "Write Use Case Specification",
        "level": "Level 1 - Basic Skill",
        "purpose": "Viết đặc tả Use Case chi tiết (Use Case Spec).",
        "inputs": ["Tên Use Case", "Sơ đồ luồng"],
        "outputs": ["Tài liệu đặc tả Use Case"],
        "process": ["Định nghĩa Pre-condition", "Viết Basic Flow (Happy Path)", "Viết Alternative Flows", "Định nghĩa Post-condition"],
        "checklist": ["Các bước có đánh số thứ tự rõ ràng không?", "Có mô tả hành động của cả User lẫn System trong từng bước không?"],
        "prompt_rules": ["Cú pháp mỗi bước luôn là: '1. Hệ thống hiển thị...', '2. User nhập...'."]
    },
    {
        "path": "02-Requirement/Non Functional",
        "name": "Phân tích NFR",
        "level": "Level 3 - Architecture Skill",
        "purpose": "Khám phá và đặc tả các yêu cầu phi chức năng (Non-Functional Requirements).",
        "inputs": ["Đặc thù nghiệp vụ", "Kỳ vọng của khách hàng"],
        "outputs": ["Danh sách NFR (Performance, Security, Usability, Reliability, Scalability)"],
        "process": ["Phỏng vấn NFR", "Xác định các thông số (Metrics: CCU, Load time, Availability)", "Đặc tả các tiêu chuẩn bảo mật (OWASP)", "Lưu trữ NFR vào SRS"],
        "checklist": ["Có quy định thời gian phản hồi (Response Time) < 2s không?", "Có chiến lược sao lưu dữ liệu (Backup) không?"],
        "prompt_rules": ["Yêu cầu phi chức năng phải LUÔN có thể đo lường được (Measurable). Đừng dùng từ 'Nhanh', hãy dùng 'Dưới 2 giây'."]
    },
    # ---------------- 04-UIUX (Advanced) ----------------
    {
        "path": "04-UIUX/Dashboard",
        "name": "Phân tích Báo cáo động",
        "level": "Level 3 - Architecture Skill",
        "purpose": "Thiết kế hệ thống báo cáo cho phép người dùng tự kéo thả (Dynamic Reporting).",
        "inputs": ["Nhu cầu phân tích dữ liệu đa chiều"],
        "outputs": ["Cấu trúc khối dữ liệu (Data Cube)", "Danh sách Dimension và Measure"],
        "process": ["Xác định Dimension (Thuộc tính phân nhóm: Thời gian, Khu vực)", "Xác định Measure (Chỉ số đo lường: Doanh thu, Số lượng)", "Thiết kế giao diện Pivot/Kéo thả"],
        "checklist": ["Có hỗ trợ Export ra Excel/PDF giữ nguyên định dạng không?", "Có phân quyền dữ liệu theo cấp độ (Row-level security) không?"],
        "prompt_rules": ["Dynamic Report cực kỳ ngốn tài nguyên. Đề xuất tạo Data Warehouse/Data Mart riêng cho báo cáo."]
    },
    {
        "path": "04-UIUX/CRUD",
        "name": "Thiết kế Role-based UI",
        "level": "Level 3 - Architecture Skill",
        "purpose": "Phân tích giao diện thay đổi linh hoạt theo quyền của người dùng (RBAC).",
        "inputs": ["Ma trận phân quyền (Permission Matrix)"],
        "outputs": ["Luồng hiển thị/ẩn các nút thao tác", "Điều hướng tùy chỉnh"],
        "process": ["Xác định các Roles", "Ánh xạ Role với View/Edit/Delete", "Mô tả trạng thái UI (Hidden vs Disabled)"],
        "checklist": ["Nút bấm mà User không có quyền thì Ẩn đi hay Làm mờ (Disabled)?", "Có kiểm tra quyền lại ở dưới Backend (API) không?"],
        "prompt_rules": ["Rule UX tốt nhất: Ẩn đi những tính năng người dùng KHÔNG CÓ QUYỀN để giảm rác giao diện, trừ khi có mục đích upsell."]
    },
    # ---------------- 05-Database (Advanced) ----------------
    {
        "path": "05-Database/Data Dictionary",
        "name": "Data Migration Analysis",
        "level": "Level 4 - Thinking Skill",
        "purpose": "Phân tích quá trình chuyển đổi dữ liệu từ hệ thống cũ sang mới.",
        "inputs": ["Cấu trúc DB cũ (As-Is)", "Cấu trúc DB mới (To-Be)"],
        "outputs": ["Mapping Document (Data Mapping)", "Kịch bản Migration"],
        "process": ["Đánh giá dữ liệu cũ", "Xây dựng bảng Mapping (Trường cũ -> Trường mới)", "Làm sạch dữ liệu (Data Cleansing)", "Thiết kế kịch bản Cut-over"],
        "checklist": ["Có xử lý dữ liệu bị mồ côi (Orphaned Data) không?", "Có chạy diễn tập (Mock run) trước khi lên Go-Live không?"],
        "prompt_rules": ["Dữ liệu rác từ hệ thống cũ KHÔNG BAO GIỜ được đưa vào hệ thống mới nếu không được làm sạch."]
    },
    # ---------------- 06-Testing (Advanced) ----------------
    {
        "path": "06-Testing/Acceptance",
        "name": "Viết kịch bản UAT nâng cao",
        "level": "Level 2 - Business Skill",
        "purpose": "Xây dựng tài liệu hướng dẫn khách hàng ký nghiệm thu (Sign-off).",
        "inputs": ["UAT Script đã review", "Tiêu chí nghiệm thu"],
        "outputs": ["Tài liệu UAT Sign-off form", "Hướng dẫn ghi nhận lỗi (Bug tracking)"],
        "process": ["Cung cấp tài khoản test", "Hướng dẫn khách hàng thao tác", "Ghi nhận phản hồi", "Phân loại Bug (Lỗi hệ thống) vs CR (Thay đổi yêu cầu)"],
        "checklist": ["Đã thống nhất định nghĩa BUG vs CR trước khi khách hàng test chưa?", "Có giới hạn số vòng UAT không?"],
        "prompt_rules": ["Mấu chốt của UAT là quản lý kỳ vọng. Khách hàng luôn thích thêm tính năng mới trong lúc UAT, hãy cứng rắn bảo vệ scope."]
    },
    # ---------------- 08-Templates (Advanced) ----------------
    {
        "path": "08-Templates",
        "name": "Tạo Template Use Case Spec",
        "level": "Level 1 - Basic Skill",
        "purpose": "Tự động sinh ra biểu mẫu chuẩn cho Use Case Specification.",
        "inputs": ["Tên Use Case", "Tác nhân"],
        "outputs": ["Cấu trúc file Markdown chuẩn"],
        "process": ["Tạo phần Header (Name, Actor, Goal)", "Tạo bảng luồng chính (Main Flow)", "Tạo bảng luồng phụ (Alt Flow)", "Phần điều kiện trước/sau"],
        "checklist": ["Có chừa sẵn không gian cho Business Rules không?", "Có phần lịch sử sửa đổi không?"],
        "prompt_rules": ["Format đầu ra LUÔN sử dụng Markdown Tables cho các luồng để dễ đọc."]
    },
    {
        "path": "08-Templates",
        "name": "Tạo Template Meeting Minutes",
        "level": "Level 1 - Basic Skill",
        "purpose": "Sinh ra biểu mẫu Biên bản họp (MOM) chuyên nghiệp.",
        "inputs": ["Tên cuộc họp", "Thành phần tham dự"],
        "outputs": ["Biểu mẫu MoM"],
        "process": ["Header cuộc họp", "Mục tiêu (Agenda)", "Nội dung trao đổi", "Action Items (Người phụ trách, Deadline)"],
        "checklist": ["Mọi Action Item đều phải có người chịu trách nhiệm rõ ràng (Assignee) và Deadline.", "Có phần kết luận chốt vấn đề chưa?"],
        "prompt_rules": ["MoM không phải là bản chép lời (transcript). Chỉ ghi nhận Quyết định và Hành động."]
    },
    # ---------------- 09-BA-Agent (Thinking Advanced) ----------------
    {
        "path": "09-BA-Agent/Thinking Skills",
        "name": "Stakeholder Analysis",
        "level": "Level 4 - Thinking Skill",
        "purpose": "Phân tích và quản trị các bên liên quan trong dự án.",
        "inputs": ["Danh sách các cá nhân/tổ chức liên quan dự án"],
        "outputs": ["Ma trận Quyền lực - Mức độ quan tâm (Power/Interest Grid)", "Chiến lược giao tiếp"],
        "process": ["Liệt kê tất cả stakeholder", "Đánh giá mức độ ảnh hưởng (Power)", "Đánh giá mức độ quan tâm (Interest)", "Xếp vào 4 góc của ma trận", "Lập kế hoạch quản trị"],
        "checklist": ["Có người phản đối (Detractor) ngầm không?", "Nhà tài trợ (Sponsor) đã được xếp vào nhóm Manage Closely chưa?"],
        "prompt_rules": ["Sử dụng ma trận Power/Interest để định hình cách ứng xử với từng nhóm."]
    },
    {
        "path": "09-BA-Agent/Thinking Skills",
        "name": "Feasibility Study",
        "level": "Level 4 - Thinking Skill",
        "purpose": "Nghiên cứu tính khả thi của một yêu cầu hoặc một dự án.",
        "inputs": ["Ý tưởng kinh doanh / Yêu cầu mới lớn"],
        "outputs": ["Báo cáo đánh giá khả thi (Go/No-Go Decision)"],
        "process": ["Đánh giá kỹ thuật (Technical Feasibility)", "Đánh giá kinh tế (Economic/Cost-Benefit)", "Đánh giá hoạt động (Operational)", "Đánh giá thời gian (Schedule)"],
        "checklist": ["Đã tính đến chi phí bảo trì (Maintenance Cost) sau khi triển khai chưa?", "Công nghệ hiện tại có đáp ứng nổi không?"],
        "prompt_rules": ["Kết luận của phân tích này luôn phải là một quyết định: NÊN LÀM (Go), KHÔNG NÊN LÀM (No-Go), hoặc ĐIỀU KIỆN ĐỂ LÀM."]
    }
]

def generate_files():
    count = 0
    for skill in skills_data:
        full_path = os.path.join(base_dir, skill["path"])
        os.makedirs(full_path, exist_ok=True)
        
        md_content = f"""# Skill Name
{skill['name']}

## Level
{skill['level']}

## Purpose
{skill['purpose']}

## Inputs
"""
        for i in skill['inputs']:
            md_content += f"- {i}\n"
        
        md_content += "\n## Process\n"
        for idx, p in enumerate(skill['process']):
            md_content += f"{idx+1}. {p}\n"
            
        md_content += "\n## Outputs\n"
        for o in skill['outputs']:
            md_content += f"- {o}\n"
            
        md_content += "\n## Checklist\n"
        for c in skill['checklist']:
            md_content += f"- [ ] {c}\n"
            
        md_file = os.path.join(full_path, f"{skill['name'].replace(' ', '_')}.md")
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(md_content)
            
        json_data = {
            "name": skill['name'],
            "category": skill['path'],
            "level": skill['level'],
            "description": skill['purpose'],
            "inputs": skill['inputs'],
            "outputs": skill['outputs']
        }
        json_file = os.path.join(full_path, f"{skill['name'].replace(' ', '_')}.json")
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=4, ensure_ascii=False)
            
        prompt_content = f"""Role: Expert Business Analyst / System Architect
Task: Apply the skill [{skill['name']}]
Level: {skill['level']}

Context / Inputs required from user:
{', '.join(skill['inputs'])}

Rules & Constraints:
"""
        for r in skill['prompt_rules']:
            prompt_content += f"- {r}\n"
            
        prompt_content += f"""
Process to follow:
{', '.join(skill['process'])}

Expected Output:
{', '.join(skill['outputs'])}
"""
        prompt_file = os.path.join(full_path, f"{skill['name'].replace(' ', '_')}.prompt")
        with open(prompt_file, "w", encoding="utf-8") as f:
            f.write(prompt_content)
            
        count += 1
        
    print(f"Successfully generated {count} skills (total {count * 3} files).")

if __name__ == "__main__":
    generate_files()
