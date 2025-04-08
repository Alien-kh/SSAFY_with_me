# A -> B
# 0319에 했던 '연산' 실습에서 연산 2가지가 빠진 버전이다.

def solve_bfs(s, cnt):
    q = []
    q.append((s, cnt))
    p_a = set()   # 집합에 넣어서 중복연산 제거

    while q:
        now, count = q.pop()
        if now == b:
            return count

        if now in p_a:
            continue

        if now > b:
            continue

        p_a.add(now)

        q.append((now * 2, count + 1))
        q.append((now * 10 + 1, count + 1))

    return -1


a, b = map(int, input().split())
result = solve_bfs(a, 1)
print(result)