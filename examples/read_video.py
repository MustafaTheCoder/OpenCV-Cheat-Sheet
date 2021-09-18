import cv2

# storing video in a variable
cap = cv2.VideoCapture("resources/example.mp4")

# runs the video
while True:
    success, img = cap.read()
    cv2.imshow("Output", img)
    # Breaks the program if the user pressed q
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break