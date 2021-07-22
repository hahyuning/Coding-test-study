def solution(i, j):
    if i > n:
        return
    if d[i][j]:
        return

    d[i][j] = True
    solution(i + 1, abs(j - coins[i + 1]))
    solution(i + 1, j)
    solution(i + 1, j + coins[i + 1])


n = int(input())
coins = [0] + list(map(int, input().split())) + [0]
# d[i][j]: i번째 추에서 j의 무게를 가지는지의 여부
d = [[False] * (n * 500 + 1) for _ in range(n + 1)]
solution(0, 0)

m = int(input())
check = list(map(int, input().split()))
for x in check:
    if x > 15000:
        print("N", end=" ")
        continue

    if d[n][x]:
        print("Y", end=" ")
    else:
        print("N", end=" ")