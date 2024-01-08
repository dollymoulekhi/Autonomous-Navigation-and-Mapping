## Importing libraries
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2


## reading image
image_name = 'C:/Users/dolly/OneDrive/Desktop/example_grid1.jpg'
image = mpimg.imread(image_name)


# Define a function to perform a color threshold for making all the values below threshold to zero and rest to 1
def color_thresh(image, rgb_thresh=(0, 0, 0)):
    color_select=np.zeros_like(image[:,:,0])
    above_tresh= ((image[:,:,0]> rgb_thresh[0]) &  (image[:,:,1]> rgb_thresh[1]) &  (image[:,:,2]> rgb_thresh[2]))

    color_select[above_tresh]=1
    return color_select


## defination of the function

def perspect_transform(image, source, dst):
    transform_mat = cv2.getPerspectiveTransform(source, dst)
    destination_image = cv2.warpPerspective(image, transform_mat, (image.shape[1], image.shape[0]))
    return destination_image


def rover_coords(binary_img):
    # Identify nonzero pixels
    ypos, xpos = binary_img.nonzero()
    # Calculate pixel positions with reference to the rover position being at the 
    # center bottom of the image.  
    x_pixel = np.absolute(ypos - binary_img.shape[0]).astype(float)
    y_pixel = -(xpos - binary_img.shape[0]).astype(float)
    return x_pixel, y_pixel


    
## calling of the function
red_threshold = 160
green_threshold = 160
blue_threshold = 160

rgb_threshold = (red_threshold, green_threshold, blue_threshold)


colorsel = color_thresh(image, rgb_thresh=rgb_threshold)




dst_size = 5 
bottom_offset = 6
source = np.float32([[14, 140], [301 ,140],[200, 96], [118, 96]])
destination = np.float32([[image.shape[1]/2 - dst_size, image.shape[0] - bottom_offset],
                  [image.shape[1]/2 + dst_size, image.shape[0] - bottom_offset],
                  [image.shape[1]/2 + dst_size, image.shape[0] - 2*dst_size - bottom_offset], 
                  [image.shape[1]/2 - dst_size, image.shape[0] - 2*dst_size - bottom_offset],
                  ])