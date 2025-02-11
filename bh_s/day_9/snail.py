A, B, V = list(map(int, input().split()))

# 도착 하루 전까지의 걸리는 날 , 뒤의 조건은 계산에서 정확히 나누어 떨어지지 않는 경우 하루 더 추가.
snail_day = (V - A) // (A - B) + (1 if (V-A) %(A - B) else 0)

print(snail_day + 1) 