from docx.api import Document

document = Document("sample-cv.docx")

def parse_table_data(rows):
    data = []
    for row in rows:
        for cell in row.cells:
            if len(cell.text) > 0:
                text = cell.text.replace("\n", " -- ")
                data.append(text)

    return data

def get_by_section(section_name):
    data = []
    for table in document.tables:
        table_section_name = table.rows[0].cells[0].text.strip().lower()

        if table_section_name == section_name:
            data = parse_table_data(table.rows)

    return data