T = int(input())

string = ''
for _ in range(T):
    R, S = input().split()
    R = int(R)
    S = list(S)
    for i in S:
        string += i * R

    print(string)
    string = ''