n = 1
rs=[]

def sumOfN(n):
    return sum(list(map(int, list(n))))

while int(n) != 0:
    n = input()
    if n == '0':
        continue
    i = 11
    check = True
    while check:
        if sumOfN(str(int(n) * i)) == sumOfN(n):
            check = False
            rs.append(i)
        i += 1

for i in rs:
    print(i)
    