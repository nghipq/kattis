item = input()
ws = 0
lc = 0
uc = 0
sb = 0
for i in item:
    if i == '_':
        ws += 1
    elif i.islower():
        lc += 1
    elif i.isupper():
        uc += 1
    else:
        sb += 1

print(ws/len(item))
print(lc/len(item))
print(uc/len(item))
print(sb/len(item))