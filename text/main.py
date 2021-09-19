import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)

"""
Here we have in the first parameter is the image you want to apply text on, then the second
one is the thing you want to be in your text, the third is the location of you text ub the gui,
the forth one is the font you want to use , the fifth one is the font scale, and the sixth one 
is the color of the font, then the last one is the thinkness of the font

- The font scale can also be in decimal points
"""
cv2.putText(img, "TEST", (300, 100), cv2.FONT_ITALIC, 1, (255,0,0), 2)

# Displaying the output
cv2.imshow("Output", img)
# Adding delay to the image
cv2.waitKey(0)