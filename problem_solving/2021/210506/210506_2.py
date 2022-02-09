from collections import Counter

n = int(input())
books = [input() for _ in range(n)]
books.sort()

books = Counter(books)
most_book = books.most_common(1)
print(most_book[0][0])
