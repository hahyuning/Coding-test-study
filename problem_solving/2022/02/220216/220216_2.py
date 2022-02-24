import heapq, sys
input = sys.stdin.readline


n = int(input())
prob = []
rev_prob = []
solved = dict()
for _ in range(n):
    p, l = map(int, input().split())
    heapq.heappush(prob, (l, p))
    heapq.heappush(rev_prob, (-l, -p))
    solved[p] = l

m = int(input())
for _ in range(m):
    op, *num = input().rstrip().split()
    num = list(map(int, num))

    if op == "recommend":
        if num[0] == -1:
            while prob[0][0] != solved[prob[0][1]]:
                heapq.heappop(prob)
            print(prob[0][1])
        else:
            while -rev_prob[0][0] != solved[-rev_prob[0][1]]:
                heapq.heappop(rev_prob)
            print(-rev_prob[0][1])

    elif op == "add":
        p, l = num
        heapq.heappush(prob, (l, p))
        heapq.heappush(rev_prob, (-l, -p))
        solved[p] = l
    else:
        solved[num[0]] = 0