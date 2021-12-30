import math
n = int(input())
if int(math.sqrt(n)) == math.sqrt(n):
    print(int(math.sqrt(n)))
else:
    print(int(math.sqrt(n)) + 1)