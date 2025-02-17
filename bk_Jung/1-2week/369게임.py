N = int(input())

for i in range(1,N+1):
    s = str(i)

    count = 0
    for j in s:
        if j == '3' or j == '6' or j == '9':
            count +=1

    if count == 0:
        print(s,end = " ")
    else:
        print('-' * count, end = " ")
    