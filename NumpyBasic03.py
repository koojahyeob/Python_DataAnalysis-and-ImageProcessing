import cv2
import time

""" img_basic = cv2.imread('cat.jpg', cv2.IMREAD_COLOR)
#cv2.imread(file_name, flag) : 이미지를 읽어 Numpy 객체로 만드는 함수
cv2.imshow('Image Basic', img_basic)
#cv2.imshow(title, image) : 특정한 이미지르르 화면에 출력하는 함수
cv2.waitKey(0)
#cv2.waitKey : 0을 입력하여 입력 전까지 창 닫히지 않게 하기
cv2.imwrite('result1.png',img_basic)
#새롭게 파일 저장

cv2.destroyAllWindows() # 창 닫기

img_gray = cv2.cvtColor(img_basic, cv2.COLOR_BGR2GRAY)
#cvtColor : 색 변환 BGR2GRAY -> 2 = to
cv2.imshow('Image Gray', img_gray)
cv2.waitKey(0)
cv2.imwrite('result2.png',img_gray) """
"-----------------------------------------------------------"
""" image = cv2.imread('cat.jpg')

# 픽셀 수 및 이미지 크기 확인
print(image.shape)
print(image.size)

# 이미지 Numpy 객체의 특정 픽셀 
px = image[100,100]

#B G R 순서로 출력
print(px)

#G 값만 출력하기
print(px[1]) """
"-------------------------------------------------------------"
""" "특정 범위 픽셀 변경"
image = cv2.imread('cat.jpg')

start_time = time.time()
for i in range(0,100):
    for j in range(0, 100) :
        image[i,j] = ([255,255,255])
print("--- %s seconds ---" % (time.time() - start_time))

# 슬라이싱 처리가 20배 이상 더 빠름
start_time = time.time()
image[0:100,0:100] = [0,0,0]
print("--- %s seconds ---" % (time.time() - start_time))

cv2.imshow('Image', image)
cv2.waitKey(0) """
"-------------------------------------------------------------"
""" "ROI 추출 및 복사 ROI = Resion Of Interest"
image = cv2.imread('cat.jpg')

# Numpy Slicing : ROI 처리 기능
roi = image[200:350, 50:200]

# ROI 단위로 이미지 복사하기
image[0:150, 0:150] = roi

cv2.imshow('Image',image)
cv2.waitKey(0) """
"--------------------------------------------------------------"
""" "픽셀별로 색상 다루기"
image = cv2.imread('cat.jpg')
image[:,:,2] = 0 #모든 픽셀의 R 부분 빨간색 값을 0으로 바꿈

cv2.imshow('Image',image)
cv2.waitKey(0)
 """