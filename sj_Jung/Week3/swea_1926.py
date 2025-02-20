num = int(input()) # 반복할 숫자 입력

num_list = [] # 출력할 숫자를 담을 리스트

for i in range(1, num+1): # 하이픈을 입력시키기 위한 반복문
    hypen_num = 0 # 하이픈 수 판별기
    if i // 100 in (3,6,9): # 100의 자리 숫자 판별
        hypen_num += 1
    if (i % 100) // 10 in (3,6,9): # 10의 숫자를 판별
        hypen_num += 1
    if (i % 10) in (3,6,9): # 1의 숫자를 판별
        hypen_num += 1
    if hypen_num >= 1: # 확인된 숫자만큼 하이픈을 여러개 출력
        num_list.append('-' * hypen_num)
    else: # 이외에는 원래 숫자 입력
        num_list.append(str(i))

print(*num_list) # 언패킹으로 출력