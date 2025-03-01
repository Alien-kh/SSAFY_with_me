# 숫자 입력
N = int(input())

# 1부터 N 까지 확인
for i in range(1, N+1):
    
    # 3, 6, 9가 나올때 마다 박수를 치는 횟수 저장 변수
    clap_count = 0
    
    # i를 사용하기 위해 다른 변수 하나 더 사용
    num = i
    
    # 반복문. num이 0이 되어야 끝난다. 
    # 내가 설계한 것은 어차피 3, 6, 9는 몇자리 수 이던, 자리수를 떼어내서 3, 6, 9를 확인할 것임.
    # 뒷 자리수 부터 확인해도 되고, 앞자리 수부터 확인해도 된다. 나는 뒷자리 수부터. 
    while num > 0: 
        # 자리수 확인 변수
        confirm_num = num % 10
        if confirm_num == 3 or confirm_num == 6 or confirm_num == 9:
            clap_count += 1
        # num 을 10으로 나눈 몫을 할당하면 뒷자리 하나를 날리기가 가능.
        num //= 10

    # clap_count 가 존재하면 i 대신 '-'를 clap_count 만큼 출력. \n이 아닌 공백을 두고 옆으로 출력.
    if clap_count > 0:
        print('-' * clap_count, end=' ')
    else:
        print(i, end=' ') 