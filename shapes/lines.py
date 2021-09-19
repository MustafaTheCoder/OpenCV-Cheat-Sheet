import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)

"""
Now as you can see this concept is a little bit difficult to understand but lets break it 
into pieces the first parameter here is the image that will be used to draw a line on, the
second paramenter is the start point of the line, the third paramenter is the ending point 
of the line, after it the forth parameter is the color of the line, and the last one is the 
thickness of the line (Not Important)
"""
cv2.line(img, (0,0), (300,300), (255, 0, 0), 5)


# Displaying the output
cv2.imshow("Output", img)
# Adding delay to the image
cv2.waitKey(0)