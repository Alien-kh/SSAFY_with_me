# 일곱 난쟁이

# 9명의 키를 다 더해서
# 2명을 선택해서 2명의 키를 뺀 값이 100인 경우를 찾기
# 이중 for 문을 사용해서 2명 고르기
nanjangi = []
sum_height = 0
for i in range(9):
    height = int(input())
    nanjangi.append(height)

sum_height = sum(nanjangi)  # sum안쓰고는 어떻게 다시 sum_height구할지 모르겠음,,,;;
for i in range(8):  # 1,8번째 난쟁이나 8,1째 난쟁이나 똑같으므로 i=9-1
    for j in range(i + 1, 9):  # j는 i+1부터 9까지(i와 동일할수는 없으니 +1)
        if sum_height - (nanjangi[i] + nanjangi[j]) == 100:
            nanjangi.pop(j)  # 항상 j>i가 성립됨
            nanjangi.pop(i)  # 큰 인덱스의 값을 먼저 pop 해줘야 인덱스 문제가 발생하지 않음
            break
    else:
        continue
    break
nanjangi.sort()
for i in nanjangi:
    print(i)
