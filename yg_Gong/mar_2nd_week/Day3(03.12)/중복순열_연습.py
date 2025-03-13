# 중복순열 [1,1,1] ~ [6,6,6] 까지 출력하는 코드를
# 재귀호출로 구현하자.
def perm(idx):
    if idx == R:
        print(perm_arr)
        return

    for i in range(N):
        perm_arr[idx] = arr[i]
        perm(idx + 1)


def perm2(idx):
    if idx == R:
        print(perm_arr)
        return
    for i in range(N):
        perm_arr[idx] = arr[i]
        perm(idx + 1)



# arr = [1,2,3,4,5,6]
# N = len(arr)
# R = 3
# perm_arr = [None] * R
#
# perm(0)
arr = [1,2,3,4]
N = len(arr)
R = 5
perm_arr = [None] * R
perm2(0)