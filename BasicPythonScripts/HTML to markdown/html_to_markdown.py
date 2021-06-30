#import markdownify
import markdownify

#taking html file  as input
try:
    html_file = input('Enter HTML file path: ')
    html = open(html_file, "r")
except:
    print('No file selected')

#creating a new markdown file
with open('markdown_file.md', 'w') as md_file:
    #convert html code to markdown format
    for data in html:
        md_file.write(markdownify.markdownify(data))
        md_file.write("\n")
md_file.close()

print('Conversion successfull')
