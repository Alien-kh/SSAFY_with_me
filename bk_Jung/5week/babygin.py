def check(player):
    for i in range(len(player)-2):
        if player[i] and player[i+1] and player[i+2]:
            return True

    for i in player:
        if i >= 3:
            return True


    return False



def solve(player1, player2):
    p1_win = False
    p2_win = False
    for i in range(len(arr)):
        if i % 2 == 0:
            player1[arr[i]] += 1
        else:
            player2[arr[i]] += 1

        p1_win = check(player1)
        if p1_win:
            return print(f'#{tc} 1')
        p2_win = check(player2)
        if p2_win:
            return print(f'#{tc} 2')
    else:
        return print(f'#{tc} 0')

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    player1 = [0] * 10
    player2 = [0] * 10
    solve(player1, player2)

