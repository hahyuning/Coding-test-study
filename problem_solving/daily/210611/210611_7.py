def next_permutation():

    i = n - 1
    while i > 0 and s[i - 1] >= s[i]:
        i -= 1
    if i <= 0:
        return False

    j = n - 1
    while s[j] <= s[i - 1]:
        j -= 1

    s[i - 1], s[j] = s[j], s[i - 1]

    j = n - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1

    return True

t = int(input())
for _ in range(t):
    s = list(input().rstrip())
    s.sort()
    n = len(s)
    print("".join(s))

    while True:
        if next_permutation():
            print("".join(s))
        else:
            break