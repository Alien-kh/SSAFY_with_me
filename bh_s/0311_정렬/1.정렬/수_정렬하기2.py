import sys

N = int(sys.stdin.readline())  # 빠른 입력
lst = [int(sys.stdin.readline()) for _ in range(N)]  # 한 번에 입력받기
lst.sort()  # 기본 정렬 (O(N log N))

sys.stdout.write("\n".join(map(str, lst)) + "\n")  # 빠른 출력

# 구현한 버블정렬, 삽입정렬만으로는 해결이 불가.
# sort()의 사용만으로도 입력에서 속도 문제가 발생. 해당 문제는 좋은 문제는 아님.