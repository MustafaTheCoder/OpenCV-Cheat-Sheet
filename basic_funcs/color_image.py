import cv2

img = cv2.imread("resources/example.jpg")

"""
Converts your image into a different color format, it takes
2 parameters the first one is the image you want to convert 
and the second one the color code you want to use for your
image

In this case we are making the image gray so we will use the
gray namespace from the opencv package.
"""
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Displaying the output
cv2.imshow("Output", imgGray)
# Adding delay to the image
cv2.waitKey(0)