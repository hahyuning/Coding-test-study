import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def solution(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    # 후위 순회에서 부모 노드
    parent = postorder[post_end]
    # 전위 순회
    print(parent, end=" ")

    # 왼쪽 인자 개수
    left = pos[parent] - in_start
    # 오른쪽 인자 개수
    right = in_end - pos[parent]
    # 왼쪽 서브트리
    solution(in_start, in_start + left - 1, post_start, post_start + left - 1)
    # 오른족 서브트리
    solution(in_end - right + 1, in_end, post_end - right, post_end - 1)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

pos = [0] * (n + 1)
for i in range(n):
    pos[inorder[i]] = i
solution(0, n - 1, 0, n - 1)