# Censor Word Detection

## Aim

In this project I have created a python script that will alert user if he/she has written any censor/abusive/curse word and save that in text file

## Purpose

Sometimes we aren't aware of what we are writing and it is possible that in flow we write some abusive words. Such words not only affect our personal image and career but also hurts the person with whom we are having conversation with and it may lead to unnecessary disputes. Therefore using this script the users can keep monitoring themselves so that they won't write any censor words in their text.  

## Short description of package/script

- For GUI Tkinter is used.
- To work with Images I have used PIL library
- I am using shortuuid to get unique name for files and also using date time module with that
- Also using Multiprocessing so that text can be analyzed in real time and data can be saved appropriately


## Workflow of the Project

1. As soon as script starts running a GUI is seen in which user has to input the text
2. I am using a dataset "full list of bad words" to detect censor words
3. Now this user input is checked with this list and if match is found the text is displayed in screen.
4. At the same time text matter is saved in text folder which is in Utils\CurseWordsDetected\ folder
5. Unique name is selected so that we can be assured that files are not overwritten
6. User can correct mistakes (if any) and then can simply click save button to save text matter
7. This file is then saved in Utils\InputFile, Naming conventions are same as above



## Setup instructions

1. Install necessary libraries from requirements.py file
2. Run censor.py file
3. Enter text in textbox and correct mistakes if any.
4. Mistakes can be seen in terminal and all the mistakes are saved in text file also
5. After satisfactory results click save button to save text and this file can be found in InputFile Folder 

## Compilation Steps

This program using multiprocessing and it runs 2 functions i.e. "sensor" and "guiForCensor" simultaneously.
As soon as user types in data the text is saved in temp file which is hidden and no use to the user.
The changes are made there in realtime and same text data is then retrieved to evaluate whether censor words exists or not

\
## Output

Display images/gifs/videos of output/result of your script so that users can visualize it


## Author(s)

Tushar Amdoskar

[Tushar's Website](https://tusharamd.github.io/)
