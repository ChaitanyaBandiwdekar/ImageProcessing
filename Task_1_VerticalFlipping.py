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
        vflip = cv2.flip(frame, 0)
        cv2.imshow('frame', vflip)
        count = 0

    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()