items = []
newItems = []
for i in range(5):
    items.append(list(map(int, input().split())))

for i in items:
    sum = 0
    for j in range(4):
        sum += i[j]
    newItems.append(sum)

print(newItems.index(max(newItems)) + 1, max(newItems))