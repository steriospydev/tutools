from gtts import gTTS
import os
"""
Requirements:
    gtts
"""

mytext = "fu "
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("test_text_to_speech.mp3")

os.system("vlc welcome.mp3")