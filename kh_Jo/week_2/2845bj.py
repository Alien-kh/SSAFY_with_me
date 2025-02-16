N, M = map(int, input().split()) # N개 바구니, M개 줄
lst = list(range(1,N +1))
for _ in range(M):
    i, j = map(int, input().split())
    # times = (j-i+1) // 2 # 첫 번쨰 방법 중간을 짤라서 왼쪽 idx 와 오른쪽 idx교환
    lst[i -1: j] = lst[i-1:j][::-1] # 두 번쨰 방법 그냥 리스트 슬라이싱을 통해 역순 변환
    # for k in range(times):
    #     lst[i +k -1], lst[j -1 -k] = lst[j -1 -k], lst[i + k -1]
print(*lst)
