import os
import PyPDF2
from PyPDF2 import PdfFileReader

fp = open('dealerTrack.pdf')
pdfFile = PdfFileReader(fp)
if pdfFile.isEncrypted:
    try:
        pdfFile.decrypt('')
        print('File Decrypted (PyPDF2)')
    except:
        command = ("cp "+ 'dealerTrack.pdf' +
            " temp.pdf; qpdf --password='' --decrypt temp.pdf " + filename
            + "; rm temp.pdf")
        os.system(command)
        print('File Decrypted (qpdf)')
        fp = open(filename)
        pdfFile = PdfFileReader(fp)
else:
    print('File Not Encrypted')
    
    
    # look into this astrix function later
    r=4
for x in range(r):
    print(____*(r-x-1)+'*'*(2*x+1))
