#required module-pip install zipfile36
from zipfile import ZipFile

#opening file ...
z = ZipFile("sample.zip", 'w')

#passing files to zip files..
z.write("ex.py")

z.write("text.txt")

#closing files...
z.close()
