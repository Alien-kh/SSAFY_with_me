N = int(input())
data = list(map(int, input().split()))

max_v = 0
for i in range(len(data)):
    if data[i] > max_v:
        max_v = data[i]

for i in range(len(data)):
    if data[i] <= max_v:
        data[i] = data[i] / max_v * 100

sum_v = 0
for i in range(len(data)):
    sum_v += data[i]

print(sum_v/len(data))
