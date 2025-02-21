from collections import deque
import sys

def solve(sentence):
    s = deque()
    left_bracket = {'(': ')', '[': ']'}
    for chr_s in sentence:
        if chr_s in left_bracket:   # 왼쪽 괄호일 때 push
            s.append(left_bracket[chr_s])
        elif chr_s in [')', ']']:  # 오른쪽 괄호일 때 pop 및 검사
            if len(s) == 0 or s.pop() != chr_s:
                return 'no'
    return 'yes' if len(s) == 0 else 'no'


# 여러 줄 입력받기 (Ctrl+D로 종료) # 백준에서 자동으로 종료한다고 함
input = sys.stdin.readline  # 속도 향상

while True:
    sentence = input().rstrip('\n')  # 개행 제거
    if sentence == '.':  # 종료 조건
        break
    print(solve(sentence))