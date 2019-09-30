import math

arr = list(map(int, input().split()))
items = []
d = math.sqrt(arr[1]**2 + arr[2]**2)

for i in range(arr[0]):
    items.append(int(input()))

for i in items:
    if i <= d:
        print('DA')
    else:
        print('NE')
    