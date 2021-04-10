def dfs(x):
    # 이미 방문한 곳이면 return
    if check[x] == True:
        return

    result.append(x)
    check[x] = True
    for y in graph[x]:
        dfs(y)

n = int(input())
# 인접 리스트
graph = [[] for _ in range(n)]
# 방문 여부 확인 리스트
check = [False] * n

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

# 확인해야 할 숫자 리스트
target = list(map(int, input().split()))
target = [x - 1 for x in target]

# 타켓의 순서를 기록한 리스트
target_order = [0] * n
for i in range(n):
    target_order[target[i]] = i

# 타켓의 입력 순서대로 인접 리스트 정렬
for i in range(n):
    graph[i].sort(key=lambda x:target_order[x])

# dfs 결과 리스트
result = []
# dfs 실행
dfs(0)

flag = True
for i in range(n):
    if result[i] != target[i]:
        flag = False
        break

print(1 if flag == True else 0)
