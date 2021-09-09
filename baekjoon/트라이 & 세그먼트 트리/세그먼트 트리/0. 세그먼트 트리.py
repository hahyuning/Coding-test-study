import math

# 세그먼트 트리 초기화
def init():
    for i in range(size - 1, 0, -1):
        tree[i] = tree[i * 2] + tree[i * 2 + 1]

# 세그먼트 트리 값 변경
def change(index, val):
    index += size - 1
    tree[index] = val

    while index > 1:
        index //= 2
        tree[index] = tree[index * 2] + tree[index * 2 + 1]

# 세그먼트 트리 부분합 구하기
def partial_sum(start, end, start_node, end_node, node_num):
    # 부분합을 구하려는 범위가 주어진 범위를 벗어나는 경우
    if start > end_node or end < start_node:
        return 0
    if start <= start_node and end >= end_node:
        return tree[node_num]

    mid = (start_node + end_node) // 2
    res = partial_sum(start, end, start_node, mid, node_num * 2) + partial_sum(start, end, mid + 1, end_node, node_num * 2 + 1)
    return res

# m: 수의 변경이 일어나는 횟수, k: 구간합을 구하는 횟수
n, m, k = map(int, input().split())

# 트리의 필요한 노드의 개수  2^(log(n)+1)-1
size = 2 ** math.ceil(math.log(n, 2))
max_size = size * 2
tree = [0] * max_size
for i in range(n):
    tree[size + i] = int(input())

# 트리 초기화
init()

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        change(b, c)
    else:
        print(partial_sum(b - 1, c - 1, 0, size - 1, 1))