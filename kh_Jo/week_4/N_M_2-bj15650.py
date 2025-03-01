N, M = map(int, input().split())  # 1부터 N까지 숫자 중에서 중복 없이 M개 선택
arr = [i for i in range(1, N + 1)]
# check = [0] * N  # 각 숫자의 사용 여부를 기록 (인덱스 0 ~ N-1)
result = []      # 현재까지 선택한 순열

def combination(start, cnt):
    if cnt == M:
        print(*result)
        return
    # 모든 숫자에 대해 사용 여부를 검사
    # for i in range(N):
        # if not check[i]:
            # check[i] = 1              # i번째 숫자를 사용 표시
    for i in range(start,N):
        result.append(arr[i])     # 결과 추가 / 숫자선택
        combination(i +1,cnt + 1)      # 다음 숫자 선택 이전에 선택한 숫자보다 뒤에 있는 숫자만 선택
        result.pop()              # 선택했던 숫자 제거 (백트래킹)
        # check[i] = 0              # 사용 표시 초기화 오름차순이니깐 이전에 사용한건뺴기

combination(0, 0)