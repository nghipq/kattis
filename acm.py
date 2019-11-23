n = 0
right = list()
wrong = dict()
rs = 0

while n != '-1':
    n = input()
    if n == '-1': continue
    items = n.split()
    if items[1] not in right and items[2] == 'wrong':
        wrong[items[1]] = wrong.get(items[1], 0) + 1
    elif items[1] not in right:
        right.append(items[1])
        rs += (int(wrong.get(items[1], 0))*20 + int(items[0])) 

print(len(right), rs)