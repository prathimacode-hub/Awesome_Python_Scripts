import tkinter as tk
import tkinter.font as tkFont
from tkinter.filedialog import askopenfilename
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

## Helper Functions 

### Get PDF details in the window
def extract_information(pdf_path):
    new_window = tk.Toplevel(root)
    new_window.title(pdf_path)
    new_window.geometry("400x200")
    with open(pdf_path, "rb") as f:
        pdf = PdfFileReader(f, strict=False)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
    txt = f"""
    Information about {pdf_path}:

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """

    new_label = tk.Label(new_window, text=txt)
    new_label.place(x=10, y=10)

# Read a pdf then create a new pdf with each page rotated
def rotate_pages(pdf_path):
    
    # Output file object
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(pdf_path)
    
    # Copy each page to the output file object
    for i in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(i).rotateClockwise(90))

    # Export the object in a pdf file
    with open("./rotate_pages.pdf", "wb") as fh:
        pdf_writer.write(fh)

# Read two pdfs and merge them into one
def merge_pdfs(pdfA, pdfB):
    
    # Reading file objects of both pdfs
    pdfA_obj = PdfFileReader(pdfA, strict=False)
    pdfB_obj = PdfFileReader(pdfB, strict=False)
    
    # Object to store merged pdf
    pdf_merge = PdfFileWriter()

    # Get all the pages from pdfA to writer object
    for pgNum in range(pdfA_obj.numPages):
        pg = pdfA_obj.getPage(pgNum)
        pdf_merge.addPage(pg)

    # Get all the pages from pdfB to writer object
    for pgNum in range(pdfB_obj.numPages):
        pg = pdfB_obj.getPage(pgNum)
        pdf_merge.addPage(pg)

    # Write out the merged PDF
    fileObj = open(".\merged_pdf.pdf", "wb")
    pdf_merge.write(fileObj)
    
    #Display confirmation message
    info_label.configure(text=f"File Saved at : {os.getcwd()}\merged_pdf.pdf")


# Split one pdf in two different pdfs 
def pdf_split(path, ranges):
    
    # Read original pdf
    pdf = PdfFileReader(path, strict=False)
    
    # Writer obeject for pdf
    pdf_writer = PdfFileWriter()

    # Get all the pages upto the provided page number
    for page in range(int(ranges)):
        pdf_writer.addPage(pdf.getPage(page))
        
    # Export the object to pdf file for the first part of the splitted pdf
    with open("./SplitA.pdf", "wb") as output_pdf:
        pdf_writer.write(output_pdf)

    # Same steps for the second part of the pdf.
    pdf_writer = PdfFileWriter()
    for page in range(int(ranges), pdf.getNumPages()):
        pdf_writer.addPage(pdf.getPage(page))
    with open("./SplitB.pdf", "wb") as output_pdf:
        pdf_writer.write(output_pdf)

# Overlay water mark on a pdf (watermark should also be a pdf)
def create_watermark(input_pdf, watermark):

    # Get watermark page after reading the pdf 
    watermark_obj = PdfFileReader(watermark, strict=False)
    watermark_page = watermark_obj.getPage(0)
    
    pdf_reader = PdfFileReader(input_pdf, strict=False)
    pdf_writer = PdfFileWriter()

    # Watermark all the pages
    for page in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page)
        page.mergePage(watermark_page)
        pdf_writer.addPage(page)
        
    # Export the writer object to a pdf
    with open("./Watermarked.pdf", "wb") as out:
        pdf_writer.write(out)
    info_label.configure(text=f"Watermark set\nCheck : {os.getcwd()}")

# Make a pdf password protected
def add_encryption(input_pdf, password):
    
    # Reader and writer objects 
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(input_pdf, strict=False)

    # Copy all the pages from the pdf to the writer object
    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))
    
    # add encryption to a writer object
    pdf_writer.encrypt(user_pwd=password, owner_pwd=None, use_128bit=True)
    
    # export the encrypted pdf 
    f = open("./Encrypted.pdf", "wb")
    pdf_writer.write(f)
    info_label.configure(text=f"Password Set\nCheck : {os.getcwd()}")


## Selection Functions

# Select file and call extract_information()
def info():
    path = askopenfilename(title="Select File", filetypes=[("PDF Document", "*pdf")])
    if path:
        extract_information(path)


# Select file and call rotate_pages()
def rotate():
    path = askopenfilename(title="Select File", filetypes=[("PDF Document", "*pdf")])
    if path:
        rotate_pages(path)

# Select two files and call merge_pdfs()
def merge():
    path_A = askopenfilename(
        title="Select First File", filetypes=[("PDF Document", "*pdf")]
    )
    path_B = askopenfilename(
        title="Select Second File", filetypes=[("PDF Document", "*pdf")]
    )
    if all(path_A, path_B):
        merge_pdfs(path_A, path_B)

