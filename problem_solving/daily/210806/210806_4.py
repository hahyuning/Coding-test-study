from collections import deque

n, w, l = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
bridge = deque([0] * w)
b_weight = 0
truck = deque(a)

while truck:
    b_weight -= bridge.popleft()
    if b_weight + truck[0] <= l:
        b_weight += truck[0]
        bridge.append(truck.popleft())
    else:
        bridge.append(0)
    ans += 1
ans += len(bridge)
print(ans)