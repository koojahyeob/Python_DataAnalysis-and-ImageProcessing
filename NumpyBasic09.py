#Contours 찾기 ( 외곽 ) 
#cv2.findContours(image, mode, method) : 이미지에서 윤곽 테두리 찾기
# mode : Contour 들을 찾는 방법


#cv2.drawContours(image, contours, contour_index, color, thickness) : Contour들을 그리는 함수
# contour_index : 그리고자 하는 Contours Line (전체 : -1)

import cv2 
# import matplotlib.pyplot as plt
image = cv2.imread("contours_image.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 127, 255, 0)

cv2.imshow('Image', thresh)
cv2.waitKey(0)
#계층
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(contours)

image = cv2.drawContours(image, contours, -1, (0,0,255), 3)

cv2.imshow('Image', image)
cv2.waitKey(0)