def find_page(end_page, target_page):
    cnt = 0
    start = 1

    while start <= end_page:
        find_mid = int((start + end_page) / 2)
        cnt += 1  # 탐색 횟수 증가

        if find_mid == target_page:
            return cnt  # 찾았을 때 탐색 횟수 반환
        elif find_mid < target_page:
            start = find_mid  # 오른쪽 탐색
        else:
            end_page = find_mid  # 왼쪽 탐색

    return cnt  


T = int(input())

for tc in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())

    cnt_a = find_page(P, Pa)  # A가 몇 번 만에 찾는지
    cnt_b = find_page(P, Pb)  # B가 몇 번 만에 찾는지

    # 결과 출력
    if cnt_a < cnt_b:
        print(f'#{tc} A')
    elif cnt_a > cnt_b:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')
