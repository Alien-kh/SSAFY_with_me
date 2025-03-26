N = int(input())

def dfs():
    nums = []   # 저장 리스트
    for i in range(1, 11):
        stack = [(i,) for i in range(10)]   # 0 ~ 9까지 튜플로 저장.
        while stack:
            cur = stack.pop()
            # 자릿수가 i에 도달하면 감소하는 수 형태로 바꾸기.
            if len(cur) == i:
                nums.append(int("".join(map(str, sorted(cur, reverse=True)))))

            else:
                # 마지막 수 보다 작은숫자를 추가해서 감소하는 수 만들기.
                for i in range(cur[-1]):
                    stack.append(cur + (i,))    # 요소가 하나인 튜플
    return sorted(nums)

dec_nums = dfs()

if N < len(dec_nums):
    print(dec_nums[N])
else:
    print(-1)