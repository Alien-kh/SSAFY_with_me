# 백준 11866번. 요세푸스 문제.

def joshephus(N,K):
    people = list(range(1, N + 1))  # 1부터 N까지 사람을 리스트로.
    ans = []
    idx = 0 # 현재 위치

    while len(people) > 0: # 모두 제거 되면 0이 되어서 종료.
        idx = (idx + K - 1) % len(people) # K 번째 사람 찾기.
        selection = people.pop(idx) # K 번째 사람을 빼서 다시 넣기 위해 저장.
        ans.append(selection)
    
    return ans

N, K = map(int, input().split())    # N명과 K번째 입력

result = joshephus(N, K)
print(f"<{', '.join(map(str,result))}>")    # 언패킹 출력. * 쓰고 싶었는데 < > 추가 때문에 join 메서드가 훨씬 편함.