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
- 배열 브로드캐스트 작업 : 형태가 다른 배열을 연산할 수 있도록 배열의 형태를 동적으로 변환
- 배열 마스킹 작업 : 각 원소에 대하여 표시(체크) T or F
이를 통해 조건식 보다 더 수월하게 처리 가능 -> 이미지 처리 시 다수 사용 (ex 픽셀값 변환)
- Numpy 집계함수
최대, 최소, 합계, 평균값

NumpyBasic03 (opencv 활용)
- opencv 기본 사용법(이미지 읽어서 numpy객체 만들기, 새롭게 파일 저장해서 만들기, 색 변환)
- 픽셀 수 및 이미지 크기 확인 // BGR 순서 RGB x
- 특정 범위에 픽셀값 변경 // 슬라이싱의 중요성
- ROI 추출 및 복사
- 픽셀 별로 색상 다루기

NumpyBasic04 (행렬 및 보간법 활용)
- 이미지 크기 변경 #cv2.resize(image, dszie, fx, fy, interpolation)
      크기 키우기: interpolation = cv2.INTER_CUBIC
      크기 줄이기 : interpolation = cv2.INTER_AREA
- 이미지 위치 변경 #cv2.warpAffine(image, M, dszie)
      M : 변환행렬 참고
![image](https://github.com/koojahyeob/Python_DataAnalysis-and-ImageProcessing/assets/70992152/8cc5ee34-bcb0-4b54-95eb-44b5de48c6c7)
- 이미지 회전 #cv2.getRotationMatrix2D(center, angle, scale)
![image](https://github.com/koojahyeob/Python_DataAnalysis-and-ImageProcessing/assets/70992152/e448c545-9d79-4788-8cbf-821f536259e8)

NumpyBasic05 (이미지 합치기) -> 겹쳐서 합치는 것
- 두 개의 이미지를 서로 겹쳐서 합치는 형태
- cv2.add()를 통해 Saturation 연산 수행

NumpyBasic06 (이미지 임계점 처리) 
- cv2.threshold(image, thresh, max_value, type) 형태
![image](https://github.com/koojahyeob/Python_DataAnalysis-and-ImageProcessing/assets/70992152/a5aeb0fa-d024-4261-9350-91974abfe9db)

- 적응 임계점 처리 (하나의 이미지에 다수의 조명 상태 존재할 경우)
- cv2.adaptiveThreshold(image, max_vallue, adaptive_method, type, block_size, C)
- ADAPTIVE_tHRESH_MEAN_C : 5BY5로 쪼개서 모든 픽셀 값에 같은 가중치 곱해서 이미지 임계점 처리
- ADAPTVIE_THRESH_GAUSSIAN_C : 정규 분포 형태로 가운데 부분부터 멀어질 때 가중치는 점점 낮춰서 계산

