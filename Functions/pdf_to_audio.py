import PyPDF2
import pyttsx3
"""
  Requirements:
    PyPDF2
    pyttsx3
"""


path = 'pytest.pdf'

pdfReader = PyPDF2.PdfFileReader(open(path, 'rb'))
speaker = pyttsx3.init()

voices = speaker.getProperty('voices')

for i  in range(len(voices)):

	speaker.setProperty('voice', voices[3].id)
	speaker.say('Hello world!')
	speaker.runAndWait()
"""
for page_num in range(pdfReader.numPages):
	if page_num >30:
	    text =  pdfReader.getPage(page_num).extractText()
	    speaker.say(text)
	    speaker.runAndWait()
"""
speaker.stop()
