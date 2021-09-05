import heapq, sys

input = sys.stdin.readline

n = int(input())
left = []
right = []
for _ in range(n):
    x = int(input())
    if len(left) == len(right):
        heapq.heappush(left, (-x, x))
    else:
        heapq.heappush(right, (x, x))

    if len(left) >= 1 and len(right) >= 1 and right[0][1] < left[0][1]:
        max_val = heapq.heappop(left)[1]
        min_val = heapq.heappop(right)[1]
        heapq.heappush(left, (-min_val, min_val))
        heapq.heappush(right, (max_val, max_val))
    print(left[0][1])