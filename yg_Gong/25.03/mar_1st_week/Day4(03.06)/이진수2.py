# 예제: 10진수 0.625를 2진수로 변환
# 연산 (×2)	        정수 부분	소수 부분
# 0.625 × 2 = 1.25	   1	      0.25
# 0.25 × 2 = 0.5	   0	      0.5
# 0.5 × 2 = 1.0	       1	      0.0

# 실수의 소수점아래를 2진수로 변환하는 함수
def float_jinsu(num):
    num2 = ''   # 2진수로 변환한값 저장할 변수
    i = num      # 남은 소수점 아래 숫자 저장할 변수

    while len(num2) < 13:
        if i * 2 > 1:   # i * 2가 1보다 크면
            num2 += str(1)  # num2에 1저장하고
            i = i * 2 - 1 # i * 2는 소숫점 아래만 남겨서 다시 i로 저장
        elif i * 2 < 1: # i * 2가 1보다 작으면
            num2 += str(0)  # num2에 0저장하고
            i = i * 2     # i * 2는 소숫점 아래의 수밖에 없으니 그대로 다시 i저장
        else:   # i * 2 == 0 이면
            num2 += str(1)  # num2 에 1 저장하고
            break           # 반복문 종료
    if len(num2) > 12:      # 12자리 넘으면 overflow 출력
        num2 = 'overflow'
    return num2

T = int(input())
for tc in range(1, T + 1):
    N = float(input())
    result = float_jinsu(N)
    print(f'#{tc} {result}')

