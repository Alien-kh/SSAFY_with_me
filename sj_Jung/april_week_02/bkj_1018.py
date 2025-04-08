def checkboard(start_y, start_x):
    now_word = 'W' # 첫 케이스를 W로 정했을떄
    cnt = 0

    for i in range(start_y, start_y+8):
        if now_word == 'B': # 다음 체스판을 옮겨갔을때 B->B
            now_word = 'W'
        elif now_word == 'W': # W->W 의 경우도 대응 가능하도록 하기 위하여...
            now_word = 'B'
        for j in range(start_x, start_x+8): # 그럼 이제 체스판을 순회해보자, 체스판은 8*8
            if wordlist[i][j] != now_word: # 만약 체스판이 중복되는 칸이 아니라면
                now_word = wordlist[i][j] # 현재의 값을 저장하고 다음 칸을 살핀다.
            else: # 만약 같은 색이라면,
                if now_word == 'B': # B일 경우
                    now_word = 'W' # 현재 값을 W로 바꾸고
                    cnt += 1 # cnt를 1 추가한다. 원래는 W가 들어가야하는 칸인데, 바꿨다친다.
                else: # W일 경우
                    now_word = 'B' # 현재 값을 B로 바꾸고
                    cnt += 1 # cnt를 1 추가한다. 원래는 B가 들어가야하는 칸인데, 바꿨다친다.
    cnt_list.append(cnt) # 반복문이 끝나면 cnt_list에 cnt를 추가한다.

    now_word = 'B' # 첫 케이스를 B로 정했을때
    cnt = 0 # 다시 cnt를 0으로 초기화.

    for i in range(start_y, start_y+8): # 위의 반복문을 그~대로 똑같이 수행한다.
        if now_word == 'B':
            now_word = 'W'
        elif now_word == 'W':
            now_word = 'B'
        for j in range(start_x, start_x+8):
            if wordlist[i][j] != now_word:
                now_word = wordlist[i][j]
            else:
                if now_word == 'B':
                    now_word = 'W'
                    cnt += 1
                else:
                    now_word = 'B'
                    cnt += 1
    cnt_list.append(cnt) # 반복문이 끝나면 cnt_list에 cnt를 추가한다.

vertical, horizen = map(int, input().split()) # 세로, 가로
wordlist = [input() for _ in range(vertical)] # 단어 리스트
cnt_list = [] # 바꿔야하는 갯수 리스트 저장용

for i in range(vertical - 7): # 만약 8 * 8 이상의 체스판이 주어졌을 경우
    for j in range(horizen - 7): # 차액만큼 시작점을 이동하면서 찾아야하기 때문에...
        checkboard(i, j) # checkboard def 호출

print(min(cnt_list)) # cnt_list 중에서 가장 적은 값을 출력하면 끝.