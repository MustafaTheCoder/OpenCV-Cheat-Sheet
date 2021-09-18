import cv2
import numpy as np

img = cv2.imread("resources/example.jpg")
kernal = np.ones((5, 5), np.uint8)

"""
What this function does it makes the edges of the picture thin, it 
is like the opposite of the dialation function
"""    
imgCanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgCanny, kernal)
imgEroded = cv2.erode(imgDialation, kernal)

# Displaying the output
cv2.imshow("Output", imgEroded)
# Adding delay to the image
cv2.waitKey(0)