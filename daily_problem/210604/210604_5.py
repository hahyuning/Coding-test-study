n = int(input())
# graph[i]: i번째 작업에 필요한 선수 작업 저장
graph = [[] for _ in range(n + 1)]
# time[i]: i번째 작업을 마치는데 까지 필요한 최소 시간
time = [0] * (n + 1)
for i in range(1, n + 1):
    t, m, *a = map(int, input().split())
    time[i] = t
    for x in a:
        graph[i].append(x)

for i in range(1, n + 1):
    if graph[i]:
        tmp = 0
        # 이전 작업들 중 최대 시간 저장
        for x in graph[i]:
            tmp = max(tmp, time[x])
        time[i] += tmp

print(max(time))
