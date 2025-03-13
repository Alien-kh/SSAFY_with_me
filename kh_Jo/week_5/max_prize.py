# arr = [1, 2, 3]
# # 카드를 한 번 바꾸는 동작 N번 하기
# N = len(arr)
# # 3번 바꿨을 때 모든 경우의 수
# K = 3
# def change(idx):
#     if idx == K:
#         print(arr)
#         return
#     for i in range(N):
#         for j in range(i + 1, N):
#             arr[i], arr[j] = arr[j], arr[i]
#             change(idx+1)
#             # 원래 모양대로 돌려놓고
#             arr[i], arr[j] = arr[j], arr[i]
# change(0)


# 내 뒤에거랑 바꿔보기
# for i in range(N):
#     for j in range(i + 1, N):
#         arr[i], arr[j] = arr[j], arr[i]
#         print(arr)
#         # 원래 모양대로 돌려놓고
#         arr[i], arr[j] = arr[j], arr[i]
def solve(lst, cnt, times, visited):
    key = (cnt, ''.join(lst))#  딕셔너리에 들어갈 키
    if key in visited: # 이미 메모이제이션 되었다면
        return visited[key]

    if cnt == times:
        return int(''.join(lst)) # 이미 횟수를 다채웠으면 그냥 반환, 최댓값(max) 비교를 위해서int반환

    # 가지 치기
    if lst == sorted(lst,reverse=True): # 만약 내림차순 정렬(최댓값)과 지금 값이 똑같으면
        # 짝수일 때는 그대로 반환하면 되는 것이고, 중복된 숫자가 있으면 마지막 자리를 안 바꿔줘도 됨 (지들끼리 바꾸면 되니깐!)
        if (times-cnt) % 2 ==0 or len(set(lst)) < len(lst):
            return int(''.join(lst))
        # 홀 수 일 때는 뒷자리만 스왚
        lst[-1], lst[-2] = lst[-2], lst[-1]
        result = int(''.join(lst))
        lst[-1],lst[-2] = lst[-2], lst[-1] # 재귀할 때 영향을 줄 수 있으니 원복
        visited[key] = result
        return result
    max_v = 0 # 가장 큰 값을 넣어야 하므로 최댓값을 비교해서 큰 값을 dict에 넣어줌
    for i in range(n-1):
        for j in range(i+1, n):
            lst[i], lst[j] = lst[j], lst[i]
            max_v = max(max_v, solve(lst, cnt+1, times, visited))
            lst[i], lst[j] = lst[j], lst[i]
    visited[key] = max_v
    return max_v






T = int(input())
for tc in range(1, T+1):
    num, times = input().split() # num 은 바꿔줄 숫자, times 는 바꿀 횟수
    times = int(times)
    lst = list(num) # swap을 편하게 하려구
    visited = dict() # 메모이제이션 용 딕셔너리
    n = len(lst)
    result = solve(lst,0, times, visited)
    print(f'#{tc} {result}')
'''
10
123 1
2737 1
757148 1
78466 2
32888 2
777770 5
436659 2
431159 7
112233 3
456789 10
'''