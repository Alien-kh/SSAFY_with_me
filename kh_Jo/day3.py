a = int(input()) # 첫째 줄
b = input() # 둘쨰 줄
lst = [] # 두 번째 숫자(문자형태)를 쪼개서 넣어줄 리스트
result =[] # 최종 결과 리스트
for ch in b: # 모든 수 쪼개서 lst에 넣어주기
    lst.append(int(ch))
for num in lst:
    result.append(a * num) # 각 수를 a와 곱해서 결과에 넣어주기
c, d, e = result[-1], result[-2], result [-3] # 백의자리 순서로 넣었으니 역순으로 지정
print(c) # 일의 자리
print(d) # 십의 자리
print(e) # 백의 자리
print(c+ (d*10) + (e * 100)) # 모두 더한 값

