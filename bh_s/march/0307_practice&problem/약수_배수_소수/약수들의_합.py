
def find_perfect(n):
    lst = []
    for i in range(1, n):
        if n % i == 0:
            lst.append(i)

    sum_v = 0
    for j in range(0, len(lst)):
        sum_v += lst[j]

    if sum_v == n:
        print(f'{n} = ' + ' + '.join(map(str, lst)))

    else:
        print(f'{n} is NOT perfect.')


while True:
    N = int(input())
    if N == -1:
        break
    find_perfect(N)

