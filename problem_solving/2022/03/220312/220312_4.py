def solution(width, height, diagonals):
    d = [[[0, 0] for _ in range(width + 1)] for _ in range(height + 1)]
    lim = 10000019

    for i in range(len(diagonals)):
        diagonals[i] = [height - diagonals[i][1], diagonals[i][0]]

    for j in range(width + 1):
        d[-1][j][0] = 1

    for i in range(height, -1, -1):
        d[i][0][0] = 1

    d[-1][0][0] = 0

    # for row in d:
    #     print(row)

    for i in range(height - 1, -1, -1):
        for j in range(1, width + 1):
            d[i][j][0] = (d[i + 1][j][0] + d[i][j - 1][0]) % lim
            d[i][j][1] = (d[i + 1][j][1] + d[i][j - 1][1])

            if [i, j] in diagonals:
                d[i][j][1] += (d[i][j - 1][0] + d[i + 1][j][0])
            else:
                if [i + 1, j] in diagonals:
                    d[i][j][1] += max(1, d[i + 2][j - 1][0])
                if [i, j - 1] in diagonals:
                    d[i][j][1] += max(1, d[i + 1][j - 2][0])

            d[i][j][1] %= lim

            print(i, j)
            for row in d:
                print(row)
            print("-----------------------")

    print(d[0][width])
    return d[0][width][1]

solution(3, 3, [[2, 2]])
# solution(51, 37, [[17, 19]])