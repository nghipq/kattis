n = int(input())
items = list(map(int, input().split()))
Sum = 0

for i in items:
    if i >= 0:
        Sum += i
    else:
        n -= 1

print(Sum/n)