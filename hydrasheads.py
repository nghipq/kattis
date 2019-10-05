h, t = (1, 1)
rs = list()

while h != 0 and t != 0:
    h, t = map(int, input().split())
    head = h
    tail = t
    if h == 0 and t == 0:
        break
    act = 0
    while head > 0 or tail > 0:
        if head % 2 == 0 and head > 0:
            head -= 2
        elif tail >= 2 and (head + tail//2) % 2 == 0:
            tail -= 2
            head += 1
        else:
            tail += 1
        act += 1
    rs.append(act)

for i in rs: print(i)
