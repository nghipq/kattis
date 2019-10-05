import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def calc(x1, y1, x2, y2, x3, y3, x, y):
    ans = 0
    ans += dist(x1, y1, x, y)
    ans += dist(x2, y2, x, y)
    ans += dist(x3, y3, x, y)
    return ans

x1, y1 = list(map(float, input().split()))
x2, y2 = list(map(float, input().split()))
x3, y3 = list(map(float, input().split()))

x = float((x1 + x2 + x3)/3)
y = float((y1 + y2 + y3)/3)

best = calc(x1, y1, x2, y2, x3, y3, x, y)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = 1000.0
while t > .00001:
    found = False
    for i in range(4):
        nextx = x + t*dx[i]
        nexty = y + t*dy[i]
        val = calc(x1, y1, x2, y2, x3, y3, nextx, nexty)
        if val < best:
            found = True
            best = val
            x = nextx
            y = nexty
    if found == False:
        t /= 2

print(round(x, 9), round(y, 9))