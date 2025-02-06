# 백준 2588
num1 = int(input())
num2 = [int(digit) for digit in input()]
print(num2)
third = num1 * num2[-1]
fourth = num1 * num2[-2]
fifth = num1 * num2[-3]
result = third + fourth*10 + fifth*100
print(f'{third}\n{fourth}\n{fifth}\n{result}')
