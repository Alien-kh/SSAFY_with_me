while True:
    a,b,c = map(int, input().split())
    if a == b == c == 0:
        break
    my_v = max(a,b,c)

    if my_v == a and a**2 == b**2 + c**2:
        print('right')
    elif my_v == b and b**2 == a**2 + c**2:
        print('right')
    elif my_v == c and c**2 == a**2 + b**2:
        print('right')
    else:
        print('wrong')


