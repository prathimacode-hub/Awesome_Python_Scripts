import cv2
import numpy as np
import os
import glob

# For Single Image
def singleImage():
    filename = input("Please Enter File Name : ") # Asking Image name
    newfilename = "Images/" + filename  # Accessing Image inside "Images" folder
    img = cv2.imread(newfilename)
    
    # Creating a blank Image which is of same size as of above image
    try:
        img2 = np.zeros((img.shape[0],img.shape[1],img.shape[2]), np.uint8)
    except:
        print("Invalid Image please check filename and extension")
        exit()
    # Open CV Images are Numpy array. So traversing each and every pixel using 2 for loops since its 2D array.
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            #print(img[i,j])
            img2[i,j] = img[i,j] # Copying The pixels on blank array
            # Each pixel contains 3 colors Blue, Green, Red so accessing them and subtracting it from 255 we would get negative of the pixel
            img2[i,j][0] = 255 - img2[i,j][0]  
            img2[i,j][1] = 255 - img2[i,j][1]
            img2[i,j][2] = 255 - img2[i,j][2]
    # After doing this write the image to the folder
    cv2.imwrite(f"Ghost of {filename}", img2)
    cv2.imshow("Negative Image",img2)
    print(f"Ghost of {filename} is created") # Display message
    cv2.waitKey(0)   

# This is for multiple images in the folder
def multiImage():
    # Using glob  we would access all jpg images. You can change it to whatever the extension is
    files = glob.glob('D:/React_apps/Negative Image/Images/*.jpg')
    PATH = "D:/React_apps/Negative Image/Images/"
    files.sort(key=os.path.getmtime) # sorting according to time and date
    # Using for looping to get every image inside files folder
    for filename in files:
        img = cv2.imread(filename)
        img2 = np.zeros((img.shape[0],img.shape[1],img.shape[2]), np.uint8) # same as before creating a blank image
        for i in range(0,img.shape[0]):
            for j in range(0,img.shape[1]):
                #print(img[i,j])
                img2[i,j] = img[i,j]
                img2[i,j][0] = 255 - img2[i,j][0]
                img2[i,j][1] = 255 - img2[i,j][1]
                img2[i,j][2] = 255 - img2[i,j][2]
        filename = filename.split("\\")  # Doing this we are getting spliting string where \ is mentioned to get image name since path is in fashion D:\Programs\image.jpg
        newfilename = "Ghost of "+ str(filename[-1]) # Getting last index where image name is mentioned 
        cv2.imwrite(os.path.join(PATH,newfilename), img2) # Writing image to folder
        print(newfilename + " is created")  # Display the message
        cv2.imshow("Ghost Image",img2)
        cv2.waitKey(0) 
        
if __name__ == "__main__":
    # Check if user needs to perform operation on single or multiple images and execute accordingly
    ans = input("If you want to work in single image type 's' else for multiple images type 'm' ")
    if ans.lower() == 's':
        singleImage()
    else:
        print("Please Wait while we process your files ...")
        multiImage()
        
    
