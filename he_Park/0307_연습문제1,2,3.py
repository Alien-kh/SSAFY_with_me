# 연습문제 1
N = input()
for i in range(0, len(N), 7):
    print(int('0b'+N[i:i+7], 2), end=' ')

# 연습문제 2
N = '1D06079861D79F99F'
bin_num = ''
for x in N:
   h = int(x, 16)
   b = bin(h)
   b = b[2:]
   while True:
       if len(b) < 4:
           b = '0' + b
       else:
           break
   bin_num += b
for i in range(0, len(bin_num), 7):
    print(int(bin_num[i:i+7], 2), end=' ')

# 연습문제 3
def solve():
    global idx
    for i in range(N - M + 1):
        for j in p:
            for k in range(M):
                if j[k] != bin_num[i+k]:
                    break
            else:
                idx = i
                return p.index(j)
    return '암호가 없습니다'

t = '0269FAC9A0'
bin_num = ''
for x in t:
   h = int(x, 16)
   b = bin(h)
   b = b[2:]
   while True:
       if len(b) < 4:
           b = '0' + b
       else:
           break
   bin_num += b

p = ['001101', '010011', '111011', '110001', '100011', '110111', '001011', '111101', '011001', '101111']
N = len(bin_num)
M = 6
print(solve(), end=' ')
while True:
    idx += M
    if idx > N:
        break
    if bin_num[idx:idx+M] in p:
        print(p.index(bin_num[idx:idx+M]), end=' ')