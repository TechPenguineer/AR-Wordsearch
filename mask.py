import cv2
import numpy as np 

def getColorMask(img):
    lowerBound = np.array([0,180,255])
    upperBound = np.array([255,255,255])
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    return cv2.inRange(hsv, lowerBound, upperBound)