a = list(map(int, input().split()))

ans = True
for i in range(len(a) - 1):
    if a[i] > a[i + 1]:
        ans = False
        break

print("Good" if ans else "Bad")