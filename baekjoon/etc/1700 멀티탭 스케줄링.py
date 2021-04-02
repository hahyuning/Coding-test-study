n, k = map(int, input().split())
order = list(map(int, input().split()))

socket = []
result = 0

for i, x in enumerate(order):
    if len(socket) < n and x not in socket:
        socket.append(x)
    elif x in socket:
        continue
    elif i == n - 1:
        result += 1
        break
    else:
        latest_index = -1
        latest_item = 0
        for y in socket:
            if y not in order[i + 1:]:
                latest_item = y
                break

            if order[i + 1:].index(y) > latest_index:
                latest_index = order[i + 1:].index(y)
                latest_item = y

        socket.remove(latest_item)
        socket.append(x)
        result += 1

print(result)