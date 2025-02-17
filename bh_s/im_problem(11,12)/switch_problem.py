N = int(input())
arr = [0] + list(map(int, input().split()))  # 첫 번째 0을 포함하여 인덱스를 1부터 사용
M = int(input())

for test in range(M):
    g, num = map(int, input().split())

    if g == 1:
        # g가 1인 경우, num부터 num의 배수에 해당하는 스위치 상태 바꾸기
        for i in range(num, N + 1, num):  # num부터 num의 배수로 스위치 상태를 변경
            arr[i] = 1 - arr[i]

    elif g == 2:
        # g가 2인 경우, num부터 양쪽 대칭 상태 확인 후 변경
        arr[num] = 1 - arr[num]  # num 위치는 먼저 상태 변경
        step = 1
        while (num - step >= 1 and num + step <= N) and arr[num - step] == arr[num + step]:
            arr[num - step] = 1 - arr[num - step]
            arr[num + step] = 1 - arr[num + step]
            step += 1

# 출력 부분
for i in range(1, N + 1):
    print(arr[i], end=' ')
    if i % 20 == 0:
        print()