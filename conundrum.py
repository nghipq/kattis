ciper = "PER"
inp = input()
index = 0
day = 0

for i in inp:
    if index > 2:
        index = 0

    if i != ciper[index]:
        day += 1
    index += 1

print(day)