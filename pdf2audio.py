from gtts import gTTS
from PyPDF2 import PdfFileReader
def text2audio(text1):
    lang1="en"
    obj = gTTS(text=text1, lang=lang1, slow= False)    
    obj.save("audio.mp3" )
 
def get_pdf_content_lines(pdf_file_path):
    with open(pdf_file_path, "rb") as f:
        pdf_reader = PdfFileReader(f)
        for page in pdf_reader.pages: 
            for line in page.extractText().splitlines():
                yield line
def appendtofile(i):
    path="C:\programms\extract.text"
    #replace path 
    f = open(path,'w')
    f.write(i)
    f.write("\n")
    f.close()
for i in get_pdf_content_lines("C:\programms\misc\Ramayan of Valmiki - Hariom Group ( PDFDrive ).pdf"):
    appendtofile(i)


f = open('C:\programms\extract.text','r') #replace path 
t=f.read().split(" ")
text= ""

for i in range(0,len(t)):
    text += t[i]

text2audio(text)