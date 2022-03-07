s = input().replace("-", " ").split(" ")
vowel = ["a", "e", "i", "o", "u", "h"]
prefix = ["c", "j", "n", "m", "t", "s", "l", "d", "qu"]

cnt = 0
for x in s:
    if "'" not in x:
        cnt += 1
        continue

    idx = x.index("'")
    if x[:idx] not in prefix:
        cnt += 1
    else:
        if x[idx + 1] in vowel:
            cnt += 2
        else:
            cnt += 1
print(cnt)