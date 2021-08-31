import heapq, sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [input().rstrip() for _ in range(n)]

# 1. 색깔을 정수로 변환
int_to_char = [""] * 100
char_to_int = [-1] * 256

cnt = 0
for i in range(n):
    for j in range(m):
        char = a[i][j]
        if char != ".":
            if char_to_int[ord(char)] == -1:
                char_to_int[ord(char)] = cnt
                int_to_char[cnt] = char
                cnt += 1

# 2. 각 색깔의 크기 구하기
graph = [[False] * cnt for _ in range(cnt)]
for k in range(cnt):
    min_x = n - 1
    max_x = 0
    min_y = m - 1
    max_y = 0

    for i in range(n):
        for j in range(m):
            if a[i][j] == int_to_char[k]:
                min_x = min(min_x, i)
                max_x = max(max_x, i)
                min_y = min(min_y, j)
                max_y = max(max_y, j)

    # 예외 처리
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            if a[i][j] == ".":
                print(-1)
                sys.exit(0)

            if a[i][j] != int_to_char[k]:
                # g[x][y]: x -> y
                graph[k][char_to_int[ord(a[i][j])]] = True

# 3. 위상정렬 수행
indegree = [0] * cnt
for i in range(cnt):
    for j in range(cnt):
        if graph[j][i]:
            indegree[i] += 1

q = []
for i in range(cnt):
    if indegree[i] == 0:
        heapq.heappush(q, int_to_char[i])

ans = ""
while q:
    now = heapq.heappop(q)
    ans += now
    x = char_to_int[ord(now)]

    for y in range(cnt):
        if graph[x][y]:
            indegree[y] -= 1
            if indegree[y] == 0:
                heapq.heappush(q, int_to_char[y])

if len(ans) == cnt:
    print(ans)
else:
    print(-1)
