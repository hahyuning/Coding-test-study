n = int(input())
path = []

while n != 0:
    # 0 번째 비트가 1인 경우 -> 2배
    if n & 1:
        path.append("[/]")
        n *= 2
    # 1 번째 비트가 1인 경우 -> 2빼기
    elif n & 2:
        path.append("[+]")
        n -= 2
    # 0 번째와 1 번째 비트가 다 0인 경우 -> 2로 나누기
    else:
        path.append("[*]")
        n //= 2

if len(path) > 99:
    print(-1)
else:
    print(len(path))
    print(" ".join(path[::-1]))