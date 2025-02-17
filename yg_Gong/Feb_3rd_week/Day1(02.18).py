N = int(input())  # 스위치 개수
arr = list(map(int, input().split()))  # 스위치 상태 (0부터 시작)

M = int(input())  # 학생 수

for _ in range(M):  # 학생 수만큼 반복
    G, num = map(int, input().split())  # G = 성별(남:1, 여:2), num: 받은 수
    num -= 1  # 입력은 1부터지만 리스트는 0부터이므로 조정

    if G == 1:  # 남학생
        for i in range(num, N, num + 1):  # num의 배수에 해당하는 인덱스 변경
            arr[i] = 1 - arr[i]

    elif G == 2:  # 여학생
        arr[num] = 1 - arr[num]  # 받은 번호 스위치 변경
        step = 1

        while num - step >= 0 and num + step < N and arr[num - step] == arr[num + step]:
            arr[num - step] = 1 - arr[num - step]
            arr[num + step] = 1 - arr[num + step]
            step += 1  # 대칭 범위 확장

# 출력 (20개씩 출력)
for i in range(N):
    print(arr[i], end=" ")
    if (i + 1) % 20 == 0:  # 20개마다 줄바꿈
        print()
