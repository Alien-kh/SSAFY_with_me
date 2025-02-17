testcase = int(input())

for tc_idx in range(1, testcase + 1):
    card_num = int(input()) # 카드 장수

    card_list = list(input().split()) # 카드 내용 입력

    final_deck = [] # 정돈 완료된 카드를 넣을 덱
    if card_num % 2 == 0: # 짝수일 경우
        for deckMaker in range(0, len(card_list)//2) : # 차례대로
            final_deck.append(card_list[deckMaker])
            final_deck.append(card_list[deckMaker + len(card_list)//2])
    else: # 홀수일 경우
        final_deck.append(card_list[0]) # 맨 윗장에 올려두고
        for deckMaker in range(1, len(card_list)//2 + 1):
            final_deck.append(card_list[deckMaker + len(card_list)//2]) # 짝수먼저
            final_deck.append(card_list[deckMaker]) # 그다음 홀수

    print(f'#{tc_idx}', *final_deck)
