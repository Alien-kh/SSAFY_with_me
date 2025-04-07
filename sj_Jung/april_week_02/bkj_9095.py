def recursion(num):
    global final_num
    if num > target_num: # 만약 num이 target_num을 초과해버렸다면.
        return # 성립되지 않는 경우의 수이므로 즉시 return
    elif num == target_num: # 만약 num이 target_num이 된다면,
        final_num += 1 # 방법의 수를 발견한 것이므로 final_num을 1 추가하고 return
        return
    else:
        recursion(num+1) # 1씩 더하는 재귀
        recursion(num+2) # 2씩 더하는 재귀
        recursion(num+3) # 3씩 더하는 재귀

testcase = int(input()) # 테스트 케이스 입력

for tc_idx in range(1, testcase+1):
    num = 0 # 시작점
    final_num = 0 # 답을 저장할 num
    target_num = int(input()) # 목표 숫자 입력
    recursion(num) # 재귀 def 호출

    print(final_num) # 답안 출력