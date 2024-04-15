# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:47:07 2024

@author: irodriguez
"""

import cv2
import numpy as np

# img =cv2.imread('image.jpg', 1)
# img =cv2.imwrite('image.png', img)
# cv2.imshow('Original', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

pic= np.zeros((500,500,3), dtype = 'uint8')
cv2.rectangle(pic, (0,0), (500, 150), (123, 200 , 98), 3, lineType=8, shift=0)

cv2.line(pic, (350,350), (500, 350), (0, 0 , 255))



color= (255, 0, 255)
cv2.circle(pic, (250, 250),50, color)

font= cv2.FONT_HERSHEY_DUPLEX
cv2.putText(pic, "udemy", (100, 100), font, 3, (255, 255, 255),4 , cv2.LINE_8)
cv2.imshow('dark', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()