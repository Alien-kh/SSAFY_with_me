a, b, V = map(int, input().split())

x = (V - a) / (a - b)
if x == int(x):
    print(int(x + 1))
else:
    x = int(x) + 1
    print(int(x + 1))