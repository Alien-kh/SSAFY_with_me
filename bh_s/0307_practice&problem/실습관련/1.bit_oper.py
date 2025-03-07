# print(7 & 5)
# print(7 | 5)
# print(bin(7 & 5))
#
# 1. 이진수로 변환
# 2 . 각 자리를 AND, OR 연산

# 1 * 3
# 16 * 10
# 16^2 * 4
#
# print(bin(0x4A3 | 25))
#
# secret_code = 1004
# print (7070 ^ secret_code)
# print (6258 ^ secret_code)
#
#
# ---------------shift 연산자
#
# print(1 << 1, bin(1 << 1))  # 2
# print(1 << 2, bin(1 << 2))  # 4
# print(1 << 3, bin(1 << 3))  # 8
# print(1 << 4, bin(1 << 4))  # 16
#
# print (7 >> 1)  # 3
#
# num = 1
# for _ in range(5):
#     print(num, bin(num))
#     num = num << 1


# -------------------- bit 연산 응용
# 1. 부분 집합의 수를 바로 구할 수 있다.

# arr = [1,2,3,4]     # 16개의 부분집합.
#
# print(f'부분 집합의 수: {1 << len(arr)}')
#
# for i in range(1 << len(arr)):
#     for idx in range(len(arr)):
#         # (1 << idx) : 0b1, 0b10, 0b100, 0b1000
#         # i번째 부분집합에 특정 숫자가 포함되어 있는지 (i 의 idx 번째 bit가 1인지)
#         if i & (i << idx):
#             print(arr[idx], end=" ")
#     print()

# ------------------- 음수 표현
print(bin(5))
print(bin(-5))

print(~4, bin(~4))  # -5
print(~(-4))    # 3