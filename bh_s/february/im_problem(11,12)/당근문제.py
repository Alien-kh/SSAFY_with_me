T = int(input())
for test in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split()))	# 당근 데이터
    
    max_length = 1		# 당근이 연속 성장한 최대 연속 횟수 변수
    current_length = 1	# 연속으로 성장했을 때 확인을 위한 변수
    
    for i in range(1, N):
        if carrots[i] > carrots[i - 1]:		# 이전 당근보다 크면
            current_length += 1
        else:
            max_length = max(max_length, current_length)	# 자라지 않았으면 max_length와 비교하면서, 현재 연속 성장 횟수 초기화
            current_length = 1
    
    max_length = max(max_length, current_length)
    
    print(f"#{test} {max_length}")
