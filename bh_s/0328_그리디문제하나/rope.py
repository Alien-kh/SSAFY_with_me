N = int(input())
max_v = 0
rope = []
for _ in range(N):
    data = int(input())
    rope.append(data)

rope.sort()
for i in range(len(rope)):
    max_v = max(max_v, rope[i]*(N-i))

print(max_v)