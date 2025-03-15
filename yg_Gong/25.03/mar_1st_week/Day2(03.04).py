# 스택2
# 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
# 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 3: 스택에 들어있는 정수의 개수를 출력한다.
# 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
# 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
import sys
N = int(sys.stdin.readline())    # 명령 수
stack = []
for _ in range(N):
    command = sys.stdin.readline().strip()

    if '1' in command:
        arr = list(command.split())
        stack.append(int(arr[1]))
    elif command == '2':
        print(-1 if not stack else stack.pop())
    elif command == '3':
        print(len(stack))
    elif command == '4':
        print(1 if not stack else 0)
    elif command == '5':
        print(-1 if not stack else stack[-1])
