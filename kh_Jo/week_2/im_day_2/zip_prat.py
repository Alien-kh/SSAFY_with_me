# python 만 있는 tip
arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# 가로 탐색
for i in range(3):
    for j in range(3):
        print(arr[i][j],end=' ')
    print()

arr = list(map(list,zip(*arr))) # 가로 탐색된 코드를 이용해서 세로 탐색 가능
for i in range(3):
    for j in range(3):
        print(arr[i][j],end=' ')
    print()

# # 세로 탐색
# for i in range(3):
#     for j in range(3):
#         print(arr[j][i],end=' ')
#     print()
# zip():
# 순회 가능한 객체를 인자로 받고
# 각각의 요소를 잘라서 튜플을 원소로 하는 객체로 반환
# a = '12345'
# b = 'qwert'
# ret = zip(a,b)
# print(ret)
# print(list(ret))
a = '12345'
b = 'qwert'
c = 'asdfg'
for i in zip(a,b,c):
    print(list(i)) # 리스트로도 출력 가능
    # 값만 출려갛려면
    for y,x,z in zip(a,b,c):
        print(y, x, z)
arr =[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in zip(arr[0], arr[1], arr[2]):
    print(list(i))
for i in zip(*arr):
    print(list(i))

arr = list(map(list, zip(*arr)))
# IM 대비
# 무조건 for 아니면if / break & continue 잘 사용하면 됨

# 알고리즘 문제 풀이 순서
#     1. 문제 잘읽기 (시간 복잡도 고려하지 않아도 됨) -> 처음에 웹툰 보듯 스키밍 2번(빠르게 2번 읽기) (10분 ~ 15분)
#     ------> 문제 다 꼼꼼하게 읽고 반드시 입력에제를 가지고 문제 제대로 이해했는지 검증
#       -> 그림 보고 정확하게 이해했는지, 대략적이라도 확인해보기
#      (문제를 눈에 익히기)
#      정독!! 2번
#      시험 끝나고 문제 뭐 나왔냐고 물업봤을 때 외울 정도로
#      2. 설계 (15~ 20분) 엄청 중요
#      최대한 꼼꼼하게. 심지어 for문 탐색 길이까지 손코딩!!!
#       연습장에 설계한 것만 보고도 코드를 작성할 수 있을 정도로
#       설계가 끝났다!!! ----> 문제 풀 수 있는지 없는지 판별
#       3. 구현 !!!
#           테스트 주도 개발       -----------> 히든 테케 만들어서 검증하기
#       4. 디버깅