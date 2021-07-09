import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def solution(root, start, end):
    if start > end:
        return

    for i in range(start, end):
        if inorder[i] == preorder[root]:
            # 왼쪽 서브트리
            solution(root + 1, start, i)
            # 오른쪽 서브트리
            solution(root + i + 1 - start, i + 1, end)
            # 후외 순회
            print(preorder[root], end=" ")

t = int(input())
for _ in range(t):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    solution(0, 0, n)
    print()