N, L, D = map(int, input().split())
melody_time = []
for i in range(N): # i번째 노래 시작점
    for j in range(L):
        melody_time.append(j + (5 + L) * i)
first_D = D  # 이거때문에 틀렸네
while True:
    if D not in melody_time:
        print(D)
        break
    # D += D
    D += first_D  # 바보인증