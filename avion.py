rs = ""
for i in range(5):
    item = input().upper()
    try:
        if item.index("FBI"):
            rs += f"{i + 1} " 
    except:
        continue

if rs == "":
    print("HE GOT AWAY!")
else:
    print(rs)