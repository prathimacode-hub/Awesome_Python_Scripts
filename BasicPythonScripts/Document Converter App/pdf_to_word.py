# importing modules
from pdf2docx import parse

# user inputs
pdf_path=input("Enter the pdf path: ")
start_page=int(input("Enter the starting page number of the pdf from which the pdf should be converted to doc: "))
end_page=int(input("Enter the page number till which the pdf should be converted to doc: "))
doc_path=input("Enter the folder where the doc has to be saved: ")
doc_name=input("Enter the name that the doc has to be saved with: ")

f_doc=doc_path+"\ "+doc_name+".doc"

# converting pdf to word
parse(pdf_path, f_doc, start=start_page, end=end_page)
