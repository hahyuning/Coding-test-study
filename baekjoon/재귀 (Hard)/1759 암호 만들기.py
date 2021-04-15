m, n = map(int, input().split())
char_list = input().split()
char_list.sort()

def check(string):
    jaum = 0
    moum = 0

    for s in string:
        if s == "a" or s == "e" or s == "i" or s == "o" or s == "u":
            moum += 1
        else:
            jaum += 1

    if moum >= 1 and jaum >= 2:
        return True
    else:
        return False

def combination(index, password):
    if len(password) == m:
        if check(password):
            print(password)
        return

    if index >= n:
        return

    combination(index + 1, password + char_list[index])
    combination(index + 1, password)

combination(0, "")