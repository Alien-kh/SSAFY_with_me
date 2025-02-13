def solve(arr,n):
    max_num = -1 # 만약에 단조가 없으면 -1 을 반환해줘야 하기에 -1로 설정(if 단조가 있으면 어짜피 그것으로 반환)
    for j in range(n):
        times = 0
        for k in range(n):# 모든 경우의 수를 곱해주는데
            if j != k: # 이때 자기 자신을 곱해줄 수는 없으니깐 인덱스는 서로 다르지만 같은 수 고려 ex 2 2 4
                times = arr[j] * arr[k]
                times_str = str(times) # str로 바꿔서 리스트로 만들 수 있게 형 변환
                times_lst = list(times_str) #이후 형변환 된것을 리스트로 나누어 각 숫자를 비교할 수 있도록(idx를 사용하여)
                for i in range(len(times_lst)-1): # 첫번째 부터 한 칸씩 밀어가면서 자신의 오른쪽과 비교하므로 len -1
                    if times_lst[i] > times_lst[i+1]:
                        break # 만약 <=를 이루지 못하는 즉 단조가 아니면 break후 다시 반복
                else:
                    if max_num < times: # 최대ㅄ 찾아주기
                        max_num = times
    return max_num






T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    result = solve(lst,N)
    print(f'#{tc} {result}')

