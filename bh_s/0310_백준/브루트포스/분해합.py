# 어떤 자연수 N에 대하여 자연수 N의 분해합은 N 과 N을 이루는 각 자리수의 합
# 어떤 자연수 M의 분해합이 N 인 경우 M을 N의 생성자라고 한다.
# ex) 245 의 분해합은 245 + 2 + 4 + 5 로 256이고, 245는 256의 생성자가 된다.

N = int(input())

for M in range(max(1, N - 9 * len(str(N))), N):
    total = M
    temp = M

    while temp > 0:
        total += temp % 10
        temp //= 10

    if total == N:
        print(M)
        break
else:
    print(0)