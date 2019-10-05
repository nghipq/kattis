items = list()
lst = list()
days = 1

x, y, num = map(int, input().split())

for i in range(num):
    item = list(map(int, input().split()))
    if item not in items:
        items.append(item)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def inrange(x, y, mx, my):
    return x > 0 and y > 0 and x <= mx and y <= my

while len(items) + len(lst) < x * y:
    temp = []
    for item in items:
        for i in range(4):
            if inrange(item[0] + dx[i], item[1] + dy[i], x, y) == False: continue
            if [item[0] + dx[i], item[1] + dy[i]] not in items and [item[0] + dx[i], item[1] + dy[i]] not in temp and [item[0] + dx[i], item[1] + dy[i]] not in lst:
                temp.append([item[0] + dx[i], item[1] + dy[i]])
    lst.extend(items)
    items = temp
    days += 1    

print(days)

