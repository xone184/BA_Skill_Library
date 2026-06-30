# Skill Name
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
