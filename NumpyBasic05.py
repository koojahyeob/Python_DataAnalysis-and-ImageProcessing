# 이미지 합치기
# case1 : cv2.add() : Saturation 연산 수행
# -> 0보다 작으면 0, 255보다 크면 255로 표현
# case2 : np.add() : Modulo 연산 수행
# -> 256은 0, 257은 1로 표현 Modulo는 나머지 의미 256%256 = 0 // 257%256 = 1
# 따라서 np.add가 조금 더 부자연스럽게 나타남
import cv2

image_1 = cv2.imread('image_1.jpg')
image_2 = cv2.imread('image_2.jpg')

result = cv2.add(image_1, image_2)
cv2.imshow('Image', result)
cv2.waitKey(0)

result = image_1 + image_2
cv2.imshow('Image', result)
cv2.waitKey(0)

#비교적 Saturation 연산 이용하면 좀 더 자연스러운 이미지로 합쳐지지만, 
#np 합치기로 만들어진 이미지 쓰이는 경우 존재
