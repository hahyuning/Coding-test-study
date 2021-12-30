from collections import defaultdict
n = int(input())
password = [input() for _ in range(n)]
check = defaultdict(int)
for x in password:
    check[x] += 1
    check[x[::-1]] += 1


a = sorted(check.items(), key=lambda x:x[1], reverse=True)
m = len(a[0][0])
print(m, a[0][0][m // 2])