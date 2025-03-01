def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # 리스트를 두 부분으로 나누기
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # 두 리스트 병합하기
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    # 두 리스트를 비교하여 작은 값을 result에 넣기
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # 남은 원소가 있다면 result에 추가
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

arr = [5, 1, 3, 7, 2, 9]
print(merge_sort(arr))