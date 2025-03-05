def inorder(v):
    global ans
    if v is None:  # 자식 없으면 종료
        return
    inorder(left[v])
    ans.append(value[v])
    inorder(right[v])

# 트리 저장은 배열에 할 거에요
T = 10
for tc in range(1, T+1):
    N = int(input())
    value = [None] * (N+1)
    left = [None] * (N+1)
    right = [None] * (N+1)
    for _ in range(N):
        lst = input().split() # idx 알파벳, 왼쪽 오른쪽 자식
        idx = int(lst[0]) # 노드 번호
        val = lst[1] # 문자
        value[idx] = val # 문자 넣어주기
        if len(lst) > 2:
            left[idx] = int(lst[2]) # 왼쪽 자식 있으면 넣어주기
        if len(lst) > 3 : #오른쪽 자식도 있응면
            right[idx] = int(lst[3])


    ans = []
    inorder(1)
    result = ''.join(ans)
    print(f'#{tc} {result}')

'''
8
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S
'''