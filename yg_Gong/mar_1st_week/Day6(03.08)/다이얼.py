phone = ['','','','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

word = input().strip()
time = 0
for i, val in enumerate(phone):
    for j in range(len(word)):
        if word[j] in val:
            time += i

print(time)