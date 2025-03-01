# 주사위 게임. 

# 우선, 임의의 '함수' 니까 함수 정의를 만든다는 아이디어 구상이 중요!
# 입력을 한 칸씩 띄워서 넣는다 -> list(map(int, input().split())) 을 쓴다!
three_dice = list(map(int,input().split()))

# three_dice 변수는 list(map(int, input().split()))
# input() 으로 입력을 한 줄로 받고, .split() 으로 공백을 기준으로 문자열을 나눈 뒤
# map(int, ...) : 리스트의 각 요소를 int 자료형으로 변환

# 이 함수의 인자를 꼭 내가 선언한 변수 이름일 필요는 없지만, 이해와 통일성을 위해서 같게 사용했다.
def dice_game(three_dice): 
    
    # 변수 개수와 리스트의 길이가 같으면 **자동으로 리스트의 요소가 각 변수에 할당된다.**
    i, j, k = three_dice

    # 조건 1. 같은 눈 3개가 나오면 10000 + (같은 눈) * 1000
    if i == j == k: 
        return 10000 + i * 1000
    
    # 조건 2. 같은 눈 2개, 1000 + (같은 눈) * 100
    # 주의! (같은 눈)으로 곱해야 하기 때문에 조건을 나눠서 생각해야 한다.
    elif i == j or i == k:
        return 1000 + i * 100 # i를 기준으로 j 또는 k 와 같은 경우.
    elif j == k:
        return 1000 + j * 100 # i는 다르고 j, k 가 같은 경우.
    
    # 조건 3. 셋 다 다른 경우. (가장 큰 눈) * 100
    else:
        return max(i,j,k) * 100
    
print(dice_game(three_dice))


# # 중간의 조건 한번 바꿔보기.
# def dice_game(three_dice): 
    
#     # 변수 개수와 리스트의 길이가 같으면 **자동으로 리스트의 요소가 각 변수에 할당된다.**
#     i, j, k = three_dice

#     # 조건 1. 같은 눈 3개가 나오면 10000 + (같은 눈) * 1000
#     if i == j == k: 
#         return 10000 + i * 1000
    
#     # 조건 2. 같은 눈 2개, 1000 + (같은 눈) * 100. dice가 i인 경우와 j인 경우를 위해 다시 if로 조건을 줘야 한다.
#     elif i == j or i == k:
#         dice = i if i == j or i == k else dice = j
#         return 1000 + dice * 100
    
#     # 조건 3. 셋 다 다른 경우. (가장 큰 눈) * 100
#     else:
#         return max(i,j,k) * 100