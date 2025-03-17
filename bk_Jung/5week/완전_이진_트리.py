def bulid_tree(arr,level,levels):
    if not arr:
        return
    
    mid = len(arr) // 2
    levels[level].append(arr[mid])
    bulid_tree(arr[:mid], level + 1,levels)
    bulid_tree(arr[mid+1:],level+1,levels)

K = int(input())
arr = list(map(int,input().split()))

levels = [[] for _ in range(K)]
bulid_tree(arr,0,levels)
for i in levels:
    print(*i)