'''
스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다.
스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는
(LIFO, Last in First out) 특성을 가지고 있다.

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다.
이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자.
임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지,
있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.
'''

sequence_num = int(input()) # 수열의 갯수 입력
seq_list = [0] * sequence_num # 빈 수열 리스트 생성

for idx in range(sequence_num): # 수열 리스트를 입력받기
    seq_list[idx] = int(input())

stack = []
num = 1
result = True
answer = ""

for i in range(sequence_num): # for N만큼 반복
    progression_now = seq_list[i]
    if progression_now >= num: # 현재 수열값 >= 오름차순 자연수: 값이 같이질 때 까지 append() 수행해야함.
        while progression_now >= num:
            stack.append(num)
            num += 1
            answer += "+\n" # 스택을 쌓았으니 + 입력 추가
        stack.pop()
        answer += "-\n" # 스택을 뺏으니 - 입력 추가
    else: # 현재 수열 값 < 오름차순 자연수: pop()을 수행해 수열 원소를 꺼냄
        n = stack.pop()
        # 스택의 가장 위의 수가 만들어야 하는 수열의 수보다 크면 수열을 출력할 수 없다.
        if n > progression_now:
            print("NO")
            result = False
            break
        else:
            answer += "-\n"

if result:
    print(answer)