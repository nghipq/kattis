t = 1

while True:
    n = int(input())
    if n == 0:
        break
    item = [input() for _ in range(n)]
    print('SET', t)
    for i in range(0, n, 2):
        print(item[i])
    for i in range(n - (n%2) -1, -1, -2):
        print(item[i])
    t+=1