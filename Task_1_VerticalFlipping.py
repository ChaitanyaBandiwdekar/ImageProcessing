import cv2
import numpy as np 

cap = cv2.VideoCapture(0)
count = None

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    
    # **Vertically flipped frame**
    vflip = cv2.flip(frame, 0)
    cv2.imshow('vflip', vflip)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()