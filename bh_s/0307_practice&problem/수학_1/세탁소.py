# 이 코드도 작동 됨. 근데 뭔가 엉성함.

def solve(M):
    R_money =''
    if M >= 25:
        R_money += str(M // 25) + ' '
        M = M % 25
    else:
        R_money += '0 '

    if M >= 10 :
        R_money += (str(M // 10)) + ' '
        M = M % 10
    else:
        R_money += '0 '

    if M >= 5:
        R_money += (str(M // 5)) + ' '
        M = M % 5
    else:
        R_money += '0 '

    if M >= 0:
        R_money += (str(M // 1)) + ' '
    else:
        R_money += '0 '

    return R_money.strip()


T = int(input())
for _ in range(T):
    money = int(input())
    result = solve(money)
    print(result)
