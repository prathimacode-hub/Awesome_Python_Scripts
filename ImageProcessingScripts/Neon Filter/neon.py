import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    filename = input("Please Enter File Name : ")  # Asking Image name
    newfilename = "Media/" + filename  # Accessing Image inside "Media" folder
    img = cv2.imread(newfilename)
    param_resize = 2000

    # Resize based on the parameters
    img = cv2.resize(img, (param_resize, param_resize))

    # Gausian
    gaussian = cv2.GaussianBlur(img,(3,3),1)

    # Split the gausian and the orginal image
    b_gaus,g_gaus,r_gaus=cv2.split(gaussian)
    b,g,r=cv2.split(img)

    # Matrix multiplication
    #When reading in with cv2 then the type is uint8, which means the range is max 255
    calculated_b_array = b_gaus.astype(int) + b.astype(int)
    calculated_g_array = g_gaus.astype(int) + g.astype(int)
    calculated_r_array = r_gaus.astype(int) + r.astype(int)

    ## If the pixelvalue is higher than 255, set it to 255
    calculated_b_array[calculated_b_array > 255] = 255
    calculated_g_array[calculated_g_array > 255] = 255
    calculated_r_array[calculated_r_array > 255] = 255

    ## Merge for visualization purposes
    merged = cv2.merge([calculated_b_array, calculated_g_array, calculated_r_array])
    img2 = np.concatenate((img, merged), axis=1)

    # After doing this write the image to the folder
    cv2.imwrite(f"Neon of {filename}", img2)
    print(f"Neon of {filename} is created")  # Display message
    cv2.waitKey(0)


if __name__ == "__main__":
    main()