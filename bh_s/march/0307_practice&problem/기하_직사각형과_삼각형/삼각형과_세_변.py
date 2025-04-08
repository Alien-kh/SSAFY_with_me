while True:
    a, b, c = map(int(input().split()))
    max_v = max(a,b,c)
    if a == b == c :
        print('Equilateral')
    elif max_v >