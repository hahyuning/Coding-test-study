from collections import deque

def solution(csv_string, keyword):
    answer = 0
    csv_list = csv_string.split("\n")
    team_list = csv_list[1:]
    n = len(csv_list)

    names = dict()
    graph = [[] for _ in range(n + 1)]
    numbers = [0] * (n + 1)

    for x in team_list:
        tmp = x.split(",")

        id, name, parent_id, num = tmp
        id = int(id)
        num = int(num)
        names[name] = id
        numbers[id] = num

        if id == 1:
            continue
        parent_id = int(parent_id)
        graph[parent_id].append(id)

    res = 0
    check = [False] * (n + 1)
    for x in names:
        if keyword in x and not check[names[x]]:

            q = deque()
            q.append(names[x])
            check[names[x]] = True

            while q:
                now = q.popleft()
                res += numbers[now]
                for nxt in graph[now]:
                    if not check[nxt]:
                        check[nxt] = True
                        q.append(nxt)

    return (res if res != 0 else -1)


print(solution("조직 ID,조직명,상위 조직 ID,소속 팀원 수\n1,토스팀,,1\n2,인터널 트라이브,1,1\n3,인터널 매니저 팀,2,7\n4,비바 플랫폼 팀,2,14\n5,아웃터널 트라이브,1,2\n6,가이드 팀,5,4\n7,피트아웃 사일로,5,11", "아웃"))
