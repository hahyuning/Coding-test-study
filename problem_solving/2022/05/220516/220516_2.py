class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def solution(line1, line2):
    a = Point(line1[0], line1[1])
    b = Point(line1[2], line1[3])
    c = Point(line2[0], line2[1])
    d = Point(line2[2], line2[3])

    if ccw(a, b, c) * ccw(a, b, d) == 0 and ccw(c, d, a) * ccw(c, d, b) == 0:
        return comparision2(a, b, c, d)

    return ccw(a, b, c) * ccw(a, b, d) <= 0 and ccw(c, d, a) * ccw(c, d, b) <= 0


def ccw(p1, p2, p3):
    return (p1.x * p2.y + p2.x * p3.y + p3.x * p1.y) - (p1.y * p2.x + p2.y * p3.x + p3.y * p1.x)


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    parent[b] = a

    if a != b:
        cnt[a] += cnt[b]


def comparison(arr1, arr2):
    if arr1 > arr2:
        arr1, arr2 = arr2, arr1
    return arr1 + arr2

def comparision2(a, b, c, d):
    if [a.x, a.y] <= [d.x, d.y] and [c.x, c.y] <= [b.x, b.y]:
        return True
    else:
        return False

if __name__ == '__main__':
    n = int(input())
    lines = [list(map(int, input().split())) for _ in range(n)]
    parent = [i for i in range(n)]
    cnt = [1] * n

    for i in range(n - 1):
        for j in range(i + 1, n):
            lines[i] = comparison(lines[i][:2], lines[i][2:])
            lines[j] = comparison(lines[j][:2], lines[j][2:])
            if solution(lines[i], lines[j]):
                union(i, j)

    ans = 0
    check = [False] * n
    for i in range(n):
        p = find(parent[i])
        if not check[p]:
            check[p] = True
            ans += 1

    print(ans)
    print(max(cnt))



