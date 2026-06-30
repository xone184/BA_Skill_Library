import os
import json

base_dir = r"e:\BA Skill Library\BA-Skills"

skills_data = [
    # ---------------- 01-Business-Domain / ERP ----------------
    {
        "path": "01-Business-Domain/ERP",
        "name": "Phân tích Procurement",
        "level": "Level 2 - Business Skill",
        "purpose": "Phân tích quy trình mua hàng (Procure-to-Pay).",
        "inputs": ["Yêu cầu mua hàng (PR)", "Báo giá NCC (Quotation)"],
        "outputs": ["Purchase Order (PO)", "Quy trình mua hàng"],
        "process": ["Tạo PR", "Duyệt PR", "Lấy báo giá", "Tạo PO", "Duyệt PO", "Gửi PO cho NCC"],
        "checklist": ["Có luồng đánh giá NCC định kỳ không?", "Có quản lý ngân sách (Budgeting) không?"],
        "prompt_rules": ["Luôn bắt buộc phải qua bước duyệt PO nếu số tiền vượt hạn mức."]
    },
    {
        "path": "01-Business-Domain/ERP",
        "name": "Phân tích Kế toán công nợ",
        "level": "Level 2 - Business Skill",
        "purpose": "Phân tích luồng công nợ phải thu (AR) và phải trả (AP).",
        "inputs": ["Hóa đơn", "Hợp đồng", "Phiếu xuất/nhập"],
        "outputs": ["Quy trình theo dõi công nợ", "Báo cáo tuổi nợ"],
        "process": ["Ghi nhận phát sinh nợ", "Đối chiếu công nợ", "Lập kế hoạch thanh toán/thu tiền", "Xóa nợ (Write-off)"],
        "checklist": ["Có hạn mức tín dụng (Credit Limit) cho khách hàng không?", "Có cảnh báo nợ quá hạn không?"],
        "prompt_rules": ["Bắt buộc phong tỏa tài khoản khách hàng nếu nợ quá hạn vượt Credit Limit."]
    },
    # ---------------- 01-Business-Domain / HRM ----------------
    {
        "path": "01-Business-Domain/HRM",
        "name": "Phân tích Chấm công",
        "level": "Level 2 - Business Skill",
        "purpose": "Phân tích quy trình quản lý thời gian làm việc (Time & Attendance).",
        "inputs": ["Dữ liệu máy chấm công", "Ca làm việc (Shift)", "Đơn từ nghỉ phép"],
        "outputs": ["Bảng công tổng hợp", "Quy trình xử lý đi trễ/về sớm"],
        "process": ["Thiết lập ca làm việc", "Mapping dữ liệu vào ra", "Trừ phép/Xử lý vi phạm", "Duyệt bảng công"],
        "checklist": ["Có xử lý làm thêm giờ (OT) không?", "Dữ liệu máy chấm công có realtime không?"],
        "prompt_rules": ["Phải mô tả rõ công thức làm tròn giờ (ví dụ: trễ 15p tính là nửa tiếng)."]
    },
    {
        "path": "01-Business-Domain/HRM",
        "name": "Phân tích Payroll",
        "level": "Level 2 - Business Skill",
        "purpose": "Phân tích luồng tính lương nhân viên.",
        "inputs": ["Bảng công", "Chính sách lương thưởng", "Khấu trừ thuế/BHXH"],
        "outputs": ["Bảng lương chi tiết", "Phiếu lương (Payslip)"],
        "process": ["Thu thập công và OT", "Tính lương cơ bản", "Cộng phụ cấp/Thưởng", "Trừ Thuế/BHXH", "Ra bảng lương cuối"],
        "checklist": ["Có xử lý lương tháng 13 không?", "Luồng duyệt bảng lương có mấy cấp?"],
        "prompt_rules": ["Luôn tách bạch Lương đóng bảo hiểm và Lương thực nhận."]
    },
    # ---------------- 03-Modeling / UML ----------------
    {
        "path": "03-Modeling/UML",
        "name": "Sequence Diagram",
        "level": "Level 3 - Architecture Skill",
        "purpose": "Vẽ biểu đồ tuần tự để thiết kế logic tương tác giữa các hệ thống.",
        "inputs": ["Use Case", "Danh sách Actor và System"],
        "outputs": ["Sequence Diagram (Mermaid)"],
        "process": ["Định nghĩa Lifelines", "Vẽ thông điệp gọi hàm (Call Message)", "Vẽ thông điệp trả về (Return Message)", "Định nghĩa các khối điều kiện (Alt/Opt/Loop)"],
        "checklist": ["Có xử lý ngoại lệ (Exception/Error) trên diagram không?", "Có Timeout/Retry logic không?"],
        "prompt_rules": ["Sử dụng PlantUML hoặc Mermaid js syntax cho sequence diagram.", "Thể hiện rõ tương tác đồng bộ (sync) và bất đồng bộ (async)."]
    },
    {
        "path": "03-Modeling/UML",
        "name": "Activity Diagram",
        "level": "Level 2 - Business Skill",
        "purpose": "Mô hình hóa luồng hoạt động chi tiết của một chức năng cụ thể.",
        "inputs": ["User Story", "Logic nghiệp vụ"],
        "outputs": ["Activity Diagram (Mermaid)"],
        "process": ["Xác định Initial Node", "Vẽ các Action Nodes", "Vẽ Decision Nodes (Rẽ nhánh)", "Xác định Final Node"],
        "checklist": ["Tất cả các rẽ nhánh đều có lối thoát (End) chưa?", "Có sử dụng Swimlane để chia Actor không?"],
        "prompt_rules": ["Bắt buộc dùng Swimlane nếu luồng nghiệp vụ có từ 2 Actor trở lên."]
    },
    {
        "path": "03-Modeling/State",
        "name": "State Machine Diagram",
        "level": "Level 3 - Architecture Skill",
        "purpose": "Thiết kế vòng đời (Lifecycle) của một đối tượng dữ liệu.",
        "inputs": ["Thực thể dữ liệu (vd: Hóa đơn, Đơn hàng)"],
        "outputs": ["State Diagram (Mermaid)"],
        "process": ["Xác định các trạng thái (States)", "Xác định sự kiện kích hoạt (Triggers/Events)", "Định nghĩa trạng thái Initial và Final", "Vẽ mũi tên chuyển đổi (Transitions)"],
        "checklist": ["Có trạng thái Cancelled/Failed không?", "Có luồng quay lui (Rollback) trạng thái không?"],
        "prompt_rules": ["Tuyệt đối không để đối tượng bị kẹt ở một trạng thái vĩnh viễn (Deadlock)."]
    },
    # ---------------- 04-UIUX ----------------
    {
        "path": "04-UIUX/Form",
        "name": "Thiết kế Form",
        "level": "Level 2 - Business Skill",
        "purpose": "Phân tích và tối ưu hóa các Form nhập liệu.",
        "inputs": ["Danh sách các trường cần nhập"],
        "outputs": ["Bố cục Form (Wireframe)", "Luật Validation"],
        "process": ["Phân nhóm trường dữ liệu (Grouping)", "Sắp xếp theo thứ tự ưu tiên", "Định nghĩa Validation rules (Required, Format, Min/Max)", "Thiết kế thông báo lỗi"],
        "checklist": ["Có hỗ trợ Auto-fill không?", "Có hiển thị rõ trường nào bắt buộc (*) không?"],
        "prompt_rules": ["Đừng dùng quá 2 cột trong Form trừ khi hệ thống đặc thù.", "Tất cả các lỗi nhập liệu phải được báo ngay (Inline Validation)."]
    },
    {
        "path": "04-UIUX/Mobile",
        "name": "Phân tích Mobile App",
        "level": "Level 3 - Architecture Skill",
        "purpose": "Phân tích nghiệp vụ và UI/UX đặc thù cho nền tảng Mobile.",
        "inputs": ["Nghiệp vụ cần mang lên Mobile"],
        "outputs": ["Sơ đồ luồng màn hình Mobile", "Thiết kế Bottom Navigation"],
        "process": ["Xác định chức năng cốt lõi cho Mobile", "Thiết kế luồng thao tác 1 tay", "Xử lý trạng thái Offline/Mất mạng", "Quản lý Push Notification"],
        "checklist": ["Có tính năng quét QR/Barcode không?", "Có lưu Cache offline không?"],
        "prompt_rules": ["Mobile App không phải là bê nguyên Web xuống. Chỉ giữ lại những gì cực kỳ thiết yếu."]
    },
    # ---------------- 05-Database ----------------
    {
        "path": "05-Database/Naming",
        "name": "Database Naming Convention",
        "level": "Level 3 - Architecture Skill",
        "purpose": "Định nghĩa quy chuẩn đặt tên cho Database.",
        "inputs": ["Các thực thể nghiệp vụ"],
        "outputs": ["Quy ước đặt tên Bảng, Cột, Khóa"],
        "process": ["Chuẩn hóa tên Bảng (số ít/số nhiều)", "Quy định tiền tố/hậu tố", "Quy định tên Khóa chính/Khóa ngoại", "Quy định Index naming"],
        "checklist": ["Đã cấm sử dụng Reserved Words chưa?", "Có quy định độ dài tối đa cho tên cột không?"],
        "prompt_rules": ["Khuyến nghị: Tên bảng dùng snake_case, số nhiều. Tên khóa chính luôn là id. Khóa ngoại là {table_name}_id."]
    },
    {
        "path": "05-Database/Relationship",
        "name": "Table Relationship Design",
        "level": "Level 3 - Architecture Skill",
        "purpose": "Thiết kế và tối ưu các mối quan hệ giữa các bảng.",
        "inputs": ["ERD nháp"],
        "outputs": ["Cấu trúc quan hệ chuẩn"],
        "process": ["Xác định loại quan hệ (1-1, 1-N, N-N)", "Thiết kế bảng Junction cho quan hệ N-N", "Kiểm tra toàn vẹn dữ liệu (Referential Integrity)", "Xác định hành vi ON DELETE/ON UPDATE"],
        "checklist": ["Sử dụng CASCADE hay RESTRICT cho ON DELETE?", "Có bị dư thừa vòng lặp (Circular Dependency) không?"],
        "prompt_rules": ["Phải mô tả rõ ràng chiến lược chống xóa nhầm dữ liệu (Soft Delete vs Hard Delete)."]
    },
    # ---------------- 07-Project ----------------
    {
        "path": "07-Project/Agile",
        "name": "Agile Manifesto & Principles",
        "level": "Level 1 - Basic Skill",
        "purpose": "Áp dụng tư duy Agile vào dự án.",
        "inputs": ["Quy trình dự án truyền thống"],
        "outputs": ["Kế hoạch chuyển đổi Agile"],
        "process": ["Đánh giá tính linh hoạt", "Cắt nhỏ giai đoạn phát hành (Iterative)", "Tăng cường giao tiếp với khách hàng", "Phản hồi với thay đổi"],
        "checklist": ["Team có họp mặt trực tiếp thường xuyên không?", "Sản phẩm có thể chạy được (Working software) mỗi cuối sprint không?"],
        "prompt_rules": ["Cá nhân và tương tác quan trọng hơn quy trình và công cụ."]
    },
    {
        "path": "07-Project/Sprint",
        "name": "Sprint Planning",
        "level": "Level 2 - Business Skill",
        "purpose": "Lên kế hoạch thực hiện cho Sprint.",
        "inputs": ["Product Backlog đã Grooming", "Vận tốc (Velocity) của team"],
        "outputs": ["Sprint Goal", "Sprint Backlog"],
        "process": ["PO trình bày độ ưu tiên", "Dev team estimate (Story Points)", "Đưa item vào Sprint", "Chốt Sprint Goal"],
        "checklist": ["Team có đồng thuận với Sprint Goal không?", "Tổng point có vượt quá sức chứa (Capacity) không?"],
        "prompt_rules": ["Không ai được quyền ép Dev team nhận nhiều task hơn mức họ có thể cam kết."]
    },
    {
        "path": "07-Project/Sprint",
        "name": "Sprint Retrospective",
        "level": "Level 2 - Business Skill",
        "purpose": "Cải tiến liên tục quy trình làm việc sau mỗi Sprint.",
        "inputs": ["Kết quả Sprint vừa qua"],
        "outputs": ["Action Items cải tiến"],
        "process": ["Thu thập dữ liệu Sprint", "Mô hình Mad/Sad/Glad hoặc Start/Stop/Continue", "Thảo luận gốc rễ vấn đề", "Đề xuất cải tiến"],
        "checklist": ["Có bầu chọn ra Action Item quan trọng nhất không?", "Có theo dõi Action Item từ Sprint trước không?"],
        "prompt_rules": ["Đây là lúc tìm GIẢI PHÁP, không phải lúc tìm người ĐỔ LỖI."]
    },
    # ---------------- 08-Templates ----------------
    {
        "path": "08-Templates",
        "name": "Tạo Template BRD",
        "level": "Level 1 - Basic Skill",
        "purpose": "Tạo cấu trúc chuẩn cho tài liệu Business Requirement Document.",
        "inputs": ["Tên dự án", "Mục tiêu"],
        "outputs": ["Khung sườn BRD"],
        "process": ["Thiết lập phần Giới thiệu", "Tạo cấu trúc Scope", "Tạo cấu trúc Yêu cầu nghiệp vụ", "Tạo cấu trúc Phụ lục"],
        "checklist": ["Có bảng Revision History (Lịch sử chỉnh sửa) không?", "Có phần ký duyệt (Sign-off) không?"],
        "prompt_rules": ["Sinh ra cấu trúc mục lục rõ ràng dưới định dạng Markdown, dùng Heading 1, 2, 3."]
    },
    {
        "path": "08-Templates",
        "name": "Tạo Template SRS",
        "level": "Level 1 - Basic Skill",
        "purpose": "Tạo cấu trúc chuẩn cho Software Requirements Specification.",
        "inputs": ["Mô tả hệ thống"],
        "outputs": ["Khung sườn SRS"],
        "process": ["Mô tả tổng quan", "Giao diện hệ thống", "Đặc tả Functional", "Đặc tả Non-Functional"],
        "checklist": ["Có mục User Roles & Permissions không?", "Có danh sách thuật ngữ (Glossary) không?"],
        "prompt_rules": ["SRS cần phần mô tả chi tiết cách xử lý lỗi (Error Handling)."]
    },
    {
        "path": "08-Templates",
        "name": "Tạo Template Change Request",
        "level": "Level 1 - Basic Skill",
        "purpose": "Tạo biểu mẫu yêu cầu thay đổi (CR) chuẩn dự án.",
        "inputs": ["Quy trình thay đổi dự án"],
        "outputs": ["Biểu mẫu CR"],
        "process": ["Thông tin yêu cầu", "Lý do thay đổi", "Đánh giá tác động (Impact Analysis)", "Đánh giá Effort & Cost", "Ký duyệt"],
        "checklist": ["Có mức độ khẩn cấp (Priority) không?", "Có mô tả giải pháp thay thế (Workaround) nếu từ chối không?"],
        "prompt_rules": ["CR luôn cần phải đánh giá ảnh hưởng lên Tiến độ (Time) và Chi phí (Cost)."]
    },
    # ---------------- 09-BA-Agent (Thinking & Advanced) ----------------
    {
        "path": "09-BA-Agent/Thinking Skills",
        "name": "Optimization & Refactoring",
        "level": "Level 4 - Thinking Skill",
        "purpose": "Tối ưu hóa quy trình nghiệp vụ đang bị cồng kềnh.",
        "inputs": ["Quy trình hiện tại", "Điểm nghẽn (Bottlenecks)"],
        "outputs": ["Quy trình tinh gọn"],
        "process": ["Đo lường thời gian xử lý", "Tìm ra điểm gây chậm trễ", "Loại bỏ các bước thừa (Non-value added)", "Tự động hóa"],
        "checklist": ["Đã áp dụng nguyên tắc ECRS (Eliminate, Combine, Rearrange, Simplify) chưa?", "Tối ưu xong có ảnh hưởng đến bảo mật/kiểm soát không?"],
        "prompt_rules": ["Bất cứ bước nào yêu cầu 'Nhập lại dữ liệu bằng tay' đều cần xem xét tự động hóa."]
    },
    {
        "path": "09-BA-Agent/Thinking Skills",
        "name": "Risk Analysis",
        "level": "Level 4 - Thinking Skill",
        "purpose": "Phân tích và quản lý rủi ro dự án / hệ thống.",
        "inputs": ["Kiến trúc hệ thống", "Kế hoạch triển khai"],
        "outputs": ["Risk Register (Ma trận rủi ro)", "Kế hoạch ứng phó (Mitigation Plan)"],
        "process": ["Nhận diện rủi ro", "Đánh giá Xác suất (Likelihood) & Mức độ ảnh hưởng (Impact)", "Lập kế hoạch giảm thiểu", "Kế hoạch dự phòng (Contingency)"],
        "checklist": ["Có phương án Rollback nếu deploy thất bại không?", "Có đánh giá rủi ro pháp lý/bảo mật không?"],
        "prompt_rules": ["Rủi ro = Xác suất x Mức độ ảnh hưởng. Hãy liệt kê tối thiểu 5 rủi ro lớn nhất."]
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
