T = int(input())
for tc in range(1, T + 1):
    stick = list(input())
    stack = []
    cnt = 0
    for i in range(len(stick)):
        if stick[i] == '(':
            stack.append(stick[i])
        else:  # ')'일 때
            if stick[i - 1] == '(':  # 레이저
                stack.pop()
                cnt += len(stack)
            else:  # 쇠막대기 끝
                stack.pop()
                cnt += 1
    print(f'#{tc} {cnt}')
