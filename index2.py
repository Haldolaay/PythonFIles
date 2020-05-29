import PyPDF2 #pdf library
import re # regex library

fileobj = open('signed3rdterm.pdf', 'rb')  # opening a file - doesn't require any libraries - if the file doesn't exist, it should throw an error, I'm not handeling errors for now cuz I'm lazy
pdfReader = PyPDF2.PdfFileReader(fileobj) #creating a file reader using pypdf2 - will need it to use functions on file
text = pdfReader.getPage(0).extractText() # extracting the text from the first page 
regex = re.compile(r'^([0-9]( |-)?)?(\(?[0-9]{3}\)?|[0-9]{3})( |-)?([0-9]{3}( |-)?[0-9]{4}|[a-zA-Z0-9]{7})$}') # temp regex to find xxx-xxx-xxxx format number
result = regex.findall(text) # using the regex to find phone values from the text, not the file
print(result)
newFile = open('newfile.txt','wb')
writer = PyPDF2.PdfFileWriter()
writer.addPage(pdfReader.getPage(0))
writer.write(newFile)