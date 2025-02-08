# 파티 참가자 구하기

# 1m^2 당 사람 수 L, 파티 장소의 넓이 P
L, P = list(map(int,input().split()))
# 신문 기사에서의 사람의 수
newspaper = list(map(int,input().split()))

# 상근이가 직접 본 참가자 수
party_attend = L * P

# 신문기사 - 직접 본 참가자. 
# +a 그냥 넣으면 한 줄씩 띄워쓰게 된다. end =' ' 를 왜 쓰는지 알게됨! \n을 하지 않고 ' ' 공백을 출력하라는 의미.
for i in range(len(newspaper)):
    print(newspaper[i] - party_attend, end=' ')