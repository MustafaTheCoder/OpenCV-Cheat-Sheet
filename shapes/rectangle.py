import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)

"""
As you can see this concept is the same as the lines one
"""    
cv2.rectangle(img, (0,0), (300,300), (255,0,0), 5) 


# Displaying the output
cv2.imshow("Output", img)
# Adding delay to the image
cv2.waitKey(0)