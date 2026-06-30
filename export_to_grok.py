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

                original_name = metadata.get('name', 'unknown-skill')
                description = metadata.get('description', metadata.get('purpose', 'BA Skill for Grok'))
                description = description.replace('\n', ' ').strip()

                # Read Prompt Content
                with open(prompt_path, 'r', encoding='utf-8') as f:
                    prompt_content = f.read()

                # Determine target directory name (slugified)
                folder_name = slugify(original_name)
                
                # IMPORTANT FOR GROK: The name in YAML MUST be slugified (a-z, 0-9, -)
                grok_name = folder_name

                skill_dir = os.path.join(dest_dir, folder_name)
                os.makedirs(skill_dir, exist_ok=True)

                # Create SKILL.md
                skill_md_content = f"""---
name: {grok_name}
description: {description}
---

{prompt_content}
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
                print(f"Exported to Grok: {folder_name}.zip")

    print(f"\n✅ Total {skill_count} skills exported successfully to {dest_dir} and zipped in {zip_dir}!")

if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    
    src = os.path.join(os.path.dirname(__file__), "BA-Skills")
    dest = os.path.join(os.path.dirname(__file__), "Grok-Skills")
    zip_dest = os.path.join(os.path.dirname(__file__), "Grok-Skills-Zip")
    print("=== Starting Export to Grok Format ===")
    export_skills(src, dest, zip_dest)
