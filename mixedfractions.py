n = None
while n != '0 0':
    n = input()
    if n == '0 0': break
    x, y = list(map(int, n.split()))
    print(x//y, x%y, '/', y)