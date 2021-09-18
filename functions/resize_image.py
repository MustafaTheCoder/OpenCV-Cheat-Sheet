import cv2
import numpy as np

img = cv2.imread("resources/example.jpg")

"""
What this function does is resizes the image with the given parameters

To check the current size of the image
print(img.shape)

Output:
(168, 300, 3) 

Here in this case 168 is the height, the second one is the width which is 168
and the last one is the color code which is 3

The first parameter here is the width which is 300, the height here is 168
"""
imgResize = cv2.resize(img, (500, 400))

# Displaying the output
cv2.imshow("Output", imgResize)
# Adding delay to the image
cv2.waitKey(0)
