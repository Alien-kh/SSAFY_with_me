T = int(input())
for tc in range(1, T + 1):
    A,B,C = map(int, input().split())
    eat_candy = 0
    if B < 2 or C < 3:  # 어떠한 방식으로 먹더라도 사탕의 개수가 순증가할 수 없을 때
        print(f'#{tc} -1')
        continue

    while C <= B :      # 우선 C가 B보다 작으면 B를 먹기
        B -= 1          # B 는 감소
        eat_candy += 1  # 먹은 사탕갯수는 증가

    while B <= A:       # B가 A보다 작으면 A를 먹기
        A -= 1          # A 는 감소
        eat_candy += 1  # 먹은 사탕갯수는 증가

    print(f'#{tc} {eat_candy}')

# 반복문 말고 B-C+1 , A-B+1과 같은 단순연산과 조건문으로 문제 해결 가능함,,,!!