n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    # 단절점인지
    if t == 1:
        if len(graph[k]) > 1:
            print("yes")
        else:
            print("no")
    # 단절선인지
    else:
        print("yes")