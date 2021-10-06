def solution(sizes):
    x = []
    y = []
    for i in range(len(sizes)):
        sizes[i].sort()
        x.append(sizes[i][0])
        y.append(sizes[i][1])

    x.sort()
    y.sort()
    return x[-1] * y[-1]