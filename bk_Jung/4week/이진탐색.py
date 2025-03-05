def binarySearch(a,N,key):
    cnt = 0
    start = 1
    end = N

    while start <= end:
        middle = (start + end) // 2
        if middle == key:
            return cnt
        elif middle > key:
            end = middle
            cnt +=1
        else:
            start = middle
            cnt +=1


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    P,A,B = map(int,input().split()) # P 는 전체 쪽수 A,B 는 각자 찾을 쪽 수

    a = [i for i in range(1,P+1)]
    b = [i for i in range(1,P+1)]

    a_cnt = binarySearch(a,P,A)
    b_cnt = binarySearch(b,P,B)
    if a_cnt < b_cnt:
        print(f'#{test_case} {"A"}')
    elif a_cnt > b_cnt:
        print(f'#{test_case} {"B"}')
    else:
        print(f'#{test_case} {0}')