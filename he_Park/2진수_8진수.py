import sys
N = sys.stdin.readline().strip()
while True:
    if len(N) % 3 != 0:
        N = '0' + N
    else:
        break
for i in range(0, len(N), 3):
    a, b, c = int(N[i]), int(N[i+1]), int(N[i+2])
    print(a*2**2 + b*2**1 + c*2**0, end='')