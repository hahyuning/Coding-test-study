from itertools import combinations_with_replacement

n = int(input())
num = [1, 5, 10, 50]
p = combinations_with_replacement(num, n)
check = dict()
cnt = 0
for x in p:
    y = sum(x)
    if y not in check:
        cnt += 1
        check[y] = 1
print(cnt)