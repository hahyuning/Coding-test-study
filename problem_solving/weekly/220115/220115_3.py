from collections import defaultdict
from copy import deepcopy

n = int(input())
target = input()
s = [input() for _ in range(n - 1)]

word = defaultdict(int)
for x in target:
    word[x] += 1

ans = 0
for comp in s:
    if abs(len(comp) - len(target)) > 1:
        continue

    word_copy = deepcopy(word)
    for x in comp:
        word_copy[x] -= 1

    check = False
    cnt = [0, 0]
    for x in word_copy:
        if word_copy[x] == 0:
            continue

        if word_copy[x] == 1:
            cnt[1] += 1
        elif word_copy[x] == -1:
            cnt[0] += 1
        else:
            check = True
            break

    if sum(cnt) > 2:
        check = True

    if not check:
        ans += 1
print(ans)
