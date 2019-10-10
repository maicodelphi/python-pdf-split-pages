from PyPDF2 import PdfFileWriter, PdfFileReader
import os

def splitPDF(patch_pdf):
    input = PdfFileReader(open("D:\\folder\\pdf.pdf", "rb"))
    file_name = os.path.splitext(patch_pdf)
    #you can call a compressor in here: https://github.com/maicodelphi/gsCompressPDF
    for i in range(input.numPages):
        output = PdfFileWriter()
        output.addPage(input.getPage(i))
        splited_file = (str(file_name[0]) + "{0}" + str(file_name[1])).format(i+1)

        with open(splited_file, "wb") as pdf_page:
            #you can call a compressor in here: https://github.com/maicodelphi/gsCompressPDF
            output.write(pdf_page)
            pdf_page.close()
