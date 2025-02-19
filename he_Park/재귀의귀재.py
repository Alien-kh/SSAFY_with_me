# 백준 25501
def is_palindrome(txt, k = 0, cnt = 1):
    if txt[0 + k] == txt[N - 1 - k]:  # 문자가 서로 같다면,
        k += 1
        if N % 2 and k == (N + 1) // 2:  # N이 홀수이고 모든 문자를 비교 완료했다면 종료
            return f'1 {cnt}'
        elif not N % 2 and k == (N + 1) // 2:  # N이 짝수이고 모든 문자를 비교 완료했다면
            cnt += 1
            return f'1 {cnt}'
        return is_palindrome(txt, k, cnt + 1)  # 다음 문자 비교
    else:  # 같지 않다면 중지(더 볼 필요 없음)
        return f'0 {cnt}'

T = int(input())
for tc in range(1, T + 1):
    txt = list(input().strip())  # ABABA
    N = len(txt)  # 5
    print(is_palindrome(txt))