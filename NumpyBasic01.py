import numpy as np #별칭

# list -> array
""" list_data = [1,2,3]
array = np.array(list_data)

print(array)
print(array.size)
print(array.dtype)
print(array[2]) """
"---------------------------------------------------------------------------"
""" # 0부터 3까지의 배열 만들기
array1 = np.arange(4)
print(array1)

# 4by4 크기의 2차원 배열 만들고, 그 값들은 0으로 초기화, 데이터 형태는 float(실수)
array2 = np.zeros((4,4), dtype = float)
print(array2)

array3 = np.ones((3,3), dtype = float)
print(array3) """
"---------------------------------------------------------------------------"
""" # 0부터 9까지 랜덤하게 초기화된 배열 만들기
array4 = np.random.randint(0,10,(3,3))
print(array4)

# 평균이 0이고, 표준편차가 1인 표준 정규를 띄는 배열
array5 = np.random.normal(0,1,(3,3))
print(array5) """
"---------------------------------------------------------------------------"
""" # Numpy 배열 합치기 concatenate 함수 사용
array1 = [1,2,3]
array2 = [4,5,6]
array3 = np.concatenate([array1,array2])

print(array3.shape)
print(array3)

# Numpy 형태 바꾸기 reshape 함수 이용 가로축
array1 = np.array([1,2,3,4])
array2 = array1.reshape(2,2)

print(array2)

# Numpy 형태 바꾸기 axis = 0 사용 세로축으로 합치기
array1 = np.arange(4).reshape(1,4)
array2 = np.arange(8).reshape(2,4)
array3 = np.concatenate([array1, array2], axis = 0 )

print(array3) """
"-----------------------------------------------------------------------------"
""" # Numpy 나누기 split 함수 이용 (인덱스 [2]를 기준으로 열이 0,1 //2,3으로 2by2로 나뉨)
array =np.arange(8).reshape(2,4)
left, right = np.split(array, [2], axis =1)
print(left.shape)
print(right.shape)
print(left) """