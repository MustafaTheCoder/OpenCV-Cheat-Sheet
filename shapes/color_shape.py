import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)

print(img.shape) # to check the measurements of the image


"""
The part below shown is done because it defines the area that you want to be colored and the
color it self.
"""
img[0:200, 300:400] = 255, 0, 0 


# Displaying the output
cv2.imshow("Output", img)
# Adding delay to the image
cv2.waitKey(0)