def merge_sort(lt, rt):
    global ans

    if lt < rt:
        mid = (lt + rt) // 2
        merge_sort(lt, mid)
        merge_sort(mid + 1, rt)

        x, y = lt, mid + 1
        tmp = []

        while x <= mid and y <= rt:
            if a[x] <= a[y]:
                tmp.append(a[x])
                x += 1
            else:
                tmp.append(a[y])
                y += 1
                ans += (mid - x + 1)

        if x <= mid:
            tmp += a[x:mid + 1]
        if y <= mid:
            tmp += a[y:rt + 1]

        for i in range(len(tmp)):
            a[lt + i] = tmp[i]

n = int(input())
a = list(map(int, input().split()))
ans = 0
merge_sort(0, n - 1)
print(ans)