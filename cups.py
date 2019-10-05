n = int(input())

rs = []

def findColor(e):
    try:
        temp = int(e[0])/2
        e[0] = e[1]
        e[1] = temp
    except:
        e[1] = int(e[1])
    return e

def rtInt(e):
    return e[1]

for i in range(n):
    item = input().split()
    rs.append(findColor(item))

rs.sort(key=rtInt)

for i in rs:
    print(i[0])
