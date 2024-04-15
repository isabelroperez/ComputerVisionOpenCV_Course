# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:39:24 2024

@author: irodriguez
"""

import cv2

# Loading the image named test.jpg
img = cv2.imread(r"LECLREC.jpg")
# Converting color mode to Grayscale
# as thresholding requires a single channeled image
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Thresholding the image placing 127 intensity level as threshold
# Pixel values below 127 would be changed to Black
# Pixel values above 127 would be changed to White (255)
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# Displaying the output image
cv2.imshow('Binary Threshold', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()


ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# Displaying the output image
cv2.imshow('Binary Inverse Threshold', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
# Displaying the output image
cv2.imshow('Truncate Threshold', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
# Displaying the output image
cv2.imshow('Truncate Threshold', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
# Displaying the output image
cv2.imshow('Truncate Threshold', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()