import sys
sys.setrecursionlimit(10 ** 6)

parent = [-1] * 10001
left = [0] * 10001
right = [0] * 10001
root = -1
cnt = 0

# 그룹 나누기
def dfs(now, mid, num):
    global cnt

    lsum = 0
    rsum = 0

    if left[now] != -1:
        lsum = dfs(left[now], mid, num)
    if right[now] != -1:
        rsum = dfs(right[now], mid, num)

    # 부모노드와 왼쪽 오른쪽 자식노드를 한 그룹에 포함하는 경우
    if num[now] + lsum + rsum <= mid:
        return num[now] + lsum + rsum

    # 부모노드와 한쪽 자식노드만 그룹으로 포함하는 경우
    if num[now] + min(lsum, rsum) <= mid:
        cnt += 1
        return num[now] + min(lsum, rsum)

    # 부모노드와 양쪽 자식노드를 모두 다른 그룹으로 만드는 경우
    cnt += 2
    return num[now]


def solution(k, num, links):
    global root, cnt

    for i in range(len(num)):
        left[i] = links[i][0]
        right[i] = links[i][1]

        if left[i] != -1:
            parent[left[i]] = i
        if right[i] != -1:
            parent[right[i]] = i

    # 루트 노드 찾기
    for i in range(len(num)):
        if parent[i] == -1:
            root = i

    # 이분탐색
    lt = max(num)
    rt = 1e9
    ans = 0
    while lt <= rt:
        mid = (lt + rt) // 2
        cnt = 1
        dfs(root, mid, num)

        if cnt <= k:
            ans = mid
            rt = mid - 1
        else:
            lt = mid + 1

    return ans
