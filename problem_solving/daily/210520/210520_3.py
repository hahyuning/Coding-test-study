from collections import deque

t = int(input())
for _ in range(t):
    command = input()
    n = int(input())
    a = input()
    a = a[1:-1]
    b = a.split(',')
    q = deque()
    for x in b:
        if x != "":
            q.append(int(x))

    check = False
    revers_check = False
    i = 0
    while i < len(command):
        if command[i] == "R":
            cnt = 1
            for j in range(i + 1, len(command)):
                if command[j] == "R":
                    cnt += 1
                else:
                    break
            if cnt % 2 == 1:
                revers_check = not revers_check
            i += cnt
        else:
            if len(q) == 0:
                check = True
                break

            if revers_check == False:
                q.popleft()
            else:
                q.pop()
            i += 1

    q = list(q)
    if not check:
        if revers_check:
            q.reverse()

        ans = ",".join(map(str, q))
        print("[" + ans + "]")
    else:
        print("error")