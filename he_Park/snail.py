# 실패
# 백준 2869
# 낮에 A미터, 밤에 B미터 미끄러짐
# 정상에 올라간 후에는 미끄러지지 않음
# 며칠 걸리는가
up, down, tree_height = map(int, input().strip().split())

while True:
    s = tree_height
    if (s - up) % (up - down) == 0:
        day = (s - up) // (up - down) + 1
        break
    s += 1

print(day)


# tree_height <= up + (up - down) * (day - 1) < tree_height + (up - down)
