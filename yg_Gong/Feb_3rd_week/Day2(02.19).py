# 바구니 뒤집기
N, M = map(int, input().split())  # 바구니 갯수, 뒤집기 횟수
arr = []

for i in range(1, N + 1):  # 바구니들을 담을 배열 생성
    arr.append(i)

for i in range(M):  # 본격적인 뒤집기
    # start 부터 end 까지 M번 뒤집을꺼임
    start, end = map(int, input().split())
    # 끝번호에서 시작번호를 빼고, 1을 더해줌 : 시작, 끝 숫자 모두 포함관계인데
    # 단순히 두개를 뺀값으로 계산하면 의도보다 1이작은 숫자가 나옴
    # 해당 숫자를 2로 나눈만큼 반복하여, 양끝쪽의 숫자위치를 서로 바꾸고
    # 그다음 작은 양끝을 바꾸며 안으로 들어가는식으로 역순을 만들어줌
    for j in range((end - start + 1) // 2):
        arr[start + j - 1], arr[end - j - 1] = arr[end - j - 1], arr[start + j - 1]

print(*arr)
