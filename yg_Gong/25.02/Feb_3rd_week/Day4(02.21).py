# 피보나치 수 5

N = int(input())
fibo = [0,1]
for i in range(2,N+1):
    fibo.append(0)
    fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo[N])

#-------------
# 어떻게 풀어야할지 감이 안잡혀서 냅다
# 배열에 0,1 넣고 계산시작해서 정답은 나왔으나
# gpt한테 추가적으로 푸는방법을 물어봄
# 현재 내 코드도 피보나치를 푸는 좋은방법이긴하나
# 배열을 쓰면 메로리를 많이 쓸 수 있어서 변수로만 푸는방법을 추천해줌!!

N = int(input())

a, b = 0, 1  # 첫 번째, 두 번째 피보나치 수

for _ in range(N):
    a, b = b, a + b  # a는 이전의 b, b는 a+b로 갱신

print(a)
