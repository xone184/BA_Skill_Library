import sys
sys.path.insert(0, r"e:\BA Skill Library")
from skill_generator import run

skills = [
    # ================================================================
    # Agile / Scrum: Agile Manifesto
    # ================================================================
    {
        "path": "07-Project/Agile",
        "name": "Agile Manifesto & Principles",
        "level": "Level 1 - Basic Skill",
        "domain": "Project",
        "tags": ["Agile", "Scrum", "Mindset", "Principles", "Transformation"],
        "purpose": "Áp dụng tư duy Agile (4 giá trị cốt lõi và 12 nguyên tắc) vào quản lý dự án phần mềm. Giúp đội ngũ (Team) chuyển đổi từ mô hình Thác nước (Waterfall) truyền thống sang mô hình linh hoạt (Agile), nhấn mạnh vào việc chuyển giao giá trị sớm và phản hồi nhanh với thay đổi.",
        "when_to_use": "Sử dụng khi khởi tạo dự án mới, khi team đang gặp vấn đề về mindset, hoặc khi khách hàng muốn thay đổi requirement liên tục nhưng quy trình cũ không đáp ứng được.",
        "prerequisites": ["Hiểu cơ bản về vòng đời phát triển phần mềm (SDLC)"],
        "inputs_detail": [
            {"name": "Quy trình dự án hiện tại", "description": "Cách team đang vận hành.", "required": True, "example": "Dự án đang dùng Waterfall, tài liệu quá nhiều, release sau 6 tháng."},
            {"name": "Vấn đề (Pain points)", "description": "Khó khăn team đang gặp phải.", "required": True, "example": "Khách hàng đổi ý, code xong phải đập đi làm lại."}
        ],
        "process_detail": [
            {"step": 1, "title": "Áp dụng 4 Giá trị Cốt lõi", "description": "Thay đổi trọng tâm dự án.", "sub_steps": [
                "Cá nhân và tương tác HƠN quy trình và công cụ.",
                "Phần mềm chạy tốt HƠN tài liệu đầy đủ.",
                "Cộng tác với khách hàng HƠN đàm phán hợp đồng.",
                "Phản hồi với thay đổi HƠN bám sát kế hoạch."
            ]},
            {"step": 2, "title": "Đánh giá 12 Nguyên tắc", "description": "Mapping nguyên tắc vào thực tế.", "sub_steps": [
                "Ưu tiên cao nhất là làm hài lòng khách hàng thông qua chuyển giao sớm.",
                "Sẵn sàng chào đón các thay đổi yêu cầu, dù là muộn.",
                "Business team và Dev team phải làm việc cùng nhau hằng ngày."
            ]},
            {"step": 3, "title": "Phân tích Khoảng cách (Agile Gap Analysis)", "description": "So sánh hiện tại và tương lai.", "sub_steps": [
                "Ví dụ: Hiện tại giao tiếp qua email -> Tương lai: Daily Standup meeting.",
                "Hiện tại release 6 tháng -> Tương lai: Sprint 2 tuần."
            ]},
            {"step": 4, "title": "Thiết lập Kế hoạch Chuyển đổi", "description": "Đưa ra Action items.", "sub_steps": [
                "Setup các Scrum Events (Planning, Daily, Review, Retro).",
                "Định nghĩa Definition of Done (DoD)."
            ]}
        ],
        "outputs_detail": [
            {"name": "Báo cáo chuyển đổi Agile (Agile Transformation Plan)", "format": "Markdown", "template": "## 1. Đánh giá hiện trạng\n- Vấn đề: Release chậm, khách hàng phàn nàn.\n\n## 2. Áp dụng Agile Principles\n- **Principle áp dụng:** Chuyển giao phần mềm thường xuyên.\n- **Hành động:** Chuyển từ chu kỳ 6 tháng sang Sprint 2 tuần.\n\n## 3. Action Items\n- [ ] Tổ chức buổi Kick-off Agile.\n- [ ] Lên lịch Daily Standup lúc 9:00 AM.\n- [ ] Thay đổi cách viết Requirement từ tài liệu 100 trang sang User Stories."}
        ],
        "sub_skills": ["Mindset Transformation", "Agile Gap Analysis"],
        "business_rules": [
            "BR-AGILE-01: Agile không có nghĩa là KHÔNG CÓ tài liệu, mà là tài liệu VỪA ĐỦ.",
            "BR-AGILE-02: Không được từ chối thay đổi requirement nếu nó mang lại lợi thế cạnh tranh cho khách."
        ],
        "edge_cases": [
            "Khách hàng đòi fix giá và fix scope từ đầu (Hợp đồng Fixed-price) -> Agile rất khó áp dụng thuần túy, cần dùng lai (Hybrid)."
        ],
        "checklist": [
            "Team đã hiểu 4 giá trị cốt lõi chưa?",
            "Có cơ chế giao tiếp hằng ngày chưa?",
            "Khách hàng có tham gia review thường xuyên không?"
        ],
        "example": "Xem Báo cáo chuyển đổi Agile trong Outputs.",
        "related_skills": ["Sprint Planning", "Backlog Grooming"],
        "quality_criteria": ["Rõ ràng Action Items", "Đúng tinh thần 12 Principles"],
        "estimated_effort": "1-3 ngày",
        "prompt_role": "Senior Agile Coach / Scrum Master.",
        "prompt_task": "Đánh giá quy trình hiện tại và đề xuất kế hoạch chuyển đổi sang Agile dựa trên 4 giá trị và 12 nguyên tắc.",
        "prompt_context": "Team đang gặp vấn đề với mô hình truyền thống và cần thay đổi mindset và quy trình sang Agile.",
        "prompt_rules": [
            "PHẢI sử dụng ngôn ngữ tư vấn (Coaching).",
            "Mỗi đề xuất PHẢI mapping với ít nhất 1 trong 12 Nguyên tắc Agile.",
            "Đề xuất PHẢI khả thi (Actionable) thay vì lý thuyết suông."
        ],
        "prompt_example": ""
    },

    # ================================================================
    # Agile / Scrum: Backlog Grooming (Refinement)
    # ================================================================
    {
        "path": "07-Project/Scrum",
        "name": "Backlog Grooming",
        "level": "Level 2 - Business Skill",
        "domain": "Project",
        "tags": ["Scrum", "Backlog", "Grooming", "Refinement", "User Story", "Estimation"],
        "purpose": "Hỗ trợ Product Owner (PO) và Team 'làm sạch' Product Backlog (Backlog Refinement). Bao gồm việc sắp xếp ưu tiên, làm rõ yêu cầu, thêm Acceptance Criteria, và chia nhỏ các User Stories quá lớn (Epics) để chuẩn bị sẵn sàng cho Sprint Planning.",
        "when_to_use": "Thường xuyên vào giữa Sprint (trước Planning) để đảm bảo Backlog luôn đủ việc cho 1-2 Sprints tiếp theo.",
        "prerequisites": ["Đã có Product Backlog sơ bộ"],
        "inputs_detail": [
            {"name": "Danh sách User Stories (Nháp)", "description": "Các yêu cầu chưa rõ ràng.", "required": True, "example": "User Story: 'Làm tính năng giỏ hàng' (chưa có chi tiết)."},
            {"name": "Mục tiêu Product (Product Goal)", "description": "Định hướng phát triển sản phẩm.", "required": False, "example": "Tăng tỷ lệ chuyển đổi mua hàng lên 10%."}
        ],
        "process_detail": [
            {"step": 1, "title": "Review và Xóa bỏ (Purge)", "description": "Loại bỏ những thứ không cần thiết.", "sub_steps": [
                "Xóa các User Stories đã quá cũ (ví dụ > 6 tháng không làm).",
                "Xóa các ý tưởng không còn phù hợp với Product Goal."
            ]},
            {"step": 2, "title": "Làm rõ yêu cầu (Detailing)", "description": "Bổ sung thông tin.", "sub_steps": [
                "Thêm Description rõ ràng (Ai, Làm gì, Để làm gì).",
                "Viết Acceptance Criteria (AC) theo chuẩn Given-When-Then.",
                "Đính kèm Mockup/UI nếu có."
            ]},
            {"step": 3, "title": "Chia nhỏ Story (Story Splitting)", "description": "Tách Epic thành Story nhỏ.", "sub_steps": [
                "Nếu Story quá lớn (VD: 'Thanh toán trực tuyến') -> Tách thành: 'Thanh toán VNPay', 'Thanh toán Momo'.",
                "Đảm bảo mỗi Story mới vẫn mang lại giá trị độc lập (INVEST)."
            ]},
            {"step": 4, "title": "Sắp xếp thứ tự ưu tiên (Prioritization)", "description": "Kéo lên trên/xuống dưới.", "sub_steps": [
                "Sử dụng MoSCoW (Must, Should, Could, Won't) hoặc Giá trị mang lại vs Nỗ lực (Value vs Effort)."
            ]},
            {"step": 5, "title": "Đánh giá Ready (Definition of Ready)", "description": "Chốt Story.", "sub_steps": [
                "Đảm bảo các Story nằm ở top Backlog thỏa mãn DoR (Có AC, Có Mockup, Đã được team review)."
            ]}
        ],
        "outputs_detail": [
            {"name": "Groomed Product Backlog", "format": "Markdown Table", "template": "### Product Backlog (Sau Grooming)\n\n| ID | User Story | Priority | Trạng thái (DoR) | Ghi chú (Action) |\n|---|---|---|---|---|\n| US-101 | As Khách, I want thanh toán VNPay... | High (Must) | Ready | Đã bổ sung 5 AC. |\n| US-102 | As Khách, I want thanh toán Momo... | Medium (Should)| Not Ready | Chờ UI Mockup. |\n| US-103 | (EPIC) Quản lý hồ sơ | Low | Splitted | Đã chia thành US-104, US-105. |"}
        ],
        "sub_skills": ["Story Splitting", "MoSCoW Prioritization", "DoR Assessment"],
        "business_rules": [
            "BR-GROOM-01: Chỉ những Story nằm ở trên cùng của Backlog mới cần phân tích chi tiết (DoR).",
            "BR-GROOM-02: Epic không bao giờ được đưa vào Sprint, phải chia nhỏ thành Story."
        ],
        "edge_cases": [
            "Story quá thiên về kỹ thuật (Technical Debt/Refactor) -> Đổi thành Technical Enabler, vẫn đưa vào backlog và gán điểm."
        ],
        "checklist": [
            "Đã chia nhỏ các Story quá lớn (Epic)?",
            "Top Backlog đã có đủ Acceptance Criteria?",
            "Thứ tự ưu tiên đã rõ ràng chưa?",
            "Đã xóa các item rác?"
        ],
        "example": "Xem Groomed Product Backlog trong Outputs.",
        "related_skills": ["Write User Story", "Sprint Planning"],
        "quality_criteria": ["Top items đạt chuẩn DoR", "Không có Epic ở top"],
        "estimated_effort": "2-4 giờ (Meeting)",
        "prompt_role": "Senior Product Owner / Scrum Master.",
        "prompt_task": "Thực hiện Grooming (Làm mịn) danh sách Backlog: Chia nhỏ, làm rõ yêu cầu và sắp xếp ưu tiên.",
        "prompt_context": "Backlog đang lộn xộn, chứa nhiều Epic lớn và các Story thiếu Acceptance Criteria.",
        "prompt_rules": [
            "NẾU gặp Epic (Story lớn): BẮT BUỘC phải đề xuất cách chia nhỏ (Splitting) thành 2-3 Story con.",
            "Các Story ở độ ưu tiên cao (Must) PHẢI được yêu cầu bổ sung Acceptance Criteria chi tiết.",
            "Output PHẢI trình bày dưới dạng Bảng (Table) rõ ràng trạng thái Trước và Sau khi Grooming."
        ],
        "prompt_example": ""
    },

    # ================================================================
    # Agile / Scrum: Sprint Review
    # ================================================================
    {
        "path": "07-Project/Scrum",
        "name": "Sprint Review",
        "level": "Level 2 - Business Skill",
        "domain": "Project",
        "tags": ["Scrum", "Sprint", "Review", "Demo", "Feedback", "Stakeholders"],
        "purpose": "Hỗ trợ chuẩn bị và tổ chức buổi Sprint Review (Demo). Mục tiêu là trình diễn (Demo) sản phẩm hoàn thiện (Increment) cho Khách hàng (Stakeholders), thu thập phản hồi, và cập nhật Product Backlog dựa trên tình hình thực tế.",
        "when_to_use": "Sử dụng vào ngày cuối cùng của Sprint, trước buổi Sprint Retrospective.",
        "prerequisites": ["Sprint đã kết thúc", "Các tính năng Demo phải đạt Definition of Done (DoD)"],
        "inputs_detail": [
            {"name": "Sprint Goal & Sprint Backlog", "description": "Mục tiêu và các task đã làm.", "required": True, "example": "Mục tiêu: Ra mắt module Login. Hoàn thành 4/5 User Stories."},
            {"name": "Sản phẩm thực tế (Increment)", "description": "Phần mềm chạy được.", "required": False, "example": "URL staging để demo."}
        ],
        "process_detail": [
            {"step": 1, "title": "Đánh giá Sprint Goal", "description": "So sánh kế hoạch và thực tế.", "sub_steps": [
                "Tuyên bố rõ: Những item nào đã 'Done' (Đạt DoD).",
                "Những item nào KHÔNG 'Done' (Không được mang ra Demo, đẩy về Product Backlog)."
            ]},
            {"step": 2, "title": "Trình diễn Sản phẩm (Demo)", "description": "Cho khách hàng xem thành quả.", "sub_steps": [
                "Không dùng slide PowerPoint, phải demo trực tiếp trên phần mềm (Working Software).",
                "Chạy theo luồng nghiệp vụ (End-to-End) thay vì bấm từng nút rời rạc."
            ]},
            {"step": 3, "title": "Thu thập Phản hồi (Feedback Collection)", "description": "Lắng nghe Stakeholders.", "sub_steps": [
                "Ghi nhận ý kiến khen/chê.",
                "Ghi nhận các yêu cầu thay đổi (Change Requests) hoặc ý tưởng mới."
            ]},
            {"step": 4, "title": "Cập nhật Product Backlog", "description": "Đưa feedback vào Backlog.", "sub_steps": [
                "Phản hồi của khách sẽ biến thành User Story mới.",
                "PO thảo luận với Stakeholders về định hướng cho Sprint tiếp theo."
            ]}
        ],
        "outputs_detail": [
            {"name": "Sprint Review Report", "format": "Markdown Document", "template": "## 1. Kết quả Sprint\n- **Sprint Goal:** [Đạt / Không đạt]\n- **Done Items:** US-01, US-02.\n- **Not Done Items:** US-03 (Thiếu test).\n\n## 2. Stakeholder Feedback\n- Giao diện đăng nhập đẹp, nhưng khách muốn thêm nút 'Đăng nhập bằng Google'.\n\n## 3. Product Backlog Update\n- **Tạo mới:** US-04 (Login by Google) - Priority: High.\n- **Đẩy lại:** Đưa US-03 về đầu Backlog cho Sprint sau."}
        ],
        "sub_skills": ["Demo Facilitation", "Feedback Structuring"],
        "business_rules": [
            "BR-REVIEW-01: Tuyệt đối KHÔNG demo những tính năng chưa hoàn thành (Chưa đạt DoD).",
            "BR-REVIEW-02: Sprint Review KHÔNG PHẢI là buổi báo cáo tiến độ (Status report), mà là buổi lấy ý kiến về SẢN PHẨM."
        ],
        "edge_cases": [
            "Khách hàng đòi thêm tính năng 'ngay lập tức' -> PO phải ghi nhận vào Backlog, không cam kết làm ngay trong lúc họp."
        ],
        "checklist": [
            "Chỉ demo phần mềm chạy được (Không dùng slide)?",
            "Đã tuyên bố rõ item nào Done / Not Done?",
            "Đã ghi nhận Feedback thành các Backlog item mới?"
        ],
        "example": "Xem Sprint Review Report trong Outputs.",
        "related_skills": ["Sprint Retrospective", "Sprint Planning"],
        "quality_criteria": ["Tách biệt Done/Not Done", "Biến Feedback thành Action/Story"],
        "estimated_effort": "2-4 giờ",
        "prompt_role": "Scrum Master / Product Owner.",
        "prompt_task": "Tổ chức kịch bản và báo cáo kết quả buổi Sprint Review. Tổng hợp phản hồi thành Backlog items.",
        "prompt_context": "Cần một báo cáo chuyên nghiệp sau buổi Demo để gửi cho toàn bộ Stakeholders và cập nhật Backlog.",
        "prompt_rules": [
            "Báo cáo PHẢI phân tách rõ ràng danh sách Done và Not Done.",
            "PHẢI biến các phản hồi (Feedback) của Stakeholders thành các Action Items hoặc User Stories mới.",
            "KHÔNG dùng ngôn từ đổ lỗi nếu Sprint không đạt Goal."
        ],
        "prompt_example": ""
    }
]

if __name__ == "__main__":
    print("=== Expanding: Agile / Project Skills (Manifesto, Grooming, Review) ===")
    run(skills)
