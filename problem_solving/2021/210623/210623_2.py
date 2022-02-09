n, m = map(int, input().split())
k, *true = map(int, input().split())
parties = []
for _ in range(m):
    x, *y = map(int, input().split())
    parties.append(set(y))

if k == 0:
    print(m)
else:
    true_set = set(true)
    check = [True] * m
    for _ in range(m):
        for i, party in enumerate(parties):
            if len(party.intersection(true_set)) > 0:
                tmp = list(party.difference(true_set))
                for x in tmp:
                    true_set.add(x)
                check[i] = False
    print(sum(check))