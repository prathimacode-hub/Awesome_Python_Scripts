# required module-pip install zipfile36
from zipfile import ZipFile

# file name
filename = "sample.zip"

# opening zip file as Zip name
with ZipFile(filename, "r") as zip:
    zip.printdir()
    print("extracting all files")
    zip.extractall()
    print("done")