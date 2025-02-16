def solve(n):
    if n ==1:
        return [[1]]
    else:
        # n-1삼각형 구하고
        prev = solve(n-1)
        last_r = prev[-1] # 삼각형 마지막 행을 가져옴(중간값을 더해주기 위해서)
        # 1로 시작하여 마지막 행에서 중간 값을 채운 뒤 [1] 추가하여 줄 완성
        new_r = [1] + [last_r[i] + last_r[i+1] for i in range(len(prev) -1)] +[1]

        return prev + [new_r]

    # 재귀
    # tri = solve(n-1)
    # last_r = tri[-1]
    # new_r = [1] # 항상 1로 시작
    # for i in range(len(last_r) - 1):
    #     new_r.append(last_r[i] + last_r[i+1])
    # new_r.append(1) # 항상 1로 끝남
    #
    # tri.append(new_r)
    # return tri
    #


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    result = solve(n)
    print(f'#{tc}')
    for r in result:
        print(' '.join(map(str,r)))