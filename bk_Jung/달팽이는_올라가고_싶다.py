A,B,V = map(int,input().split())
C = A - B
D = V - A
if D % (C) == 0 :
    print(D // C + 1 )
else:
    print(D // C + 2)
