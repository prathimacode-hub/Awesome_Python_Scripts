import tkinter as tk
from tkinter import *
from PIL import Image
from PIL import ImageTk
from datetime import date
import shortuuid
import multiprocessing
import time

### This Function is used to detect censor words ###
def censor(listOfWords):
    listOfWords=listOfWords.split(",") ## This list contains dataset of curse words
    #print(" ugly" in listOfWords)
    li=[]  # In this list we are putting the detected words so that there won't be any repetitions 
    filename = "Utils/CurseWordsDetected/detectedWords"+str(shortuuid.uuid())+".txt" #For unique name
    while True:
        f = open("Utils/tempFile.txt","r")
        userInput=f.read()
        userInput=userInput.replace(".", " ")
        userInput=userInput.replace(",", " ")
        userInput=userInput.replace("/", " ")
        userInputList=userInput.split( )
        #Removing fullstops and commas which can be problematic later
        
        #userInput=userInput.split(" ")
        #print(userInput)
        
        # Traversing the dataset and checking if any match is found or not
        for ele in listOfWords:
            #for eleUserinp in userInput:
            #print(eleUserinp,"INPUT") if str(ele).strip() in str(eleUserinp).strip():
            
            if str(ele).strip() in str(userInput):
                ## Now match is found but there is possibility of false alert eg. in homework there is word ho, so it will be false positive so removing that
                
                if len(str(ele).strip().split(" "))<2 and str(ele).strip() not in userInputList:
                    continue
                    #print("Less than 2",len(str(ele).strip().split(" ")))
                    #print("False Alert")
                #else:
                    #print(len(str(ele).strip().split(" ")))
                    #pass
                
                # Print on terminal detected word
                print(ele,"detected")
                
                
                # Save in text file
                f = open(filename,"a+")
                
                if ele not in li:
                    li.append(ele)
                    ele=ele+"\n"
                    f.write(ele)
                
                time.sleep(1)
            else:
                #print(ele,userInput)
                continue

## This function creates GUI for detector

def guiForCensor():
    
    # This function is for saving written input by the user to the file after clicking save button
    def saveToFile():
    
        nameOfFile = 'Utils/InputFile/'+str(date.today())+str(shortuuid.uuid())+'.txt'
        inputTextMatter=inputtxt.get(1.0,"end-1c")
        f = open(nameOfFile, "w+")
        f.write(str(inputTextMatter))
        print(">> saveFunction")
        
    # This is for backend purpose, we are saving file in temp so we can get it later    
    def printInput():
        inputTextMatter=inputtxt.get(1.0,"end-1c")
        f = open("Utils/tempFile.txt", "w+")
        f.write(str(inputTextMatter))
        frame.after(2000, printInput)
        
    # Creating Frame    
    frame = tk.Tk()
    frame.title("Censor Words")
    frame.geometry('640x480')
    
    # Setting Background and necessary components
    bg="Images/bg.jpg"
    image=Image.open(bg)
    image = image.resize((640,480), Image.ANTIALIAS)
    bg = ImageTk.PhotoImage(image)
    
    bglabel=Label(frame,image=bg)
    bglabel.place(x=0,y=0)
    
    inputtxt = tk.Text(frame, height = 15,width = 50)
    inputtxt.place(x=120,y=100)
    
    heading = tk.Label(frame, text="Censor Words", font=("Gentium Basic", 25), bg='#255543', fg='#fff')
    heading.place(x=220,y=50)
    
    saveButton = tk.Button(frame,text="Save",command=saveToFile)
    saveButton.place(x=315,y=400)
    
    frame.after(2000, printInput)
    frame.mainloop()

# opening dataset    
f = open("Utils/censor_word_list.txt", "r")
listOfWords = f.read()    

# Use of multiprocessing to run both functions at same time
p1 = multiprocessing.Process(target=censor,args=(listOfWords,))
p2 = multiprocessing.Process(target=guiForCensor)    
if __name__ == "__main__":
    p1.start()
    p2.start()
    #censor(listOfWords)
    #guiForCensor()
    
    
    