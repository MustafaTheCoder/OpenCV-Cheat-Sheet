import cv2

img = cv2.imread("resources/example.jpg")

cv2.imshow("Output", img)
cv2.waitKey(0)