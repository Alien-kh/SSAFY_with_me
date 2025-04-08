# N = int(input())
# lst = [0]*N
# for i in range(N):
#     num = int(input())
#     lst[i] = num
#
# lst.sort()
#
# for k in range(N):
#     print(lst[k])


import sys

N = int(sys.stdin.readline())
lst = sys.stdin.read().split()  # 전체 입력을 한 번에 받아서 공백 기준으로 나눔
lst = map(int, lst)  # 문자열을 정수로 변환
lst = sorted(lst)  # 정렬 수행

sys.stdout.write("\n".join(map(str, lst)) + "\n")  # 빠른 출력