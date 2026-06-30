# Thiết kế API Contract

## Level
Level 3 - Architecture Skill

## Purpose
Thiết kế đặc tả giao tiếp giữa Front-end và Back-end (hoặc giữa 2 hệ thống) qua RESTful API. Cung cấp rõ ràng Endpoints, Method, Request Payload (Body/Params), Response Payload và Error Codes để 2 bên có thể làm việc độc lập.

## When to Use
Sử dụng trong giai đoạn System Design, trước khi Dev bắt đầu code.

## Prerequisites
- Đã có ERD và UI Mockups
- Hiểu RESTful API principles

## Inputs
### Nghiệp vụ chức năng
- **Mô tả:** Chức năng API cần phục vụ.
- **Bắt buộc:** Có
- **Ví dụ:** Chức năng: Lấy danh sách sản phẩm (có phân trang, filter) và Tạo mới sản phẩm.

## Process
### Bước 1: Xác định Endpoints & Methods
Thiết kế URL chuẩn REST.

- Dùng danh từ số nhiều: `/api/v1/products`
- GET: Lấy dữ liệu (List, Detail)
- POST: Tạo mới
- PUT: Cập nhật toàn bộ
- PATCH: Cập nhật 1 phần (VD: update status)
- DELETE: Xóa

### Bước 2: Thiết kế Request (Input)
Dữ liệu Front-end gửi lên.

- Headers: `Authorization: Bearer <token>`, `Content-Type: application/json`
- Path Variables: VD `/products/{id}`
- Query Params (dùng cho GET): `?page=1&limit=20&status=active`
- Body (JSON - dùng cho POST/PUT/PATCH): Xác định các trường, kiểu dữ liệu, required?

### Bước 3: Thiết kế Response (Output) - Happy Path
Dữ liệu trả về khi thành công.

- Status Code: 200 OK (GET, PUT), 201 Created (POST)
- Body Data: Cấu trúc JSON trả về.
- Nên bọc data trong response chuẩn: `{ 'success': true, 'data': {...}, 'message': '' }`
- Có Pagination meta data nếu là API List

### Bước 4: Thiết kế Error Codes - Negative Path
Các trường hợp lỗi.

- 400 Bad Request: Lỗi validation (thiếu trường, sai format)
- 401 Unauthorized: Chưa đăng nhập, token hết hạn
- 403 Forbidden: Đã đăng nhập nhưng không có quyền
- 404 Not Found: Không tìm thấy entity
- 500 Internal Server Error: Lỗi hệ thống

## Outputs
### API Document (Swagger/OpenAPI style)
- **Định dạng:** Markdown
- **Mẫu:**

```
## 1. Lấy danh sách sản phẩm
- **Endpoint:** `GET /api/v1/products`
- **Description:** Trả về danh sách sản phẩm có phân trang.

### Request
- **Query Params:**
  - `page` (int, default=1)
  - `limit` (int, default=20)
  - `search` (string, optional)

### Response (200 OK)
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "code": "PRD-001",
      "name": "Sản phẩm A",
      "price": 10000
    }
  ],
  "meta": {
    "total": 150,
    "page": 1,
    "last_page": 8
  }
}
```

## 2. Tạo sản phẩm mới
- **Endpoint:** `POST /api/v1/products`
### Request Body (JSON)
```json
{
  "code": "PRD-002", // Required, Unique
  "name": "Sản phẩm B", // Required
  "price": 20000 // Required, > 0
}
```
### Response (201 Created)
...
### Errors
- `400 Bad Request`: {"success": false, "message": "Mã sản phẩm đã tồn tại"}
```

## Sub-Skills (Kỹ năng con)
- RESTful Design
- JSON Modeling
- Error Code Mapping

## Business Rules
- BR-API-01: Endpoints phải dùng danh từ số nhiều (VD: /users, /orders).
- BR-API-02: Không dùng verb trong URL (VD SAI: /get-users. ĐÚNG: GET /users).
- BR-API-03: Mọi Response phải có cấu trúc chuẩn thống nhất (success, data, message, error).
- BR-API-04: API List bắt buộc phải có Pagination.

## Edge Cases & Exceptions
- Payload quá lớn → Thiết kế Bulk Insert API hoặc Async Processing
- Rate Limiting → Cần trả về 429 Too Many Requests nếu spam API

## Checklist
- [ ] Method HTTP có chuẩn REST chưa?
- [ ] URL có đúng nguyên tắc số nhiều không?
- [ ] Request Body đã định nghĩa field/type/required chưa?
- [ ] Response Body (Thành công) có cấu trúc chưa?
- [ ] Đã mô tả mã lỗi 400, 401, 403, 404, 500 chưa?
- [ ] Có xử lý phân trang cho API danh sách không?

## Example
Xem API Document template trong Outputs.

## Related Skills
- Thiết kế ERD
- Thiết kế module
- Phân tích màn hình CRUD
