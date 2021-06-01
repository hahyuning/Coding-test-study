n = int(input())
a = []
for _ in range(n):
    s = input()
    s_list = []
    num = ""
    for x in s:
        if x.isdigit():
            num += x
        else:
            if num != "":
                s_list.append(num)
                num = ""
            s_list.append(x)
    print(s_list)
