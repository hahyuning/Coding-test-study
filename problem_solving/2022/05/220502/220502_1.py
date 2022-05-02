def palindrome(s):
    global max_len

    if len(s) == 1:
        return

    if s == s[::-1]:
        max_len = max(max_len, len(s))
        return

    palindrome(s[1:])


if __name__ == '__main__':
    s = input()
    max_len = 1
    palindrome(s)

    print((len(s) - max_len) * 2 + max_len)
