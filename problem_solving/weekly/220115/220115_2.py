n = int(input())
time = 0
win = -1
ans1 = 0
ans2 = 0
cnt1 = 0
cnt2 = 0
for _ in range(n):
    team, t = input().split()
    team = int(team)
    m, s = t.split(":")
    t = int(m) * 60 + int(s)

    if team == 1:
        cnt1 += 1
    else:
        cnt2 += 1

    if cnt1 > cnt2:
        if win == 1:
            continue
        time = t
        if win == 2:
            ans2 += t - time
        win = 1
    elif cnt1 < cnt2:
        if win == 2:
            continue
        time = t
        if win == 1:
            ans1 += t - time
        win = 2
    else:
        if win == 1:
            ans1 += t - time
        elif win == 2:
            ans2 += t - time
        win = -1

if cnt1 > cnt2:
    ans1 += 48 * 60 - time
elif cnt1 < cnt2:
    ans2 += 48 * 60 - time

def print_time(num):
    m = str(num // 60).zfill(2)
    s = str(num % 60).zfill(2)
    print(m + ":" + s)

print_time(ans1)
print_time(ans2)

