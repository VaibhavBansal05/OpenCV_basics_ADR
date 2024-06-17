import numpy as np
import cv2
from PIL import Image 

red = [0, 255, 255]  # Red in BGR colorspace
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 170, 70])
    upper_red = np.array([9, 255, 255])

    mask = cv2.inRange(hsvImage, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    kernel = np.ones((3,3),np.uint8)
    erosion = cv2.erode(res,kernel,iterations = 1)

    mask_ = Image.fromarray(erosion)
    
    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('frame', frame)
    #cv2.imshow('erode', erosion)
    #cv2.imshow('res', res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()