import cv2
import numpy as np

# def nothing(x):
#     return 0

cap = cv2.VideoCapture(0)
#cv2.namedWindow('HSV')

# cv2.createTrackbar('Hue Low', 'HSV', 0, 180, nothing)
# cv2.createTrackbar('Hue High', 'HSV', 0, 180, nothing)

# cv2.createTrackbar('Saturation Low', 'HSV', 0, 255, nothing)
# cv2.createTrackbar('Saturation High', 'HSV', 0, 255, nothing)

# cv2.createTrackbar('Value Low', 'HSV', 0, 255, nothing)
# cv2.createTrackbar('Value High', 'HSV', 0, 255, nothing)

_, Main = cap.read()

while True:
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # hl = cv2.getTrackbarPos('Hue Low', 'HSV')
    # sl = cv2.getTrackbarPos('Saturation Low', 'HSV')
    # vl = cv2.getTrackbarPos('Value Low', 'HSV')

    # hh = cv2.getTrackbarPos('Hue High', 'HSV')
    # sh = cv2.getTrackbarPos('Saturation High', 'HSV')
    # vh = cv2.getTrackbarPos('Value High', 'HSV')

    # lower = np.array([hl, sl, vl])
    # upper = np.array([hh, vh, sh])

    lower = np.array([0, 65, 0])
    upper = np.array([30, 255, 255])
    kernel = np.ones((5,5), np.uint8)

    mask = cv2.inRange(hsv, lower, upper)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    des = cv2.bitwise_and(frame, frame, mask=closing)

    inv = cv2.bitwise_not(closing)

    fg = cv2.bitwise_and(Main, Main, mask = closing)
    bg = cv2.bitwise_and(frame, frame, mask = inv)

    res = fg + bg

    # _, contours, _ = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame, contours, -1, (0,255,0), 2)

    cv2.imshow('frame', frame)
    #cv2.imshow('HSV', des)
    cv2.imshow('res', res)

    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()