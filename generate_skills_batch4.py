import os
import json

base_dir = r"e:\BA Skill Library\BA-Skills"

skills_data = [
    # ---------------- 01-Business-Domain / Tài sản (EAM) ----------------
    {
        "path": "01-Business-Domain/EAM",
        "name": "Phân tích Quản lý Tài sản",
        "level": "Level 2 - Business Skill",
        "purpose": "Phân tích vòng đời của tài sản doanh nghiệp (Enterprise Asset Management).",
        "inputs": ["Danh mục tài sản", "Chính sách khấu hao"],
        "outputs": ["Luồng Quản lý tài sản", "Cấu trúc dữ liệu Asset"],
        "process": ["Mua sắm tài sản", "Ghi tăng tài sản & Cấp phát", "Bảo trì bảo dưỡng", "Khấu hao", "Thanh lý (Ghi giảm)"],
        "checklist": ["Có tạo mã vạch/QR code cho mỗi tài sản không?", "Có theo dõi lịch sử luân chuyển tài sản giữa các phòng ban không?"],
        "prompt_rules": ["Luôn tách biệt giữa 'Tài sản cố định' (Fixed Asset) cần khấu hao và 'Công cụ dụng cụ' (Tools) chỉ phân bổ một lần."]
    },
    {
        "path": "01-Business-Domain/EAM",
        "name": "Phân tích Bảo trì Thiết bị",
        "level": "Level 2 - Business Skill",
        "purpose": "Phân tích quy trình bảo trì phòng ngừa (Preventive Maintenance) và bảo trì khắc phục (Corrective Maintenance).",
        "inputs": ["Lịch bảo trì máy móc", "Yêu cầu sửa chữa"],
        "outputs": ["Work Order bảo trì", "Luồng phê duyệt vật tư thay thế"],
        "process": ["Lập kế hoạch bảo trì định kỳ", "Tiếp nhận báo hỏng", "Điều phối kỹ thuật viên", "Xuất vật tư thay thế", "Nghiệm thu & Đóng Work Order"],
        "checklist": ["Có liên kết tồn kho phụ tùng với Work Order không?", "Có dừng máy (Downtime) khi bảo trì không?"],
        "prompt_rules": ["Bắt buộc phải lưu lại chi phí bảo trì (nhân công + vật tư) vào lịch sử tài sản."]
    },
    # ---------------- 01-Business-Domain / POS & Retail ----------------
    {
        "path": "01-Business-Domain/POS",
        "name": "Phân tích Bán hàng tại quầy (POS)",
        "level": "Level 2 - Business Skill",
        "purpose": "Phân tích luồng thao tác của thu ngân tại cửa hàng.",
        "inputs": ["Danh mục hàng hóa", "Chương trình khuyến mãi (Promotion)"],
        "outputs": ["Luồng thao tác máy POS", "Xử lý thanh toán đa phương thức"],
        "process": ["Quét mã vạch sản phẩm", "Áp dụng khuyến mãi/Voucher", "Chọn phương thức thanh toán", "In hóa đơn", "Trừ tồn kho"],
        "checklist": ["Có hỗ trợ Split Payment (Khách trả 1 nửa tiền mặt, 1 nửa thẻ) không?", "Có chế độ Offline Mode khi mất mạng không?"],
        "prompt_rules": ["Hệ thống POS phải xử lý giao dịch dưới 3 giây. Đề xuất kiến trúc Microservices cho POS và Sync Offline/Online."]
    },
    # ---------------- 02-Requirement (Advanced Analysis) ----------------
    {
        "path": "02-Requirement/Functional",
        "name": "Phân tích Business Rules",
        "level": "Level 3 - Architecture Skill",
        "purpose": "Trích xuất và chuẩn hóa các quy tắc nghiệp vụ rải rác.",
        "inputs": ["Quy trình nghiệp vụ", "Chính sách công ty"],
        "outputs": ["Bảng Business Rules Catalog", "Decision Table (Bảng quyết định)"],
        "process": ["Đọc tài liệu nghiệp vụ", "Trích xuất các câu điều kiện (If-Then)", "Tổ chức thành Decision Table hoặc Decision Tree", "Gán ID cho từng rule để trace"],
        "checklist": ["Có Rule nào mâu thuẫn với Rule khác không?", "Có Rule nào chưa có cách xử lý (Missing Else) không?"],
        "prompt_rules": ["Tuyệt đối không nhúng Business Rule vào trong UI, phải quản lý tập trung ở Backend hoặc Rule Engine."]
    },
    {
        "path": "02-Requirement/Elicitation",
        "name": "Data Flow Analysis",
        "level": "Level 3 - Architecture Skill",
        "purpose": "Phân tích luồng di chuyển của dữ liệu qua các hệ thống.",
        "inputs": ["Sơ đồ kiến trúc hiện tại", "Quy trình nghiệp vụ"],
        "outputs": ["Data Flow Diagram (DFD)", "Danh sách Data Store"],
        "process": ["Xác định External Entities", "Vẽ luồng DFD Level 0 (Context)", "Vẽ luồng DFD Level 1 (Chi tiết)", "Xác định nơi lưu trữ dữ liệu"],
        "checklist": ["Có dữ liệu nào đi vào mà không đi ra không (Blackhole)?", "Có dữ liệu nào tự sinh ra không có nguồn gốc không (Miracle)?"],
        "prompt_rules": ["Một Data Store (Kho dữ liệu) không thể tự động truyền dữ liệu cho nhau nếu không thông qua một Process (Xử lý)."]
    },
    # ---------------- 03-Modeling (Advanced UML) ----------------
    {
        "path": "03-Modeling/UML",
        "name": "Class Diagram",
        "level": "Level 3 - Architecture Skill",
        "purpose": "Vẽ biểu đồ lớp để thiết kế hướng đối tượng.",
        "inputs": ["Danh từ trong tài liệu Yêu cầu", "Quy tắc nghiệp vụ"],
        "outputs": ["Class Diagram (Mermaid)"],
        "process": ["Xác định Classes", "Định nghĩa Attributes (Thuộc tính)", "Định nghĩa Methods (Hành động)", "Vẽ Relationships (Association, Inheritance, Aggregation)"],
        "checklist": ["Có lạm dụng Inheritance (Kế thừa) thay vì Composition không?", "Visibility (Public/Private) đã rõ ràng chưa?"],
        "prompt_rules": ["Sử dụng cú pháp Mermaid classDiagram. Mọi thuộc tính quan trọng phải có kiểu dữ liệu rõ ràng."]
    },
    # ---------------- 06-Testing (Security & Perf) ----------------
    {
        "path": "06-Testing/Security",
        "name": "Phân tích Security Testing",
        "level": "Level 3 - Architecture Skill",
        "purpose": "Xác định các lỗ hổng bảo mật và viết kịch bản test an toàn thông tin.",
        "inputs": ["Kiến trúc hệ thống", "Tài liệu API"],
        "outputs": ["Security Test Cases (OWASP Top 10)"],
        "process": ["Phân tích Authorization/Authentication", "Phân tích rủi ro Injection (SQL, XSS)", "Viết kịch bản kiểm thử bảo mật", "Lên kế hoạch Pentest"],
        "checklist": ["API có Rate Limiting không?", "Mật khẩu có được băm (Hashed) trước khi lưu không?"],
        "prompt_rules": ["Phải liệt kê rõ các biện pháp chống Brute-force attack và SQL Injection trong hệ thống."]
    },
    {
        "path": "06-Testing/Regression",
        "name": "Regression Testing Plan",
        "level": "Level 2 - Business Skill",
        "purpose": "Lập kế hoạch kiểm thử hồi quy khi có tính năng mới.",
        "inputs": ["Danh sách tính năng mới", "Impact Analysis Report"],
        "outputs": ["Bộ Regression Test Suite", "Quy trình Automation Test"],
        "process": ["Xác định vùng ảnh hưởng", "Chọn lọc Test Case cũ cần chạy lại", "Bổ sung Test Case mới", "Thực thi và báo cáo"],
        "checklist": ["Đã phủ hết các module dùng chung (Shared libraries) chưa?", "Có ưu tiên test các tính năng Core (Tiền bạc, Đăng nhập) không?"],
        "prompt_rules": ["Kiểm thử hồi quy phải bao phủ 100% các tính năng P1 (Critical) của hệ thống."]
    },
    # ---------------- 07-Project (Scrum Ceremonies) ----------------
    {
        "path": "07-Project/Scrum",
        "name": "Sprint Review",
        "level": "Level 2 - Business Skill",
        "purpose": "Tổ chức buổi Demo sản phẩm cuối Sprint.",
        "inputs": ["Sản phẩm đã hoàn thành (Done Increment)"],
        "outputs": ["Feedback từ Stakeholders", "Cập nhật Product Backlog"],
        "process": ["Trình bày Sprint Goal", "Dev team demo tính năng chạy thực tế", "Nhận phản hồi từ khách hàng/PO", "Cập nhật Backlog cho Sprint sau"],
        "checklist": ["Chỉ Demo những tính năng đã hoàn toàn 'Done' đúng không?", "Khách hàng có tham gia đầy đủ không?"],
        "prompt_rules": ["Không bao giờ dùng slide PowerPoint để Demo, phải thao tác trên phần mềm thật."]
    },
    # ---------------- 08-Templates (Advanced Documents) ----------------
    {
        "path": "08-Templates",
        "name": "Tạo Template RTM",
        "level": "Level 1 - Basic Skill",
        "purpose": "Tạo ma trận truy xuất yêu cầu (Requirement Traceability Matrix).",
        "inputs": ["Danh sách BRD", "Danh sách Test Case"],
        "outputs": ["Bảng RTM chuẩn"],
        "process": ["Tạo cột Requirement ID", "Tạo cột Use Case ID", "Tạo cột Design ID", "Tạo cột Test Case ID", "Tạo cột Status"],
        "checklist": ["Có Requirement nào bị 'mồ côi' (Không có Test Case) không?", "Tất cả ID đã được map 1-1 hoặc 1-N chưa?"],
        "prompt_rules": ["Sử dụng Markdown Table. RTM là bắt buộc để chứng minh hệ thống đã làm đủ những gì cam kết."]
    },
    {
        "path": "08-Templates",
        "name": "Tạo Template API Doc",
        "level": "Level 3 - Architecture Skill",
        "purpose": "Tự động sinh ra cấu trúc tài liệu Swagger/OpenAPI.",
        "inputs": ["API Contract"],
        "outputs": ["Markdown API Documentation"],
        "process": ["Mô tả Endpoint & Method", "Đặc tả Request Headers (Auth Token)", "Đặc tả Request Body (JSON Schema)", "Đặc tả Response 200/400/500"],
        "checklist": ["Có ví dụ (Example) cụ thể cho chuỗi JSON không?", "Mã lỗi (Error Codes) có được giải thích không?"],
        "prompt_rules": ["Tài liệu API phải cực kỳ rõ ràng, luôn đi kèm JSON format example. Sử dụng code block `json`."]
    },
    # ---------------- 09-BA-Agent (Thinking) ----------------
    {
        "path": "09-BA-Agent/Thinking Skills",
        "name": "Cost-Benefit Analysis",
        "level": "Level 4 - Thinking Skill",
        "purpose": "Phân tích chi phí và lợi ích để ra quyết định đầu tư tính năng.",
        "inputs": ["Chi phí ước tính (Dev, Vận hành)", "Lợi ích kỳ vọng (Tăng doanh thu, Giảm nhân sự)"],
        "outputs": ["Báo cáo ROI (Return on Investment)", "Thời gian hoàn vốn (Payback Period)"],
        "process": ["Định lượng toàn bộ Chi phí (Hữu hình & Vô hình)", "Định lượng toàn bộ Lợi ích", "Tính ROI = (Lợi ích - Chi phí) / Chi phí", "Đưa ra khuyến nghị"],
        "checklist": ["Đã tính chi phí Server/Cloud hàng tháng chưa?", "Lợi ích vô hình (Uy tín thương hiệu) có được đánh giá không?"],
        "prompt_rules": ["Là một Senior BA, phải luôn dùng những con số định lượng ($) để thuyết phục sếp/khách hàng, thay vì cảm tính."]
    },
    {
        "path": "09-BA-Agent/Thinking Skills",
        "name": "SWOT Analysis",
        "level": "Level 4 - Thinking Skill",
        "purpose": "Phân tích Điểm mạnh, Điểm yếu, Cơ hội và Thách thức của sản phẩm.",
        "inputs": ["Thông tin thị trường", "Tính năng đối thủ"],
        "outputs": ["Ma trận SWOT", "Chiến lược hành động"],
        "process": ["Xác định Strengths (Nội bộ)", "Xác định Weaknesses (Nội bộ)", "Xác định Opportunities (Bên ngoài)", "Xác định Threats (Bên ngoài)", "Mapping giải pháp (S-O, W-O)"],
        "checklist": ["Đã so sánh trực tiếp với Competitor chưa?", "Threats có tính đến rủi ro pháp lý/luật pháp không?"],
        "prompt_rules": ["SWOT không chỉ để liệt kê, mà phải đưa ra Chiến lược (Ví dụ: Dùng Điểm mạnh nào để đánh chiếm Cơ hội nào)."]
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
