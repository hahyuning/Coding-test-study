from collections import defaultdict

while True:
    n, m = map(int, input().split())
    if n == 0:
        break

    score = defaultdict(int)
    for _ in range(n):
        tmp = list(map(int, input().split()))
        for i in range(m):
            score[tmp[i]] += 1

    res = []
    for key, val in score.items():
        res.append((val, key))
    res.sort(key=lambda x:(-x[0], x[1]))

    second = res[1][0]
    for x in res:
        if x[0] == second:
            print(x[1], end=" ")
    print()