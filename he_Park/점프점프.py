def solve(start):
    current = arr[start]
    visited[start] = 1

    if 0 < start - current <= N:
        solve(start - current)

    if 0 < start + current <= N:
        solve(start + current)

N = int(input())
arr = [0] + list(map(int, input().split()))
start_point = int(input())
visited = [0] * (N + 1)


solve(start_point)
print(visited.count(1))