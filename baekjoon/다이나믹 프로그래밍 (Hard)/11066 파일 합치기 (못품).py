t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # d[i][j]: a[i] 부터 a[j]까지 파일을 합칠 때의 최소 비용
