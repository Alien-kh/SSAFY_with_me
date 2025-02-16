# import sys
# sys.stdin = open('input.txt', 'r')

def getSum(index): # A의 길이만큼 곱들의 합을 구해서 리턴
    Sum = 0
    for i in range(len(A)):
        value = A[i]*B[i+index]
        Sum+= value
    return Sum



testcase= int(input())
for tc in range(1, testcase+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 두 리스트의 길이를 비교
    # A를 짧은 리스트로 세팅
    if N > M:
        A, B = B,A

    Max = -21e8 # -21억 (overflow 직전인듯?)
    for i in range(len(B)- len(A) +1):
        result = getSum(i)
        if result>Max:
          Max=result
        #   Max-max(Max,result)



    print(f'#{tc} {Max}')