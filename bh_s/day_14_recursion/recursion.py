# 재귀의 귀재
def recursion(s, l, r, count):
    count[0] += 1  # 호출 횟수 증가
    if l >= r:  # 왼쪽 문자 인덱스가 오른쪽 문자 인덱스 보다 크거나 같으면 회문. 1(True) 반환
        return 1
    elif s[l] != s[r]:  # 양 쪽 끝 문자가 다르면 회문이 아님. 0(False)반환.
        return 0
    else:       # 더 안쪽을 검사하기 위해 재귀 호출.
        return recursion(s, l+1, r-1, count)

def isPalindrome(s):
    count = [0]  # 호출 횟수를 저장할 리스트 (기본값은 0)
    result = recursion(s, 0, len(s)-1, count)   # recursion 함수 호출해서 재귀 함수 실행 및 count.
    return result, count[0]  # 팰린드롬 여부와 호출 횟수를 반환

# 입력 받기
T = int(input())  # 테스트 케이스 수
for _ in range(T):
    S = input().strip() # 굳이 strip 안써도 되긴함.
    result, call_count = isPalindrome(S)    # isPalindrome 에서 반환 받은 값 언패킹.
    print(f'{result} {call_count}')