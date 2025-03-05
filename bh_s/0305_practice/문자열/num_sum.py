N = int(input())
lst = []
sum_v = 0
chr = input()
for n in range(N):
    lst.append(int(chr[n]))
    sum_v += lst[n]
print(sum_v)
