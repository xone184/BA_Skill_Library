import os
import json
import re
import shutil
import unicodedata

def slugify(value):
    """
    Chuyển đổi chuỗi tiếng Việt có dấu thành không dấu, thay thế khoảng trắng và ký tự đặc biệt bằng dấu gạch ngang.
    """
    value = str(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = value.lower()
    value = re.sub(r'[^\w\s-]', '', value).strip()
    value = re.sub(r'[-\s]+', '-', value)
    return value

def export_skills(src_dir, dest_dir, zip_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.makedirs(dest_dir)
    
    if os.path.exists(zip_dir):
        shutil.rmtree(zip_dir)
    os.makedirs(zip_dir)

    skill_count = 0

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.json'):
                base_name = file.replace('.json', '')
                json_path = os.path.join(root, file)
                md_path = os.path.join(root, base_name + '.md')
                prompt_path = os.path.join(root, base_name + '.prompt')

                if not os.path.exists(prompt_path):
                    continue

                # Read Metadata
                with open(json_path, 'r', encoding='utf-8') as f:
                    try:
                        metadata = json.load(f)
                    except Exception as e:
                        print(f"Error loading {json_path}: {e}")
                        continue

                name = metadata.get('name', 'Unknown Skill')
                description = metadata.get('description', metadata.get('purpose', 'BA Skill for Claude'))
                description = description.replace('\n', ' ').strip()

                # Read Prompt Content
                with open(prompt_path, 'r', encoding='utf-8') as f:
                    prompt_content = f.read()

                # Determine target directory name (slugified)
                folder_name = slugify(name)
                skill_dir = os.path.join(dest_dir, folder_name)
                os.makedirs(skill_dir, exist_ok=True)

                # Create SKILL.md
                enterprise_rules = """
## Enterprise Documentation Standards (BẮT BUỘC TUÂN THỦ)

Bạn PHẢI tuân thủ Bộ quy tắc chuẩn hóa Tài liệu & Diagram Nghiệp vụ (Version 1.0) sau đây trong mọi output:

### 1. General & Quality Gates
- **CLEAR, COMPLETE, CONSISTENT, TESTABLE, TRACEABLE**.
- ID Convention: Functional Requirement (FR-[MODULE]-[No]), Use Case (UC-[MODULE]-[No]), User Story (US-[MODULE]-[No]), Business Rule (BR-[MODULE]-[No]).
- Luôn đánh dấu [ASSUMPTION] và [OPEN QUESTION] cho những điều chưa rõ.

### 2. Diagram Rules
- **Activity Diagram**: BẮT BUỘC dùng Swimlane (User | System). Luồng Top-down. Trắng đen (Monochrome), không dùng màu sắc (không gradient, nền trắng, chữ viền đen). Max 10-20 activities. Tên activity: Động từ + Tân ngữ. Không giao cắt đường truyền.
- **BPMN**: Pool = Hệ thống/Tổ chức, Lane = Vai trò. User Task (Nền xanh #6094DB, chữ trắng), System Task (Nền trắng, viền màu), Gateway (Không nền, viền đậm). Message Flow chỉ dùng giữa các Pool.
- **Sequence Diagram**: Dùng combined fragments (alt/opt/loop). Message phải có nhãn (functionName).
- **ERD/Data Model**: Bảng số nhiều (snake_case hoặc UPPER_CASE). Khóa chính `[bảng_số_ít]_id`. Luôn ghi rõ cardinality (Crow's foot). Tối thiểu 3NF.
- **Wireframe**: Grayscale (đen/trắng/xám). Phải có Screen ID. Luôn thể hiện 5 trạng thái (Default, Empty, Loading, Error, Success).

### 3. Requirement & User Story
- User Story chuẩn: "Là [vai trò], tôi muốn [mục tiêu] để [lợi ích]". Sử dụng MoSCoW.
- Acceptance Criteria (AC) BẮT BUỘC viết dưới dạng Gherkin (Given-When-Then). Phải bao gồm Happy Path và Exception Flow.

### 4. Domain-Specific Priorities (MES & CRM)
- **MES (Manufacturing Execution System)**: 
  - Ưu tiên dùng BPMN cho quy trình xuyên phòng ban. Activity Diagram chỉ dùng cho thao tác tại một trạm. 
  - Data Model PHẢI đặc tả tần suất ghi nhận (real-time/batch) và Đơn vị đo lường.
- **CRM System**: 
  - Wireframe là BẮT BUỘC cho màn hình quản lý khách hàng/đơn hàng/báo giá. 
  - BẮT BUỘC tách riêng Business Rule về bảo mật API và phân quyền dữ liệu.
"""

                skill_md_content = f"""---
name: {name}
description: {description}
---

{prompt_content}

{enterprise_rules}
"""
                with open(os.path.join(skill_dir, "SKILL.md"), 'w', encoding='utf-8') as f:
                    f.write(skill_md_content)
                
                # Create references/documentation.md
                if os.path.exists(md_path):
                    ref_dir = os.path.join(skill_dir, "references")
                    os.makedirs(ref_dir, exist_ok=True)
                    shutil.copy2(md_path, os.path.join(ref_dir, "documentation.md"))
                
                # Create resources/metadata.json
                res_dir = os.path.join(skill_dir, "resources")
                os.makedirs(res_dir, exist_ok=True)
                shutil.copy2(json_path, os.path.join(res_dir, "metadata.json"))

                # Create examples/ directory
                examples_dir = os.path.join(skill_dir, "examples")
                os.makedirs(examples_dir, exist_ok=True)
                
                # Zipping the skill directory
                zip_path = os.path.join(zip_dir, folder_name)
                shutil.make_archive(zip_path, 'zip', skill_dir)
                
                skill_count += 1
                print(f"Exported (Rich & Zipped): {folder_name}.zip")

    print(f"\n✅ Total {skill_count} skills exported successfully to {dest_dir} and zipped in {zip_dir}!")

if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    
    src = os.path.join(os.path.dirname(__file__), "BA-Skills")
    dest = os.path.join(os.path.dirname(__file__), "Claude-Skills")
    zip_dest = os.path.join(os.path.dirname(__file__), "Claude-Skills-Zip")
    print("=== Starting Rich Export & Zipping to Claude Format ===")
    export_skills(src, dest, zip_dest)
