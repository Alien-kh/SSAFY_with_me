# ord 함수 원리를 꼭 알아놓을 것.

check_lst = [-1] * 26
S = input()
index = 0

for char in S:
    idx = ord(char) - ord('a')
    if check_lst[idx] == -1:
        check_lst[idx] = index
    index += 1

print(*check_lst)
