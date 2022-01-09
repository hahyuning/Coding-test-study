a = int(input())
t = int(input())
x = int(input())
student = [i for i in range(a)]

turn = 2
bd = []
total = 0
cnt = 0
while cnt != t:
    bd += [0, 1, 0, 1]

    for _ in range(turn):
        bd.append(0)
    for _ in range(turn):
        bd.append(1)

    if len(bd) // 2 >= t:
        for y in bd:
            total += 1
            if y == x:
                cnt += 1

                if cnt == t:
                    break
    else:
        turn += 1

print(student[total % a - 1])

