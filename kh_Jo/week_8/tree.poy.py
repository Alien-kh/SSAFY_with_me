import sys
input = sys.stdin.readline

def find_set(x):
    if x == p[x]:
        return x
    p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    bx = find_set(x)
    by = find_set(y)
    if bx != by:
        p[bx] = by

V, E = map(int, input().split())
tree = []
p = [x for x in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    tree.append((c, a, b))  # (가중치, 노드1, 노드2)

tree.sort()

total_w = 0
cnt = 0
for weight, u, v in tree:
    if find_set(u) != find_set(v):
        union(u, v)
        total_w += weight
        cnt += 1
    if cnt == V - 1:
        break

print(total_w)