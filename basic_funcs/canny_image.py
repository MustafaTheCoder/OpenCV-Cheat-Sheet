import cv2

img = cv2.imread("resources/example.jpg")

"""
This function takes 2 parameters the first one is the image
you want to blur the second one is the amount of blur you 
want to apply to the image.

Kernal Size = Blur Amount
(Ignore the last parameter it is not that important)
"""    
imgCanny = cv2.Canny(img, 150, 200)

# Displaying the output
cv2.imshow("Output", imgBlur)
# Adding delay to the image
cv2.waitKey(0)