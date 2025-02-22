# 순열

arr = ['a','b','c']
N = len(arr)
M = 3 # 한도
perm = [None] * M
used = [0] * N # 0은 사용 안함 1은 사용 함

# perm의 idx번쨰에 arr의 모든 요소 넣어보기

def permutation(idx):
    if idx == M:
        print(perm)
        return
    for i in range(N):
        #if not used[i]:
            perm[idx] = arr[i]
            used[i] = 1
            permutation(idx + 1)
            used[i] = 0


permutation(0)