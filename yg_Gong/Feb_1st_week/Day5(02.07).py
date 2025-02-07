# L = 1^2m 당 사람의 수
# P =  파티가 열렸던 곳의 넓이
L, P = map(int, input().split())
# 신문기사 5개에 실린 각각의 참가자 수
people_num_news = list(map(int, input().split()))

# 반복문을 통해서 뉴스 기사의 인원과
# L * P 인원의 차이값을 출력
gap_news_real = [0] * 5
for i in range(5):
    # 찐 참석 인원
    people_num_real = L * P

    gap_news_real[i] = people_num_news[i] - people_num_real
# * 언패킹으로 리스트에 담아놓은 숫자들 출력하기
print(*gap_news_real)

