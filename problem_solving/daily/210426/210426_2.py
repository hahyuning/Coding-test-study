def binary(n, c):
    n = int(n)
    ans = ""
    while n > 0:
        n, d = divmod(n, 2)
        ans += str(d)

    if c == 1:
        while len(ans) < 4:
            ans += "0"
    else:
        while len(ans) < 3:
            ans += "0"
    return ans[::-1]


a = {"ADD": "0000", "SUB": "0001", "MOV": "0010", "AND": "0011", "OR": "0100", "NOT": "0101", "MULT": "0110",
     "LSFTL": "0111", "LSFTR": "1000", "ASFTR": "1001", "RL": "1010", "RR": "1011"}

n = int(input())

for _ in range(n):
    ans = ""
    s = list(input().split(" "))

    b = s[0]

    if b[-1] == "C":
        b = b[:-1]
        c = s[1:-1]
        d = s[-1]
        ans = ans + a[b] + "10"

        for x in c:
            ans += binary(x, 0)
        ans += binary(d, 1)
        print(ans)
    else:
        c = s[1:]
        ans = ans + a[b] + "00"

        for x in c:
            ans += binary(x, 0)
        ans += "0"
        print(ans)