#Select file and get range and then call pdf_split
def split():
    path = askopenfilename(title="Select File", filetypes=[("PDF Document", "*pdf")])

    def assign():
        ranges = Range.get()
        pdf_split(path, ranges)
        newWindow.destroy()

    if path:
        # Small windo basic tkinter setup
        # this window is responsible of creating a popup and ask user the required informationn
        newWindow = tk.Toplevel(root)
        newWindow.title("Enter Split Ranges")
        newWindow.geometry("400x200")
        newWindow.rowconfigure([0, 1, 2], minsize=50)
        newWindow.columnconfigure([0], minsize=400)
        labelh = tk.Label(newWindow, text="Enter Split Range middle point and Press GO")
        labelE = tk.Label(newWindow, text="Eg: 1-23 and 24-36 can be written as 23")
        labelh.grid(row=0, column=0)
        labelE.grid(row=1, column=0)
        container = tk.Frame(newWindow)
        container.columnconfigure([0, 1], minsize=200)
        container.rowconfigure([0], minsize=50)
        Range = tk.Entry(container)
        submit = tk.Button(container, text="GO", command=assign)
        Range.grid(row=0, column=0)
        submit.grid(row=0, column=1, padx=10, pady=10)
        container.grid(row=2, column=0)


# Select two files and call creat_watermark()
def watermark():
    path = askopenfilename(title="Select File", filetypes=[("PDF Document", "*pdf")])
    pathW = askopenfilename(
        title="Select Watermark File", filetypes=[("PDF Document", "*pdf")]
    )
    if all(path, pathW):
        create_watermark(path, pathW)


def encrypt():
    path = askopenfilename(title="Select File", filetypes=[("PDF Document", "*pdf")])

    def assign():
        passwordText = password.get()
        add_encryption(path, passwordText)
        newWindow.destroy()

    if path:
        
        # Small windo basic tkinter setup
        # this window is responsible of creating a popup and ask user the required informationn
        newWindow = tk.Toplevel(root)
        newWindow.title("Create Password")
        newWindow.geometry("400x200")

        newWindow.rowconfigure([0, 1], minsize=100)
        newWindow.columnconfigure([0], minsize=400)
        label1 = tk.Label(newWindow, text="Create a Strong password to encrypt PDF")
        label1.grid(row=0, column=0)

        container = tk.Frame(newWindow)
        container.rowconfigure([0], minsize=100)
        container.columnconfigure([0, 1], minsize=200)
        password = tk.Entry(container)
        submit = tk.Button(container, text="Encrypt", command=assign)
        password.grid(row=0, column=0)
        submit.grid(row=0, column=1)
        container.grid(row=1, column=0)


# Basic root tkinter setup, geometry, title
root = tk.Tk()
root.geometry("800x600")
root.wm_title("PDF Utility Tool")
root.resizable(False, False)
fontStyle = tkFont.Font(size=42)
btnText = tkFont.Font(size=12)

# Creating two rows and one column in the window
root.columnconfigure(0, minsize=800)
root.rowconfigure(0, minsize=200)
root.rowconfigure(2, minsize=400)

# Title label
label1 = tk.Label(
    text="PDF Utility Tool", font=fontStyle, borderwidth=2, relief="groove"
)

# Information label shows the confirmation messages
info_label = tk.Label(text="", font=btnText)
label1.grid(row=0, column=0)
info_label.place(x=200, y=150)

# Container to store all the function buttons
container = tk.Frame(root)

container.columnconfigure([0, 1], minsize=300)
container.rowconfigure([0, 1, 2], minsize=100)

# Button for evry function and custom command attribute to call the functions
btn_merge = tk.Button(
    container,
    text="Merge",
    bg="#FFE882",
    padx=15,
    pady=15,
    width=9,
    height=2,
    command=merge,
)
btn_rotate = tk.Button(
    container,
    text="Rotate",
    bg="#FFE882",
    padx=15,
    pady=15,
    width=9,
    height=2,
    command=rotate,
)
btn_split = tk.Button(
    container,
    text="Split",
    bg="#FFE882",
    padx=15,
    pady=15,
    width=9,
    height=2,
    command=split,
)
btn_watermark = tk.Button(
    container,
    text="Watermark",
    bg="#FFE882",
    padx=15,
    pady=15,
    width=9,
    height=2,
    command=watermark,
)
btn_encrypt = tk.Button(
    container,
    text="Encrypt",
    bg="#FFE882",
    padx=15,
    pady=15,
    width=9,
    height=2,
    command=encrypt,
)
btn_extract = tk.Button(
    container,
    text="Extract Info",
    bg="#FFE882",
    padx=15,
    pady=15,
    width=9,
    height=2,
    command=info,
)


# Placing all the buttons in the grid setup
btn_merge.grid(row=0, column=0)
btn_rotate.grid(row=0, column=1)
btn_split.grid(row=1, column=0)
btn_watermark.grid(row=1, column=1)
btn_encrypt.grid(row=2, column=0)
btn_extract.grid(row=2, column=1)

container.grid(row=1, column=0)

root.mainloop()
