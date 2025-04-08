# 두 숫자를 입력받아 숫자간 약수, 배수 관계 판단
while True:
    a, b = map(int, input().split())
    # 입력이 0 0이면 종료
    if a == 0 and b == 0:
        break
    # a가 b의 약수라면 factor
    # a가 b의 배수라면 multiple
    # 둘 다 아니라면 neither

    # b를 a로 나눴을 때 나머지가 0이라면 약수
    # a를 b로 나눴을 때 나머지가 0이라면 배수
    if b % a == 0 :
        print('factor')
    elif a % b == 0 :
        print('multiple')
    else :
        print('neither')