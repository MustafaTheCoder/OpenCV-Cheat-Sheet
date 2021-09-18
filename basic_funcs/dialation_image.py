import cv2
import numpy as np

img = cv2.imread("resources/example.jpg")
kernal = np.ones((5, 5), np.uint8)

"""
What this function does it like sketches the whoel picture
and returns it

This function takes 3 parameters the first one is the image
you want to apply canny on the second one is the threshold1
and the third one is threshold2
"""    
imgDialation = cv2.dilate(img, kernel)
# Displaying the output
cv2.imshow("Output", imgCanny)
# Adding delay to the image
cv2.waitKey(0)