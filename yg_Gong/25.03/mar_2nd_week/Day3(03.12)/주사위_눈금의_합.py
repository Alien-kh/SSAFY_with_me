# 3개의 주사위를 던져 나올 수 있는 중복순열에 대해,
# 합이 10 이하가 나오는 경우는 총 몇가지 인가?
dice = [1,2,3,4,5,6]
N = len(dice)
cnt = 0
three_dice = [None] * 3

def dice10(x, sum):
    global cnt
    if sum > 10:    # 합이 10이넘으면 종료(가지치기)
        return
    if x == 3:      #(3번던진 주사위의 합이 10이하면 cnt += 1)
        cnt += 1
        return
    for i in range(N):
        three_dice[x] = dice[i]
        dice10(x + 1, sum + dice[i])

dice10(0,0)
print(cnt)
