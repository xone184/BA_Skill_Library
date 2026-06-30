import os

base_dir = r"e:\BA Skill Library\BA-Skills"

structure = {
    "01-Business-Domain": ["CRM", "WMS", "MES", "ERP", "HRM"],
    "02-Requirement": ["Elicitation", "Functional", "Non Functional", "BRD", "SRS", "User Story", "Use Case", "Requirement List"],
    "03-Modeling": ["BPMN", "UML", "Activity", "Sequence", "State", "ERD", "Architecture"],
    "04-UIUX": ["Dashboard", "CRUD", "Form", "Mobile"],
    "05-Database": ["Data Dictionary", "Naming", "Relationship"],
    "06-Testing": ["Test Case", "UAT", "Acceptance"],
    "07-Project": ["Agile", "Scrum", "Sprint"],
    "08-Templates": ["BRD", "FRD", "SRS", "Requirement List", "Change Request"],
    "09-BA-Agent": ["Prompts", "Workflows", "Knowledge"]
}

for parent, children in structure.items():
    parent_path = os.path.join(base_dir, parent)
    os.makedirs(parent_path, exist_ok=True)
    for child in children:
        child_path = os.path.join(parent_path, child)
        os.makedirs(child_path, exist_ok=True)

# 1. Requirement Analysis
req_analysis = """# Skill Name
Requirement Analysis

## Purpose
Thu thập và phân tích requirement đầy đủ.

## When to use
Sử dụng khi bắt đầu giai đoạn phân tích yêu cầu với khách hàng để làm rõ phạm vi và các nghiệp vụ cần thiết.

## Input
- Khách hàng
- Module
- Mục tiêu

## Process
1. Chuẩn bị tài liệu và câu hỏi phỏng vấn
2. Phỏng vấn lấy yêu cầu từ khách hàng/stakeholders
3. Phân tích, phân loại yêu cầu và xác định Actor, Action
4. Hệ thống hóa yêu cầu

## Output
- Requirement List
- User Story
- Acceptance Criteria

## Example
Khách hàng muốn làm chức năng quản lý kho. Output sẽ là danh sách các tính năng như Nhập kho, Xuất kho, Tồn kho... kèm User Story chi tiết.
"""
with open(os.path.join(base_dir, "02-Requirement", "Requirement Analysis.md"), "w", encoding="utf-8") as f:
    f.write(req_analysis)

# 2. Create Requirement List
create_req_list = """# Skill Name
Create Requirement List

## Purpose
Sinh Requirement List.

## When to use
Sử dụng sau khi đã hiểu rõ Business Flow và cần phân rã thành các requirement chi tiết cho đội dev.

## Input
- Module
- Business Flow

## Process
1. Đọc nghiệp vụ
2. Tìm Actor
3. Tìm Action
4. Sinh Requirement

## Output
- Requirement List

## Example
- Actor: Nhân viên kho
- Action: Tạo phiếu nhập kho
- Requirement: Hệ thống cho phép nhân viên kho tạo phiếu nhập kho bằng cách quét mã vạch sản phẩm.
"""
with open(os.path.join(base_dir, "02-Requirement", "Requirement List", "Create Requirement List.md"), "w", encoding="utf-8") as f:
    f.write(create_req_list)

# 3. Thiết kế module
module_design = """# Skill Name
Thiết kế module

## Purpose
Thiết kế module doanh nghiệp.

## When to use
Sử dụng ở giai đoạn thiết kế kiến trúc tổng thể (Architecture Skill) để xác định rõ cấu trúc hệ thống.

## Input
- Business
- Requirement

## Process
1. Phân tích Requirement
2. Gom nhóm tính năng thành các module độc lập
3. Xác định quy trình và luồng dữ liệu (Workflow, Database, API)
4. Xác định phân quyền và giao diện

## Output
- Module List
- Menu
- Permission
- Workflow
- Database
- API
- Screen

## Checklist
- [ ] Có Dashboard chưa
- [ ] Có CRUD chưa
- [ ] Có Import
- [ ] Có Export
- [ ] Có Approval
- [ ] Có Log
- [ ] Có Notification
- [ ] Có Search
- [ ] Có Filter
- [ ] Có Pagination
- [ ] Có Permission
- [ ] Có Report
- [ ] Có Audit
"""
with open(os.path.join(base_dir, "03-Modeling", "Architecture", "Thiết kế module.md"), "w", encoding="utf-8") as f:
    f.write(module_design)

# 4. Review Requirement
review_req = """# Skill Name
Review Requirement

## Purpose
Kiểm tra Requirement, đảm bảo tính đầy đủ và chính xác.

## When to use
Sử dụng ở bước cuối của quá trình lấy yêu cầu (Review Skill), trước khi chốt scope với khách hàng hoặc bàn giao cho team dev.

## Input
- Requirement List / SRS / BRD

## Process
1. Đọc từng requirement
2. Đối chiếu với checklist các yếu tố thường thiếu
3. Đặt câu hỏi cho khách hàng nếu có điểm chưa rõ
4. Đưa ra gợi ý cải thiện

## Output
- Requirement (đã review)
- Question
- Suggestion

## Checklist
- [ ] Missing Business Rule?
- [ ] Missing Exception?
- [ ] Missing Validation?
- [ ] Missing Permission?
- [ ] Missing UI?
- [ ] Missing API?
- [ ] Missing Database?
- [ ] Missing Workflow?
- [ ] Missing Report?
- [ ] Missing Notification?

## Prompt Example
Role: Senior Business Analyst
Task: Review Requirement
Rules:
- Không được bỏ sót requirement.
- Luôn tìm requirement còn thiếu.
- Đưa ra câu hỏi cần hỏi khách hàng.
"""
with open(os.path.join(base_dir, "02-Requirement", "Review Requirement.md"), "w", encoding="utf-8") as f:
    f.write(review_req)

# Knowledge Base
crm_knowledge = """# CRM Knowledge
Khách hàng
Lead
Opportunity
Quotation
Contract
Invoice
Payment
"""
with open(os.path.join(base_dir, "09-BA-Agent", "Knowledge", "CRM_Knowledge.md"), "w", encoding="utf-8") as f:
    f.write(crm_knowledge)

wms_knowledge = """# WMS Knowledge
Warehouse
Location
Bin
Inbound
Outbound
Picking
Packing
Transfer
Cycle Count
"""
with open(os.path.join(base_dir, "09-BA-Agent", "Knowledge", "WMS_Knowledge.md"), "w", encoding="utf-8") as f:
    f.write(wms_knowledge)

mes_knowledge = """# MES Knowledge
Work Order
Production Plan
Machine
Operator
Material
QC
OEE
"""
with open(os.path.join(base_dir, "09-BA-Agent", "Knowledge", "MES_Knowledge.md"), "w", encoding="utf-8") as f:
    f.write(mes_knowledge)

print("Created BA Skill Library structure successfully!")
