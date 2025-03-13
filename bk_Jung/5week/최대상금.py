def permutation(idx):
    global max_value
    if idx == M:
        change = int(''.join(arr))
        if change in lst[idx]:
            return
        lst[idx].append(change)
        if max_value < change:
            max_value = change
        return
 
    for i in range(N):
        for j in range(i+1,N):
            arr[i],arr[j] = arr[j],arr[i]
 
            a = int(''.join(arr)) # 리스트를 정수로 변환
            if a in lst[idx]:   # 만약 바꿨었더라면 원래대로 바꾸고 리턴
                arr[i], arr[j] = arr[j], arr[i]
                continue
 
            lst[idx].append(a) # 나온적 없는 숫자라면 idx 번 재귀 층에 넣음
 
            permutation(idx+1) # 다음 재귀로
 
            arr[i],arr[j] = arr[j],arr[i]
 
 
 
T = int(input())
for tc in range(1,T+1):
    arr,M = input().split()
    M = int(M)
    arr = list(arr)
    N = len(arr)
    lst = [[] for _ in range(M+1)]
 
    max_value = 0
    permutation(0)
    print(f'#{tc} {max_value}')