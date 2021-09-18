import cv2
import numpy as np

img = cv2.imread("resources/example.jpg")
kernal = np.ones((2, 2), np.uint8)

"""
What this function does it makes the edges of the functions thick 
so that the canny function can process them in a better way, and also
numpy is used here in the kernal variable to do that main part which is 
deciding the amount of thinkness needed for canny to process the lines of 
the edges in a better way
"""    
imgCanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgCanny, kernal)

# Displaying the output
cv2.imshow("Output", imgDialation)
# Adding delay to the image
cv2.waitKey(0)