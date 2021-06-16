import PyPDF2
import pyttsx3

infile = open('Related/sample.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(infile)
num_Pages = pdfReader.numPages
print(num_Pages)

start = pyttsx3.init()
print("Playing audio..")

for i in range(0, num_Pages):
	page = pdfReader.getPage(i)
	text = page.extractText()
	start.say(text)
	start.runAndWait()


	