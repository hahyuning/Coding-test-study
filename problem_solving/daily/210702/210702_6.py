def zero(idx, res):
    if idx == n:
        tmp = res
        res = res.replace(" ", "")
        if eval(res) == 0:
            print(tmp)
        return

    zero(idx + 1, res + " " + str(idx + 1))
    zero(idx + 1, res + "+" + str(idx + 1))
    zero(idx + 1, res + "-" + str(idx + 1))

t = int(input())
for _ in range(t):
    n = int(input())
    zero(1, "1")
    print()