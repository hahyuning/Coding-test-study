from collections import deque

t = int(input())
for _ in range(t):
    n, target = map(int, input().split())
    printer = deque(list(map(int, input().split())))

    ans = 0
    while True:
        now = printer.popleft()
        target -= 1

        # 프린터가 비어있는 경우
        if not printer:
            ans += 1
            break

        # 우선순위가 높은 문서가 프린터에 있는 경우
        if now < max(printer):
            printer.append(now)
            if target < 0:
                target = len(printer) - 1
        else:
            ans += 1
            if target == -1:
                break
    print(ans)