N, M = map(int,input().split())
basket = list(range(1, N+1))
for i in range(1, M+1):
    k, j = map(int, input().split())
    basket[k-1], basket[j-1] = basket[j-1], basket[k-1]

print(*basket)