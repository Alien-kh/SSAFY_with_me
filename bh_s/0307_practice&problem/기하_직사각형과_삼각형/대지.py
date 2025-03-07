
def ground(d):
    x = max(p[0] for p in d) - min(p[0] for p in d)
    y = max(p[1] for p in d) - min(p[1] for p in d)
    return x * y


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
result = ground(data)
print(result)
