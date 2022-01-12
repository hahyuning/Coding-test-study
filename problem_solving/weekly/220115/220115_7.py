money = int(input())
machineDuck = list(map(int, input().split()))

x = y = money
a, b = 0, 0
for price in machineDuck:
    if x // price > 0:
        x, a = x - price * (x // price), a + x // price

for i in range(3, 14):
    if machineDuck[i - 3] < machineDuck[i - 2] < machineDuck[i - 1] < machineDuck[i]:
        y, b = y + b * machineDuck[i], 0
    elif machineDuck[i - 3] > machineDuck[i - 2] > machineDuck[i - 1] > machineDuck[i]:
        y, b = y - machineDuck[i] * (y // machineDuck[i]), b + y // machineDuck[i]

j_money = x + machineDuck[-1] * a
s_money = y + machineDuck[-1] * b

if j_money > s_money:
    print("BNP")
elif j_money < s_money:
    print("TIMING")
else:
    print("SAMESAME")