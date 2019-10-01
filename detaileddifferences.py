n = int(input())
items = []

for i in range(n):
    item = []
    str3 = ""
    for j in range(2):
        item.append(str(input()))
    for j in range(len(item[0])):
        if item[0][j] == item[1][j]:
            str3 += '.'
        else:
            str3 += '*'
    item.append(str3)
    items.append(item)

for i in items:
    print(i[0])
    print(i[1])
    print(i[2])
    print('')