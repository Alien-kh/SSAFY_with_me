num_input = input()

bi_ten = int(num_input, 2) # 2진수 -> 10진수 변환

ten_oct = oct(bi_ten) # 10진수 -> 8진수 변환

answer = ''

for i in ten_oct[2:]: # 변환된 8진수 앞 2글자 제거
  answer += i

print(answer)