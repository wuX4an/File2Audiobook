# File2Audiobook
This Python script converts text from a file into an audiobook using either the Google Text-to-Speech (gTTS) or eSpeak text-to-speech engine. Users can specify the input file, output filename, language, and voice engine via command-line options.

## Installation
``` 
git clone https://github.com/wuX4an/File2Audiobook
cd File2Audiobook
pip install -r requirements.txt
```

## Usage
```
python main.py -f example/text.txt -n book -l en -v gtts
```

* `-f`, `--file`: Path to the text file you want to convert (required).
* `-l`, `--lang`: Language for the output audio (default: "en").
* `-s`, `--speed`: Playback speed of the voice (currently has no effect with gTTS, default: "150").
* `-n`, `--name`: Name of the output audiobook file (default: "audiobook").
* `-v`, `--voice`: Voice engine to use ("gtts" or "espeak", default: "espeak").

## Features
File2Audiobook already support:
* `txt` text files.
* `epub` ebook files.
* `pptx` powerpoint files.
* `docx` word files.

> [!NOTE]
> This tool is very heasy to use, if you wish to crate your reader go [here.](src/readers) and create a file named `read_<extension_of_the_file_to_read>.py`. NOTE: the output must be continuous text, i.e. without `\n`. Add the extesion of the file on `__init__`, on `selector` and `detect_file`.
