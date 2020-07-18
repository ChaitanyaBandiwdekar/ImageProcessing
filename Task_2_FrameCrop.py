import cv2
import numpy as np 

cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    rows, cols, ch = frame.shape
    roi = frame[rows//2-50:rows//2+50, cols//2-50:cols//2+50]
    
    if count==0:
        cv2.imshow('frame', frame)
        count = 1
    
    else:
        cv2.imshow('frame', roi)
        count = 0

    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()