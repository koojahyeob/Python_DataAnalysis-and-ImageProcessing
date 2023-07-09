import cv2
import numpy as np
import matplotlib.pyplot as plt

# 직선그리기
#cv2.line(image, start, end, color, thickness) : 하나의 직선을 그리는 함수

image = np.full((512,512,3), 255, np.uint8)
# 512 x 512, rgb 3가지 색상 의미, 255 full로 하고 8비트로)
image = cv2.line(image, (0,0), (340,255), (255,0,0), 10)

plt.imshow(image)
plt.show()
"-----------------------------------------------------------------------------"

#사각형 그리기
#cv2.rectangle(image, start, end, color, thickness) : 하나의 사각형을 그리는 함수

image = np.full((512, 512, 3), 255, np.uint8)
image = cv2.rectangle(image, (20,20), (255,255), (0,255,0),-1)

plt.imshow(image)
plt.show()

#원 그리기
#cv2.circle(image, center, radian, color, thickness)

image = np.full((512,512,3), 255, np.uint8)
image = cv2.circle(image, (255,255), 30, (255,0,0), -1)

plt.imshow(image)
plt.show()

#다각형 그리기
#cv2.polylines(image, points, is_closed, color, thickness)
# points : 꼭지점들, is_closed : 닫힌 도형 여부, thickness : 선의 두께 (채우기 : -1)

image = np.full((512,512,3), 255, np.uint8)
points = np.array([[5,5], [128, 256], [444,444], [256,128]])
image = cv2.polylines(image, [points], True, (0,256,0), 2)

plt.imshow(image)
plt.show()

#텍스트 그리기
#cv2.putText(image, text, position, font_type, font_scale, color)
#position : 텍스트 출력될 위치, font_type : 글씨체, font_scale : 글씨 크기 가중치

image = np.full((512,512,3), 255, np.uint8)
image = cv2.putText(image, "Koo Ja Hyeob", (0,256), cv2.FONT_ITALIC, 2, (0,0,256))

plt.imshow(image)
plt.show()