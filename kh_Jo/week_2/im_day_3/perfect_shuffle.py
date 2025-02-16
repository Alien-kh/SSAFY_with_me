def solve(n,arr):
    half_idx = 0
    if n % 2 ==0:
        half_idx = (n // 2) # 만약에 짝수라면 정확히 절반까지
    else:
        half_idx = (n // 2) + 1 # 홀수라면 몫을 구한뒤 왼쪽 +1
    left_half = arr[0:half_idx]  # 먼저 올 절반
    right_half = arr[half_idx:]  # 나머지 반
    result_arr = []              # 결과를 넣을 리스트
    for i in range(half_idx):
        result_arr.append(left_half[i])
        if i < len(right_half):     # 인덱스가 존재할 때 까지 넣어주기 (홀수의 경우 1개가 부족하므로)
            result_arr.append(right_half[i])
    return result_arr


T = int(input())
for tc in range(1, T +1):
    N = int(input())
    word_lst = list(input().split()) # 단어를 받고
    result = solve(N, word_lst) # 받은 단어와 개수를 함수에 넣어주기
    result = ' '.join(result) # 문제와 비슷하게 양식 맞쳐주기
    print(f'#{tc} {result}')
