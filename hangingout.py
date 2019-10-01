inp = list(map(int, input().split()))
count = 0
Sum = 0
for i in range(inp[1]):
    item = input().split()
    if item[0] == "enter":
        if Sum + int(item[1]) <= inp[0]:
            Sum += int(item[1])
        else:
            count += 1
    else:
        if Sum > 0:
            Sum -= int(item[1])

print(count) 