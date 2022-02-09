import heapq

n = int(input())
dic = dict()
ans = 0
for _ in range(n):
    a, b, *c = input().split()
    if a == "1":
        if b not in dic:
            q = []
            for x in c[1:]:
                heapq.heappush(q, -int(x))
            dic[b] = q
        else:
            for x in c[1:]:
                heapq.heappush(dic[b], -int(x))
    else:
        if b not in dic:
            continue
        else:
            tmp = dic[b]
            for _ in range(int(c[0])):
                if not tmp:
                    break
                x = heapq.heappop(tmp)
                ans += -x
            dic[b] = tmp
print(ans)


