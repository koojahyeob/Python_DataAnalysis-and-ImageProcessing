# KNN 알고리즘 숫자 인식 예제

import cv2
import numpy as np

img = cv2.imread('digits.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#cv2.imshow('Image', gray)
#cv2.waitKey(0)

# 세로로 50줄, 가로로 100줄로 사진 나누기
cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]
x = np.array(cells)
print(x.shape)

# 각 (20x20) 크기의 사진을 한 줄 (1x400)으로 바꾸기 벡터 형태로 한 줄로
train = x[:, :].reshape(-1, 400).astype(np.float32)
print(train.shape)

# 0이 500개, 1이 500개, ---- 로 총 5,000개가 들어가는 (1 x 5000) 배열 만들기
k = np.arange(10)
train_labels = np.repeat(k, 500)[: , np.newaxis]
print(train_labels.shape)

np.savez("trained.npz", train=train, train_labels = train_labels)

import matplotlib.pyplot as plt

# 다음과 같이 하나씩 글자를 출력할 수 있다.
plt.imshow(cv2.cvtColor(x[0, 0], cv2.COLOR_GRAY2RGB))
plt.show()
# 0~4열 -> 0 // 5~9열 -> 1 .....

# 다음과 같이 하나씩 글자를 저장할 수 있다.
cv2.imwrite('test_0.png', x[0,0])
cv2.imwrite('test_1.png', x[5,0])
cv2.imwrite('test_2.png', x[10,0])
cv2.imwrite('test_3.png', x[15,0])
cv2.imwrite('test_4.png', x[20,0])
cv2.imwrite('test_5.png', x[25,0])
cv2.imwrite('test_6.png', x[30,0])
cv2.imwrite('test_7.png', x[35,0])
cv2.imwrite('test_8.png', x[40,0])
cv2.imwrite('test_9.png', x[45,0])

import cv2
import numpy as np
import glob

FILE_NAME = 'trained.npz'

# 파일로부터 학습 데이터를 불러온다.
def load_train_data(file_name) :
    with np.load(file_name) as data:
        train = data['train']
        train_labels = data['train_labels']
    return train, train_labels

# 손 글씨 이미지를 (20 x 20) 크기로 Scaling 하기
def resize20(image) :
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_resize = cv2.resize(gray, (20, 20))
    plt.imshow(cv2.cvtColor(gray_resize, cv2.COLOR_GRAY2RGB))
    plt.show()
    # 최종적으로는 (1 x 400) 크기로 반환
    return gray_resize.reshape(-1, 400).astype(np.float32)

def check(test, train, train_labels):
    knn = cv2.ml.KNearest_create()
    knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
    # 가장 가까운 5개의 글자를 찾아, 어떤 숫자에 해당하는지 찾기
    ret, result, neighbours, dist = knn.findNearest(test, k = 5)

    return result

train, train_labels = load_train_data(FILE_NAME)

# glob 함수 : 파일들의 리스트를 뽑을 때 사용, 리스트 반환
for file_name in glob.glob('./test_*.png'):
    test = resize20(file_name)
    result = check(test, train, train_labels)
    print(result)
