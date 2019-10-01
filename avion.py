rs = []
for i in range(5):
    item = input().upper()
    try:
        if item.index("F") and item.index("B") and item.index("I"):
            rs.append(i + 1)
    except:
        continue

if rs == []:
    print("HE GOT AWAY!")
else:
    rs.sort()
    for i in rs:
        print(i, end=" ")