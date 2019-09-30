x = int(input())
n = int(input())
items = []

for i in range(n):
    items.append(int(input()))

rs = x
for i in items:
    rs = rs - i + x
print(rs)  