# 1. N개의 당근은 대, 중, 소 상자로 구분하여 포장
# 2. 같은 크기의 당근은 같은 상자에
# 3. 비어있는 상자 X
# 4. 한 상자에 N//2를 초과하는 당근이 있어서는 안됨
# 5. 각 상자에 든 당근 개수 차이가 최소가 되도록 해야 함.
# 답: 이때의 개수 차이

T = int(input().strip())
for tc in range(1, T+1):
    N = int(input().strip())
    Ci = list(map(int, input().strip().split()))

    min_gap = N  # (조건5) 각 상자에 든 당근 개수 차이. 초기값은 대충 최대한 크게 설정
    is_find = False
    for x in range(1, N//2+1):
        for y in range(1, N//2+1):
            z = N - (x + y)
            if 1 <= z <= N//2:
                l1, l2, l3 = Ci[:x], Ci[x:x+y], Ci[x+y:]
                if set(l1) & set(l2) or set(l1) & set(l3) or set(l2) & set(l3):
                    continue

                else:  # 교집합이 없다 == 조건 2를 만족한다.
                    is_find = True
                    max_v = 0
                    min_v = N  # 대충 최대한 크게
                    for j in [l1, l2, l3]:
                        if max_v < len(j):
                            max_v = len(j)  # l1, l2, l3 중 길이가 가장 긴 리스트
                        if min_v > len(j):
                            min_v = len(j)  # l1, l2, l3 중 길이가 가장 짧은 리스트
                    if min_gap > (max_v - min_v):
                        min_gap = (max_v - min_v)
    if is_find:
        print(f'#{tc} {min_gap}')
    else:
        print(f'#{tc} -1')