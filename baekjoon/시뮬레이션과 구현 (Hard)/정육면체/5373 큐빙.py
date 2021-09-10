from copy import deepcopy


#   0       윗면
# 4 1 2     앞면, 옆면
#   5       바닥
#   3

def plane_rotate(a):
    # (0, 0) (0, 1) (0, 2)
    # (1, 0) (1, 1) (1, 2)
    # (2, 0) (2, 1) (2, 2)
    #          |
    #          v
    # (2, 0) (1, 0) (0, 0)
    # (2, 1) (1, 1) (0, 1)
    # (2, 2) (1, 2) (0, 2)

    temp = a[0][0]
    a[0][0] = a[2][0]
    a[2][0] = a[2][2]
    a[2][2] = a[0][2]
    a[0][2] = temp
    temp = a[0][1]
    a[0][1] = a[1][0]
    a[1][0] = a[2][1]
    a[2][1] = a[1][2]
    a[1][2] = temp


def left(a):
    # 0 1 3 5
    temp = deepcopy(a[0])
    for i in range(3):
        a[0][i][0] = a[3][i][0]
        a[3][i][0] = a[5][i][0]
        a[5][i][0] = a[1][i][0]
        a[1][i][0] = temp[i][0]
    plane_rotate(a[4])


def right(a):
    # 0 3 5 1
    temp = deepcopy(a[0])
    for i in range(3):
        a[0][i][2] = a[1][i][2]
        a[1][i][2] = a[5][i][2]
        a[5][i][2] = a[3][i][2]
        a[3][i][2] = temp[i][2]
    plane_rotate(a[2])


def up(a):
    # 0 2 5 4
    temp = deepcopy(a[0])
    a[0] = a[4]
    a[4] = a[5]
    a[5] = a[2]
    a[2] = temp

    plane_rotate(a[5])
    plane_rotate(a[5])
    plane_rotate(a[4])
    plane_rotate(a[4])
    plane_rotate(a[1])
    plane_rotate(a[3])
    plane_rotate(a[3])
    plane_rotate(a[3])


def front(a):
    # 0 1 5 3
    temp = deepcopy(a[1])
    a[1] = a[4]
    a[4] = a[3]
    a[3] = a[2]
    a[2] = temp

    plane_rotate(a[2])
    plane_rotate(a[2])
    plane_rotate(a[2])
    plane_rotate(a[3])
    plane_rotate(a[3])
    plane_rotate(a[3])
    plane_rotate(a[4])
    plane_rotate(a[4])
    plane_rotate(a[4])
    plane_rotate(a[1])
    plane_rotate(a[1])
    plane_rotate(a[1])
    plane_rotate(a[0])
    plane_rotate(a[0])
    plane_rotate(a[0])
    plane_rotate(a[5])


t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    for color in "wrbogy":
        a.append([[color] * 3 for _ in range(3)])

    order = input().split()
    for x in order:
        cnt = 1
        if x[-1] == "-":
            cnt = 3
        if x[0] == "U":
            up(a)
            for _ in range(cnt):
                right(a)
            for _ in range(3):
                up(a)
        elif x[0] == "D":
            up(a)
            for _ in range(cnt):
                left(a)
            for _ in range(3):
                up(a)
        elif x[0] == "F":
            front(a)
            for _ in range(cnt):
                right(a)
            for _ in range(3):
                front(a)
        elif x[0] == "B":
            front(a)
            for _ in range(cnt):
                left(a)
            for _ in range(3):
                front(a)
        elif x[0] == "L":
            for _ in range(cnt):
                left(a)
        else:
            for _ in range(cnt):
                right(a)

    for i in range(3):
        print("".join(a[0][i]))
