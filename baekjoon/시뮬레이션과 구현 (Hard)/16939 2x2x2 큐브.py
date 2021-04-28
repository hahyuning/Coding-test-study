#           1 2
#           3 4
#     13 14 5 6 17 18 21 22
#     15 16 7 8 19 20 23 24
#           9 10
#           11 12

# ul : 13, 14, 5, 6, 17, 18, 21, 22
# lu : 1, 3, 5, 7, 9, 11, 24, 22
# fl: 3, 4, 17, 19, 10, 9, 16, 14

def ul_rotate(b):
    a = b[:]
    tmp = a[13]
    a[13] = a[5]
    a[5] = a[17]
    a[17] = a[21]
    a[21] = tmp
    tmp = a[14]
    a[14] = a[6]
    a[6] = a[18]
    a[18] = a[22]
    a[22] = tmp
    return a

def lu_rotate(b):
    a = b[:]
    tmp = a[1]
    a[1] = a[5]
    a[5] = a[9]
    a[9] = a[24]
    a[24] = tmp
    tmp = a[3]
    a[3] = a[7]
    a[7] = a[11]
    a[11] = a[22]
    a[22] = tmp
    return a

def fl_rotate(b):
    a = b[:]
    a = b[:]
    tmp = a[3]
    a[3] = a[17]
    a[17] = a[10]
    a[10] = a[16]
    a[16] = tmp
    tmp = a[4]
    a[4] = a[19]
    a[19] = a[9]
    a[9] = a[14]
    a[14] = tmp
    return a

def ur_rotate(b):
    a = b[:]
    a = ul_rotate(a)
    a = ul_rotate(a)
    a = ul_rotate(a)
    return a

def ld_rotate(b):
    a = b[:]
    a = lu_rotate(a)
    a = lu_rotate(a)
    a = lu_rotate(a)
    return a

def fr_rotate(b):
    a = b[:]
    a = fl_rotate(a)
    a = fl_rotate(a)
    a = fl_rotate(a)
    return a

def check(b):
    for i in range(1, 22, 4):
        for j in range(4):
            if b[i] != b[i + j]:
                return False
    return True

colors = [0] + list(map(int, input().split()))

if check(ul_rotate(colors)) or check(lu_rotate(colors)) or check(fl_rotate(colors)) or check(ur_rotate(colors)) or check(ld_rotate(colors)) or check(fr_rotate(colors)):
    print(1)
else:
    print(0)