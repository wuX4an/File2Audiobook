from .readers import *
from .detect_file import file_type


def selector(path):
    if file_type(path) == "txt":
        return read_txt(path)
    if file_type(path) == "pptx":
        return read_pptx(path)
    if file_type(path) == "docx":
        return read_docx(path)
    if file_type(path) == "epub":
        return read_epub(path)
