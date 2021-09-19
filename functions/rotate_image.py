import cv2

img = cv2.imread("resources/example.jpg")

imgRotate = cv2.rotate(img, cv2.ROTATE_180)

cv2.imshow("Output", imgRotate)
cv2.waitKey(0)