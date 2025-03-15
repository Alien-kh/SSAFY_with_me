# 멱집합을 구해서
# 멱집합의 요소가 K가 될 때 cnt +=1
def count_k(idx, current_sum):
    global cnt
    if idx == N:    # 부분집합의 인덱스가 주어진 자연수의 갯수를 벗어남
        if current_sum == K:    # 부분집합 요소의 합이 K인지 확인
            cnt += 1            # k이면 cnt += 1
        return
    # idx번 요소를 포함하는 경우
    count_k(idx + 1, current_sum + numbers[idx])
    # idx번 요소를 포함하지 않는 경우
    count_k(idx + 1, current_sum)

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())    # N:자연수의 갯수, K: 합해서 나와야하는 값
    numbers = list(map(int, input().split()))
    cnt = 0
    count_k(0,0)
    print(f"#{tc} {cnt}")
