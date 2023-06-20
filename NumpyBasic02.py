import numpy as np

""" array = np.random.randint(1,10, size =4).reshape(2,2)
print(array)

# 배열 연산하기 (덧셈,뺄셈,곱셈,나눗셈)
result_array = array + 10
print(result_array) """
"------------------------------------------------------------"
""" # 배열 브로드캐스트 작업
# 형태가 다른 배열을 연산할 수 있도록 배열의 형태를 동적으로 변환
array1 = np.arange(4).reshape(2,2) #2by2 배열
array2 = np.arange(2) #1by2 배열
array3 = array1 + array2

print(array3) """
"------------------------------------------------------------"
""" # 브로드캐스트 작업 확장
array1 = np.arange(0,8).reshape(2,4)
array2 = np.arange(0,8).reshape(2,4)
array3 = np.concatenate([array1,array2], axis = 0)
array4 = np.arange(0,4).reshape(4,1)

print(array3 + array4) """
"------------------------------------------------------------"
""" # 마스킹 작업 : 각 원소에 대하여 체크 (T,F) -> 이미지 처리 시 많이 사용 ex 픽셀값 변환
# 조건식 보다 마스킹 작업으로 수행하는 것이 처리하는 데에 있어서 더 수월함
array1 = np.arange(0,16).reshape(4,4)
print(array1)

array2 = array1 < 5
print(array2)

array1[array2] = 100 #array1에 마스킹된 array2 대입하여 만족하는(True)값만 작업 수행
print(array1) """
"------------------------------------------------------------"
""" # Numpy 집계함수
array = np.arange(16).reshape(4,4)

print("최대값 :",np.max(array))
print("최솟값 :",np.min(array))
print("합계 :",np.sum(array))
print("평균값 :",np.mean(array))
# 특정한 열에 대해서도 가능
print("합계 :",np.sum(array, axis= 0)) """