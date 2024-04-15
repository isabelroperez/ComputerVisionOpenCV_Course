# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:48:14 2024

@author: irodriguez
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('LECLREC.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"

#%% CONVOLUTION
kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()

#%% FILTERS
assert img is not None, "file could not be read, check with os.path.exists()"

blur = cv.blur(img,(5,5))

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

blur = cv.GaussianBlur(img,(5,5),5)
cv.imshow('Blurred Image', blur)
cv.waitKey(0)
cv.destroyAllWindows()

median = cv.medianBlur(img,5)
cv.imshow('Median Blur Image', median)
cv.waitKey(0)
cv.destroyAllWindows()

bilateral = cv.bilateralFilter(img,9,205,75)
cv.imshow('Bilateral Filter Image', bilateral)
cv.waitKey(0)
cv.destroyAllWindows()