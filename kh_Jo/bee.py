# swea 벌꿀 채집
def max_profit(num_lst): #최댓값 구하기
    n = len(num_lst)
    def dfs(idx, total, profit): # 최댓값을 뽑기위해 조합 만들기
        if total > C:
            return 0
        max_val = profit
        for i in range(idx, n):
            next_val = dfs(i+1, total +num_lst[i],profit + num_lst[i] **2)
            max_val = max(max_val, next_val)
        return max_val
    return dfs(0,0,0) #시작지점

def solve():
    visited = [[False] * (N-M+1) for _ in range(N)] # 추후에 값을 구하고 저장할 때 사용
    for r in range(N):
        for c in range(N-M+1):
            curr_v = arr[r][c:c+M]
            total_v = max_profit(curr_v)
            visited[r][c] = total_v
    max_total = 0
    total_max_lst = [False] * N # 각 줄에서 최댓값만 뽑아서 (한 줄에 한 명만 꿀을 뽑을 . 있으니깐)
    for row in range(N):
        total_max_lst[row] = max(visited[row])
    max_total += max(total_max_lst) #최댓값 뽑고
    total_max_lst.remove(max(total_max_lst)) #최댓값 버려서 다음 최댓값 찾아주기
    max_total += max(total_max_lst)


    return max_total

'''
1
4 2 13
6 1 9 7    
9 8 5 8
3 4 5 3
8 2 6 7
1
3 3 10
7 2 9
6 6 6
5 5 7

'''
T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int,input().split()) # N 은 벌통의 크기 , M은 선택할 수 있는 벌통의 개수,  양은 C
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    result = solve()
    print(f'#{tc} {result}')