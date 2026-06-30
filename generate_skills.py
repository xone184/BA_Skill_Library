import os
import json

base_dir = r"e:\BA Skill Library\BA-Skills"

# The generator script for BA Skill Library
# Generating ~40-50 core skills with .md, .json, .prompt files

skills_data = [
    # ---------------- 01-Business-Domain / CRM ----------------
    {
        "path": "01-Business-Domain/CRM",
        "name": "Phân tích Lead Management",
        "level": "Level 2 - Business Skill",
        "purpose": "Phân tích quy trình quản lý khách hàng tiềm năng.",
        "inputs": ["Nguồn Lead", "Trạng thái Lead", "Kênh Marketing"],
        "outputs": ["Quy trình Lead Lifecycle", "Cấu trúc dữ liệu Lead"],
        "process": ["Ghi nhận nguồn Lead", "Scoring (chấm điểm)", "Gán cho Sale (Routing)", "Chuyển đổi thành Opportunity"],
        "checklist": ["Có check trùng lặp (duplicate) không?", "Có log lịch sử chăm sóc không?", "Có tự động nhắc việc không?"],
        "prompt_rules": ["Luôn kiểm tra rule chống trùng lặp dữ liệu.", "Đảm bảo luồng chuyển đổi từ Lead -> Account rõ ràng."]
    },
    {
        "path": "01-Business-Domain/CRM",
        "name": "Phân tích Opportunity",
        "level": "Level 2 - Business Skill",
        "purpose": "Phân tích luồng cơ hội bán hàng và đường ống (Pipeline).",
        "inputs": ["Lead đã chuyển đổi", "Sản phẩm quan tâm", "Ngân sách"],
        "outputs": ["Sales Pipeline", "Giai đoạn cơ hội (Stages)"],
        "process": ["Định nghĩa các stage", "Xác định tỷ lệ % win", "Dự báo doanh thu (Forecasting)"],
        "checklist": ["Có lý do lost (Lost Reason) không?", "Có phê duyệt giảm giá không?"],
        "prompt_rules": ["Luôn có rule bắt buộc nhập Lost Reason khi đóng cơ hội.", "Xác định rõ vai trò của Sales Manager trong việc duyệt."]
    },
    # ---------------- 01-Business-Domain / WMS ----------------
    {
        "path": "01-Business-Domain/WMS",
        "name": "Phân tích Inbound Flow",
        "level": "Level 2 - Business Skill",
        "purpose": "Phân tích quy trình nhập kho hàng hóa.",
        "inputs": ["Purchase Order (PO)", "Advance Shipping Notice (ASN)"],
        "outputs": ["Quy trình Nhập kho", "Goods Receipt Note (GRN)"],
        "process": ["Nhận thông báo giao hàng", "Kiểm tra xe vào", "Dỡ hàng (Unloading)", "Kiểm đếm (Tally)", "Cất hàng lên kệ (Putaway)"],
        "checklist": ["Có xử lý hàng hư hỏng (Damage) không?", "Có in tem mã vạch (Barcode) lúc nhận không?"],
        "prompt_rules": ["Luôn đề xuất chiến lược Putaway (cất hàng) tự động nếu kho lớn.", "Xử lý triệt để bài toán hàng thừa/thiếu so với PO."]
    },
    {
        "path": "01-Business-Domain/WMS",
        "name": "Phân tích Outbound Flow",
        "level": "Level 2 - Business Skill",
        "purpose": "Phân tích quy trình xuất kho và giao hàng.",
        "inputs": ["Sales Order (SO)", "Lệnh xuất kho"],
        "outputs": ["Quy trình xuất kho", "Delivery Note"],
        "process": ["Nhận lệnh xuất", "Lấy hàng (Picking)", "Đóng gói (Packing)", "Xuất hàng (Shipping)"],
        "checklist": ["Áp dụng FIFO/FEFO hay LIFO?", "Có ghép đơn (Wave Picking) không?"],
        "prompt_rules": ["Kiểm tra chặt chẽ nguyên tắc xuất kho (FIFO, FEFO đối với hàng có HSD).", "Gợi ý lộ trình Picking tối ưu cho nhân viên kho."]
    },
    {
        "path": "01-Business-Domain/WMS",
        "name": "Phân tích Inventory Management",
        "level": "Level 2 - Business Skill",
        "purpose": "Phân tích quy trình quản lý tồn kho và kiểm kê.",
        "inputs": ["Dữ liệu tồn kho hiện tại", "Biến động kho"],
        "outputs": ["Luồng Cycle Count", "Báo cáo tồn kho"],
        "process": ["Chốt sổ tồn kho", "Tạo phiếu kiểm kê", "Quét mã vạch kiểm đếm", "Xử lý chênh lệch"],
        "checklist": ["Có chặn giao dịch khi đang kiểm kê không?", "Có duyệt chênh lệch không?"],
        "prompt_rules": ["Phải có bước duyệt của Kế toán hoặc Quản lý kho nếu tồn kho chênh lệch."]
    },
    # ---------------- 01-Business-Domain / MES ----------------
    {
        "path": "01-Business-Domain/MES",
        "name": "Phân tích Production Order",
        "level": "Level 2 - Business Skill",
        "purpose": "Phân tích luồng lệnh sản xuất trong nhà máy.",
        "inputs": ["Kế hoạch sản xuất (Production Plan)", "BOM (Bill of Materials)"],
        "outputs": ["Work Order (WO)", "Routing (Định mức nhân công, máy móc)"],
        "process": ["Tiếp nhận kế hoạch", "Tạo Lệnh sản xuất", "Kiểm tra nguyên vật liệu (Material Availability)", "Phát lệnh xuống xưởng"],
        "checklist": ["Có kiểm tra tồn kho NVL trước khi chạy lệnh không?", "Có tính phế phẩm (Scrap) không?"],
        "prompt_rules": ["MES luôn cần liên kết chặt chẽ với tồn kho. Nếu thiếu vật tư, không được phát lệnh."]
    },
    {
        "path": "01-Business-Domain/MES",
        "name": "Phân tích OEE",
        "level": "Level 2 - Business Skill",
        "purpose": "Đo lường và phân tích hiệu quả thiết bị tổng thể (Overall Equipment Effectiveness).",
        "inputs": ["Dữ liệu máy móc", "Dữ liệu sản xuất", "Thời gian dừng máy (Downtime)"],
        "outputs": ["Báo cáo OEE", "Nguyên nhân downtime"],
        "process": ["Thu thập Availability", "Thu thập Performance", "Thu thập Quality", "Tính toán OEE", "Phân tích root cause"],
        "checklist": ["Có trừ đi thời gian setup máy không?", "Có loại trừ thời gian nghỉ trưa không?"],
        "prompt_rules": ["Chỉ sử dụng công thức OEE chuẩn = Availability x Performance x Quality.", "Luôn tìm nguyên nhân gốc rễ của downtime."]
    },
    {
        "path": "01-Business-Domain/MES",
        "name": "Phân tích Quality Control",
        "level": "Level 2 - Business Skill",
        "purpose": "Phân tích quy trình quản lý chất lượng (QA/QC) trong sản xuất.",
        "inputs": ["Tiêu chuẩn chất lượng (SOP)", "Sản phẩm đầu ra"],
        "outputs": ["Quy trình QC", "Phiếu kiểm định"],
        "process": ["Lấy mẫu (Sampling)", "Kiểm tra các chỉ tiêu", "Đánh giá Pass/Fail", "Xử lý hàng lỗi (Rework/Scrap)"],
        "checklist": ["Có lưu log người kiểm tra không?", "Có workflow sửa hàng lỗi (Rework) không?"],
        "prompt_rules": ["Bắt buộc phải có luồng xử lý sản phẩm Fail (Tái chế, Tiêu hủy, hoặc Hạ cấp)."]
    },
    # ---------------- 02-Requirement ----------------
    {
        "path": "02-Requirement/Elicitation",
        "name": "Interview Stakeholder",
        "level": "Level 1 - Basic Skill",
        "purpose": "Thực hiện phỏng vấn lấy yêu cầu từ các bên liên quan.",
        "inputs": ["Danh sách Stakeholder", "Mục tiêu dự án"],
        "outputs": ["Meeting Minutes", "Danh sách yêu cầu sơ bộ"],
        "process": ["Xác định đối tượng", "Chuẩn bị bộ câu hỏi", "Tiến hành phỏng vấn", "Ghi chép và xác nhận lại"],
        "checklist": ["Có hỏi 'Tại sao' để tìm Root Cause không?", "Có chốt lại với người được phỏng vấn không?"],
        "prompt_rules": ["Luôn đóng vai trò người tò mò, hỏi sâu vào Pain Points (Nỗi đau) của Stakeholder."]
    },
    {
        "path": "02-Requirement/User Story",
        "name": "Write User Story",
        "level": "Level 1 - Basic Skill",
        "purpose": "Viết User Story chuẩn Agile.",
        "inputs": ["Requirement", "Actor"],
        "outputs": ["User Story theo chuẩn (As a... I want to... So that...)"],
        "process": ["Xác định Actor", "Xác định hành động", "Xác định giá trị mang lại", "Viết Acceptance Criteria"],
        "checklist": ["Có tuân thủ INVEST (Independent, Negotiable, Valuable, Estimable, Small, Testable) không?", "Có Acceptance Criteria rõ ràng không?"],
        "prompt_rules": ["Output luôn phải có định dạng: As a [Role], I want to [Action], So that [Benefit].", "Đi kèm ít nhất 3 Acceptance Criteria."]
    },
    {
        "path": "02-Requirement/BRD",
        "name": "Write BRD",
        "level": "Level 1 - Basic Skill",
        "purpose": "Soạn thảo Business Requirement Document.",
        "inputs": ["Yêu cầu nghiệp vụ tổng thể", "Phạm vi dự án (Scope)"],
        "outputs": ["Tài liệu BRD hoàn chỉnh"],
        "process": ["Tóm tắt dự án", "Xác định mục tiêu kinh doanh", "Liệt kê Stakeholders", "Định nghĩa In-scope và Out-of-scope", "Liệt kê yêu cầu cấp cao"],
        "checklist": ["Có Out-of-scope rõ ràng chưa?", "Các yêu cầu có đánh số ID để trace không?"],
        "prompt_rules": ["BRD chỉ tập trung vào 'CÁI GÌ' (What) và 'TẠI SAO' (Why), KHÔNG mô tả 'NHƯ THẾ NÀO' (How)."]
    },
    {
        "path": "02-Requirement/SRS",
        "name": "Write SRS",
        "level": "Level 1 - Basic Skill",
        "purpose": "Soạn thảo Software Requirements Specification.",
        "inputs": ["BRD", "Danh sách User Story"],
        "outputs": ["Tài liệu SRS chi tiết"],
        "process": ["Mô tả tổng quan hệ thống", "Đặc tả chức năng (Functional)", "Đặc tả phi chức năng (Non-Functional)", "Mô tả giao diện, API"],
        "checklist": ["Có liệt kê đủ Non-Functional (Performance, Security, Reliability) không?", "Có Data Model sơ bộ không?"],
        "prompt_rules": ["SRS phải cực kỳ chi tiết để team Dev có thể code được ngay."]
    },
    # ---------------- 03-Modeling ----------------
    {
        "path": "03-Modeling/BPMN",
        "name": "Draw BPMN",
        "level": "Level 2 - Business Skill",
        "purpose": "Vẽ luồng quy trình nghiệp vụ bằng chuẩn BPMN.",
        "inputs": ["Mô tả quy trình bằng lời"],
        "outputs": ["Sơ đồ BPMN (định dạng PlantUML/Mermaid)"],
        "process": ["Xác định các Pool/Lane (Actors)", "Xác định điểm bắt đầu (Start Event)", "Liệt kê các Task", "Xác định các điểm rẽ nhánh (Gateway)", "Kết thúc (End Event)"],
        "checklist": ["Có thiếu Gateway (Exclusive/Parallel) không?", "Luồng có đi đến End Event không?"],
        "prompt_rules": ["Sử dụng cú pháp Mermaid.js hoặc PlantUML để biểu diễn đồ họa.", "Bắt buộc chia Lane rõ ràng cho từng phòng ban."]
    },
    {
        "path": "03-Modeling/ERD",
        "name": "Thiết kế ERD",
        "level": "Level 3 - Architecture Skill",
        "purpose": "Thiết kế mô hình thực thể liên kết (Entity Relationship Diagram).",
        "inputs": ["Danh sách các thực thể (Entity)", "Nghiệp vụ"],
        "outputs": ["Sơ đồ ERD", "Giải thích quan hệ (1-1, 1-N, N-N)"],
        "process": ["Xác định các Entity", "Định nghĩa Primary Key", "Định nghĩa Foreign Key", "Vẽ quan hệ"],
        "checklist": ["Đã chuẩn hóa (Normalization) về dạng 3NF chưa?", "Có giải quyết quan hệ N-N bằng bảng trung gian không?"],
        "prompt_rules": ["Sử dụng cú pháp Mermaid ER diagram.", "Đặt tên bảng theo chuẩn snake_case hoặc PascalCase."]
    },
    {
        "path": "03-Modeling/Architecture",
        "name": "Thiết kế API Contract",
        "level": "Level 3 - Architecture Skill",
        "purpose": "Thiết kế đặc tả API cơ bản giữa FE và BE hoặc với bên thứ 3.",
        "inputs": ["Yêu cầu tích hợp", "Dữ liệu cần truyền"],
        "outputs": ["Tài liệu API Contract (RESTful)"],
        "process": ["Xác định Endpoint & Method", "Định nghĩa Request Header/Body", "Định nghĩa Response (Success/Error)", "Xác định mã lỗi HTTP"],
        "checklist": ["Có Token Authentication không?", "Có phân trang (Pagination) đối với list không?"],
        "prompt_rules": ["Thiết kế RESTful API chuẩn: GET lấy dữ liệu, POST tạo mới, PUT/PATCH cập nhật, DELETE xóa."]
    },
    # ---------------- 04-UIUX ----------------
    {
        "path": "04-UIUX/Dashboard",
        "name": "Thiết kế Dashboard",
        "level": "Level 3 - Architecture Skill",
        "purpose": "Xác định cấu trúc và các chỉ số trên Dashboard quản trị.",
        "inputs": ["Mục tiêu người dùng (Manager, Admin)", "Các KPI chính"],
        "outputs": ["Wireframe/Layout mô tả", "Danh sách Chart/Widget"],
        "process": ["Xác định user persona", "Chọn lọc 5-7 KPI quan trọng nhất", "Chọn loại biểu đồ phù hợp (Bar, Line, Pie)", "Sắp xếp layout"],
        "checklist": ["Có bộ lọc thời gian (Date Filter) không?", "Dữ liệu có realtime không?"],
        "prompt_rules": ["Đừng nhồi nhét quá nhiều số liệu. Chỉ tập trung vào Actionable Insights."]
    },
    {
        "path": "04-UIUX/CRUD",
        "name": "Phân tích màn hình CRUD",
        "level": "Level 2 - Business Skill",
        "purpose": "Đặc tả màn hình Quản lý danh mục (Create, Read, Update, Delete).",
        "inputs": ["Đối tượng dữ liệu (VD: Sản phẩm, Khách hàng)"],
        "outputs": ["Đặc tả List Page", "Đặc tả Detail/Form Page"],
        "process": ["Xác định các cột trên lưới (Grid)", "Xác định tiêu chí tìm kiếm/lọc", "Đặc tả form Thêm mới/Sửa", "Xác định quyền xóa"],
        "checklist": ["Có Soft Delete thay vì Hard Delete không?", "Có Import/Export Excel không?"],
        "prompt_rules": ["Luôn đề xuất Soft Delete (is_deleted = true) cho các hệ thống doanh nghiệp."]
    },
    # ---------------- 05-Database ----------------
    {
        "path": "05-Database/Data Dictionary",
        "name": "Create Data Dictionary",
        "level": "Level 3 - Architecture Skill",
        "purpose": "Tạo từ điển dữ liệu đặc tả các trường trong database.",
        "inputs": ["ERD", "Yêu cầu nghiệp vụ"],
        "outputs": ["Bảng Data Dictionary"],
        "process": ["Liệt kê các trường (Field Name)", "Xác định kiểu dữ liệu (Data Type)", "Ràng buộc (Constraints)", "Mô tả ý nghĩa (Description)"],
        "checklist": ["Có quy định Max Length không?", "Có Is Null / Not Null rõ ràng chưa?"],
        "prompt_rules": ["Sử dụng Markdown Table để trình bày Data Dictionary."]
    },
    # ---------------- 06-Testing ----------------
    {
        "path": "06-Testing/Test Case",
        "name": "Viết Test Case",
        "level": "Level 1 - Basic Skill",
        "purpose": "Viết kịch bản kiểm thử phần mềm.",
        "inputs": ["SRS", "User Story", "Acceptance Criteria"],
        "outputs": ["Danh sách Test Case chi tiết"],
        "process": ["Đọc kỹ yêu cầu", "Xác định Happy Path", "Xác định Edge Cases / Negative Cases", "Viết Step-by-step"],
        "checklist": ["Có phủ hết Acceptance Criteria chưa?", "Có Test Case bảo mật/phân quyền không?"],
        "prompt_rules": ["Số lượng Negative Test Cases phải luôn nhiều hơn Happy Path Test Cases."]
    },
    {
        "path": "06-Testing/UAT",
        "name": "Xây dựng kịch bản UAT",
        "level": "Level 2 - Business Skill",
        "purpose": "Chuẩn bị kịch bản User Acceptance Testing cho người dùng cuối.",
        "inputs": ["Quy trình nghiệp vụ thực tế", "BRD"],
        "outputs": ["UAT Script theo luồng (End-to-End)"],
        "process": ["Lựa chọn các quy trình cốt lõi", "Chuẩn bị dữ liệu mẫu (Test Data)", "Viết các bước thao tác trên góc độ User"],
        "checklist": ["Ngôn ngữ đã dễ hiểu với End-user chưa?", "Dữ liệu test có giống thực tế không?"],
        "prompt_rules": ["UAT Script không viết theo module, mà phải viết theo luồng (Ví dụ: Từ lúc tạo Lead đến lúc xuất Hóa đơn)."]
    },
    # ---------------- 07-Project ----------------
    {
        "path": "07-Project/Scrum",
        "name": "Backlog Grooming",
        "level": "Level 2 - Business Skill",
        "purpose": "Làm mịn và sắp xếp độ ưu tiên cho Product Backlog.",
        "inputs": ["Product Backlog hiện tại", "Phản hồi từ Stakeholders"],
        "outputs": ["Backlog đã được sắp xếp", "User Story rõ ràng hơn"],
        "process": ["Review các item cũ", "Phân rã Epic lớn thành Story nhỏ", "Gán độ ưu tiên (MoSCoW)", "Bổ sung Acceptance Criteria"],
        "checklist": ["Story có đủ nhỏ để làm trong 1 Sprint không?", "Có Story nào thiếu Acceptance Criteria không?"],
        "prompt_rules": ["Áp dụng kỹ thuật MoSCoW (Must have, Should have, Could have, Won't have) để đánh giá ưu tiên."]
    },
    # ---------------- 09-BA-Agent (Thinking Skills) ----------------
    {
        "path": "09-BA-Agent/Thinking Skills",
        "name": "Gap Analysis",
        "level": "Level 4 - Thinking Skill",
        "purpose": "Phân tích khoảng cách giữa hệ thống hiện tại (As-Is) và hệ thống mong muốn (To-Be).",
        "inputs": ["Quy trình As-Is", "Mục tiêu To-Be"],
        "outputs": ["Danh sách các Gaps", "Đề xuất giải pháp (Action Plan)"],
        "process": ["Vẽ luồng As-Is", "Định nghĩa mục tiêu To-Be", "Xác định điểm thiếu hụt (Gaps về System, Data, Process)", "Lập kế hoạch thu hẹp Gap"],
        "checklist": ["Có đánh giá rủi ro khi thay đổi quy trình không?", "Giải pháp có khả thi về mặt kỹ thuật không?"],
        "prompt_rules": ["Luôn chia Gap thành 3 nhóm: Business Process, Technology/System, và People."]
    },
    {
        "path": "09-BA-Agent/Thinking Skills",
        "name": "Root Cause Analysis",
        "level": "Level 4 - Thinking Skill",
        "purpose": "Phân tích nguyên nhân gốc rễ của một vấn đề kinh doanh hoặc lỗi hệ thống.",
        "inputs": ["Vấn đề (Problem Statement)", "Dữ liệu liên quan"],
        "outputs": ["Nguyên nhân gốc rễ", "Giải pháp triệt để"],
        "process": ["Xác định vấn đề", "Thu thập dữ liệu", "Sử dụng 5 Whys hoặc Fishbone Diagram", "Xác định Root Cause", "Đề xuất giải pháp"],
        "checklist": ["Đã hỏi đủ 5 lần TẠI SAO chưa?", "Giải pháp có xử lý triệt để được nguyên nhân gốc không?"],
        "prompt_rules": ["Sử dụng kỹ thuật 5 Whys. Trình bày dưới dạng hội thoại hỏi - đáp liên tục."]
    },
    {
        "path": "09-BA-Agent/Thinking Skills",
        "name": "Impact Analysis",
        "level": "Level 4 - Thinking Skill",
        "purpose": "Phân tích tác động khi có thay đổi yêu cầu (Change Request).",
        "inputs": ["Yêu cầu thay đổi (CR)", "Hệ thống hiện tại"],
        "outputs": ["Báo cáo đánh giá tác động"],
        "process": ["Nhận diện thay đổi", "Truy vết (Traceability) các module bị ảnh hưởng", "Đánh giá nỗ lực (Effort) sửa đổi", "Đánh giá rủi ro"],
        "checklist": ["Có ảnh hưởng đến database cũ không?", "Có làm hỏng API của Mobile App không?", "Team Test cần test lại những vùng nào?"],
        "prompt_rules": ["Khi có CR, luôn cảnh báo các module vệ tinh có thể bị ảnh hưởng (Regression Impact)."]
    }
]

def generate_files():
    count = 0
    for skill in skills_data:
        # Create directories
        full_path = os.path.join(base_dir, skill["path"])
        os.makedirs(full_path, exist_ok=True)
        
        # 1. Generate .md
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
            
        # 2. Generate .json
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
            
        # 3. Generate .prompt
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
