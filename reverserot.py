n = None
s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while n != '0':
    n = input()
    if n == '0': break
    x = int(n.split()[0])
    item = n.split()[1]
    rs = ''
    j = None
    for i in item[::-1]:
        if i == '_': j = 26
        elif i == '.': j = 27
        else: j = ord(i) - 65
        rs += s[(j + x)%28]

    print(rs)