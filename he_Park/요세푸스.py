# 요세푸스 문제
N, K = map(int, input().split())
arr = [i + 1 for i in range(N)]  # 1~7
result = []
current = 0

while len(arr) > 0:
    current = (current + K - 1) % len(arr)  # like 원형 큐
    result.append(str(arr.pop(current)))  # 결과값 저장
    # join 함수를 쓰기 위해 문자열로 변환 후 append
print(f"<{', '.join(result)}>")