def Counting_Sort(DATA, TEMP, k):
    # DATA[]: 입력 배열 (0부터 k까지의 값들이 포함됨)
    # TEMP[]: 정렬된 결과를 저장할 배열 (초기화 되어 있어야 함)
    # k: 데이터 배열의 최대 값 (0부터 k까지의 값들만 존재)

    # COUNTS[]: 각 숫자의 등장 횟수를 저장할 카운트 배열 (0부터 k까지 크기)
    COUNTS = [0] * (k + 1)

    # 1단계: 데이터의 각 값을 카운트 배열에 등장 횟수 기록
    for i in range(0, len(DATA)):
        COUNTS[DATA[i]] += 1  # DATA[i]의 값에 해당하는 인덱스의 카운트를 1 증가

    # 2단계: 카운트 배열을 누적 합으로 변환 (카운트 배열이 각 값의 위치를 알려주도록 함)
    for i in range(1, k + 1):
        COUNTS[i] += COUNTS[i - 1]  # COUNTS[i]는 i 이하의 값들이 몇 번 등장했는지 나타냄

    # 3단계: 데이터를 역순으로 TEMP 배열에 정렬
    # 이 단계에서는 데이터를 뒤에서부터 처리하여, 동일한 값이 있을 때 원래의 순서를 유지함
    for i in range(len(TEMP) - 1, -1, -1):
        COUNTS[DATA[i]] -= 1  # 해당 값의 카운트를 하나 줄임 (같은 값이 여러 번 등장할 경우, 그 값을 올바르게 배치하기 위함)
        TEMP[COUNTS[DATA[i]]] = DATA[i]  # 해당 값의 올바른 위치에 데이터를 배치

arr = [0,4,1,3,1,2,4,1]
tmp = [0]*len(arr)
Counting_Sort(arr, tmp, 5)
print(tmp)