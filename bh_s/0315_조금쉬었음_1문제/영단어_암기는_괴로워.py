N, M = map(int, input().split())

words = []
counts = []
for _ in range(N):
    word = input()
    if len(word) >= M:  # 길이가 M 이상인 단어만 저장
        if word in words:
            index = words.index(word)
            counts[index] += 1
        else:
            words.append(word)
            counts.append(1)


# 정렬 기준: 1. 빈도수 내림차순, 2. 길이 내림차순, 3. 알파벳 오름차순
# 이 부분 GPT 사용 했음. 아이디어는 떠올랐는데 문법 자체를 몰랐음.

# 단어와 나오는 횟수 합치기
word_data = [[words[i], counts[i]] for i in range(len(words))]

sorted_words = sorted(word_data, key=lambda x: (-x[1], -len(x[0]), x[0]))

# 단어장 출력. 내가 (word, 횟수)로 단어를 저장했는데, 횟수라는 변수는 안쓰고 싶으니까 _ 사용
for word, _ in sorted_words:
    print(word)
