def solution(res):
    global cnt
    if res != "":
        if eval(res) == n:
            cnt += 1
            if cnt == k:
                print(res)
            return
        if eval(res) > n:
            return

    for i in range(1, 4):
        if res == "":
            solution(str(i))
        else:
            solution(res + "+" + str(i))

n, k = map(int, input().split())
cnt = 0
solution("")

if cnt < k:
    print(-1)