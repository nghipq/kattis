t = list(map(int, input().split()))

o = t[1] - 45
if t[0] == 0:
    t[0] = 24
if o < 0:
    t[0] -= 1
    t[1] = 60 + o
else:
    t[1] = o

print(t[0], t[1])