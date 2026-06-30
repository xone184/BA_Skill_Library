# Skill Name
Table Relationship Design

## Level
Level 3 - Architecture Skill

## Purpose
Thiết kế và tối ưu các mối quan hệ giữa các bảng.

## Inputs
- ERD nháp

## Process
1. Xác định loại quan hệ (1-1, 1-N, N-N)
2. Thiết kế bảng Junction cho quan hệ N-N
3. Kiểm tra toàn vẹn dữ liệu (Referential Integrity)
4. Xác định hành vi ON DELETE/ON UPDATE

## Outputs
- Cấu trúc quan hệ chuẩn

## Checklist
- [ ] Sử dụng CASCADE hay RESTRICT cho ON DELETE?
- [ ] Có bị dư thừa vòng lặp (Circular Dependency) không?
