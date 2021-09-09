def solution(new_id):
    special = ["-", "_", "."]
    step1 = []
    for x in new_id:
        if x.isupper():
            step1.append(x.lower())
        elif x.islower() or x.isdigit() or x in special:
            step1.append(x)

    step2 = []
    i = 0
    prev = 0
    while i < len(step1):
        if step1[i] == ".":
            cnt = 1
            for j in range(i + 1, len(step1)):
                if step1[j] == ".":
                    cnt += 1
                else:
                    break
            if cnt >= 2:
                step2 += step1[prev:i + 1]
            else:
                step2 += "."

            i += cnt
            prev = i
        else:
            step2 += step1[i:i + 1]
            i += 1
            prev = i

    step2 += step1[prev:]

    while step2 and step2[0] == ".":
        step2.pop(0)
    while step2 and step2[-1] == ".":
        step2.pop()

    if len(step2) == 0:
        step2.append("a")
    elif len(step2) > 15:
        step2 = step2[:15]

    while step2 and step2[-1] == ".":
        step2.pop()

    while len(step2) < 3:
        step2.append(step2[-1])

    return "".join(step2)

print(solution("...!@BaT#*..y.abcdefghijklm"))