import cv2
import numpy as np
import os
import glob

def singleImage():
    filename = input("Please Enter File Name : ")
    newfilename = "Images/" + filename
    img = cv2.imread(newfilename)
    
    try:
        img2 = np.zeros((img.shape[0],img.shape[1],img.shape[2]), np.uint8)
    except:
        print("Invalid Image please check filename and extension")
        exit()

    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            #print(img[i,j])
            img2[i,j] = img[i,j]
            img2[i,j][0] = 255 - img2[i,j][0]
            img2[i,j][1] = 255 - img2[i,j][1]
            img2[i,j][2] = 255 - img2[i,j][2]
    cv2.imwrite(f"Ghost of {filename}", img2)
    cv2.imshow("Negative Image",img2)
    print(f"Ghost of {filename} is created")
    cv2.waitKey(0)   
    
def multiImage():
    files = glob.glob('D:/React_apps/Negative Image/Images/*.jpg')
    PATH = "D:/React_apps/Negative Image/Images/"
    files.sort(key=os.path.getmtime)
    for filename in files:
        img = cv2.imread(filename)
        img2 = np.zeros((img.shape[0],img.shape[1],img.shape[2]), np.uint8)
        for i in range(0,img.shape[0]):
            for j in range(0,img.shape[1]):
                #print(img[i,j])
                img2[i,j] = img[i,j]
                img2[i,j][0] = 255 - img2[i,j][0]
                img2[i,j][1] = 255 - img2[i,j][1]
                img2[i,j][2] = 255 - img2[i,j][2]
        filename = filename.split("\\")
        newfilename = "Ghost of "+ str(filename[-1])
        cv2.imwrite(os.path.join(PATH,newfilename), img2)
        print(newfilename + " is created")
        cv2.imshow("Ghost Image",img2)
        cv2.waitKey(0) 
        
if __name__ == "__main__":
    ans = input("If you want to work in single image type 's' else for multiple images type 'm' ")
    if ans.lower() == 's':
        singleImage()
    else:
        print("Please Wait while we process your files ...")
        multiImage()
        
    