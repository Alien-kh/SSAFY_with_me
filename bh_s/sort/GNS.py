# 카운팅 정렬로 푸는 5일차,GNS
def counting_sort(data):
    num_dict ={"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4,
        "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    
    # 각 숫자가 나오는 횟수를 셀 리스트
    count = [0] * 10

    # 데이터에서 각 숫자 세기
    for word in data:
        count[num_dict[word]] += 1

    # 나온 횟수에 맞게 다시 리스트 만들기.
    result = []
    for num in range(10):
        # 해당 숫자에 해당하는 단어 count[num] 만큼 반복해서 추가
        for _ in range(count[num]):
            for key, value in num_dict.items(): # key와 value 둘 다 쓰기 위한 .items()
                if value == num:
                    result.append(key)
                    break

    return " ".join(result)

T = int(input())

for _ in range(T):
    test_case = input().split() 
    case_num = test_case[0] # #기호와 테스트케이스 번호
    case_len = int(test_case[1])
    data = input().split()
    print(f'{case_num} {counting_sort(data)}')