def solution(arr, brr):
    ans = 0
    for i in range(len(arr) - 1):
        x = arr[i]
        y = brr[i]
        if x == y:
            continue

        ans += 1
        if x < y:
            diff = y - x
            arr[i + 1] -= diff
        else:
            diff = x - y
            arr[i + 1] += diff

    return ans