# Import the module
import os

# Function for creating new folder


def create_folder(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)  # Make a folder with the name given by the user

# Function to move files inside the folder


def move_files(folder_name, files):
    for file in files:
        # Moving all the files inside the folder
        os.replace(file, f"{folder_name}/{file}")


# Driver function
if __name__ == "__main__":
    path = r"C:\Users\Dell\Downloads\All"
    os.chdir(path)  # Jump to the directory where all the files present
    all_files = os.listdir()  # List all the files of the directory
    for i in range(len(all_files)):
        try:
            # Check only for the files not for the folders
            all_files[i] = "."+all_files[i].split(".")[1]
        except:
            pass  # If it'a a folder then nothing to do
    # List all the files which contains extension, not folders because folders don;t have any extension
    all_files = [file for file in all_files if "." in file]

    for file in all_files:  # Loop for arranging all the files in a separate folders
        folder_name = f"{file[1:].upper()} Files"
        create_folder(folder_name)
        files = [fil for fil in os.listdir() if os.path.splitext(fil)
                 [1] == file]
        move_files(folder_name, files)
