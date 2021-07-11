from bisect import bisect_left

t = int(input())
for _ in range(t):
    # k: 보트의 특정값, n: 각 반의 학생수
    k, n = map(int, input().split())
    students = [list(map(int, input().split())) for _ in range(4)]
    a = []
    b = []
    for i in range(n):
        for j in range(n):
            a.append(students[0][i] + students[1][j])
            b.append(students[2][i] + students[3][j])
    b.sort()

    ans = a[0] + b[0]
    for x in a:
        target = k - x
        idx = bisect_left(b, target)
        if idx == 0:
            tmp = b[0] + x
        elif idx == n * n:
            tmp = b[-1] + x
        else:
            tmp1 = b[idx - 1] + x
            tmp2 = b[idx] + x
            if abs(k - tmp1) <= abs(k - tmp2):
                tmp = tmp1
            else:
                tmp = tmp2

        if abs(k - tmp) <= abs(k - ans):
            if abs(k - tmp) == abs(k - ans):
                ans = min(ans, tmp)
            else:
                ans = tmp
    print(ans)