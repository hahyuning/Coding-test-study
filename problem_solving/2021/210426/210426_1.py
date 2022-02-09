import sys
input = sys.stdin.readline

common, *vars = input().rstrip().split(" ")
for i in range(len(vars)):
    var = list(vars[i][:-1])

    if len(var) == 1:
        print(common + " " + str(var[0]) + ";")
        continue

    index = -1
    for j, x in enumerate(var):
        if x in ["[", "]", "&", "*"]:
            index = j
            break

    if index == -1:
        print(common + " " + "".join(var) + ";")
        continue

    v = "".join(var[:index])
    additional = var[index:]
    for j in range(len(additional)):
        if additional[j] == "[":
            additional[j] = "]"
        elif additional[j] == "]":
            additional[j] = "["

    print(common + "".join(additional[::-1]) + " " + v + ";")

