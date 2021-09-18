import cv2
import numpy as np

img = cv2.imread("resources/example.jpg")

"""
What this function does is crops the specific part of the image that was provided
in the parameters

We don't need any cv2 function for this as we can do this manually in a very easy way
"""
imgCrop = img[0:400, 100:300]

# Displaying the output
cv2.imshow("Output", imgCrop)
# Adding delay to the image
cv2.waitKey(0)
