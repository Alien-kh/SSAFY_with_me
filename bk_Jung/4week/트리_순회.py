class Node:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right

def preorder(node):
    if node.data!='.': print(node.data,end = "")
    if node.left != '.': preorder(tree[node.left])
    if node.right != '.': preorder(tree[node.right])

def inorder(node):
    if node.left != '.': inorder(tree[node.left])
    if node.data!='.': print(node.data,end = "")
    if node.right != '.': inorder(tree[node.right])

def postorder(node):
    if node.left != '.': postorder(tree[node.left])
    if node.right != '.': postorder(tree[node.right])
    if node.data!='.': print(node.data,end = "")
N = int(input())
tree = {}

for i in range(N):
    data,left,right = map(str,input().split())
    tree[data] = Node(data,left,right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
print()