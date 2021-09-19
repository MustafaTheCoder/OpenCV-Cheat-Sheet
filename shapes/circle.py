import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)

"""
This concept is slightly different from the other shapes in the first parameters comes the center point of the
circle, then comes the radius of the circle, then next comes the color and in the last comes the thickness 

To fill the circle you can just do
cv2.circle(img, (255,255), 30, (255,0,0), cv2.FILLED)
"""    
cv2.circle(img, (255,255), 30, (255,0,0), 5)

# Displaying the output
cv2.imshow("Output", img)
# Adding delay to the image
cv2.waitKey(0)