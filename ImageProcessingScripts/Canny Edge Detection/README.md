<h1>Canny Edge Detection</h1>
<h2>Introduction</h2>
<p>The Canny edge detector is an edge detection operator that uses a multi-stage algorithm to detect a wide range of edges in images. 
  The Canny edge detector is arguably the most well known and the most used edge detector in all of computer vision and image processing.
  OpenCV provides method to seamlessly implement Canny edge detection over any images using <b>canny() method.</b>
  <p>
  The Canny edge detection algorithm is composed of 5 steps:</p>
  <ul>
  <li>Noise reduction</li>
  <li>Gradient calculation</li>
  <li>Non-maximum suppression</li>
  <li>Double threshold</li>
<li>Edge Tracking by Hysteresis.</li>
    </ul>
  </p>
  
  <h2>How does it work</h2>
  <p>
  <li>Input any images that you want to apply canny edge opeartion.</li>
  <li>Reading the input images</li>
  <li>Displaying original images</li>
  <li>Applying canny() method of OpenCV to detect edges of the input images</li>
  <li>Displaying the Output image after applying canny edge detection algorithm.</l
  </p>
  
  <h2>Let's Take a Look at the Sample output:</h2>
    <div>
    <b>Original Image</b>
    <p><img src="Images\flower.jpg" width=300 heigth=300/></p>
    <b>Canny Edge Detected Image</b>
    <p><img src="Images\demo1.PNG" width=300 height=300/></p>
    </div>
    
  <div>
    <b>Original Image</b>
    <p><img src="Images\flower1.jpg" width=300 heigth=300/></p>
    <b>Canny Edge Detected Image</b>
    <p><img src="Images\demo2.PNG" width=300 height=300/></p>
   </div>
      
