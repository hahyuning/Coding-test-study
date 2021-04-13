import sys
input = sys.stdin.readline

n, m = map(int, input().split())
name_dic = {}

for _ in range(n):
    name = input().strip()
    name_dic[name] = 1

for _ in range(m):
    name = input().strip()
    if name in name_dic:
        name_dic[name] -= 1

name_list = []
res = 0

for name, cnt in name_dic.items():
    if cnt == 0:
        res += 1
        name_list.append(name)

name_list.sort()

print(res)
for x in name_list:
    print(x)