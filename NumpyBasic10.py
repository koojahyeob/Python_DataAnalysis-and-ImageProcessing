# Contours 처리

# Contour의 사각형 외각 찾기
import cv2

image = cv2.imread('digit.png')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 230, 255, 0)
thresh = cv2.bitwise_not(thresh)
# 하얀색과 검은색 반전 시키는 것 (배경과 숫자)
cv2.imshow('Image', image)
cv2.waitKey(0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(image, contours, -1, (0, 0, 255), 4)
# B G R 순서로 빨간색 나옴 // 모든 contours 값 나타나게 함 -> -1 값 // 
cv2.imshow('Image', image)
cv2.waitKey(0)

contour = contours[0]
x, y , w, h = cv2.boundingRect(contour)
image = cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 3)
# 직사각형 테두리 만듦
cv2.imshow('Image', image)
cv2.waitKey(0)
"------------------------------------------------------------------"
# Contour의 Convex Hull
# cv2.convexHull(contour) : Convex Hull 알고리즘으로 외곽을 구하는 함수

contour = contours[0]
hull = cv2.convexHull(contour)
image = cv2.drawContours(image, [hull], -1, (255,0,0), 4)
cv2.imshow('Image', image)
cv2.waitKey(0)
"--------------------------------------------------------------------"
# Contour의 유사 다각형 구하기
# cv2.approxPolyDP(curve, epsilon, closed)  근사치 Contour 구하기
# curve : Contour // epsilon : 최대 거리 (클수록 Point 개수 감소) // closed : 폐곡선 여부

contour = contours[0]
epsilon = 0.001 * cv2.arcLength(contour, True)
# 입실론 값을 줄이면 줄일수록 원래의 CONTOUR와 유사한 모양으로 더 정교하게 나옴
approx = cv2.approxPolyDP(contour, epsilon, True)
image = cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)

cv2.imshow('Image', image)
cv2.waitKey(0)
"------------------------------------------------------------------------"
#Contour의 기본 정보
# cv2.contourArea(contour) : Contour의 면적 구하기
# cv2.arcLength(contour) : Contour의 둘레 구하기
# cv2.moments(contour) : Contour의 특징 추출

contour = contours[0]
area = cv2.contourArea(contour)
print(area)
length = cv2.arcLength(contour, True)
print(length)
M = cv2.moments(contour)
print(M)
