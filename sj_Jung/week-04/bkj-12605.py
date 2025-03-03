testcase = int(input())

for tc_idx in range(1, testcase+1):
    word_list = input().split()

    for i, j in zip(range(len(word_list)), range(len(word_list)-1, -1, -1)):
        if i < j: # ij가 추월하지 않는 한,
            word_list[i], word_list[j] = word_list[j], word_list[i] # swap

    print(f'Case #{tc_idx}:', *word_list)