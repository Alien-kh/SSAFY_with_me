# import sys
# 치타 승
# sys.stdin = open('input.txt', 'r')

code_dict = {
(3, 2, 1, 1) : 0,
(2, 2, 2, 1) : 1,
(2, 1, 2, 2) : 2,
(1, 4, 1, 1) : 3,
(1, 1, 3, 2) : 4,
(1, 2, 3, 1) : 5,
(1, 1, 1, 4) : 6,
(1, 3, 1, 2) : 7,
(1, 2, 1, 3) : 8,
(3, 1, 1, 2) : 9,
}

# 암호 코드를 스캔해서 결과를 반환하는 함수
def solve():
    # 암호코드를 읽어오기, 암호코드 7*8 = 56개
    # 배경 0, 암호코드의 시작 0 하나일 수도 있고 2개 일수도 있고....3
    total_code = set() # 나중에 패턴 저장용
    for row in data:# 만약 전부 16진수로 바꿔주면 앞에 번호가 날라가긴 함
        # 행을 탐색할 때 뒤에서 부터 탐색, 코드 길이가 56이니까.. 55번까지 확인
        bin_row = bin(int(row, 16))[2:].zfill(len(row) * 4) # 패턴이 여러개 나왔을 때 앞에 0을 보장해주기 위해
        # print(bin_row)
        i = len(bin_row) -1# 끝에서 부터 앞으로 쭉 와야됨

        while i> 0: # 0이면 그 줄은 다 돈거임
            i -= 1 # 한 칸씩 줄여가면서 찾기
            code = [] # 코드 비워주고, 넣어주기
            if bin_row[i] == '1': # 만약 1이 나오면 패턴의 시작이라는 뜻
                c1, c2, c3, c4 = 0, 0, 0, 0  # c1, c2, c3, c4
                # 일단 비율을 구해야됨. 이떄 비율은 1, 그냥 세주거나, 2.최솟값의 비중을 보거나
                # 1의 개수를 세주기

                while bin_row[i] == '1':
                    c4 += 1
                    i -= 1
                while bin_row[i] == '0':
                    c3 += 1
                    i -= 1
                while bin_row[i] == '1':
                    c2 += 1
                    i -= 1
                while bin_row[i] == '0':
                    c1 += 1
                    i -=1
                scale = min(c1, c2, c3, c4) # 이제 비율을 구했음
                valid_code = code_dict[(c1 // scale, c2 // scale, c3 // scale, c4 // scale)] # 비율에 따라 나눠주기
                code.append(valid_code)
                # 이제 남은 7개 단어들도 구해줘야됨
                for _ in range(7):
                    c1, c2, c3, c4 = 0, 0, 0, 0  # c1, c2, c3, c4;
                    while bin_row[i] == '1':
                        c4 += 1
                        i -= 1
                    while bin_row[i] == '0':
                        c3 += 1
                        i -= 1
                    while bin_row[i] == '1':
                        c2 += 1
                        i -= 1
                    c1 = 7* scale - c2 - c3 - c4 # 비율만 달라지는 거니깐
                    i -= c1
                    code.append(code_dict[(c1 // scale, c2 // scale, c3 // scale, c4 // scale)]) # 여기까지 왔으면 일단 숫자는 한 문장 패턴은 다 찾은 상황
                # print(code)
                    # 유효성 검증

                odd_sum = code[1] + code[3] + code[5] + code[7]
                even_sum = code[0] + code[2] + code[4] + code[6] # 어짜피 유효코드도 짝수라 그냥 더해주면 됨
                if (odd_sum*3 + even_sum) % 10 == 0:
                    total_code.add(tuple(code)) # 각패턴을 뽑아 중복 처리 방지 , sum을 넣어주면 뒤에 테케에 걸림(패턴의 합이 중복됨)
                else:
                    total_code.add(0)
    # 이제 튜플 형태로 모든 코드들을 다 넣었으니 합을 구해줘야됨
    # final_code = list(total_code) # tuple 도 리스트를 비슷하게 사용 가능 (sum, for문에으로 하나씩 뽑기)
    final_sum = 0 # 최종적으로 반환할 값
    for sum_pw in total_code:
        if sum_pw != 0:
            final_sum += sum(sum_pw)
    return final_sum


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    result = solve()
    print(f'#{tc} {result}')
    # for row in data:
    #     print(row)
