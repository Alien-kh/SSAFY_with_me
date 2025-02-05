a, b, c = map(int, input().split()) # 일단 입력받는 3개의 눈을 각각 변수 a, b, c에 넣어주고
if a == b == c: # 세 가지 눈이 같은 경우
    result = 10000 + a * 1000
elif a == b or a == c: # 만약 2개가 같으면서 a와 같은 경우
    result = 1000 + a * 100
elif b == c: # 2개가 같은 경우 중 남은 경우의 수 1개
    result = 1000 + b * 100
else: # 다 다른 경우
    result = max(a, b, c) * 100 # 최댓값을 뽑은다음 100을 곱해준다
print(result) #결과 리턴
