T = int(input())
for i in range(T):
    R, S = input().split()
    R = int(R)
    result = ''
    for j in range(len(S)):
        result += S[j]*R
    print(result)
