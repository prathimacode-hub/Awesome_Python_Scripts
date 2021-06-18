# Extract Text from PDF using Python Module

## Modules Required
- PyPDF2 - It is used in Python for PDF related operations

## How it Works?
* Import PyPDF2 Module to:-
  * Read the pdf into the program to further manipulate it 
  * Count the number of pages in the PDF
  * Extract the text from a single PDF page
* Initialize an empty string
* A for loop parses through each page 
  * The extractText() function is used to extract text from the parsed PDF page
  * The extracted text is added to the emptry string initialized
* After parsing is done, the string in which the extracted text is stored is written in a new file named **extracted_text.txt** using basic File Handling in Python

----------------------------------------------------------------------------------
## PyPDF2: 
A Pure-Python library built as a PDF toolkit.
To know more: [PyPDF2 Docs](https://pythonhosted.org/PyPDF2/)

## File handling
Python has some inbuilt methods to handles files and perform operations like reading and writing.
read about them : [File Handling Docs](https://www.geeksforgeeks.org/reading-writing-text-files-python/)
