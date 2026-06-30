import zipfile, xml.etree.ElementTree as ET

def extract_text(docx_path):
    try:
        with zipfile.ZipFile(docx_path) as z:
            xml_content = z.read('word/document.xml')
            tree = ET.fromstring(xml_content)
            namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            paragraphs = []
            for p in tree.findall('.//w:p', namespaces):
                texts = [node.text for node in p.findall('.//w:t', namespaces) if node.text]
                if texts:
                    paragraphs.append(''.join(texts))
            return '\n'.join(paragraphs)
    except Exception as e:
        return str(e)

with open('extracted_docs.txt', 'w', encoding='utf-8') as f:
    f.write('--- Activity_Diagram_Generation_Rules_Enterprise.docx ---\n')
    f.write(extract_text('e:/BA Skill Library/Activity_Diagram_Generation_Rules_Enterprise.docx') + '\n\n')
    f.write('--- BoQuyTac_TaiLieu_BA_v1.0.docx ---\n')
    f.write(extract_text('e:/BA Skill Library/BoQuyTac_TaiLieu_BA_v1.0.docx') + '\n')
