from collections import deque, defaultdict

def solution(tickets):
    tickets.sort(reverse=True)
    a = defaultdict(list)
    for x, y in tickets:
        a[x].append(y)

    q = deque()
    q.append("ICN")

    # 리프 노드 -> 루트 노드 순으로 저장
    path = []
    while q:
        now = q.pop()
        # now 가 리프 노트인 경우
        if now not in a or not a[now]:
            path.append(now)
        # 더 탐색할 수 있는 경우 큐에 다음 경로 삽입
        else:
            q.append(now)
            q.append(a[now].pop())
    path.reverse()
    return path

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))