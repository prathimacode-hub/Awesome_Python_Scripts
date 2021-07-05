# Invisibility Cloak

# Aim
  Hello EVERYONE,lets do some magic using computer vision. I hope you all know about ‘invisible cloak’, this will make you invisible. We will see how we can do the same magic       trick   with the help of computer vision. I will code with python and use the opencv and numpy library.
  
# Purpose  
  Our purpose is to become Invisible using a cloak with the help of various Python libraries.
  
# Setup instructions
  
  1. Install the latest python 3.5 and above and once you finish installing it .
  2. Add opencv library.
  3. Add Numpy library.
  
# Detailed explanation
  
  We wll learn how to create our own ‘Invisibility Cloak’ using simple computer vision techniques in OpenCV. Here we have written this code in Python because it provides             exhaustive and sufficient library to build this program.

  Here, we will create this magical experience using an image processing technique called Color detection and segmentation. In order to run this code, you need an mp4 video named   “video.mp4“. You must have a cloth of same color and no other color should be visible into that cloth. We are taking the red cloth. If you are taking some other cloth, the code   will remain the same but with minute changes.
  
  firstly the program when you run it it will capture the background image and then. When you put a red colored colored cloth in front of camera the program will detect the colored cloak using color detection and segmentation algorithm . And the program will generate a mask to determine the region in the frame corresponding to the detected color(red in this case). Program  will refine this mask and then use it for segmenting out the cloth from the frame. Program will replace the pixels value of the detected red color region with corresponding pixel values of the static background. 

# Compilation Steps

1. Capture and store the background frame
2. Detect the defined color using color detection and segmentation algorithm.
3. Segment out the defined colored part by generating a mask.
4. Generate the final augmented output to create a magical effect. 



# Output


![](Media/output.gif)





# Author(s):-
  [Kartik Srivardhan](http://github.com/Cartikx3)



