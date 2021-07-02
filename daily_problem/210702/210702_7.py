def password(idx):
    global cnt

    if idx == n:
        if check(ans):
            cnt += 1
        return
    for i in range(10):
        ans[idx] = i
        password(idx + 1)

def check(ans):
    for x in a:
        if x not in ans:
            return False
    return True

n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = [0] * n
cnt = 0
password(0)
print(cnt)