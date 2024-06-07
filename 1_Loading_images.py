import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)
#   IMREAD_GRAYSCALE
#   IMREAD_UNCHANGED
#   cv2.imshow('image',img)
#   cv2.waitKey(0)
#   cv2.destroyAllWindows()
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.plot([75,150],[50,100],'c', linewidth=5)
plt.show()