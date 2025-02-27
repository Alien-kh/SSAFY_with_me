T = int(input()) # TestCase
for tc in range(T):
    N = int(input()) # 순열의 크기
    arr =[0] + list(map(int,input().split())) # 1부터 시작한 순열과 같이 연결될 순열 # 1부터 시작이니깐
    visited =[0] * (N+1) # 0~N개까지
    cycle = 0 #순열 사이클
    for i in range(1, N+1):
        if visited[i] ==1: # 만약 방문한 경로라면 넘어가기
            continue

        curr_node = i
        cycle += 1
        visited[curr_node] = 1
        curr_node = arr[curr_node]
        while True:
            if visited[curr_node] == 1:
                break
            visited[curr_node] = True
            curr_node = arr[curr_node]
    print(cycle)