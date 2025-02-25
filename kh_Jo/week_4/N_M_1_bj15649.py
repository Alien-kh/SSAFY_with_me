# N, M = map(int, input().split())  # 1부터 N까지 숫자 중에서 중복 없이 M개 선택
# arr = [i for i in range(1, N + 1)]
# check = [0] * N # 길이는 N
# result = []
#
# def combination(idx, cnt):
#     # 선택한 원소의 수가 M개이면 결과 출력
#     if cnt == M:
#         result = [arr[i] for i in range(N) if check[i] == 1]
#         print(*result)
#         return
#     # 더 이상 선택할 원소가 없으면 종료
#     if idx >= N:
#         return
#
#     # 현재 원소를 선택하는 경우
#     for i in range(N):
#         if not check[i]:
#             check[i] = 1  # i번째 숫자를 사용함을 표시
#             result.append(arr[i])  # 결과에 추가
#             permutation(cnt + 1)  # 다음 숫자 선택
#             result.pop()  # 선택했던 숫자 제거 (백트래킹)
#             check[i] = 0  # 사용 표시 초기화
#
#     permutation(0)
N, M = map(int, input().split())  # 1부터 N까지 숫자 중에서 중복 없이 M개 선택
arr = [i for i in range(1, N + 1)]
check = [0] * N  # 각 숫자의 사용 여부를 기록 (인덱스 0 ~ N-1)
result = []      # 현재까지 선택한 순열

def permutation(cnt):
    if cnt == M:
        print(*result)
        return
    # 모든 숫자에 대해 사용 여부를 검사
    for i in range(N):
        if not check[i]:
            check[i] = 1              # i번째 숫자를 사용 표시
            result.append(arr[i])     # 결과 추가
            permutation(cnt + 1)      # 다음 숫자 선택
            result.pop()              # 선택했던 숫자 제거 (백트래킹)
            check[i] = 0              # 사용 표시 초기화

permutation(0)
