item1 = int(input())

check = True

while check:
    item2 = 0
    for i in str(item1):
        item2 += int(i)
    if item1 % item2 == 0:
        print(item1)
        check = False
    item1 += 1 

