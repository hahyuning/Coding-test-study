import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def solution(start, end):
    if start > end:
        return

    # 부모 노드
    parent = tree[start]
    # 루트 노드보다 커지는 지점 찾기
    idx = start + 1
    while idx <= end:
        if parent < tree[idx]:
            break
        idx += 1

    # 왼쪽 서브트리
    solution(start + 1, idx - 1)
    # 오른족 서브트리
    solution(idx, end)
    # 후위 순회
    print(tree[start])

tree = []
while True:
    try:
        tmp = int(input())
        tree.append(tmp)
    except:
        break
solution(0, len(tree) - 1)