A, B, V = map(int,input().split())
# current = 0 # while을 썼을 때
# day =1
# while current < V:
#     current+=A
#     if current < V:
#         current -= B
#         day += 1
#
#     else:
#         break
if A >= V: # 만약 하루 만에 다 올라가면 +1
    print(1)
else:
    # 마지막 날을 더해주기 위해 +1
    days = ((V-A) + (A-B) -1) //(A-B) + 1# 목적지에 도달하기 전까지는 A-B로 올라가므로/ 그리고 -1은 올림을 위해(정수 나눗셈)을 위해 사용
    print(days)