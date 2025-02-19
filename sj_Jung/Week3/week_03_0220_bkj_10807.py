def fibo(fibo_num):
    fibo_1 = 0  # 문제에 제시된 0부터 시작.
    fibo_2 = 1  # 그리고 다음 자리수인 1 추가. 이게 기준점이 될 예정.
    if fibo_num == 0: # 제시된 자리수에 0이 있었으므로 0의 조건도 기재. 피보나치 수열의 0번은 0이다.
        return 0
    if fibo_num == 1 or fibo_num == 2: # 피보나치 수는 1, 1, 2, 3, 5, ... 이다. 즉 1이나 2면 무조건 1이다.
        return 1
    for i in range(1, fibo_num): # if 가 아닐시 정상적인 피보나치 수가 출력
        fibo_1, fibo_2 = fibo_2, fibo_2 + fibo_1 # 반복문을 활용하여 계속 갱신시킴

    return fibo_2 # 반복이 끝나면 fibo_2 리턴

fibo_num = int(input()) # 구할 피보나치 수 자릿수 구하기.

result = fibo(fibo_num) # 값 저장
