N = int(input())
data = list(map(int, input().split()))

stack = []
target = 1

for num in data:
    # 스택이 있고, 스택의 맨 위의 값이 타겟일때
    while stack and stack[-1] == target:
        stack.pop()
        target += 1

    if num == target:
        # 출력해야 하는 수가 바로 나온 경우
        target += 1
    else:
        # 아니라면 스택에 넣기
        stack.append(num)

while stack and stack[-1] == target:
    stack.pop()
    target += 1

if target == N + 1:
    print("Nice")
else:
    print("Sad")
