testcase = int(input())

for tc_index in range(1, testcase+1):
    a, b = map(int, input().split())
    stonelist = list(map(int, input().split()))

    for _ in range(b):
        i, j = map(int, input().split())
        i -= 1
        for idx in range(1, j+1):
            if i - idx >= 0 and i + idx < a:
                if stonelist[i-idx] == stonelist[i+idx]:
                    if stonelist[i - idx] == 1:
                        stonelist[i - idx] = 0
                        stonelist[i + idx] = 0
                    else:
                        stonelist[i - idx] = 1
                        stonelist[i + idx] = 1

    print(f'#{tc_index}', *stonelist)