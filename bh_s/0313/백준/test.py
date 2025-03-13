import sys

data = sys.stdin.read().strip().splitlines()

for line in data:
    a, b = map(int, line.split())
    print(a + b)