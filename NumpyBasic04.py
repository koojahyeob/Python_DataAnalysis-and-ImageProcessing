# 보간법(Interpolation) : 새로 생기는 픽셀들을 나타내는 방법(중간값, 분포 따르기)
# 행렬의 곱 등 행렬의 기본 개념 파악
import cv2
import numpy as np

# 이미지 크기 변경
""" image = cv2.imread('cat.jpg')
cv2.imshow('Image', image)
cv2.waitKey(0)

#cv2.resize(image,dsize, fx, fy, interpolation)

#dsize : Manual Size
#fx = 가로 비율 // fy = 세로 비율
#interpolation : 보간법 // INTER_CUBIC : 사이즈 크게 / INTER_AREA : 사이즈 작게

크기 키우기
expand = cv2.resize(image, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)
cv2.imshow('Image',expand)
cv2.waitKey(0)

크기 줄이기
shrink = cv2.resize(image, None, fx=0.7, fy=0.7, interpolation=cv2.INTER_AREA)
cv2.imshow('Image', shrink)
cv2.waitKey(0) """
"----------------------------------------------------------------------------------"
""" # 이미지 위치 변경
# cv2.warpAffine(image, M, dsize)
# M : 변환 행렬
# dsize : Manual Size

image = cv2.imread('cat.jpg')

#행 과 열 정보만 저장
height, width = image.shape[:2]

M = np.float32([[1, 0, 200],[0, 1, 10]])
dst = cv2.warpAffine(image, M, (width, height))
cv2.imshow('Image', dst)
cv2.waitKey(0)
 """
"--------------------------------------------------------------------------------------"
""" # 이미지 회전
# cv2.getRotationMatrix2D(center, angle, scale)
# center : 회전 중심 // angle : 회전 각도 // scale : Scale Factor

image = cv2. imread('cat.jpg')

#행과 열 정보만 저장
height, width = image.shape[:2]

M = cv2.getRotationMatrix2D((width/2, height/2), 60, 0.5)
dst = cv2.warpAffine(image, M, (width, height))
cv2.imshow('Image', dst)
cv2.waitKey(0) """
