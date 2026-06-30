import os
from skill_generator import generate_skill

def build_optimized_diagram_skills():
    print("Generating Optimized Diagram Skills (Activity Diagram & BPMN)...")
    
    # 1. Activity Diagram (UML)
    generate_skill(
        domain="03-Modeling",
        category="UML",
        skill_name="Activity_Diagram",
        level="Level 2 - Business Skill",
        purpose="Mô hình hóa luồng hoạt động (Workflow) và thao tác nghiệp vụ có phân làn (Swimlanes), triệt tiêu lỗi đứt gãy luồng và chồng chéo giao diện.",
        inputs={
            "Quy trình": "Đoạn mô tả bằng chữ hoặc các gạch đầu dòng về các bước thực hiện."
        },
        process="""### Bước 1: Xác định Actor và Làn (Swimlanes)
- Phân tích rõ những ai tham gia vào quy trình (VD: Người dùng, Hệ thống, Kế toán).
- Thiết lập Swimlanes (Nếu dùng Mermaid: subgraph, Nếu dùng PlantUML: |Actor|).

### Bước 2: Thiết lập Luật Trình bày (Cực kỳ quan trọng)
- **HƯỚNG BẮT BUỘC:** Phải dàn theo chiều ngang (Sử dụng `flowchart LR` cho Mermaid hoặc `left to right direction` cho PlantUML) để khớp với làn ngang.
- **TỐI ƯU LINE:** Hạn chế nhảy qua lại giữa 2 làn liên tục. Phải gom nhóm các hành động liên tiếp của 1 Actor rồi mới chuyển.
- **HỘI TỤ (SINGLE END):** Chỉ có 1 Start Node. Mọi nhánh rẽ (Lỗi, Hủy, Thành công) BẮT BUỘC phải hội tụ về 1 (hoặc tối đa 2) End Node thông qua cổng gom. Nghiêm cấm đặt End Node rải rác.

### Bước 3: Xuất Mã Code (Mermaid / PlantUML)
- Sinh mã chuẩn xác, không được thiếu đóng/mở ngoặc.
- Không dùng ký tự đặc biệt trong ID của node.""",
        business_rules=[
            "Chỉ được có 1 Start Node.",
            "Tất cả các nhánh (branch) phải hội tụ về một End Node cuối cùng hoặc dùng Join Node để nhập luồng, KHÔNG thả nổi luồng hoặc vứt End Node lung tung.",
            "Bắt buộc dùng `flowchart LR` (Mermaid) hoặc `left to right direction` (PlantUML) để render không bị rối.",
            "Luôn phân làn rõ ràng bằng tính năng Swimlanes."
        ],
        edge_cases=[
            "Nếu người dùng đưa quy trình quá phức tạp (> 20 bước), hãy chia thành 2 sơ đồ con để không làm đứng trình duyệt khi render."
        ],
        output_format="""- Phân tích ngắn gọn (Dưới 3 dòng).
- Mã Code (PlantUML hoặc Mermaid.js) bọc trong Markdown Code Block tương ứng (```mermaid hoặc ```plantuml)."""
    )
    
    # 2. Draw BPMN
    generate_skill(
        domain="03-Modeling",
        category="BPMN",
        skill_name="Draw_BPMN",
        level="Level 2 - Business Skill",
        purpose="Vẽ sơ đồ BPMN chuẩn xác, không đứt đoạn luồng, hỗ trợ PlantUML/Mermaid với kiến trúc luồng hội tụ.",
        inputs={
            "Mô tả quy trình": "Business process flow bằng text."
        },
        process="""### Bước 1: Khai báo Pool và Lanes
- Xác định Pool (Tên quy trình) và Lanes (Các Actor).

### Bước 2: Thiết lập Layout và Gateways
- **LAYOUT:** Bắt buộc áp dụng `flowchart LR` hoặc `left to right direction` để sơ đồ dễ nhìn từ trái qua phải, không bị ép dọc.
- **GATEWAYS:** Phân biệt rõ Exclusive Gateway (XOR - Chỉ chọn 1) và Parallel Gateway (AND - Song song).
- **HỘI TỤ:** Mọi Gateway khi tẽ nhánh ra thì BẮT BUỘC phải có một Gateway tương ứng để gom nhánh (Merge) lại trước khi tiến đến End Event.

### Bước 3: Xuất Sơ đồ
- Ưu tiên dùng Mermaid hoặc PlantUML.
- Đối với Mermaid BPMN, dùng cú pháp đúng chuẩn hoặc dùng Flowchart giả lập BPMN tùy theo yêu cầu của hệ thống (Khuyến nghị Flowchart LR với các node hình thoi cho dễ render).""",
        business_rules=[
            "Cấm ngặt việc để một luồng (Sequence Flow) bị đứt đoạn không có điểm đến.",
            "Luôn có 1 Start Event duy nhất, và hạn chế tối đa số lượng End Events (Nên quy tụ về 1 End Event thành công và 1 End Event thất bại/hủy).",
            "Mọi nhánh mở (Split) phải có nhánh đóng (Join).",
            "Bắt buộc dàn trang theo chiều ngang (Left-to-Right)."
        ],
        edge_cases=[
            "Nếu là quy trình duyệt nhiều cấp phức tạp, hãy làm rõ các nhánh từ chối (Reject) vòng ngược lại (Loop back) bằng đường mũi tên rõ ràng, tránh bắt chéo qua các ô khác."
        ],
        output_format="""- Mã Code (Mermaid/PlantUML) để người dùng copy paste."""
    )
    
    print("✅ Optimized Diagram Skills generated successfully!")

if __name__ == "__main__":
    build_optimized_diagram_skills()
