import math

def prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

palindrome = dict()
for i in range(1, 10):
    palindrome[i] = True
for i in range(1, 10000):
    x = str(i)
    palindrome[int(x + x[::-1])] = True

    if i < 1000:
        for j in range(10):
            palindrome[int(x + str(j) + x[::-1])] = True

s, e = map(int, input().split())
ans = []
for x in palindrome.keys():
    if s <= x <= e:
        if prime(x):
            ans.append(x)
ans.sort()
for x in ans:
    print(x)
print(-1)