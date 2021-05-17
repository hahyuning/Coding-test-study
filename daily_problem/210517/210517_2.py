import heapq
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    while len(a) < n:
        b = list(map(int, input().split()))
        a += b

    # 최대 힙, 최소 힙
    left, right = [], []
    # 정답 리스트
    ans = []

    median = a[0]
    ans.append(median)
    for i in range(1, n):
        if a[i] < median:
            heapq.heappush(left, -a[i])
        else:
            heapq.heappush(right, a[i])

        if i % 2 == 0:
            if len(left) > len(right):
                heapq.heappush(right, median)
                median = -heapq.heappop(left)
            elif len(left) < len(right):
                heapq.heappush(left, -median)
                median = heapq.heappop(right)
            ans.append(median)

    print(len(ans))
    for i in range(len(ans)):
        print(ans[i], end=" ")
        if i % 10 == 9:
            print()
    print()



