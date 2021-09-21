from collections import Counter

while True:
    try:
        a = list(input())
        b = list(input())

        a_set = Counter(a)
        b_set = Counter(b)

        c = a_set & b_set
        print("".join(sorted(list(c.elements()))))
    except:
        break