# 첫줄에 n (출입기록 수)
# enter가 오면 사람이 들어온 것. leave가 오면 사람이 떠난 것.

# sort()는 리스트만 가능하며, 원본을 변경함
# sorted()는 iterable 객체-> for문 사용 가능한 것에 모두 사용 가능(반복가능)

S = set()
n = int(input())
for _ in range(n):
    data = list(input().split())
    if data[1] == 'enter':
        S.add(data[0])
    elif data[1] == 'leave':
        S.remove(data[0])

for name in sorted(S, reverse=True):
    print(name)
