# 최대 공약수 -> 0이 될 때 까지 두 수를 서로 번갈아가며 자기 자신으로 남는 나머지가 0이 될때까지.
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# 최소 공배수 = 두 수의 곱을 최대 공약수로 나누면 나온다. 단 정수임으로 //으로 해준다.
def lcm(a,b):
    return (a * b) // gcd(a, b)

num1, num2 = map(int, input().split())
print(gcd(num1,num2))
print(lcm(num1,num2))