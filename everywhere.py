items = []
n = int(input())

for i in range(n):
    m = int(input())
    item = []
    for j in range(m):
        item.append(str(input()))
    items.append(item)

for i in items:
    temp = []
    for j in i:
        if j not in temp:
            temp.append(j)
    print(len(temp))