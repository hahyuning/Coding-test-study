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

def check():
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            return False
    return True

s = list(input())
s.sort()
n = len(s)
ans = 0
if check():
    ans += 1

while True:
    if next_permutation():
        if check():
            ans += 1
    else:
        break

print(ans)