n = int(input())

rs = list()

for i in range(n):
    item = input()
    try:
        item.index('=')
        rs.append('skipped')
    except:
        item = list(map(int, item.split('+')))
        rs.append(item[0] + item[1])

for item in rs:
    print(item)