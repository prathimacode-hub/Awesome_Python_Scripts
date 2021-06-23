import numpy as np
import matplotlib.pyplot as plt

def rgb2gray(rgb_img):
    "convert an RGB image into single channel grayscale image"
    r, g, b = rgb_img[:, :, 0], rgb_img[:, :, 1], rgb_img[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray


def histogram_equalization(img):
    """mapping of a low contrast histogram into one with high contrast
     using the cummulative distribution function(cdf)"""
    img = rgb2gray(img).astype('int')
    #transform the image into 1D for better performance
    img_1D = img.ravel()
    hist, _ = np.histogram(img_1D, 256, density=True)
    bins = np.array(range(256))
    histNorm = hist/hist.size
    cdf = (histNorm.cumsum()*255**2).astype('int')
    output = np.zeros(img.size)
    #mapping of each pixel into better contrast hist
    for i in range(img.size):
        output[i] = cdf[img_1D[i]]
    output = np.reshape(output, img.shape)
    return output

def show_images(img, output):
    """compare the input and output images"""
    plt.figure()
    plt.subplot(121), plt.imshow(img, cmap='gray'), plt.title('original image'), plt.axis('off')
    plt.subplot(122), plt.imshow(output, cmap='gray'), plt.title('contrast enhancement img'), plt.axis('off')
    plt.show()

if __name__ == '__main__':
    img = plt.imread('images/lumbar_spine.jpg')
    output = histogram_equalization(img)
    show_images(img, output)
