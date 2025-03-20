N, M = map(int,input().split())
word_dict = dict()
for _ in range(N):
    word = input()
    if word in word_dict: # 만약 단어가 dict안에 있다면 value값만 변경
        word_dict[word] += 1
    elif len(word) >= M:
        word_dict[word] = 1
# print(word_dict)
tuple_lst = []
for i in word_dict:
    tuple_lst.append((i, word_dict[i]))
# tuple_lst.sort()

# tuple_lst.sort(key= lambda x:x[1], reverse=True)
tuple_lst.sort(key=lambda x: (-x[1], -len(x[0]),x[0]))# 빈도 내림차순, 길이 긴 수, 알파벳은 순서대로
for i in tuple_lst:
    print(i[0])