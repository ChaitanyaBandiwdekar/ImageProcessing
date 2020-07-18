import cv2
import numpy as np 
import time

cap = cv2.VideoCapture(0)

start = time.time()
while True:
    ret, frame = cap.read()  
    cv2.imshow('frame', frame)
    
    if int(time.time()-start)%4==0:
        vnflip = cv2.flip(frame, 0)
        cv2.imshow('frame', vnflip)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()