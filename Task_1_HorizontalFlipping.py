import cv2
import numpy as np 

cap = cv2.VideoCapture(0)
count = None

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    
    # **Horizontally flipped frame**
    hflip = cv2.flip(frame, 1)
    cv2.imshow('hflip', hflip)

    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()