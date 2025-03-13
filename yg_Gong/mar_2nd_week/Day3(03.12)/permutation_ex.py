# perm_arr의 idx 번째에 모든 요소들 다 넣어보기
def perm1(idx):
    if idx == N:    # N-1번 인덱스까지 숫자가 확정이 되었다면,
    # if idx == R 로하고 R값을 준다면 R개씩 뽑은 중복수열 출력 가능
        print(perm_arr)
        return
    # perm_arr[idx] = arr[0]
    # perm_arr[idx] = arr[1]
    # perm_arr[idx] = arr[2]
    # ...
    # perm_arr[idx] = arr[N-1]
    for i in range(N):
        perm_arr[idx] = arr[i]
        perm1(idx + 1)

# idx 번째에 들어갈 숫자를 고르기
def perm2(idx):
    if idx == R:    # idx가 R 이라면 이미 원하는 만큼 숫자를 뽑은 상태
        print(perm2_arr)
        return

    # 못 뽑았으면... 전체 요소 중에 하나 뽑아서 넣기

    for i in range(N):
        perm2_arr.append(arr[i])
        perm2(idx + 1)
        # 아까전에 선택했던 숫자는... 빼기
        perm2_arr.pop()

# 중복 순열 코드(perm1(),perm2()에서 요소를 중복으로 고르지 못하게 하는 부분만 추가)
# >>>>> 순열
def perm3(idx):
    if idx == R:
        print(perm3_arr)
        return

    # idx 번째에 가능한 모든 요소 선택해보기
    for i in range(N):
        if check[i] == 0:
            perm3_arr[idx] = arr[i]
            check[i] = 1 # i번째 요소 사용함
            perm3(idx + 1)
            check[i] = 0



arr = [1,2,3,4,5,6,7]
N = len(arr)
R = 3
perm_arr = [None] * R
perm2_arr = []
perm3_arr = [None] * R
check = [0] * N
# perm1(0)
# perm2(0)
perm3(0)