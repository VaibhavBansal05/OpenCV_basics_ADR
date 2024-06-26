import numpy as np
import cv2

img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)

#   Drawing a line
cv2.line(img,(0,0),(150,150),(255,255,0),7)
# blue = (225,0,0)
# green = (0,255,0)
# black = (0,0,0)

#   Drawing a reactangle
cv2.rectangle(img,(15,25),(200,150),(0,0,255),5)

# Drawing a circle
cv2.circle(img,(50,50), 50, (0,0,0), -1)

# Polygon
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV Text...',(10,130), font, 1.25, (255,255,255), 2, cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()