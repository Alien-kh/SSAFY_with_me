#테스트케이스
T = int(input())

for tc in range(1, T + 1):
    # 부하들 키
    height = list(map(int, input().split()))

    sum_height = 0  #부하들 키 합
    seven_height = 0  #7번째 부하 키
    max_height = 0  # 6명 중 제일 큰 키
    # 6명의 키 합을 구함과 동시에 제일 큰 키 찾기
    for i in height:
        sum_height += i
        if i > max_height:
            max_height = i

    # 최대키인 1000까지 반복하면서 7로 나웠을 때 정수인 최소값찾기
    for j in range(max_height + 1,1001):
        if ((j + sum_height) % 7) == 0:
            seven_height = j
            break   # 최솟값을 찾기 위해 찾는 순간 break

    print(seven_height)

# ------------------------------------
# 위의 방법은 테스트케이스 17개중에 14개만 맞아서 오류,,,
# 아래의 방법으로 수정
T = int(input())

for tc in range(1, T + 1):
    height = list(map(int, input().split()))

    sum_height = 0  # 부하들 키 합
    seven_height = 0  # 7번째 부하 키
    max_height = 0  # 6명 중 제일 큰 키

    # 6명의 키 합을 구함과 동시에 제일 큰 키 찾기
    for i in height:
        sum_height += i
        if i > max_height:
            max_height = i

    # 7번째 부하는 max_height보다 크므로 +1부터 시작
    seven_height = max_height + 1

    # 7로 나누어떨어지는 최솟값 찾을 때까지 반복
    # while문으로 7번째 부하의 키가 1000이 넘을 경우도 처리
    while (sum_height + seven_height) % 7 != 0:
        seven_height += 1

    print(seven_height)
