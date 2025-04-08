N = int(input())

place =' '
star = '*'
for n in range(N):
    print(place*(N-1-n)+star*(n+1))