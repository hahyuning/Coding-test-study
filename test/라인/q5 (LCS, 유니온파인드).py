def id_check(a, b):
    n = len(a)
    m = len(b)

    a = " " + a
    b = " " + b
    d = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i] == b[j]:
                d[i][j] = d[i - 1][j - 1] + 1
            else:
                if d[i - 1][j] < d[i][j - 1]:
                    d[i][j] = d[i][j - 1]
                # a
                else:
                    d[i][j] = d[i - 1][j]

    ans = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            ans = max(ans, d[i][j])
    return n + m - 2 * ans

def email_check(a, b):
    a_list = a.split("@")
    b_list = b.split("@")

    diff = id_check(a_list[0], b_list[0])
    if diff > 1:
        return False
    if diff == 1 and a_list[1] != b_list[1]:
        return False

    return True

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(nicks, emails):
    n = len(nicks)
    parent = [i for i in range(n)]

    for i in range(n - 1):
        for j in range(i + 1, n):
            id_diff = id_check(nicks[i], nicks[j])
            if id_diff >= 3:
                continue

            e_check = email_check(emails[i], emails[j])
            if e_check:
                union(i, j, parent)

    ans = set()
    for i in range(n):
        x = find(i, parent)
        ans.add(x)

    return len(ans)

solution(["imhero111", "moneyman", "hero111", "imher1111", "hro111", "mmoneyman", "moneymannnn"], ["superman5@abcd.com", "batman432@korea.co.kr", "superman@abcd.com", "supertman5@abcd.com", "superman@erty.net", "batman42@korea.co.kr", "batman432@usa.com"])