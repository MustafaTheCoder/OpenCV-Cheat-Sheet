import cv2

img = cv2.imread("resources/example.jpg")

"""
What this function does it like sketches the whoel picture
and returns it

This function takes 3 parameters the first one is the image
you want to apply canny on the second one is the threshold1
and the third one is threshold2
"""    
imgCanny = cv2.Canny(img, 150, 200)

# Displaying the output
cv2.imshow("Output", imgBlur)
# Adding delay to the image
cv2.waitKey(0)