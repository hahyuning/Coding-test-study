def base_conversion(num, base):
    T = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    n, d = divmod(num, base)
    if n == 0:
        if T[d].isdigit():
            return [T[d]]
        else:
            return [ord(T[d]) - ord("A") + 10]

    if T[d].isdigit():
        return base_conversion(n, base) + [T[d]]
    else:
        return base_conversion(n, base) + [ord(T[d]) - ord("A") + 10]


a, b = map(int, input().split())
m = int(input())
c = input().split()

num = 0
for i in range(m):
    if c[i].isdigit():
        num += int(c[i]) * a ** (m - 1 - i)
    else:
        x = ord(c[i]) - ord("A") + 10
        num += x * a ** (m - 1 - i)

print(*base_conversion(num, b))