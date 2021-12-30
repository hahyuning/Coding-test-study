from collections import defaultdict, deque

n = int(input())
parents = list(map(int, input().split()))
delete = int(input())
tree = defaultdict(list)

for i in range(n):
    if i != delete and parents[i] != delete:
        tree[parents[i]].append(i)

q = deque()
res = 0
if -1 in tree:
    q.append(-1)

while q:
    now = q.popleft()
    if now not in tree:
        res += 1
    else:
        for nxt in tree[now]:
            q.append(nxt)
print(res)