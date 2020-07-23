import cv2
import numpy as np

def nothing(x):
    return 0

cap = cv2.VideoCapture(0)
cv2.namedWindow('HSV')

cv2.createTrackbar('Hue Low', 'HSV', 0, 180, nothing)
cv2.createTrackbar('Hue High', 'HSV', 0, 180, nothing)

cv2.createTrackbar('Saturation Low', 'HSV', 0, 255, nothing)
cv2.createTrackbar('Saturation High', 'HSV', 0, 255, nothing)

cv2.createTrackbar('Value Low', 'HSV', 0, 255, nothing)
cv2.createTrackbar('Value High', 'HSV', 0, 255, nothing)

while True:
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hl = cv2.getTrackbarPos('Hue Low', 'HSV')
    sl = cv2.getTrackbarPos('Saturation Low', 'HSV')
    vl = cv2.getTrackbarPos('Value Low', 'HSV')

    hh = cv2.getTrackbarPos('Hue High', 'HSV')
    sh = cv2.getTrackbarPos('Saturation High', 'HSV')
    vh = cv2.getTrackbarPos('Value High', 'HSV')

    lower = np.array([hl, sl, vl])
    upper = np.array([hh, vh, sh])

    mask = cv2.inRange(hsv, lower, upper)
    des = cv2.bitwise_and(frame, frame, mask=mask)

    x, y, w, h = cv2.boundingRect(mask)
    cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

    cv2.imshow('frame', frame)
    cv2.imshow('HSV', des)

    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()