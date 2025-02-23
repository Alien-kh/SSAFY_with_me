# SWEA 1926
N = int(input())  # N은 10 이상 1000 이하
for num in range(1, N+1):
    num = str(num)
    num = num.replace('3', '.')
    num = num.replace('6', '.')
    num = num.replace('9', '.')
    if num.count('.') == 1:
        num = '-'
    if num.count('.') == 2:
        num = '--'
    if num.count('.') == 3:
        num = '---'

    print(num, end = ' ')