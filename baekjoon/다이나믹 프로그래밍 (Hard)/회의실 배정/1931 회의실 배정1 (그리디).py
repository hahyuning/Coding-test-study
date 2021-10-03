n = int(input())
a = []
for _ in range(n):
    s, e = map(int, input().split())
    a.append((e, s))
a.sort()

end_time = 0
cnt = 0
for e, s in a:
    if s >= end_time:
        end_time = e
        cnt += 1
print(cnt)