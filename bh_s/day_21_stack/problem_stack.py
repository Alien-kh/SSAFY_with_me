# 정수를 저장하는 스택 구현 후 명령에 대한 동작하기!
# 조건문이 좀 더럽게 나오는 문제.... stack을 만들기는 하지만 사실 조건문을 얼마나 잘 쓰는지를 확인하는 문제였다.
# + 좀 심각한 문제이긴 한데 테스트 케이스가 100만에 가까운 경우를 백준에서 넣어놨다. 그래서 import sys가 강제된다.

import sys
input = sys.stdin.readline  # 빠른 입력

N = int(input())    
stack = []
# 주의! 명령 중에는 2개로 입력해야하는 order 1 이 있다.
# input이 느리기에 미리 한꺼번에 받아서 처리하는 방향으로 바꾸었다. N개의 order를 각 행마다 명령 저장.
orders = [input().split() for _ in range(N)] 
  
for order in orders:
    if order[0] == '1':     # input()에 따로 자료형 변환을 하지 않으면 문자열이다. 꼭 생각해야한다.
        stack.append(order[1])  
    elif order[0] == '2':
        if stack :
            print(stack.pop())
        else:
            print(-1)
    elif order[0] == '3':
        print(len(stack))
    elif order[0] == '4':
        if not stack:
            print(1)
        else:
            print(0)
    elif order[0] == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)