#!/usr/bin/env python
import subprocess
import optparse
from gtts import gTTS
from src import selector


parser = optparse.OptionParser()

parser.add_option("-f", "--file", dest="file", help="File path to read")
parser.add_option("-l", "--lang", dest="lang", help="Language output", default="en")
parser.add_option("-s", "--speed", dest="speed", help="Speed of the voice", default="150")
parser.add_option("-n", "--name", dest="name", help="Name of the file audiobook", default="audiobook")
parser.add_option("-v", "--voice", dest="voice", help="Use 'espeak' or 'gtts'", default="espeak")

(options, arguments) = parser.parse_args()

name = options.name
speed = options.speed
language = options.lang
file = options.file
voice = options.voice

def main():
    try:
        text = selector(file)
        if voice == "gtts":
            if speed != "150":
                print(speed)
                print("Currently, gTTS does not offer a direct way to adjust the playback speed of the generated audio.")
            text = selector(file)
        
            tts = gTTS(text=text, lang=language)
            tts.save(f"{name}.mp3")
            print(f"Your audiobook has been saved as: {name}.mp3")
        
        if voice == "espeak":    
        # print(text)
            text = selector(file)
            subprocess.run(["espeak", "-w", name + ".mp3", "-s", speed, "-v", language, text])
            print(f"Your audiobook has been saved as: {name}.mp3")
    except Exception:
        return None

if __name__ == "__main__":
    main()
