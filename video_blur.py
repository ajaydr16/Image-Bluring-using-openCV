import numpy
import cv2

face_cascade = cv2.CascadeClassifier('train.xml')

cap = cv2.VideoCapture(0)

blurred = False
framed = False

while True: 

    temp, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        if blurred:
            frame[y:(y + h), x:(x + w)] = cv2.blur(frame[y:(y + h), x:(x + w)], (25, 25))
        if framed:
            cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (0, 0, 255), 2)

    cv2.imshow('Video', frame)
    ch = 0xFF & cv2.waitKey(1)
    if ch == ord("b"):
        blurred = not blurred

    if ch == ord("f"):
        framed = not framed

    if ch == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
