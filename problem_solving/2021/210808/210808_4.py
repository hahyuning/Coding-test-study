def find_g():
    global g_cnt

    for i in range(1, n + 1):
        if connectd[i] >= 3:
            g_cnt += (connectd[i] * (connectd[i] - 1) * (connectd[i] - 2)) // 6

def find_d():
    global d_cnt

    for now in range(1, n + 1):
        if connectd[now] <= 1:
            continue

        for nxt in tree[now]:
            if nxt < now:
                continue
            if connectd[nxt] <= 1:
                continue
            d_cnt += (connectd[now] - 1) * (connectd[nxt] - 1)

n = int(input())
tree = [[] for _ in range(n + 1)]
connectd = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    connectd[a] += 1
    connectd[b] += 1

d_cnt = 0
g_cnt = 0

find_d()
find_g()

if d_cnt > 3 * g_cnt:
    print("D")
elif d_cnt < 3 * g_cnt:
    print("G")
else:
    print("DUDUDUNGA")