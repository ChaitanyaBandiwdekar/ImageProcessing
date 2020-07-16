import cv2
import numpy as np 

cap = cv2.VideoCapture(0)
count = None

while True:
    ret, frame = cap.read()
    
    # ** Thought of flipping as rotation, and did not knew about the flip function **
    # lst = frame.shape
    # rows = lst[0]
    # cols = lst[1]
    # M = cv2.getRotationMatrix2D((rows/2,cols/2), 180, 1)
    # dst = cv2.warpAffine(frame,M,(cols,rows))
    # cv2.imshow('flip', dst)
    
    cv2.imshow('frame', frame)
    
    #** Vertical flipping every 50 frames **
    if count==50 or count==None:
        vnflip = cv2.flip(frame, 0)
        cv2.imshow('flip', vnflip)
        cv2.waitKey(0)
        count = 0
    cv2.imshow('flip', frame)
    count += 1

    # **Vertically flipped frame**
    vflip = cv2.flip(frame, 0)
    cv2.imshow('vflip', vflip)
    
    # **Horizontally flipped frame**
    hflip = cv2.flip(frame, 1)
    cv2.imshow('hflip', hflip)


    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()