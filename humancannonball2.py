import math
g = 9.81
n = int(input())

rs = []

def func(v, o, x, h1, h2):
    t = x/(v*math.cos(math.radians(o)))
    y = v*t*math.sin(math.radians(o)) - 0.5*g*(t**2)
    if y > h1+1 and y < h2-1:
        return 'Safe'
    else:
        return 'Not Safe'

for i in range(n):
    item = list(map(float, input().split()))
    rs.append(func(item[0], item[1], item[2], item[3], item[4]))

for i in rs:
    print(i)