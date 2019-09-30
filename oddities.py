n = int(input())
items = []
for i in range(n):
    items.append(int(input()))

for i in items:
    if i % 2 == 0:
        print(i, 'is even')
    else:
        print(i, 'is odd')    