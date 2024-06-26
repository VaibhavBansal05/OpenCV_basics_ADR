import cv2
import numpy as np
 
img = cv2.imread("led.png")
 
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
 
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])
 
lower_purple = np.array([129, 50, 70])
upper_purple = np.array([158, 255, 255])
  
mask_red = cv2.inRange(hsv, lower_red, upper_red)
mask_purple = cv2.inRange(hsv, lower_purple, upper_purple)

contours_red, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours_purple, _ = cv2.findContours(mask_purple, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours_red:
    contour_area = cv2.contourArea(cnt)
    if contour_area > 50 and contour_area < 500:
        cv2.drawContours(img, contours_red, -1, (0, 0, 255), 2)
     
for cnt in contours_purple:
    contour_area = cv2.contourArea(cnt)
    if contour_area > 50 and contour_area < 500:
        cv2.drawContours(img, contours_purple, -1, (170, 30, 20), 2)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()