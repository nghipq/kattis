l = int(input())
d = int(input())
x = int(input())

def func1(l, d, x):
    i = l
    while i <= d:
        sum = 0
        item = i
        while item > 0:
           sum += item % 10
           item //= 10
        if sum == x:
            return i
        i += 1

def func2(l, d, x):
    i = d
    while i >= l:
        sum = 0
        item = i
        while item > 0:
            sum += item % 10
            item //= 10
        if sum == x:
            return i
        i -= 1
print(func1(l, d, x))
print(func2(l, d, x))
