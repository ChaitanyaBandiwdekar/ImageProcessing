import cv2
import numpy as np 

cap = cv2.VideoCapture(0)
count = None

while True:
    ret, frame = cap.read()  
    cv2.imshow('frame', frame)
    
    #** Vertical flipping every 50 frames **
    if count==50 or count==None:
        vnflip = cv2.flip(frame, 0)
        cv2.imshow('flip', vnflip)
        cv2.waitKey(0)
        count = 0
    cv2.imshow('flip', frame)
    count += 1

    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()