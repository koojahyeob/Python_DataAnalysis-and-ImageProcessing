# OpenCV Filtering
# 이미지에 커널을 적용하여 이미지를 흐리게(Blurring = Smoothing) 처리
# 이미지 흐리게 -> 노이즈 및 손상 줄임

# Basic Kernel 5x5 가중치 1/25
# Gaussian Kernel (항상 홀수) 5x5 1/273 41 26 16 7 4 1 순서

import cv2
import numpy as np

image = cv2.imread('grey.png')
cv2.imshow('Image', image)
cv2.waitKey(0)

size = 4
kernel = np.ones((size, size), np.float32) / (size ** 2)
print(kernel)

# filter2D 함수와 blur 함수 동일
dst = cv2.filter2D(image, -1, kernel) #destination
cv2.imshow('Image', dst)
cv2.waitKey(0) 
"------------------------------------------------------------------"
dst = cv2.blur(image, (4,4))
cv2.imshow('Image', dst)
cv2.waitKey(0)

#kernel_size : 홀수 
dst = cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow('Image', dst)
cv2.waitKey(0)
