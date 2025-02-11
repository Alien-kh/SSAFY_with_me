N, M = map(int, input().split()) # 바구니 정보와 역순으로 뒤집을 명령어 횟수를 정하기

baguni_list = [] # 바구니 세팅

for i in range(1, N+1): # 바구니 리스트 생성
    baguni_list.append(i)

for i in range(M): # 역순으로 뒤집을 횟수 사전에 입력한 만큼 역순으로 뒤집기
    start, end = map(int, input().split()) # 시작지점과 종료 지점 입력
    for j, k in zip(range(start-1, end-1), range(end-1, start-2, -1)): # 인덱스 정보를 입력해야하는데, 동시에 정방향으로 동시에 역방향으로 가야하니 zip 함수 활용
        if j == k or j > k: # 만약 j == k(즉 중간값)이거나 j값이 k 값을 초월하면 더이상 바뀌지 말아야하므로 break 시킨다.
            break
        else: # 그 이외의 경우라면
            baguni_list[j], baguni_list[k] = baguni_list[k], baguni_list[j] # 스와프 시킨다.

print(*baguni_list) # 그 후 언패킹하여 프린트
