from epub2txt import epub2txt
from warnings import filterwarnings

filterwarnings("ignore", category=FutureWarning, module="ebooklib.epub")

def read_epub(path):
    content = epub2txt(path).replace("\n", " ")
    return content
