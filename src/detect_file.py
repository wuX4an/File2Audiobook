def detect_input_file(path):
    extension = path.split(".")
    if len(extension) > 1:
        return extension[-1]
    else:
        return ""


def file_type(path):
    if detect_input_file(path) == "txt":
        return "txt"
    if detect_input_file(path) == "epub":
        return "epub"
    if detect_input_file(path) == "pptx":
        return "pptx"
    if detect_input_file(path) == "docx":
        return "docx"
    else:
        return "File type not supported"
