n = int(input())
teas = list(map(int, input().split()))
m = int(input())
topping = list(map(int, input().split()))
items = list()

for i in range(n):
    item = list(map(int, input().split()))
    item.remove(item[0])
    items.append(item)

rs = list()
for i in range(n):
    if items[i] != []:
        temp = []
        for item in items[i]:
            temp.append(topping[item - 1])
        rs.append(teas[i] + min(temp))


moneys = int(input())

cups = moneys // min(rs)
if cups > 0:
    print(cups - 1)
else:
    print(0)