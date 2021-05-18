def KMPSearch(pat, txt):
    m = len(pat)
    n = len(txt)

    lps = [0] * m

    computeLPS(pat, lps)

    i = 0
    j = 0
    while i < n:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        elif pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

        if j == m:
            return 1

    return 0


def computeLPS(pat, lps):
    length = 0
    i = 1
    while i < len(pat):
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

txt = input()
pat = input()
print(KMPSearch(pat, txt))