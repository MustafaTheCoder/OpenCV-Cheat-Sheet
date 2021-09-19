import cv2

img = cv2.imread("resources/example.jpg")


imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)



cv2.imshow('Output', imgHSV)
cv2.waitKey(0)