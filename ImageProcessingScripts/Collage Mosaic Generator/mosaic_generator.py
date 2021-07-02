# Import the required files

import os, random, argparse
from PIL import Image
import imghdr
import numpy as np

#-----------------------------------------------------------------------------------

def Average(image):  # function to get the image width, heidht and dimension.
    
    im = np.array(image) # to get array of the image
    width,height,dimension = im.shape #shape of the image
    
    return tuple(np.average(im.reshape(width*height, dimension), axis=0)) # get average value

#-----------------------------------------------------------------------------------

def Split(image, size): # function to get row*column list of image
    
    Wid, Hei = image.size[0],image.size[1] 
    row, column = size
    w, h =int(Wid/column), int(Hei/row)

    img = [] # list of images

    for j in range(row): # generate list dimension
        for i in range(column):
            img.append(image.crop((i*w, j*h, (i+1)*w, (j+1)*h))) #append the croped image
    return img

#-----------------------------------------------------------------------------------

def Get(image_dir): # function to get list of image

    file = os.listdir(image_dir)
    images = [] # image list 

    for i in file: # path to the files
        filepath = os.path.abspath(os.path.join(image_dir, i))
        
        try:
            f = open(filepath, 'rb') # opening the file
            im = Image.open(f) # opening hte image
            images.append(im)
            im.load()  #loading the image from file
            f.close  # closing the file
        except:
            print("Invalid Image" , filepath)
            
    return images

#-----------------------------------------------------------------------------------
            
def Filename(image_dir): # function to get list of image file names

    file = os.listdir(image_dir)
    f_names = [] # ilst of file names

    for i in file: # path to the file
        filepath = os.path.abspath(os.path.join(image_dir, i))

        try:
            img_Type = imghdr.what(filepath)
            if img_Type:
                f_names.append(filepath)
        except:
            print("Invalid Image", filepath)

    return f_names

#-----------------------------------------------------------------------------------

def Match(i_avg, avgs): # function to get the image index to place the image

    avg = i_avg # average input

    ind = 0
    min_ind = 0
    min_dist = float("inf")

    for i in avgs:
        dist = ((i[0] - avg[0])*(i[0] - avg[0])+(i[1] - avg[1])*(i[1] - avg[1]) +
                            (i[2] - avg[2])*(i[2] - avg[2]))

        if dist < min_dist: #caluclate min distance
            min_dist = dist;
            min_ind = ind
            ind+=1

    return min_ind

#-----------------------------------------------------------------------------------

def Create(images, dims): # function to create grid for easy fitting images

    row, column = dims

    assert row*column == len(images)

    width = max([img.size[0] for img in images]) # maimum width
    height = max([img.size[1] for img in images]) # maimum height

    grid_img = Image.new('RGB', (column*width, row*height)) # formating output image

    
    for i in range(len(images)): # Fitting the images in the grid
            row = int(i/column)
            col = i - column*row
            grid_img.paste(images[i], (col*width, row*height))
	
    return grid_img

#-----------------------------------------------------------------------------------

def Mosaic(t_img, inp_img, grid_size, reuse=True): #Functtion to create photomosaic

    t_img = Split(t_img, grid_size) # Split function is used
    out_img = [] #output images

    c = 0
    b_size = int(len(t_img)/10)

    avgs = []
    for img in inp_img:
        avgs.append(Average(img))

    for img in t_img:
        avg = Average(img)
        
        match_index = Match(avg, avgs) # to find the matching index
        out_img.append(inp_img[match_index])

        if c > 0 and b_size > 10 and count % b_size is 0:
            c += 1
        if not reuse: #if flag set remove selected image
            inp_img.remove(match)
                
    mosaic_image = Create(out_img, grid_size)
    return mosaic_image

#-----------------------------------------------------------------------------------

def main():

    # parser arguments
    parser = argparse.ArgumentParser(description='Creates a photomosaic from input images')
    parser.add_argument('--target-image', dest='target_image', required=True)
    parser.add_argument('--input-folder', dest='input_folder', required=True)
    parser.add_argument('--grid-size', nargs=2, dest='grid_size', required=True)
    parser.add_argument('--output-file', dest='outfile', required=False)

    args = parser.parse_args()

    target_image = Image.open(args.target_image) # target the image

    input_image = Get(args.input_folder) # input image
    
    if input_image == []:
        print('No input images found in %s. Exiting.' % (args.input_folder, ))
        exit()

    random.shuffle(input_image)

    grid_size = (int(args.grid_size[0]), int(args.grid_size[1])) #Grid size
    
    output_filename = 'mosaic.png' # output image
    if args.outfile:
        output_filename = args.outfile

    reuse_images = True
    resize_input = True

    if not reuse_images:
        if grid_size[0]*grid_size[1] > len(input_image):
            exit()

    if resize_input:
        dims = (int(target_image.size[0]/grid_size[1]),int(target_image.size[1]/grid_size[0]))
       
    for img in input_image:
        img.thumbnail(dims)

        
    # creating mosaic images    
    mosaic_image = Mosaic(target_image, input_image, grid_size, reuse_images)

    mosaic_image.save(output_filename, 'PNG')

    # user understanding message
    print("saved output to %s" % (output_filename,))
    print('done.')

#-----------------------------------------------------------------------------------
     
if __name__ == '__main__':
    main()  # call the main program



            
