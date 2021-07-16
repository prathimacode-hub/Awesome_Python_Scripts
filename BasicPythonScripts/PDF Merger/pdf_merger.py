from PyPDF2 import PdfFileMerger
import os
#using the inbuilt function of library
merger = PdfFileMerger()
#getting all the pdfs as per name/sequence
for items in os.listdir():
    #checking that the file selected is pdf only or not
    if items.endswith('.pdf'):
        merger.append(items)
#making the newly merged file
merger.write("new.pdf")