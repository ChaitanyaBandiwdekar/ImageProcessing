import cv2
import numpy as np 

cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    
    if count==0:
        cv2.imshow('frame', frame)
        count = 1
    
    else:
        hflip = cv2.flip(frame, 1)
        cv2.imshow('frame', hflip)
        count = 0

    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()