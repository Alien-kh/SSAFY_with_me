word = [list(input().strip()) for _ in range(5)]
string = ''

for i in range(len(word)):
    for j in range(len(word[i])):
        if i < len(word[j]):  # 현재 단어에서 i번째 문자가 존재하면 추가
            string += word[j][i]
print(string)



### 기존코드
# word = [list(input().strip()) for _ in range(5)]
# string = ''
#
# for i in range(len(word)):
#     for j in range(len(word[i])):
#         string += word[j][i]
# print(string)



# IndexError (런타임 에러)가 발생하는 이유는 word[j][i]에서 i가 현재 단어의 길이를 넘어설 수 있기 때문
# 여기서 word[j][i]를 접근할 때,
# i가 word[j]의 길이를 초과하는 경우 IndexError가 발생