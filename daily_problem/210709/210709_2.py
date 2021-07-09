n = input()
if "0" not in n:
    print(-1)
else:
    s = 0
    for x in n:
        s += int(x)
    if s % 3 != 0:
        print(-1)
    else:
        num_list = list(map(int, list(n)))
        num_list.sort(reverse=True)
        print("".join(map(str, num_list)))