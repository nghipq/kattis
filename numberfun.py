n = int(input())
rs = list()

for item in range(n):
    x, y, z = list(map(int, input().split()))
    if x / y == z or y / x == z or x + y == z or abs(x - y) == z or x * y == z:
        rs.append('Possible')
    else:
        rs.append('Impossible')

for item in rs:
    print(item) 