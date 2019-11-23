c = 1

while c != 0:
    c = int(input())
    if c == 0: break
    am = []
    pm = []
    for _ in range(c):
        item = input().split()
        item1 = list(map(int, item[0].split(":")))
        if item1[0] == 12: item1[0] = 0 
        (h, m, t) = (item1[0], item1[1], item1[0]*60 + item1[1])
        if item[1] == 'a.m.':
            am.append((h, m, t))
        else: pm.append((h, m, t))
    am = sorted(am, key=lambda x: x[2])
    pm = sorted(pm, key=lambda x: x[2])
    for h, m, _ in am:
        if h == 0: h = 12
        if m < 10: print(f"{h}:0{m} a.m.")
        else: print(f"{h}:{m} a.m.")
    for h, m, _ in pm:
        if h == 0: h = 12
        if m < 10: print(f"{h}:0{m} p.m.")
        else: print(f"{h}:{m} p.m.")
    print('')
    