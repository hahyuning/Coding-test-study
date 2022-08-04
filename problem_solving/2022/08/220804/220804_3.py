def solution(order):
    container = []

    ans = 0
    now = 0
    for i in range(1, len(order) + 1):
        if i == order[now]:
            ans += 1
            now += 1
        else:
            if container and container[-1] == order[now]:
                ans += 1
                container.pop()
                now += 1

                if order[now] == i:
                    ans += 1
                    now += 1
                else:
                    container.append(i)
            else:
                container.append(i)

    while now < len(order) and container and container[-1] == order[now]:
        ans += 1
        container.pop()
        now += 1

    return ans

solution([5, 4, 3, 2, 1])