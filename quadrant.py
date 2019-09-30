x = int(input())
y = int(input())

q = 1
if x < 0 and y > 0:
    q = 2
elif x > 0 and y < 0:
    q = 4
elif x < 0 and y < 0:
    q = 3
print(q)