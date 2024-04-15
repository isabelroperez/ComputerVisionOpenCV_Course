# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:09:01 2024

@author: irodriguez
"""

import cv2 as cv
from matplotlib import pyplot as plt
 
img = cv.imread('LECLREC.jpg')
cv.imshow("Original", img)
cv.waitKey(0)
cv.destroyAllWindows()

assert img is not None, "file could not be read, check with os.path.exists()"
edges = cv.Canny(img,100,200)
cv.imshow('Edges Image', edges)
cv.waitKey(0)
cv.destroyAllWindows()

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
 
plt.show()
