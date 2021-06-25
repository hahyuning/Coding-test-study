lst = []
while True:
    tmp = list(map(int, input().split()))
    if tmp:
        if tmp[-1] == -1 and tmp[-2] == -1:
            break
        else:
            lst += tmp

all_graph = []
graph = dict()
all_node = []
node = dict()
for i in range(0, len(lst), 2):
    if lst[i] == 0 and lst[i + 1] == 0:
        all_graph.append(graph)
        graph = dict()
        all_node.append(node)
        node = dict()
        continue
    if lst[i] in graph:
        graph[lst[i]].append(lst[i + 1])
    else:
        graph[lst[i]] = [lst[i + 1]]

    if lst[i] not in node:
        node[lst[i]] = 0
    if lst[i + 1] not in node:
        node[lst[i + 1]] = 1
    else:
        node[lst[i + 1]] += 1

for i, g in enumerate(all_graph, start=1):
    # 1. 루트 노드 1개
    # 2. 나머지 노드 간선 1개
    # 3. 경로 유일

    n = len(all_node[i - 1].keys())
    if n == 0:
        print("Case " + str(i) + " is a tree.")
    else:
        cnt1 = 0
        cnt2 = False
        for x in all_node[i - 1].values():
            if x == 0:
                cnt1 += 1
            elif x > 1:
                cnt2 = True
        cnt3 = 0
        for x in g.values():
            cnt3 += len(x)

        if cnt1 > 1 or cnt1 == 0:
            print("Case " + str(i) + " is not a tree.")
        elif cnt2:
            print("Case " + str(i) + " is not a tree.")
        else:
            if cnt3 == n - 1:
                print("Case " + str(i) + " is a tree.")
            else:
                print("Case " + str(i) + " is not a tree.")
