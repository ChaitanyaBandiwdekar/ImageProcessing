import cv2
import numpy as np

entered = True
top = []
bottom = []

def roi(event, x, y, flags, param):
    global top, bottom, entered

    if event == cv2.EVENT_LBUTTONDOWN and entered:
        top.append(y)
        top.append(x)
        entered = False

    if event == cv2.EVENT_LBUTTONUP:
        bottom.append(y)
        bottom.append(x)

cap = cv2.VideoCapture(0)
cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame', roi)
taken = True

while True:
    _, frame = cap.read()
    
    if len(top)==2 and len(bottom)==2: 
        if taken:
            template = frame[top[0]:bottom[0], top[1]:bottom[1]]
            template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
            _, w, h = template.shape[::-1]
            taken = False
    
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        res = cv2.matchTemplate(gray,template_gray,cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.95)

        for pt in zip(*loc[::-1]):
            cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0,255,0), 1)
            cv2.putText(frame, 'Smile', pt, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)
        
    cv2.imshow('Frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
