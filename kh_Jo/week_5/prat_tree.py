# # 이진 트리에 포화 이진 트리에
# # 번호를 매기는 방식으로 적용
# # 루트 노드 : 1
# # 왼쪽 자식 : 부모 번호 *2
# # 오른쪽 자식은 : 부모 번호 * 2 + 1
# H = 2
# V = 2 ** (H+1)
# tree = [None] * V
#
# tree[1] = 'S'
# tree[2] = 'S'
# tree[3] = 'A'
# tree[4] = 'F'
# tree[5] = 'Y'
# tree[6] = '!'
# tree[7] = '!'
# print(tree)
#
# tree_value = [None] * V
# tree_value[5] = 'S'
# tree_value[1] = 'S'
# tree_value[2] = 'A'
# tree_value[3] = 'F'
# tree_value[7] = 'Y'
# tree_value[6] = '!'
# tree_value[4] = '!'
#
# print(tree_value)
# # 인접 리스트 형태로 저장 가능
# tree = [[] * V for _ in range(V)]
# tree[1] = [3, 7]
# tree[2] = [6, 4]
# tree[5] = [1, 2]
#
# # 부모 번호를 인덱스로
# # 왼쪽 자식과 오른쪽 자식을 저장
# left = [None] * V
# right = [None] * V
# left[5] = 1
# right[5] = 2
# left[1] = 3
# right[1] = 7
# left[2] = 6
# right[2] = 4
# print(left)
# print(right)
#
# # 자식 번호를 인덱스로 부모 번호를 저장
# parent = [None] * V
# parent[1] = 5
# parent[2] = 5
# parent[3] = 1
# parent[4] = 2
# parent[6] = 2
# # 트리 저장은 배열에 함
# left = [None] * 16
# right= [None] * 16
# left[1] = 2
# right[1] = 3
# left[2] = 4
# left[3] = 6
# right[3] = 7
# left[6] = 12
# right[6] = 13
#
# # 트리의 모든 노득를 순회
# # 전위 순회 : 루트노드에서 작업처리(방문) 하고, 왼쪽 서브트리, 오른쪽 서브트리 순서로 방문
# # v번 노드에서 작업 처리하기
# def preorder(v):
#     if v is None:
#         return
#     print(v, end=' ')
#     preorder(left[v]) # 재귀는 일종의 dfs
#     preorder(right[v])
#
# preorder(1)
# # 중위 순회
# # v번에서 작업처리
# def inorder(v):
#     if v is None:
#         return
#     preorder(left[v])
#     print(v, end=' ')
#     preorder(right[v])
#
# inorder(1)
#
# # 후위 순회
# def postorder(v):
#     if v is None:
#         return
#     preorder(left[v])
#     preorder(right[v])
#     print(v, end=' ')
#
# preorder(1)
# 최대힙

def enq(n):
    global last
    last += 1       # 마지막 정점 추가
    heap[last] = n  # 마지막 정점에 key 추가

    c = last
    p = c // 2      # 완전이진트리에서 부모 정점 번호
    while p and heap[p] < heap[c]: # 부모가 있고, 부모 < 자식 인경우 자리 교환
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2

def deq():
    global last
    tmp = heap[1]           # 루트 백업
    heap[1] = heap[last]    # 삭제할 노드의 키를 루트에 복사
    last -= 1               # 마지막 노드 삭제
    p = 1                   # 루트에 옮긴 값을 자식과 비교
    c = p * 2               # 왼쪽 자식
    while c <= last:        # 자식이 하나라도 있으면
        if c+1 <= last and heap[c] < heap[c+1]: # 오른쪽 자식도 있고, 오른쪽 자식이 더 크면
            c += 1                      # 비교 대상을 오른쪽 자식으로 정함
        if heap[p] < heap[c]:   # 자식이 더 크면 최대힙 규칙에 어긋나므로
            heap[p], heap[c] = heap[c], heap[p]
            p = c               # 자식을 새로운 부모로
            c = p * 2           # 왼쪽 자식 번호를 계산
        else:                   # 부모가 더 크면
            break               # 비교 중단,
    return tmp

heap = [0] * 100
last = 0

enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(6)
while last:
    print(deq())