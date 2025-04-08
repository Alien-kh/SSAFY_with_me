
h, m = map(int, input().split())

if m < 45:
    if h > 0:
        h -= 1
    else:
        h = 23
    result = (m+60) - 45
    print(f'{h} {result}')

else:
    print(f'{h} {m-45}')
