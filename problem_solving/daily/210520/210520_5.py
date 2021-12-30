n = int(input())
a = list(map(int, input().split()))
left = 0
right = n - 1
min_val = abs(a[left] + a[right])
ans = [a[left], a[right]]

while left < right:
    mix = a[left] + a[right]
    if abs(mix) < min_val:
        min_val = abs(mix)
        ans = [a[left], a[right]]

    if mix > 0:
        right -= 1
    elif mix < 0:
        left += 1
    else:
        break

print(" ".join(map(str, ans)))
