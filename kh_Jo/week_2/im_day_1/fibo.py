def solve(n):
    if n ==1:
        return 1
    if n ==0:
        return 0
    return solve(n-1) + solve(n-2)



N = int(input())
result = solve(N)
print(result)