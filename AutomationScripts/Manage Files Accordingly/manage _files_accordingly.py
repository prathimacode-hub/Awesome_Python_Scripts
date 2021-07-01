# Import the following modules
import os
import time
import shutil
import datetime
import glob


# Change the directory and jump to the location where you want to arrange the files
os.chdir(r"C:\Users\Dell\Downloads\FireShot")
all_files = list(os.listdir())  # List the directories and make a list
outputs = os.getcwd()  # Get the current working directory

# Run a loop for traversing through all the files in the current directory
for files in all_files:
    try:
        inputs = glob.glob(files+"\\*")  # Jump to the directories files
        for ele in inputs:  # Now again run a loop for travering through all the files in side the folder
            shutil.move(ele, outputs)  # Now, move the files one-by-one
        # After extracting files from the folders, delete that folder
        shutil.rmtree(files)
    except:
        pass

# Again run a loop for traversing through all the files in the current directory
for files in os.listdir('.'):
    # Get all the details of the file creation and modification
    time_format = time.gmtime(os.path.getmtime(files))
    # Now, extract only the Year, Month, and Day
    datetime_object = datetime.datetime.strptime(str(time_format.tm_mon), "%m")
    full_month_name = datetime_object.strftime(
        "%b")  # Provide the number and find the month
    dir_name = full_month_name + '-' + \
        str(time_format.tm_mday) + "-" + \
        str(time_format.tm_year)  # Give the name of the folder

    if not os.path.isdir(dir_name):  # Check if the folder exists or not
        os.mkdir(dir_name)  # If not then make the new folder
    dest = dir_name
    shutil.move(files, dest)  # Move all the files to their respective folders
print("Suceessfully moved...")
