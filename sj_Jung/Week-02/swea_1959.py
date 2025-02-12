test_case = int(input())
for tc_index in range(1, test_case + 1):
    Ai, Bj = map(int, input().split())
    a_list = list(map(int,input().split()))
    b_list = list(map(int,input().split()))
    multiple_list = []
    if len(a_list) < len(b_list):
        for i in range(Bj - Ai + 1):
            inner_multiple = []
            for idx in range(Ai):
                multiple = a_list[idx] * b_list[idx+i]
                inner_multiple.append(multiple)
            multiple_sum = 0
            for idx in range(len(inner_multiple)):
                multiple_sum += inner_multiple[idx]
            multiple_list.append(multiple_sum)
        answer = 0
        for idx in range(len(multiple_list)):
            if multiple_list[idx] > answer:
                answer = multiple_list[idx]
    else:
        for i in range(Ai - Bj + 1):
            inner_multiple = []
            for idx in range(Bj):
                multiple = a_list[idx+i] * b_list[idx]
                inner_multiple.append(multiple)
            multiple_sum = 0
            for idx in range(len(inner_multiple)):
                multiple_sum += inner_multiple[idx]
            multiple_list.append(multiple_sum)
        answer = 0
        for idx in range(len(multiple_list)):
            if multiple_list[idx] > answer:
                answer = multiple_list[idx]

    print(f'#{tc_index} {answer}')