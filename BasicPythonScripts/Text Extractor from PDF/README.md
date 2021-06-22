# Extract Text from PDF using Python Module

## Modules Required
- PyPDF2 - It is used in Python for PDF related operations

## AIM
To build a Python Script using the PyPDF2 Module which can extract text from a PDF file.

## COMPILATION STEPS
* Import PyPDF2 Module to:-
  * Read the pdf into the program to further manipulate it 
  * Count the number of pages in the PDF
  * Extract the text from a single PDF page
* Initialize an empty string which will store the text being extracted from the PDF file
* A for loop is made to parse through each page 
  * The extractText() function is used to extract text from the parsed PDF page
  * The extracted text is added to the emptry string initialized using simple string concatenation
* After parsing is done, the string in which the extracted text is stored is written in a new file named **extracted_text.txt** using basic File Handling in Python

## PDF FILE WITH TEXT
![Image1](https://github.com/Sakalya100/Awesome_Python_Scripts/blob/main/BasicPythonScripts/Text%20Extractor%20from%20PDF/Images/PDF%20File.png)



## OUTPUT OF EXTRACTED TEXT SHOWN IN NEW TEXT FILE **extracted_text.txt**
![Image2](https://github.com/Sakalya100/Awesome_Python_Scripts/blob/main/BasicPythonScripts/Text%20Extractor%20from%20PDF/Images/Output.png)



----------------------------------------------------------------------------------
## PyPDF2: 
A Pure-Python library built as a PDF toolkit.
To know more: [PyPDF2 Docs](https://pythonhosted.org/PyPDF2/)

## File handling
Python has some inbuilt methods to handles files and perform operations like reading and writing.
read about them : [File Handling Docs](https://www.geeksforgeeks.org/reading-writing-text-files-python/)

## Author

- [@Sakalya Mitra](https://github.com/Sakalya100)

