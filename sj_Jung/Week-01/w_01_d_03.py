while True: # 0 0 이 입력되어야 종료된다는 조건이 붙었으므로 While 문을 사용하여 무한 반복한다.
    nums = list(map(int, input().split())) # 2가지 숫자를 받아야 하므로 list, map을 사용

    if nums[1] > nums[0] and nums[1] % nums[0] == 0: # factor의 경우
        print("factor")
    elif nums[0] > nums[1] and nums[0] % nums[1] == 0: # multiple의의 경우
        print("multiple")
    elif nums[0] == 0 and nums[1] == 0: # 탈출코드
        break # while 조건문 관계없이 탈출함.
    else:
        print("neither") # 이외의 경우는 neither