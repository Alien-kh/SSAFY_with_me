T= int(input())
for tc in range(1, T+1):
    N = int(input()) # 학생 수
    arr = [0]*201 # 맨 끝 방이 400번인데, 짝수(아래 라인만 사용한다고 가정)
    for i in range(N):
        a, b = map(int, input().split()) # a랑 b는 방 번호(항상 b가 크다고 가정)
        #짝수만 사용한다고 했으니
        new_a = (a+1) // 2  # 예를 들면 3이면 3+1  // 2 => 2 4 +1 //2 => 2
        new_b = (b+1) // 2
        if new_a > new_b:
            new_a, new_b = new_b, new_a # a가 b보다 클 경우 swap
        for i in range(new_a, new_b):
            arr[i] +=1
    print(f'#{tc} {max(arr)}')

'''
3  
4  
10 20 
30 40
50 60
70 80
2 
1 3
2 200
3
10 100
20 80
30 50
'''