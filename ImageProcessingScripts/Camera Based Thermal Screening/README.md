# Camera Based Thermal Screening

#### AIM:  
We will build a project that can help us in thermal screening for checking temperature using any image. This project can be done with the help of some libraries using Python programming.


#### PURPOSE: 

In this project we will be doing thermal screening based on the image taken from a video of thermal camera with the help of some libraries using Python programming.

#### DESCRIPTION:
The details of python libraries and how they are working is here- 

**LIBRARIES USED**
- **Numpy:** `numpy` forms the basis of powerful machine learning libraries like scikit-learn and SciPy. As machine learning grows, so does the list of libraries built on `numpy`. TensorFlow’s deep learning capabilities have broad applications — among them speech and image recognition, text-based applications, time-series analysis, and video detection. PyTorch, another deep learning library, is popular among researchers in computer vision and natural language processing.

- **OpenCV:** `opencv` is a library of programming functions mainly aimed at real-time computer vision. Originally developed by Intel, it was later supported by Willow Garage then Itseez. The library is cross-platform and free for use under the open-source Apache 2 License.

- **Matplotlib:** `matplotlib` is a plotting library for the Python programming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK.

#### INSTALLATION:
Install the following libraries using `pip` command in any terminal

```python
pip install numpy
pip install opencv-python
pip install matplotlib
```

#### WORKFLOW:

1. We are importing the required libraries 
2. Reading the image taken from a video of thermal camera
3. converting the image into grayscale, changing and applying the ColorMap, black and white to black and red
4. Then applying mask on the image
5. using function zeros_like() it will take all the structures like zero and then x, y, w, h are the coordinate for rectangle, copying the small rectangle part from this image using mask and then printing the average value of pixels to get the temperature
6. Now performing the bitwise and operator on heatmap and we have created not mask
7. After that draw rectangles for visualisation and write temperature for each rectangle, and finally display it
    
#### USAGE:

To start using this project, follow the below guidelines: 

**1.**  Fork this project/repository.

**2.**  Clone your forked copy of the project/repository.

```
git clone https://github.com/<your-github-username>/Awesome_Python_Scripts.git
```

**3.** Navigate to the project directory.

```
cd Awesome_Python_Scripts/Camera Based Thermal Screening/
```

**4.** Install the `requirements.txt` using the given command.

```
pip install -r requirements.txt
```

**5.** Run `camera_based_thermal_screening.ipynb` file in Google Colab or Jupyter Notebook or any other platform.

#### CONCLUSION:
We have created a project for thermal screening of any person using python with an image. And we have also learnt how to make such type of project for thermal screening, the output we got with this project is also attached here.

#### SCREENSHOTS:

**1. Initial Image**
<div align="center">

<img width="700" height="450" src="https://github.com/Umesh-01/Awesome_Python_Scripts/blob/patch-10/ImageProcessingScripts/Camera%20Based%20Thermal%20Screening/Images/thermal_scr_img.png">
</div>


**2. Final Output**
<div align="center">

<img width="700" height="450" src="https://github.com/Umesh-01/Awesome_Python_Scripts/blob/patch-10/ImageProcessingScripts/Camera%20Based%20Thermal%20Screening/Images/image_with_temp.png">
</div>


### Contributor
<a href="https://github.com/Umesh-01">Umesh Singh</a>
