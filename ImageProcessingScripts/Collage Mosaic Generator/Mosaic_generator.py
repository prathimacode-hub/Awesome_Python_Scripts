# Import the required files

import os, random, argparse
from PIL import Image
import imghdr
import numpy as np

#-----------------------------------------------------------------------------------

def Average(image):
    
    im = np.array(image)
    width,height,dimension = im.shape
    
    return tuple(np.average(im.reshape(width*height, dimension), axis=0))

# ----------------------------------------------------------------------------------

def Split(image, size):
    
    Wid, Hei = image.size[0],image.size[1]
    row, column = size
    w, h =int(Wid/column), int(Hei/row)

    img = []

    for j in range(row):
        for i in range(column):
            img.append(image.crop((i*w, j*h, (i+1)*w, (j+1)*h)))
    return img

#-----------------------------------------------------------------------------------

def Get(image_dir):

    file = os.listdir(image_dir)
    images = []

    for i in file:
        filepath = os.path.abspath(os.path.join(image_dir, i))

        try:
            f = open(filepath, 'rb')
            im = Image.open(f)
            images.append(im)
            im.load()
            f.close
        except:
            print("Invalid Image" , filepath)
            
    return images

#-----------------------------------------------------------------------------------
            
def Filename(image_dir):

    file = os.listdir(image_dir)
    f_names = []

    for i in file:
        filepath = os.path.abspath(os.path.join(image_dir, i))

        try:
            img_Type = imghdr.what(filepath)
            if img_Type:
                f_names.append(filepath)
        except:
            print("Invalid Image", filepath)

    return f_names

#-----------------------------------------------------------------------------------

def Match(i_avg, avgs):

    avg = i_avg

    ind = 0
    min_ind = 0
    min_dist = float("inf")

    for i in avgs:
        dist = ((i[0] - avg[0])*(i[0] - avg[0])+(i[1] - avg[1])*(i[1] - avg[1]) +
                            (i[2] - avg[2])*(i[2] - avg[2]))

        if dist < min_dist:
            min_dist = dist;
            min_ind = ind
            ind+=1

    return min_ind

#-----------------------------------------------------------------------------------

def Create(images, dims):

    row, column = dims

    assert row*column == len(images)

    width = max([img.size[0] for img in images])
    height = max([img.size[1] for img in images])

    grid_img = Image.new('RGB', (column*width, row*height))

    
    for i in range(len(images)):
            row = int(i/column)
            col = i - column*row
            grid_img.paste(images[i], (col*width, row*height))
	
    return grid_img

#-----------------------------------------------------------------------------------

def Mosaic(t_img, inp_img, grid_size, reuse=True):

    t_img = Split(t_img, grid_size)
    out_img = []

    c = 0
    b_size = int(len(t_img)/10)

    avgs = []
    for img in inp_img:
        avgs.append(Average(img))

    for img in t_img:
        avg = Average(img)
        
        match_index = Match(avg, avgs)
        out_img.append(inp_img[match_index])

        if c > 0 and b_size > 10 and count % b_size is 0:
            c += 1
        if not reuse:
            inp_img.remove(match)
                
    mosaic_image = Create(out_img, grid_size)
    return mosaic_image

#-----------------------------------------------------------------------------------

def main():

    parser = argparse.ArgumentParser(description='Creates a photomosaic from input images')
    parser.add_argument('--target-image', dest='target_image', required=True)
    parser.add_argument('--input-folder', dest='input_folder', required=True)
    parser.add_argument('--grid-size', nargs=2, dest='grid_size', required=True)
    parser.add_argument('--output-file', dest='outfile', required=False)

    args = parser.parse_args()

    target_image = Image.open(args.target_image)

    input_image = Get(args.input_folder)
    
    if input_image == []:
        print('No input images found in %s. Exiting.' % (args.input_folder, ))
        exit()

    random.shuffle(input_image)

    grid_size = (int(args.grid_size[0]), int(args.grid_size[1]))
    
    output_filename = 'mosaic.png'
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
        
    mosaic_image = Mosaic(target_image, input_image, grid_size, reuse_images)

    mosaic_image.save(output_filename, 'PNG')
    print("saved output to %s" % (output_filename,))
    print('done.')

#-----------------------------------------------------------------------------------
     
if __name__ == '__main__':
    main()



            
