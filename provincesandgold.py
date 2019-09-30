inp = list(map(int, input().split()))

cost = inp[0]*3 + inp[1]*2 + inp[2]*1

rs = []

cards = [6, 3, 0]

def vict(cost):
    items = [[8, 'Province'], [5, 'Duchy'], [2, 'Estate']]
    for i in items:
        if cost >= i[0]:
            return i[1]

def card(cost):
    items = [[6, 'Gold'], [3, 'Silver'], [0, 'Copper']]
    for i in items:
        if cost >= i[0]:
            return i[1]

rs.append(vict(cost))
rs.append(card(cost))

if rs[0] == None:
    print(rs[1])
else:
    print(f'{rs[0]} or {rs[1]}')