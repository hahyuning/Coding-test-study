n = int(input())
k = int(input())
a = list(map(int, input().split()))

if k >= n:
    print(0)
else:
    sensor = []
    for x in a:
        if x not in sensor:
            sensor.append(x)
    sensor.sort()
    n = len(sensor)
    interval = []
    for i in range(n - 1):
        interval.append(sensor[i + 1] - sensor[i])

    while k - 1 > 0:
        max_val = max(interval)
        interval.remove(max_val)
        k -= 1

    print(sum(interval))
