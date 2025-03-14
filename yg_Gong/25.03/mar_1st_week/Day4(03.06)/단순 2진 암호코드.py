codes = ['0001101', '0011001', '0010011', '0111101', '0100011',
         '0110001', '0101111', '0111011', '0110111', '0001011']

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N = 세로, M = 가로
    code_arr = [list(map(int, input().strip())) for _ in range(N)]
    x, y = 0, 0
    found1 = False
    for i in range(N):                  # 모든 코드의 뒷자리는 1으로 끝나기때문에
        for j in range(M - 1, -1, -1):  # 미로의 시작위치를 찾듯 1으로 끝나는 가장 첫번째 좌표를 찾음
            if code_arr[i][j]:
                x, y = i, j
                found1 = True   # 처음 1을 찾게되면 True로 변경하고 이중포문 break
                break
        if found1:
            break

    find_code = [''] * 8

    for k in range(8):
        for l in range(7):
            find_code[k] += str(code_arr[x][y - 55 + l + (7 * k)])

    for i in range(8):  # 맨처음에 만든 코드배열과 비교하여 일치하는 인덱스로 대체
        for j in range(10):
            if find_code[i] == codes[j]:
                find_code[i] = j

    right_code = ((find_code[0] + find_code[2] + find_code[4] + find_code[6]) * 3) + \
                 (find_code[1] + find_code[3] + find_code[5]) + find_code[7]

    if right_code % 10 == 0 :   # 주어진 공식에 해당하는지 확인(올바른코드 여부)
        result = sum(find_code)
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} 0')