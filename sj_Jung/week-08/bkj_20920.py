import sys

input_num, min_len = map(int, sys.stdin.readline().split())

word_dict = {}

final_list = [] # 마지막 값을 저장하는 리스트

for i in range(input_num):
    input_word = input()
    if len(input_word) < min_len: # 만약 이 단어가 최소 요건 길이보다 짧다면
        pass # 무시
    elif input_word in word_dict: # 만약 dict안에 해당 값이 있다면
        word_dict[input_word] += 1 # value를 +1 한다.
    else: # 없다면
        word_dict[input_word] = 1 # 해당 key를 추가한다.

# 람다식을 이용해 정렬한다. 람다식에서 '-' 를 붙히면 내림차순으로 정렬된다.
sorted_list = sorted(word_dict.items(), key=lambda words: (-words[1], -len(words[0]), words[0]))

for i in sorted_list:
    print(i[0])