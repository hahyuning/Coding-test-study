n = int(input())
a = list(map(int, input().split()))
# d[i][j]: a[i:j + 1] 을 팰린드롬으로 만들기 위해서 추가해야 하는 수의 최소
d = [[-1] * n for _ in range(n)]

def solution(i, j):
    if i >= j:
        return 0

    if d[i][j] != -1:
        return d[i][j]

    if a[i] == a[j]:
        d[i][j] = solution(i + 1, j - 1)
    else:
        d[i][j] = min(solution(i + 1, j), solution(i, j - 1)) + 1
    return d[i][j]

print(solution(0, n - 1))