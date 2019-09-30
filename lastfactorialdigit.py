n = int(input())
items = []

for i in range(n):
    items.append(int(input()))

def digit(n):
    if n == 0:
        return 1
    else:
        return n*digit(n -1)

for i in items:
    print(digit(i)%10)