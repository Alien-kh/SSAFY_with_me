# 첫째줄 - 현재 시각
# 둘째줄 - 필요한 시간

h, minu = map(int, input().split())
run_time = int(input())
add_v = 0

if minu + run_time >= 60:
    add_v = (minu + run_time) // 60
    result = (minu + run_time) % 60
    r_h = (h + add_v) % 24
    print(f'{r_h} {result}')

else:
    minu += run_time
    r_h = (h + add_v) % 24
    print(f'{r_h} {minu}')
