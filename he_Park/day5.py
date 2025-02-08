# 백준 2845
L, P = map(int, input().split())

news_cnt = list(map(int, input().split()))
SG_cnt = L * P
gap = []
for i in news_cnt:
    gap.append(i - SG_cnt)
    
print(*gap, end=" ")
