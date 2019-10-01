item = input()
rs = ''
temp = ''

for i in item:
    if i != temp:
        rs += i
    temp = i

print(rs)