n = int(input())
items = list(map(int, input().split()))
temp = 1
total = 0
items.sort(reverse=True)

while items != []:
    total = max(total, items[0] + temp)
    temp += 1
    items.pop(0)

print(total + 1)    
