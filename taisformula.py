n = int(input())
items = []
totals = 0

def takeFirst(e):
    return e[0]

for i in range(n):
    items.append(list(map(float, input().split())))

items.sort(key=takeFirst)

for i in range(1, 3):
    totals += ((items[i-1][1] + items[i][1])/ 2)*(items[i][0] - items[i - 1][0])/1000

print(totals)