import sys

def dfs(s):
    global ans
    if len(s) == n + 1:
        print(int(s))
        sys.exit(0)

    for i in range(1, 4):
        if i == s[-1]:
            continue
        if check(s + str(i)):
            dfs(s + str(i))

def check(s):
    s = s[1:]
    for l in range(1, len(s) // 2 + 1):
        if s[-l:] == s[-2 * l:-l]:
            return False
    return True

n = int(input())
dfs("0")
