s = input()
num = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]
dic = dict()
for i in range(26):
    dic[chr(i + ord("A"))] = num[i]

a = []
for x in s:
    a.append(dic[x])
while len(a) > 1:
    ans = []
    for i in range(0, len(a), 2):
        if i + 1 >= len(a):
            ans.append(a[i])
        else:
            ans.append((a[i] + a[i + 1]) % 10)
    a = ans

if sum(a) % 2 == 0:
    print("You're the winner?")
else:
    print("I'm a winner!")