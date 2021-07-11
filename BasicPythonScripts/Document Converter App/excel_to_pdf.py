# This script converts excel files to pdf files

# Import Module
from win32com import client

# Open Microsoft Excel
excel = client.Dispatch("Excel.Application")

excel_path = input("Enter the path of the excel file completely: ")
pdf_path = input(
    "Enter the path of the folder where you want pdf file to be present: ")
pdf_name = input("Enter the name by which pdf file should be saved: ")
# Read Excel File
sheets = excel.Workbooks.Open(excel_path)
work_sheets = sheets.Worksheets[0]

# Convert into PDF File
work_sheets.ExportAsFixedFormat(0, pdf_path+'\ '+pdf_name+".pdf")
