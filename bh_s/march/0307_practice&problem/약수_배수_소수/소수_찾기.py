def find_num(lst):
    f_cnt = 0
    for num in lst:
        cnt = 0
        for i in range(1, num + 1):
            if num % i == 0:
                cnt += 1
        if cnt == 2:
            f_cnt += 1

    return f_cnt


N = int(input())
num_lst = list(map(int, input().split()))
result = find_num(num_lst)
print(result)