import math
n = int(input())
items = []

for i in range(n):
    items.append(list(map(float, input().split())))

for i in items:
    print(round((60*(i[0] - 1))/i[1],4), round((60*(i[0]))/i[1],4), round((60*(i[0] + 1))/i[1],4))