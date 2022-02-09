n = int(input())
a = [int(input()) for _ in range(n)]
a.sort()

negative = []
positive = []
ans = []
for x in a:
    if x <= 0:
        negative.append(x)
    elif x == 1:
        ans.append(x)
    else:
        positive.append(x)

if len(negative) % 2 == 0:
    for i in range(0, len(negative), 2):
        ans.append(negative[i] * negative[i + 1])
else:
    for i in range(0, len(negative) - 1, 2):
        ans.append(negative[i] * negative[i + 1])
    ans.append(negative[-1])

positive.reverse()
if len(positive) % 2 == 0:
    for i in range(0, len(positive), 2):
        ans.append(positive[i] * positive[i + 1])
else:
    for i in range(0, len(positive) - 1, 2):
        ans.append(positive[i] * positive[i + 1])
    ans.append(positive[-1])

print(sum(ans))