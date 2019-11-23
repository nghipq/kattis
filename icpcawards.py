n = int(input())
rs = list()
for i in range(n):
    item = input().split(' ')
    check = True
    for j in range(len(rs)):
        if rs[j][0] == item[0]: check = False
    if rs == []: check = True
    if check: rs.append(item)

for i in range(12):
    print(rs[i][0], rs[i][1])