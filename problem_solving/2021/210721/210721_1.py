def check(num):
    if num == num[::-1]:
        return True
    return False

while True:
    n = input()
    if n == "0":
        break

    m = len(n)
    i = 0
    while True:
        tmp = str(int(n) + i)
        k = len(tmp)
        tmp = "0" * (m - k) + tmp
        if check(tmp):
            print(i)
            break
        i += 1

