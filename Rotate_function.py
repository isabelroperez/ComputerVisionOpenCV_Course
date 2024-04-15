# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:28:56 2024

@author: irodriguez
"""
import cv2

image = cv2.imread('image.jpg', 1)
cv2.imshow("Original", image)

# grab the dimensions of the image and calculate the center of the
# image
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

# rotate our image by 45 degrees around the center of the image
M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated_45 = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", rotated_45)

# rotate our image by -90 degrees around the image
M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
rotated_neg_90 = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", rotated_neg_90)

cv2.waitKey(0)
cv2.destroyAllWindows()