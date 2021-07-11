from pdf2image import convert_from_path

pdf_path = input("Enter the pdf path: ")
start_page = int(input(
    "Enter the starting page number of the pdf from which the pdf should be converted to jpg: "))
end_page = int(
    input("Enter the page number till which the pdf should be converted to jpg: "))

# Store Pdf with convert_from_path function
images = convert_from_path(pdf_path)

for i in range(start_page, end_page):

    # Save pages as images in the pdf
    images[i].save('page' + str(i) + '.jpg', 'JPEG')
