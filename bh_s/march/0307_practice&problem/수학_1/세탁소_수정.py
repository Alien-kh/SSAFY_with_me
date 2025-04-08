def solve(M):
    R_money = []  # 리스트 사용

    if M >= 25:
        R_money.append(str(M // 25))
        M = M % 25
    if M >= 10:
        R_money.append(str(M // 10))
        M = M % 10
    if M >= 5:
        R_money.append(str(M // 5))
        M = M % 5
    if M >= 1:
        R_money.append(str(M // 1))

    return ' '.join(R_money)  # 리스트를 문자열로 변환

T = int(input())
for _ in range(T):
    money = int(input())
    result = solve(money)
    print(result)