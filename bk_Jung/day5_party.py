a,b = map(int,input().split())
arr = list(map(int,input().split()))
result = []
for i in arr:
    c = a * b
    result.append(i - c)
# 야호
for i in result:
    print(i,end = " ")