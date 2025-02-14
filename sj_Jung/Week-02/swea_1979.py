def blk_word_finder(puzzle_map, map_len):
    global blk_word_list  # 전역 변수 선언으로 편집
    for verti_idx in range(len(puzzle_map)):  # 가로 구하기
        len_finder = 0
        for horiz_idx in range(len(puzzle_map[verti_idx])):  # 브루트 포스 방식으로 하나하나 선형검색하여 구하는 방식을 채택.
            if puzzle_map[verti_idx][horiz_idx] == 1:  # 1이 등장하면 칸수 판별기에 1씩 추가
                len_finder += 1
                if horiz_idx + 1 == map_len:  # 끝칸이면
                    if len_finder > 1:  # len_finder가 1 이상일 시
                        blk_word_list.append(len_finder)  # 리스트 추가
                        len_finder = 0
            elif puzzle_map[verti_idx][horiz_idx] == 0:  # 값이 0일시
                if len_finder > 1:  # len_finder가 1 이상일 시
                    blk_word_list.append(len_finder)  # 리스트 추가
                    len_finder = 0
                else:  # 그게 아니면 그냥 초기화
                    len_finder = 0

    verti_map = list(zip(*puzzle_map))  # 놀랍게도 이 코드를 쓰면 세로줄이랑 가로줄이 뒤바뀐답니다. 대신 내부 코드는 튜플로 처리되니 주의.
    for verti_idx in range(len(verti_map)):  # 세로 구하기
        len_finder = 0
        for horiz_idx in range(len(verti_map[verti_idx])):
            if verti_map[verti_idx][horiz_idx] == 1:  # 1이 등장하면 칸수 판별기에 1씩 추가
                len_finder += 1
                if horiz_idx + 1 == map_len:
                    if len_finder > 1:  # len_finder가 1 이상일 시
                        blk_word_list.append(len_finder)  # 리스트 추가
                        len_finder = 0
            elif verti_map[verti_idx][horiz_idx] == 0:
                if len_finder > 1:  # len_finder가 1 이상일 시
                    blk_word_list.append(len_finder)  # 리스트 추가
                    len_finder = 0
                else:  # 그게 아니면 그냥 초기화
                    len_finder = 0


testcase = int(input())

for tc_idx in range(1, testcase + 1):
    puzzle_map = []
    blk_word_list = []  # 2칸 이상의 빈줄을 수집하는 리스트
    ans = 0  # 빈칸으로 주어진 칸과 딱 맞게 일치하는 수를 구하는 변수

    map_len, word_len = map(int, input().split())  # 가로 세로 길이 N과 단어의 길이 K
    for map_maker_idx in range(map_len):  # 지도 제작
        map_maker = list(map(int, input().split()))
        puzzle_map.append(map_maker)

    blk_word_finder(puzzle_map, map_len)  # def 호출

    for i in range(len(blk_word_list)):  # 2칸 이상의 빈칸을 조사해둔 리스트를 대상으로
        if blk_word_list[i] == word_len:  # 제시된 단어 길이와 완전 일치하는 수 만큼
            ans += 1  # 답 1 추가

    print(f'#{tc_idx} {ans}')