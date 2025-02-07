how_many_people = list(map(int, input().split())) # 상근이가 생각하고 있는 사람 수
mess_media = list(map(int, input().split())) # 신문 기사에 나온 사람 수

fact_check = [] # 참가자의 수가 몇 명 만큼 잘못 되었는지 검색

for fact_checker in mess_media: # 신문 마다 팩트 체크 개시
    if fact_checker == how_many_people[0] * how_many_people[1]: # 일치하면
        fact_check.append(0)
        # 0 출력. 사실 그냥 if-else 없이 fact_check.append(fact_checker - how_many_people[0] * how_many_people[1]) 만 해도 되긴할듯.
    else:
        fact_check.append(fact_checker - how_many_people[0] * how_many_people[1]) # 차이가 발생하면 차이만큼 입력

print(*fact_check) # 언패킹하면서 출력