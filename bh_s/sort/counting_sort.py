def counting_sort(arr):
    # 최소값과 최대값을 찾기 (max, min 함수 없이)
    max_val = arr[0]
    min_val = arr[0]
    
    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    
    # 카운팅 배열 초기화 (최소값부터 최대값까지의 범위를 사용)
    count = [0] * (max_val - min_val + 1)
    
    # 각 값에 대해 등장 횟수 세기
    for num in arr:
        count[num - min_val] += 1
    
    # 카운팅 배열을 이용해 정렬된 배열 만들기
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i + min_val] * count[i])  # 해당 값이 등장한 만큼 추가
    
    return sorted_arr

# 예시 배열
arr = [0, 1, 4, 1, 3, 1, 2, 4, 1]
sorted_arr = counting_sort(arr)

print("정렬된 배열:", sorted_arr)