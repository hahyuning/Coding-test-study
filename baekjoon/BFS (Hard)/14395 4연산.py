from collections import deque

s, t = map(int, input().split())

# 크기가 10억인 배열을 만드는 것은 비효율적이므로 방문 여부 확인을 위해 set 사용
check = set()
q = deque()
q.append((s, ""))
check.add(s)

while q:
    now, op = q.popleft()
    if now == t:
        if len(op) == 0:
            print("0")
        else:
            print(op)
        exit(0)

    if 0 <= now * now <= 1000000000 and now * now not in check:
        q.append((now * now, op + "*"))
        check.add((now * now))
    if 0 <= now + now <= 1000000000 and now + now not in check:
        q.append((now + now, op + "+"))
        check.add((now + now))
    if 0 not in check:
        q.append((now - now, op + "-"))
        check.add((now - now))
    if now != 0 and 1 not in check:
        q.append((now // now, op + "/"))
        check.add((now // now))

print(-1)
