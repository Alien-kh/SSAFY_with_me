import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    stones = list(map(int,input().split()))

    for _ in range(M):  # M번 반복하면서 돌 뒤집기를 시행.
        idx, spread = map(int, input().split())
        idx -= 1    # 헷갈리니까. 리스트 형태와 맞춰주자.

        for s in range(1, spread + 1):
            left = idx - s  # 비교하려는 왼쪽 인덱스.
            right = idx + s # 비교하려는 오른쪽 인덱스.

            # 범위 밖으로 나가면, 더 이상 안뒤집어 봐도 된다.
            if left < 0 or right >= N:
                break
            
            # 양쪽의 같은 색의 돌이라면
            # 1과 0의 결과값이라면 이렇게 쓰면 바꾸기가 쉽다.
            if stones[left] == stones[right]:
                stones[left] = 1 - stones[left]
                stones[right] = 1 - stones[right]
    
    print(f"#{tc}", *stones)