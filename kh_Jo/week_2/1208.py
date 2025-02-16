#1. dump수를 받고
#2. 가장 높은 값을 찾고
#3. 가장 낮은 것에 넣어준다
#4. dump수 끝날때 까지 반복
#5. 반환
T = 10 # test case
result = []
for tc in range(T):
    dump = int(input())
    box_lst = list(map(int,input().split()))

    cnt = 1 # 추후에 덤프수를 세기 위해
    while cnt <= dump:
        max_box = box_lst[0]
        min_box = box_lst[0]
        max_box_idx = 0
        min_box_idx = 0
        idx = 0
        while True:
            if max_box < box_lst[idx]:
                max_box = box_lst[idx]
                max_box_idx = idx

            if min_box > box_lst[idx]:
                min_box = box_lst[idx]
                min_box_idx = idx
            idx += 1

            if box_lst[idx-1] == box_lst[-1]:
                break

        max_box_idx -= 1 # 제일 많은 박스에서 하나 빼서 (dump)
        box_lst[min_box] += 1 #제일 작은 박스에 넣어주기
        cnt +=1 #cnt가 dump랑 같아질 때 까지
    print(f'#{tc+1} {max_box-min_box}')
#     result.append(f'#{tc+1} {max_box-min_box}')
# print(*result)