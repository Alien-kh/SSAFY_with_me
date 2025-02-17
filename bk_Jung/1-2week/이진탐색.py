def binary_search(start, end, key):
    count = 0  # 탐색 횟수
 
    while start <= end:
        mid = int((start + end) / 2) #문제에서 주어진것 처럼 적음..
        count += 1  # 탐색 시도 횟수 증가. mid 하고 밑에 돌면 횟수 +1되므로.
 
        if mid == key:
             return count
            
        elif mid > key:
            end = mid 
 
        else:
            start = mid
 
    return None #반복문 나와서 count값 반환환
 
 
t = int(input())
 
for i in range(1, t + 1):
    P, A, B = map(int, input().split())
 
    result1 = binary_search(1, P, A)
    result2 = binary_search(1, P, B)
 
    if result1 < result2:
        print(f'#{i} A')
    elif result1 > result2:
        print(f'#{i} B')
    else:
        print(f'#{i} 0')  # 탐색 횟수가 같으면 0 출력