r, c, y, x = map(int, input().split())

items = [input() for _ in range(r)]

for item in items:    
    for i in range(y):
        for j in item:
            for k in range(x):
                print(j, end="")
        print("")

