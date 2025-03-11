# 브루트포스 '6' 이 3번 연속하도록 만들기.

def six_three(n):
    num = 666
    cnt = 0
    while True :
        if '666' in str(num):
            cnt += 1
            if cnt == n:
                return num
        num += 1


N = int(input())
result = six_three(N)
print(result)
