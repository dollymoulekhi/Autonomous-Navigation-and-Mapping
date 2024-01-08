## Importing libraries
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

## reading image
image_name = 'C:/Users/dolly/OneDrive/Desktop/example_grid1.jpg'
image = mpimg.imread(image_name)


# Define a function to perform a color threshold for making all the values below threshold to zero and rest to 1
def color_thresh(image, rgb_thresh=(0, 0, 0)):
    color_select=np.zeros_like(image[:,:,0])
    above_tresh= ((image[:,:,0]> rgb_thresh[0]) &  (image[:,:,1]> rgb_thresh[1]) &  (image[:,:,2]> rgb_thresh[2]))

    color_select[above_tresh]=1
    return color_select
    
red_threshold = 160
green_threshold = 160
blue_threshold = 160

rgb_threshold = (red_threshold, green_threshold, blue_threshold)


colorsel = color_thresh(image, rgb_thresh=rgb_threshold)




###############################################################################
def perspect_transform(image, source, dst):
    transform_mat = cv2.getPerspectiveTransform(source, dst)
    destination_image = cv2.warpPerspective(image, transform_mat, (320, 160))
    return destination_image


dst_size = 5 
bottom_offset = 6


source = np.float32([[14, 140], [301 ,140],[200, 96], [118, 96]])
destination = np.float32([[image.shape[1]/2 - dst_size, image.shape[0] - bottom_offset],
                  [image.shape[1]/2 + dst_size, image.shape[0] - bottom_offset],
                  [image.shape[1]/2 + dst_size, image.shape[0] - 2*dst_size - bottom_offset], 
                  [image.shape[1]/2 - dst_size, image.shape[0] - 2*dst_size - bottom_offset],
                  ])


warped=perspect_transform(image, source, destination)


cv2.polylines(image, np.int32([source]), True, (0, 0, 255), 3)
cv2.polylines(warped, np.int32([destination]), True, (0, 0, 255), 3)



f, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 6), sharey=True)
f.tight_layout()
ax1.imshow(image)
ax1.set_title('Original Image', fontsize=40)

ax2.imshow(warped, cmap='gray')
ax2.set_title('Result', fontsize=40)
plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)

###############################################################################


# Display the original image and binary               
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(21, 7), sharey=True)
f.tight_layout()
ax1.imshow(image)
ax1.set_title('Original Image', fontsize=40)

ax2.imshow(colorsel, cmap='gray')
ax2.set_title('Your Result', fontsize=40)
plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)
plt.show()