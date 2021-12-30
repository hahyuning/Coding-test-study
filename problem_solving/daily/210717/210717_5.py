def solution(b, l):
    if l == 2:
        tmp = []
        for i in range(2):
            for j in range(2):
                tmp.append(b[i][j])
        tmp.sort(reverse=True)
        print(tmp[1])
        return

    c = [[0] * (l // 2) for _ in range(l // 2)]
    for i in range(0, l, 2):
        for j in range(0, l, 2):
            tmp = []
            tmp.append(b[i][j])
            tmp.append(b[i][j + 1])
            tmp.append(b[i + 1][j])
            tmp.append(b[i + 1][j + 1])
            tmp.sort(reverse=True)
            c[i // 2][j // 2] = tmp[1]

    solution(c, l // 2)

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
solution(a, n)

