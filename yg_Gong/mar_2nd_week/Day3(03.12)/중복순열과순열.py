# N개의 주사위를 던져 나올 수 있는 모든
# 중복 순열(type1)과 순열(type2)를 출력하시오
def perm_dup(idx, R):
    if idx == R:
        print(perm_arr)
        return
    for i in range(num):
        perm_arr[idx] = dice[i]
        perm_dup(idx + 1, R)

def perm_no_dup(idx, R):
    if idx == R:
        print(perm_arr)
        return
    for i in range(num):
        if check[i] == 0:
            perm_arr[idx] = dice[i]
            check[i] = 1
            perm_no_dup(idx + 1,R)
            check[i] = 0



dice = [1,2,3,4,5,6]
num = len(dice)
N, Type = map(int, input().split())
perm_arr = [None] * N
check = [0] * num

if Type == 1:
    perm_dup(0, N)
elif Type == 2:
    perm_no_dup(0, N)
