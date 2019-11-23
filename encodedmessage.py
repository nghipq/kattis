import math
n = int(input())

for i in range(n):
    inp = input()
    rs = list()
    ans = ''
    x = 0
    ln = int(math.sqrt(len(inp)))
    y = ln

    for j in range(ln):
        rs.append(inp[x:y])
        x = y
        y += ln
    for j in range(ln-1, -1, -1):
        for items in rs:
            ans += items[j]

    print(ans)
