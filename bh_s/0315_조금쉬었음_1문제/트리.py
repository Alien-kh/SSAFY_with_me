def preorder(node):
    if node == '.':
        return ''
    result = node
    result += preorder(tree[node][0])  # 왼쪽 자식
    result += preorder(tree[node][1])  # 오른쪽 자식
    return result

def inorder(node):
    if node == '.':
        return ''
    result = inorder(tree[node][0])  # 왼쪽 자식
    result += node                    # 루트
    result += inorder(tree[node][1])  # 오른쪽 자식
    return result

def postorder(node):
    if node == '.':
        return ''
    result = postorder(tree[node][0])  # 왼쪽 자식
    result += postorder(tree[node][1])  # 오른쪽 자식
    result += node                      # 루트
    return result


N = int(input()) 
tree = {}

for _ in range(N):
    node, left, right = input().split()
    tree[node] = (left, right)

# 루트는 항상 'A'이므로 'A'를 시작점으로 순회
print(preorder('A'))
print(inorder('A'))
print(postorder('A'))