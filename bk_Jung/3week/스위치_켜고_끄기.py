N = int(input())
arr = [0] + list(map(int,input().split()))

student_num = int(input())

for i in range(student_num):
    a,b = map(int,input().split())

    if a == 1:
        for j in range(b,N+1,b):
            arr[j] = 1 - arr[j]

    if a == 2:
        j = 1
        arr[b] = 1 - arr[b]
        while  (b - j > 0 and b + j <= N) and (arr[b+j] == arr[b-j]):
            arr[b + j] = 1 - arr[b + j]
            arr[b-j] = 1 - arr[b-j]
            j += 1
 
for i in range(1,N+1):
    print(arr[i],end =" ") 
    if i % 20 == 0:
        print()
'''
1 3
0 1 0 1 0 0 0 1
-> 0 1 1 1 0 1 0 0

2 3
0 1 1 1 0 1 0 0
0 0 1 0 0 1 0 0
1 0 1 0 1 1 0 0
'''
