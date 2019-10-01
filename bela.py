dic = {'A':[11,11], 'K':[4,4], 'Q':[3,3], 'J':[20,2],
       'T':[10,10], '9':[14,0], '8':[0,0], '7':[0,0]}

mul, trump = input().split()
rs = 0

for i in range(4*int(mul)):
    item = input()
    if item[1] == trump:
        rs += dic.get(item[0])[0]
    else:
        rs += dic.get(item[0])[1]

print(rs)