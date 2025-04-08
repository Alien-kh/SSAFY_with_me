# 정수 N, M 이 주어질 때, M의 이진수 표현의 마지막 N  비트가 모두 1로 켜져 있는지 아닌지를 판별하여 출력.

# M의 우측 N개를 확인할 예정.
# 1개의
# def solution():
#     target = M
#     # N 번 확인
#     for _ in range(N):
#         # 맨 우측 비트가 1인지 체크
#         # 0x1, 0b1, 1 다 사용 가능.
#         # - 0x1: 비트 연산이라는 것을 명시
#         if target & 0x1 == 0:
#             return False
#         # 맨 우측 비트를 삭제.
#         target = target >> 1
#     return True

# 단순하게 하는 방법
def solution():
    # N 개의 1 을 구하기
    mask = (1 << N) - 1
    check = (M & mask) == mask
    if check is True:
        ans = 'ON'
    else:
        ans = 'OFF'
    return ans


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = solution()
    print(f'#{tc} {result}')
