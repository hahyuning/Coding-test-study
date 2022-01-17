c, n = map(int, input().split())
cost, customer = [], []
for _ in range(n):
    a, b = map(int, input().split())
    cost.append(a)
    customer.append(b)

d = [0] * (1000 * 100 + 1)
for i in range(n):
    for j in range(len(d)):
        if j - cost[i] >= 0:
            d[j] = max(d[j], d[j - cost[i]] + customer[i])

for i in range(len(d)):
    if d[i] >= c:
        print(i)
        break
