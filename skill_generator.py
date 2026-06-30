import os
import json
import textwrap
import sys
sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"e:\BA Skill Library\BA-Skills"

def write_skill(skill):
    """Generate expanded .md, .json, .prompt files for a skill."""
    full_path = os.path.join(base_dir, skill["path"])
    os.makedirs(full_path, exist_ok=True)
    fname = skill["name"].replace(" ", "_")

    # ===== 1. GENERATE EXPANDED .md =====
    md = f"""# {skill['name']}

## Level
{skill['level']}

## Purpose
{skill['purpose']}

## When to Use
{skill['when_to_use']}

## Prerequisites
"""
    for p in skill.get("prerequisites", []):
        md += f"- {p}\n"

    md += "\n## Inputs\n"
    for inp in skill["inputs_detail"]:
        md += f"### {inp['name']}\n"
        md += f"- **Mô tả:** {inp['description']}\n"
        md += f"- **Bắt buộc:** {'Có' if inp['required'] else 'Không'}\n"
        md += f"- **Ví dụ:** {inp['example']}\n\n"

    md += "## Process\n"
    for step in skill["process_detail"]:
        md += f"### Bước {step['step']}: {step['title']}\n"
        md += f"{step['description']}\n\n"
        if step.get("sub_steps"):
            for ss in step["sub_steps"]:
                md += f"- {ss}\n"
            md += "\n"

    md += "## Outputs\n"
    for out in skill["outputs_detail"]:
        md += f"### {out['name']}\n"
        md += f"- **Định dạng:** {out['format']}\n"
        if out.get("template"):
            md += f"- **Mẫu:**\n\n```\n{out['template']}\n```\n\n"

    if skill.get("sub_skills"):
        md += "## Sub-Skills (Kỹ năng con)\n"
        for ss in skill["sub_skills"]:
            md += f"- {ss}\n"
        md += "\n"

    md += "## Business Rules\n"
    for br in skill.get("business_rules", []):
        md += f"- {br}\n"

    md += "\n## Edge Cases & Exceptions\n"
    for ec in skill.get("edge_cases", []):
        md += f"- {ec}\n"

    md += "\n## Checklist\n"
    for c in skill.get("checklist", []):
        md += f"- [ ] {c}\n"

    md += f"\n## Example\n{skill.get('example', 'N/A')}\n"

    md += "\n## Related Skills\n"
    for rs in skill.get("related_skills", []):
        md += f"- {rs}\n"

    with open(os.path.join(full_path, f"{fname}.md"), "w", encoding="utf-8") as f:
        f.write(md)

    # ===== 2. GENERATE EXPANDED .json =====
    json_data = {
        "name": skill["name"],
        "category": skill["path"],
        "level": skill["level"],
        "description": skill["purpose"],
        "tags": skill.get("tags", []),
        "domain": skill.get("domain", ""),
        "sub_skills": skill.get("sub_skills", []),
        "related_skills": skill.get("related_skills", []),
        "inputs": [{"name": i["name"], "description": i["description"], "required": i["required"], "example": i["example"]} for i in skill["inputs_detail"]],
        "outputs": [{"name": o["name"], "format": o["format"]} for o in skill["outputs_detail"]],
        "business_rules": skill.get("business_rules", []),
        "quality_criteria": skill.get("quality_criteria", []),
        "estimated_effort": skill.get("estimated_effort", "N/A")
    }
    with open(os.path.join(full_path, f"{fname}.json"), "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)

    # ===== 3. GENERATE EXPANDED .prompt =====
    prompt = f"""# System Prompt for Skill: {skill['name']}

## Role
{skill.get('prompt_role', 'Senior Business Analyst với 10+ năm kinh nghiệm trong lĩnh vực phần mềm doanh nghiệp.')}

## Task
{skill.get('prompt_task', skill['purpose'])}

## Context
{skill.get('prompt_context', '')}

## Input từ User
Yêu cầu user cung cấp đầy đủ các thông tin sau trước khi bắt đầu:
"""
    for inp in skill["inputs_detail"]:
        prompt += f"- **{inp['name']}**: {inp['description']} (Ví dụ: {inp['example']})\n"

    prompt += f"""
## Rules & Constraints
"""
    for r in skill.get("prompt_rules", []):
        prompt += f"- {r}\n"

    prompt += f"""
## Quy trình thực hiện (Bắt buộc tuân thủ)
"""
    for step in skill["process_detail"]:
        prompt += f"### Bước {step['step']}: {step['title']}\n"
        prompt += f"{step['description']}\n"
        if step.get("sub_steps"):
            for ss in step["sub_steps"]:
                prompt += f"  - {ss}\n"
        prompt += "\n"

    prompt += "## Output Format\n"
    prompt += "Kết quả trả về PHẢI bao gồm các phần sau:\n\n"
    for out in skill["outputs_detail"]:
        prompt += f"### {out['name']}\n"
        prompt += f"Định dạng: {out['format']}\n"
        if out.get("template"):
            prompt += f"```\n{out['template']}\n```\n"
        prompt += "\n"

    prompt += "## Quality Gates (Kiểm tra chất lượng trước khi trả kết quả)\n"
    for qc in skill.get("quality_criteria", []):
        prompt += f"- [ ] {qc}\n"

    if skill.get("prompt_example"):
        prompt += f"\n## Ví dụ mẫu\n{skill['prompt_example']}\n"

    with open(os.path.join(full_path, f"{fname}.prompt"), "w", encoding="utf-8") as f:
        f.write(prompt)

    return fname

def run(skills):
    count = 0
    for s in skills:
        name = write_skill(s)
        count += 1
        print(f"  [{count}] {name}")
    print(f"\nTotal: {count} skills ({count*3} files)")
    return count
