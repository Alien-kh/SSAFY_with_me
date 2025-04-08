# A,J,Q,K 네 종류의 카드들이 다량으로 쌓여져 있다.
# 이 중, 5장의 카드를 뽑아 나열하고자 한다.
card = ['A', 'J', 'Q', 'K']
five_card = [None] * 5
cnt = 0
def cont_three():
    if five_card[0] == five_card[1] == five_card[2]:
        return True
    elif five_card[1] == five_card[2] == five_card[3]:
        return True
    elif five_card[2] == five_card[3] == five_card[4]:
        return True
    else:
        return False

def perm(x):
    global cnt
    if x == 5:
        if cont_three():
            cnt += 1
        return

    for i in range(4):
        five_card[x] = card[i]
        perm(x + 1)

perm(0)
print(cnt)


