n = int(input())
items = []

for i in range(n):
    items.append(list(map(int, input().split())))

for i in items:
    if i[0] < (i[1] - i[2]):
        print('advertise')
    elif i[0] == (i[1] - i[2]):
        print('does not matter')
    else:
        print('do not advertise')