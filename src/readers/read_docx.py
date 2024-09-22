from docx import Document


def read_docx(path):

    doc = Document(path)
    fullText = []
    for shape in doc.paragraphs:
        fullText.append(shape.text)
    return "\n".join(fullText).replace("\n", " ")
