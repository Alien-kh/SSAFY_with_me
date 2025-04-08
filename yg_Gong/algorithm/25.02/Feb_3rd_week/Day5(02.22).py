# 간단한 369게임
# 3,6,9 들어가면 - 출력
# 해당 숫자가 들어간 숫자만큼 - 출력
# ex. 36 => -- , 633 => ---
N = int(input())
numbers = []
cnt = 0

for i in range(1, N+1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):    # i에 3,6,9있으면
        num = list(str(i))  # i를 문자로 하나하나분해해서
        for j in range(len(num)):
            if num[j] in ['3', '6', '9']:
                cnt += 1    # 3,6,9,의 갯수를세고
        numbers.append('-'*cnt) # 그 갯수만큼 - 출력
        cnt = 0 # 다시 갯수 초기화
    else:   # 3,6,9 없으면 그냥 숫자 출력
        numbers.append(i)
print(*numbers)