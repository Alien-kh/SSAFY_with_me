data = input()
lst = [int(c) for c in data]  # 입력된 숫자를 리스트로 변환
lst.sort(reverse=True)  # 내림차순 정렬
result = ''.join(map(str, lst))  # 정렬된 숫자 리스트를 문자열로 변환
print(result)
