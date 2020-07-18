import cv2
import numpy as np 
import time

cap = cv2.VideoCapture(0)

while True:
    start = time.time()

    while time.time()-start<=4:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(1)

    start = time.time()
    while time.time()-start<=1:
        ret, frame = cap.read()
        flip = cv2.flip(frame, 0)
        cv2.imshow('frame', flip)
        cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
