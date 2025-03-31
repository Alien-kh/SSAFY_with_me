'''
1 1 1 0
'''
# 재귀
# def KFC(x):
#     if x == 2:
#         return
#
#     KFC(x + 1)
#     KFC(x + 1)
#     KFC(x + 1)
#     print(x, end=' ')
#
# KFC(0)

#--------------
# 순열
# N = 3
# used = [0] * N
# path = []
# def perm(cnt):  # N개의 숫자 중에 cnt개를 뽑는다
#     if cnt == 2:
#         print(path)
#         return
#
#     for i in range(N):
#         # if not used[i]:  # 얘가 있으면 중복 아닌 순열
#         used[i] = 1
#         path.append(i)
#         perm(cnt + 1)
#         used[i] = 0
#         path.pop()  # 다음 for문을 돌기 전에 초기화
#
# perm(0)

#------------
# 완전 탐색: 주사위 3개를 던져 합이 10 이하인 경우의 수?

# def recur(cnt, total):
#     global cnt1
#     if total > 10:
#         return
#
#     if cnt == 3:
#         cnt1 += 1
#         return
#
#     for i in range(1, 7):
#         recur(cnt + 1, total + i)
#
# cnt1 = 0
# recur(0, 0)
# print(cnt1)  # 답 108

#-------------------
# 조합
# 5명 중 n명 뽑기
# arr = ['a', 'b', 'c', 'd', 'e']
# n = 3
# path = []
#
# def recur(start, cnt):
#     if cnt == n:
#         print(*path)
#         return
#
#     for i in range(start, len(arr)):
#         path.append(arr[i])
#         recur(i + 1, cnt + 1)
#         path.pop()
#
# recur(0, 0)

#-------------
# [도전] 주사위 던지기: 주사위 3개를 던져 나올 수 있는 모든 조합
#
# arr = [1, 2, 3, 4, 5, 6]
# n = 3
# path = []
#
# def recur(cnt, start):
#     if cnt == 3:
#         print(*path)
#         return
#     for i in range(start, len(arr)):
#         path.append(arr[i])
#         recur(cnt + 1, i)  # start 범위만 바꿔주면 됨
#         path.pop()
#
#
# recur(0, 0)

#------------------
# 그리디 - 회의실 배정
# 5 9 6 10 8 11 1 4 3 5 1 6 5 7 3 8 2 13 12 14
# arr = list(map(int, input().split()))
# activities = []
# for i in range(0, len(arr), 2):
#     activities.append((arr[i], arr[i + 1]))  # 시작 시간, 종료 시간
#
# activities = sorted(activities, key=lambda x: x[1])  # 종료 시간을 기준으로 오름차순 정렬
#
# prev_end = 0
# selected = []
# for activity in activities:
#     if prev_end <= activity[0]:
#         selected.append(activity)
#         prev_end = activity[1]
#
# print(selected)  # [(1, 4), (5, 7), (8, 11), (12, 14)]

#-----------------
# 퀵 정렬
# 3 2 4 6 9 1 8 7 5
# data = list(map(int, input().split()))
#
# def quick_sort(arr):
#
#     if len(arr) < 2:  # == 1이 아닌 이유는 빈 리스트일수도 있기 때문.
#         return arr
#
#     pivot = arr[0]
#     left = []
#     right = []
#
#     for i in range(1, len(arr)):
#         if arr[i] < pivot:
#             left.append(arr[i])
#         else:
#             right.append(arr[i])
#
#     left = quick_sort(left)
#     right = quick_sort(right)
#
#     sorted_arr = left + [pivot] + right
#     return sorted_arr  # 리턴을 꼭 해주자(왜인지는 모름)
#
# print(quick_sort(data))

#--------------
# N Queen
# 4 x 4 퀸 배치 경우의 수

# N = 4
# cnt = 0
# visited = [[0]*N for _ in range(N)]
#
# def check(row, col):
#     for i in range(row):
#         if visited[i][col]:
#             return True
#     # 왼쪽 대각선 확인
#     i, j = row - 1, col - 1
#     while i >= 0 and j >= 0:
#         if visited[i][j] == 1:
#             return True
#         i -= 1
#         j -= 1
#
#     # 오른쪽 대각선 확인
#     i, j = row - 1, col + 1
#     while i >= 0 and j < N:
#         if visited[i][j] == 1:
#             return True
#         i -= 1
#         j += 1
#
#     return False
#
#
# def recur(row):
#     global cnt
#
#     if row == N:  # 퀸을 모두 배치한다면
#         cnt += 1
#         return
#
#     for col in range(N):
#         if not check(row, col):  # 아직 해당 열에 방문하지 않았다면
#             visited[row][col] = 1
#             recur(row + 1)
#             visited[row][col] = 0  # 다음 열로 가기 전에 초기화
#
# recur(0)
# print(cnt)

#-----------------------
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# 원소의 합이 10인 부분 집합을 모두 출력하시오.
arr = [i for i in range(1, 11)]

def recur(start, total, subset):
    if total > 10:
        return

    if total == 10:
        print(subset)
        return

    for i in range(start, len(arr)):
        recur(i + 1, total + arr[i], subset + [arr[i]])

recur(0, 0, [])
