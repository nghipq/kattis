items = []
done = 0

while done != -1:
    item = []
    done = int(input())
    if done == -1:
        continue
    else:
        for i in range(done):
            item.append(list(map(int, input().split())))
        items.append(item)

for i in items:
    rs = 0
    for j in range(len(i)):
        if j == 0:
            rs += i[j][0] * i[j][1]
        else:
            rs += i[j][0] * (i[j][1] - i[j - 1][1])
    print(rs, 'miles')