# 숫자는 뒤집을 수 없으니 str로 입력받아서 뒤집고 int로변환하기
A, B = input().split()

A, B = int(A[::-1]), int(B[::-1])

if A > B :
    print(A)
elif A < B :
    print(B)
