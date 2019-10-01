items = []
rs = []

for i in range(3):
    items.append(list(map(int, input().split())))

for i in range(2):
    temp = items[0][i]
    if items[1][i] == temp:
        rs.append(items[2][i])
    elif items[2][i] == temp:
        rs.append(items[1][i])
    else:
        rs.append(temp)

print(rs[0], rs[1])
