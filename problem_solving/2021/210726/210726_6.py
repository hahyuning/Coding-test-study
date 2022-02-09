import heapq

n = int(input())
m = list(map(int, input().split()))
w = list(map(int, input().split()))

m_minus = []
m_plus = []
w_minus = []
w_plus = []
for x, y in zip(m, w):
    if x < 0:
        heapq.heappush(m_minus, -x)
    else:
        heapq.heappush(m_plus, x)
    if y < 0:
        heapq.heappush(w_minus, -y)
    else:
        heapq.heappush(w_plus, y)

ans = 0
while m_minus and w_plus:
    x = heapq.heappop(m_minus)
    y = w_plus[0]
    if y < x:
        ans += 1
        heapq.heappop(w_plus)

while w_minus and m_plus:
    x = heapq.heappop(w_minus)
    y = m_plus[0]
    if x > y:
        ans += 1
        heapq.heappop(m_plus)
print(ans)