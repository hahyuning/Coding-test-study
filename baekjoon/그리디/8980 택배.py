n, m = map(int, input().split())
k = int(input())
a = [list(map(int, input().split())) for _ in range(k)]
# 도착순서가 빠른 순서대로 정렬
a.sort(key=lambda x:x[1])
ans = 0
# 각 마을에 도착했을 때 트럭의 무게 (최대 m)
truck = [m] * (n + 1)

for i in range(k):
    tmp = m
    # 출발지에서 도착지까지 실을 수 있는 가장 작은 무게 찾기
    for j in range(a[i][0], a[i][1]):
        tmp = min(tmp, truck[j])
    # 박스 싣기
    tmp = min(tmp, a[i][2])
    for j in range(a[i][0], a[i][1]):
        truck[j] -= tmp
    ans += tmp

print(ans)