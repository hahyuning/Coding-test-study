from collections import deque

n, k = map(int, input().split())
num_list = deque([i for i in range(1, n + 1)])

ans = "<"
i = 1
while num_list:
    x = num_list.popleft()
    if i % k == 0:
        ans += str(x) + ", "
    else:
        num_list.append(x)
    i += 1

ans = ans[:-2]
ans += ">"
print(ans)