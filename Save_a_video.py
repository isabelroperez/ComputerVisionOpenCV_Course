# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:34:08 2024

@author: irodriguez
"""
import cv2

cap = cv2.VideoCapture('SampleVideo.mp4')

while (cap.is0pened()):
    ret, frame =cap.read()
    cv2.imshow("vid", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()