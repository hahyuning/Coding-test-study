import sys
input = sys.stdin.readline

n, m = map(int, input().split())

groups = dict()
members = dict()
for _ in range(n):
    team = input().rstrip()
    num = int(input())
    member = [input().rstrip() for _ in range(num)]
    groups[team] = sorted(member)

    for x in member:
        members[x] = team

for _ in range(m):
    name = input().rstrip()
    q = int(input())

    if q == 0:
        for x in groups[name]:
            print(x)
    else:
        print(members[name])
