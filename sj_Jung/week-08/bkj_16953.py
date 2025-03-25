import sys

def solve(current_num):
    global cnt, min_cnt

    if current_num > end: # 만약 재귀를 통하여 값이 end 값보다 높아지면 안 되므로 높아지는 즉시 return처리한다.
        return

    if current_num == end: # 만약 원하는 값이 되었을 떄
        if cnt < min_cnt: # min_cnt값이 현 cnt값보다 높은경우
            min_cnt = cnt # 그 값으로 교체한 후 return한다.
            return

    cnt += 1 # 재귀를 한번 시킬때마다 1씩 더하고
    one_add = int(str(current_num)+str(1)) # 오른쪽에 1을 계속 붙이는 경우 str로 형변환 시켜서 진행하면 편하다.
    solve(one_add) # 이 재귀는 끝자리에 1을 더한 경우의 재귀
    cnt -= 1 # return 되었다면 cnt를 다시 -1 한다. 잘못된 재귀를 취소처리하였으니.

    cnt += 1 # 다시 1을 더하고
    solve(current_num*2) # 2를 곱한 값으로 재귀한다.
    cnt -= 1 # 그래도 없으면 위와 같은 이유로 cnt를 -1한다.


start, end = map(int, sys.stdin.readline().split()) # 시작값과 끝값을 받는다.

cnt = 1 # A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다...라는데 그냥 1부터 시작하면 된다.

min_cnt = 0xfffff # 셀수없는 최댓값을 무작위로 작성하였다.

solve(start) # 재귀 def 시작

if min_cnt == 0xfffff : # 만약 min_cnt 값이 변하지 않았다면,
    print(-1) # 그건 구할 수 없는 값이었으므로 -1로 출력한다.
else: # 그리고 답이 구해졌다면,
    print(min_cnt) # 그 min_cnt의 값을 출력한다.