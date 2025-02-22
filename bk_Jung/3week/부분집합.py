arr = [1,2,3,4,5]
N = len(arr)
M = 3

check = [0] * N

# check의 각 idx에 0 또는 1을 넣을건데 몇개가 포함 되는지 알아야 한다.

def combination(idx,cnt):
    if cnt == M:
        print(check)
        return
    if idx == N:
        #print(check) # 정답을 못찾은 상태, 마지막 인덱스 까지 M개의 원소를 선택하지 못함
        # cnt = 0
        # for i in range(N): # 요소가 몇개 포함 되었는지 확인
        #     if check[i]:
        #         cnt += 1
        #
        return
    check[idx] = 1
    combination(idx + 1,cnt + 1)
    print(f'after_recur1_a{idx}')
    check[idx] = 0
    combination(idx + 1, cnt)
    print(f'after_rcure_b{idx}')

    check[idx] = 0

combination(0,0)