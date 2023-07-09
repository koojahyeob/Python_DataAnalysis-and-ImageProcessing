#Tracker
# cv2.createTrackbar(track_bar_name, window_name, value, count, on_change)
# value : 초기값 // count : max값 (min = 0) // on_change : 값 변경시 호출되는 callback 함수


import cv2
import numpy as np

def change_color(x):
    r = cv2.getTrackbarPos("R", "Image")
    g = cv2.getTrackbarPos("G", "Image")
    b = cv2.getTrackbarPos("B", "Image")
    image[:] = [b,g,r]
    cv2.imshow("Image", image)

image = np.zeros((600, 600, 3), np.uint8)
cv2.namedWindow("Image")

cv2.createTrackbar("R", "Image", 0 , 255, change_color)
cv2.createTrackbar("G", "Image", 0 , 255, change_color)
cv2.createTrackbar("B", "Image", 0 , 255, change_color)

cv2.imshow('Image', image)
cv2.waitKey(0)