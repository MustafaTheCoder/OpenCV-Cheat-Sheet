import cv2

# storing image in a variable
img = cv2.imread("resources/example.jpg")

# showing the image
cv2.imshow("Output", img)
# stopping the gui from getting disappered by adding a delay
cv2.waitKey(0)