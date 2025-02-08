# 입력받는 테스트 케이스 수
T = int(input())

# 테스트 케이스 만큼 반복문 실행.
for _ in range(1, T+1):
    # 테스트 케이스는 한 줄로 입력을 받은 후, 공백을 기준으로 나누어(6명의 키 구별), int 로 변환하여 list 형태인 data 변수에 저장!
    data = list(map(int,input().split()))
    # data 리스트에 할당한 6명의 키를 tatal_sum 변수에 합으로 할당.
    total_sum = 0
    max_v = 0 

    # 6명 키 합과 최대 키 구하기
    for tall in data:
        total_sum += tall # 6명의 키 합
        if tall > max_v:  # 제일 큰 키 값 찾기.
            max_v = tall

    # 사라진 사람의 키를 저장하는 변수 초기화.
    possible_cm = 0

    # data 리스트에서 가장 큰 키 값에서 + 1 에서 조건: 7명의 평균 키가 정수가 되는 사라진 사람의 키(x)를 찾는 반복문.
    # 굳이 10000까지 할 필요는 없습니다. 다만, 키를 나타내는 정수가 1 ~ 1000 까지 이기 때문에 범위를 완벽히 잡으시려면 1008로 잡으면 됩니다.
    for x in range(max_v+1, 10000):
        if (total_sum + x) % 7 == 0:
            possible_cm = x
            break   # 사라진 사람의 최소 키 값을 찾았으면 break 로 반복문 종료.
    
    print(possible_cm)  # 사라진 사람의 키 출력.