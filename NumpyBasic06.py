# 이미지 임계점 처리하기
# cv2,threshold(image, thresh, max_value, type)
# 임계값을 기준으로 흑/백으로 분류하는 함수
# image : 처리할 Gray Scale 이미지
# thresh : 임계 값 (전체 픽셀 적용)
# max_value : 임계 값을 넘었을 때 적용할 값
# type : 임계점을 처리하는 방식

import cv2

image = cv2.imread('grey.png', cv2.IMREAD_GRAYSCALE)

images = []
ret, thres1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
ret, thres2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
ret, thres3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC) 
ret, thres4 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)
ret, thres5 = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)

# 밝기가 127 이상인 부분은 255(하얀색) 아닌 부분은 0(흑색)
images.append(thres1)
images.append(thres2)
images.append(thres3)
images.append(thres4)
images.append(thres5)

for i in images:
    cv2.imshow('Image', i)
    cv2.waitKey(0)
"------------------------------------------------------------------------------------"

# 이미지의 적응 임계점 처리
# 하나의 이미지에 다수의 조명 상태가 존재하는 경우 적용하면 좋다.

# cv2.adaptiveThreshold(image, max_value, adaptive_method, type, block_size, C) - 적응 임계점 처리 함수
# max_value : 임계 값을 넘었을 때 적용할 값 // adaptive_method : 임계 값을 결정하는 계산 방법 (자동)
# ADAPTIVE_THRESH_MEAN_C : 주변영역의 평균값 결정 // ADAPTIVE_THRESH_GAUSSIAN_C : 가우스 분포(정규 분포 흡사)
# type : 임계점을 처리하는 방식 // block_size : 임계 값을 적용할 영역의 크기 // C : 평균이나 가중 평균에서 차감할 값


import cv2
image = cv2.imread('grey.png', cv2.IMREAD_GRAYSCALE)

thres1 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 3)
thres2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 3)

cv2.imshow('Image', thres1)
cv2.waitKey(0)

cv2.imshow('Image', thres2)
cv2.waitKey(0)
