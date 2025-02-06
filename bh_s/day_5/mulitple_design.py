# day_5 폴더의 이미지를 참고. 세자리 수 2개 (1),(2)를 입력받아 (3),(4),(5),(6) 을 출력하는 프로그램 작성.

# 두 수 입력
num1 = int(input())
num2 = int(input())

# 각 자리 수 곱셈 생각해보기
# num1 은 원본으로 두고, 두번째 수의 일의 자리, 십의 자리, 백의 자리 순으로 곱 결과를 만들면 된다.

num2_digit_one = num2 % 10 # 10으로 나눈 나머지가 일의자리
num2_digit_two = (num2 // 10) % 10 # num2 를 10으로 나눈 몫만 남기면 일의자리의 숫자가 사라진채로 바뀐다 ex) 382 -> 38 이걸 일의 자리처럼 나머지를 남기면 된다.
num2_digit_three = num2 // 100 # 100으로 나눈 몫이 바로 백의자리.

# (3),(4),(5) 는 num1 과 각 자리수와 곱 연산 결과, (6) 은 num1 과 num2의 곱 연산 결과.

result3 = num1 * num2_digit_one
result4 = num1 * num2_digit_two
result5 = num1 * num2_digit_three
result6 = num1 * num2

print(f'{result3}\n{result4}\n{result5}\n{result6}')