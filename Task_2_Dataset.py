import cv2
import numpy as np

cap = cv2.VideoCapture(0)
count = 1

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    cv2.imwrite("Img%d.jpg" %count, frame)
    cv2.waitKey(1)
    count += 1
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()