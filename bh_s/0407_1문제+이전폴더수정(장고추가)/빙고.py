def mark(num):
    for i in range(5):
        for j in range(5):
            if data[i][j] == num:
                data[i][j] = 0
                return

def solve():
    count = 0

    # 가로
    for row in data:
        if all(x == 0 for x in row):
            count += 1

    # 세로
    for col in range(5):
        if all(data[row][col] == 0 for row in range(5)):
            count += 1

    # 대각선
    if all(data[i][i] == 0 for i in range(5)):
        count += 1
    if all(data[i][4 - i] == 0 for i in range(5)):
        count += 1

    return count



data = [list(map(int, input().split())) for _ in range(5)]


numbers = []
for _ in range(5):
    numbers += list(map(int,input().split()))

for idx, num in enumerate(numbers):
    mark(num)
    if solve() >= 3:
        print(idx + 1)
        break
