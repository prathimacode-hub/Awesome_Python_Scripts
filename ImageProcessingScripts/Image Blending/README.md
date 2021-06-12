
<h1>Image Blending</h1>
<div>
  <h2>Description</h2>
  <p> Image Blending is an image processing technique where in two input images are mixed together.
    The output image is a combination of the corresponding pixel values of the input images.
    OpenCV is a very mature library and contains many out-of-the-box image processing algorithms.Image Blending can be seamlessly done using OpenCv wherein different weights are given to images so that it gives a feeling of blending or transparency.The function that is used for this is <b>The addWeighted() function</b>.
  </p>
  <p>OpenCV-Python uses the <b>addWeighted() function</b> to blend images. The function and its parameters are as follows.
    <pre>cv.addWeighted(src1,alpha, src2, beta, gamma[, dst[, dtype]])</pre>
  <ul>
    <li>src1- first input array.</li>
    <li>alpha- weight of the first array elements.</li>
    <li>src2- second input array</li>
    <li>beta- weight of second array elements</li>
  <li>gamma- scalar added to each sum.
    and two optional arguments which are not required for this demonstration.</li></ul>
  </p>
  
  </div>
  
  <div>
  </div>
