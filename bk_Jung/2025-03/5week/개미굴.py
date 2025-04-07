def insert(tree,path):
    node = tree
    for i in path:
        if i not in node:
            node[i] = {}
        node = node[i]

def preorder(tree,depth):
    for k in sorted(tree.keys()):
        print('--' * depth + k)
        preorder(tree[k],depth+1)

N = int(input())
tree = {}
for i in range(N):
    data = input().split()
    insert(tree,data[1:])


preorder(tree,0)