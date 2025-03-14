# 주사위 세개

dices = list(map(int, input().split()))

# 주사위 3개가 다 같은 수가 나올 경우
if dices[0] == dices[1] == dices[2]:
    num = 10000 + (dices[0] * 1000)
else:  
    pair_num = None  # 2개만 같을 경우 해당 숫자 저장할 변수

    # 2개만 같은 경우 찾기
    for num in dices:
        if dices.count(num) == 2:
            pair_num = num
            break # 같은 숫자 2개 나오면 break

    if pair_num is not None:
        num = 1000 + (pair_num * 100)

    # 모두 다를 경우
    else:
        num = max(dices) * 100


print(num)



