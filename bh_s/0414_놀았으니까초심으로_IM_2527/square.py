
def square(r1,r2):
    x1, y1, p1, q1 = r1
    x2, y2, p2, q2 = r2

    # 공통 부분 없음
    if p1 < x2 or p2 < x1 or q1 < y2 or q2 < y1:
        return 'd'

    # 점
    if (p1 == x2 and q1 == y2) or (p1 == x2 and y1 == q2) or \
       (x1 == p2 and q1 == y2) or (x1 == p2 and y1 == q2):
        return 'c'

    # 선분
    if (p1 == x2 or p2 == x1) and not (q1 <= y2 or q2 <= y1):
        return 'b'
    if (q1 == y2 or q2 == y1) and not (p1 <= x2 or p2 <= x1):
        return 'b'

    # 직사각형
    return 'a'


for _ in range(4):
    nums = list(map(int, input().split()))
    r1 = nums[:4]
    r2 = nums[4:]
    print(square(r1, r2))