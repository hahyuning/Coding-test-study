import sys
input = sys.stdin.readline

def count(mid):
    words = []
    for j in range(m):
        word = ""
        for i in range(mid, n):
            word += strs[i][j]
        if word in words:
            return False
        words.append(word)
    return True

n, m = map(int, input().split())
strs = [input().rstrip() for _ in range(n)]

lt = 0
rt = n - 1
ans = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if count(mid):
        ans = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(ans)
