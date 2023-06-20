# Python_DataAnalysis-and-ImageProcessing

파이썬 데이터분석 및 이미지처리 강의 공부자료 (REF.나동빈)

NumpyBasic01 
- 배열 만들기(n차원 배열, 랜덤한 정수의 배열)
#np.arange #np.zeros #np.random.randint
- 배열 합치기 #np.concatenate
- 배열 형태 바꾸기
#reshape # axis = 0
- 배열 나누기
#np.split

NumpyBasic02
- 배열 연산하기
- 배열 브로드캐스트 작업
브로드캐스트 작업 : 형태가 다른 배열을 연산할 수 있도록 배열의 형태를 동적으로 변환
- 배열 마스킹 작업
마스킹 작업 : 각 원소에 대하여 표시(체크) T or F
이를 통해 조건식 보다 더 수월하게 처리 가능 -> 이미지 처리 시 다수 사용 (ex 픽셀값 변환)
- Numpy 집계함수
최대, 최소, 합계, 평균값
