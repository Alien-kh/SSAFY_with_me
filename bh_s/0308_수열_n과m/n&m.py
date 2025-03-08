N, M = map(int, input().split())
stack = [1] * M  # 초기값을 1로 설정

while True:
    print(*stack)  # 현재 수열 출력
    
    # 마지막 원소부터 증가 가능한 위치 찾기
    for i in range(M-1, -1, -1):
        if stack[i] < N:
            stack[i] += 1  # 현재 위치 값 증가
            for j in range(i+1, M):
                stack[j] = stack[i]  # 뒤의 값들을 현재 값과 동일하게 설정
            break
    else:
        break  # 모든 값을 증가시킬 수 없는 경우 종료