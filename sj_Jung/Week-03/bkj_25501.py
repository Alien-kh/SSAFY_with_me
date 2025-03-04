def recursion(s, l, r):
    global call_resursion # 카운트 하기위해 전역변수 설정
    call_resursion += 1 # recursion의 횟수를 세기위한 += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

testcase = int(input())
for tc_idx in range(1, testcase + 1):
    call_resursion = 0
    target_word = input()
    print(f'{isPalindrome(target_word)} {call_resursion}') # 지문에서 시키는 대로 출력하자.