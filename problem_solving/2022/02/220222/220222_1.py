from collections import Counter

n, k = map(int, input().split())
public = list(map(int, input().split()))
team = list(map(int, input().split()))
check = Counter(team)

prod = [(x * y, y) for x in public for y in team]
prod.sort()

while k > 0:
    num, i = prod.pop()
    if check[i] <= 0:
        continue
    else:
        check[i] -= 1
        k -= 1

while check[prod[-1][1]] <= 0:
    prod.pop()

print(prod[-1][0])