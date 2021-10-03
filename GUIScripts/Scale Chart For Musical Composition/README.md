# 🎼 **SCALE CHART FOR MUSICAL COMPOSITION**
<p align="center">
  <img width="500" height="300" src="https://media.giphy.com/media/EA4ZexjGOnfP2/giphy.gif">
</p>

## :ideograph_advantage: **INTRODUCTION**
* Beginners in the field of music learning, especially guitar learners face a lot of dilemma on where to begin with and many at times they lose a track of their learning which makes learning a complicated task. So to cut this slack off, we come with an easy, yet an efficient interface that would facilitate better learning.
* Python 3 and Tk can be used for building a creative application that visually represents different scales, notes, modes, and keys. Such tools are particularly common for string instruments like the guitar. Here, the users can navigate different scales (major, natural minor, harmonic minor, pentatonic, blues, etc.) and chords (5 chords, major, minor, diminished, augmented, and so on) on a 24- fret chart. The purpose of this project is to create a program with which you can find the position of the notes of a given scale in the guitar. 

## :question: **WHAT IS TKINTER ?**
Python offers multiple options for developing GUI (Graphical User Interface). Out of all the GUI methods, tkinter is the most commonly used method. It is a standard Python interface to the Tk GUI toolkit shipped with Python. Python with tkinter is the fastest and easiest way to create the GUI applications. Creating a GUI using tkinter is an easy task.

## ❓ **WHY EXACTLY DO WE NEED A SCALE CHART ?**
Pretend that you can imagine the spectrum of audible sound, and try to divide it into a musical system that makes sense for you and everyone around you. This is not easy! After centuries of struggle, humans have come up with a system but there are still disputes going on. Using the intervals of a given scale as index, we can retrieve the notes that make up the scale. This is all you need to understand. We will be applying this principle over and over again to extract the notes that compose a given scale. Using this information, we will then plot where these notes are located in the guitar. These plots all together make a SCALE CHART.
<p align="center">
 <img width="500" height="300" src="https://user-images.githubusercontent.com/36481036/135743837-ef05b516-cb7b-409b-adec-6ab39fa94a8e.png">
</p>


## :bookmark: **MODULE DESCRIPTION**
* The project being a GUI based application is made using Tkinter, a Python binding to the GUI toolkit. We started off from scratch and saw how we can use lists, dictionaries to build a tool that can help us play the guitar. We all know Music theory is a complex subject made up of a lot of components. For the purposes of this post, we will be simplifying things here quite a bit.
* Here we will treat the fretboard as a UX Component and treat it as an image.  Based on the design guidelines and the test variations, we introduce potential flaws in direct correlation to the design input. These flawed design mockups are manifested as images. Proper labeling of these images ensure proper organization of test data. Once we have a minimal set of images in our arsenal, we are ready to train our model.

![workflow](https://user-images.githubusercontent.com/36481036/135594695-dcba5d00-fc95-4ae8-abec-7d8d28ed54d5.png)

## :bulb: **STEPS FOLLOWED**
1. The first and the most important step was to import the tkinter package and the OrderedDict package.
2. Then we needed to define the notes that would help us to get a Note name from 0-11 INT.
3. After entering the name of the scales in a rotated sorted array, we return a scale of 16 notes.
4. Then we set the default scale and the offnote.
5. When the user wants to change the scale, we need to reset the window and redraw the table. And also highlight the tabs that must be played.
6. Until now we have created all the required fundamentals that will be the modules of the GUI. After this, we configure our main window.


## :white_check_mark: **HOW TO USE ?**
Import the code and in the command line type <code> python scale_chart_code.py> </code>

## :chart_with_upwards_trend: **ADVATANGES OF THE INTERFACE**
* It will be  easy way to create chromatic scales (without typing them explicitly). 
* We can play any scale we want to without having to google it all the time. 
* It will be very useful in teaching students in musical school. 
* Easy understanding and  learning of musical instruments is possible through this project.
* Common people can learn any musical instrument without attending any coaching or workshops.
* It will help to produce quality music.
* Combining music with high end programming technologies might help create a global impact on the music industry.

## :key: **PREQUISITES**
All the dependencies and required libraries are included in the file <code>requirements.txt</code> [See here](./requirements.txt)

## :round_pushpin: **CODE OUTPUTS**
<p align="center">
  <img width="600" height="300" src="https://user-images.githubusercontent.com/36481036/135593785-f8abbb1e-03fb-4176-aab9-e6e5eeba9600.png">

</p>


<p align="center">
  <img width="600" height="250" src="https://user-images.githubusercontent.com/36481036/135593790-730c662a-2926-4afb-a2f4-9a4bf7e27738.png">

</p>

<p align="center">
  <img width="3000" height="300" src="https://user-images.githubusercontent.com/36481036/135742600-16311aaa-5a85-4612-8c41-e3927fbf22f2.gif">

</p>

## :bust_in_silhouette: **CREDITS & REFERENCES**
* https://github.com/crawsome/GuitarScaleChart
* https://tkdocs.com/
* https://github.com/kevinadi/scales
* https://giphy.com/

**:sunglasses:** **CREATOR**- https://github.com/theshredbox





