n = int(input())
k = 4
s = 3

while n > s:
    s = s * 2 + k
    k += 1

k -= 1
while True:
    t = (s - k) // 2
    # 앞부분인 경우
    if n <= t:
        k -= 1
        s = t
    # 뒷부분인 경우
    elif n > t + k:
        n -= (t + k)
        k -= 1
        s = t
    # 가운데인 경우
    else:
        n -= t
        break

if n == 1:
    print("m")
else:
    print("o")