def solution(arr):
    global ans
    if len(arr) <= 1:
        return

    min_val = min(arr)
    min_idx = arr.index(min_val)
    if min_idx == 0:
        nxt_val = arr[1]
        arr = arr[1:]
    elif min_idx == len(arr) - 1:
        nxt_val = arr[-2]
        arr = arr[:-1]
    else:
        if abs(min_val - arr[min_idx - 1]) < abs(min_val - arr[min_idx + 1]):
            nxt_val = arr[min_idx - 1]
        else:
            nxt_val = arr[min_idx + 1]
        arr = arr[:min_idx] + arr[min_idx + 1:]

    ans += nxt_val - min_val
    solution(arr)

n = int(input())
a = []
for _ in range(n):
    x = int(input())
    if not a:
        a.append(x)
    else:
        if a[-1] != x:
            a.append(x)

ans = 0
solution(a)
print(ans)