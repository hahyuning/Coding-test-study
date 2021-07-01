import heapq, sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    # 최대힙
    q1 = []
    # 최소힙
    q2 = []
    check = [False] * 1000001
    for i in range(n):
        op, num = input().rstrip().split()
        num = int(num)
        if op == "I":
            heapq.heappush(q1, (-num, i))
            heapq.heappush(q2, (num, i))
            check[i] = True
        else:
            if num == 1:
                while q1 and not check[q1[0][1]]:
                    heapq.heappop(q1)
                if q1:
                    check[q1[0][1]] = False
                    heapq.heappop(q1)
            else:
                while q2 and not check[q2[0][1]]:
                    heapq.heappop(q2)
                if q2:
                    check[q2[0][1]] = False
                    heapq.heappop(q2)

    # 동기화
    while q1 and not check[q1[0][1]]:
        heapq.heappop(q1)
    while q2 and not check[q2[0][1]]:
        heapq.heappop(q2)

    if q1 and q2:
        print(-q1[0][0], q2[0][0])
    else:
        print("EMPTY")



