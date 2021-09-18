import cv2

# storing video in a variable
cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

# runs the video
while True:
    success, img = cap.read()
    cv2.imshow("Output", img)
    # Breaks the program if the user pressed q
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break