def read_txt(path):
    with open(path, "r") as file:
        content = file.read().replace("\n", " ")
    return content
