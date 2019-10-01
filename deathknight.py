n = int(input())
count = 0

for i in range(n):
    item = input()
    try:
        item.index("CD")
        continue
    except:
        count += 1

print(count)