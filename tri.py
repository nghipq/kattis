a, b, c = list(map(int, input().split()))

ops = {
    '+': lambda x, y: x+y,
    '-': lambda x, y: x-y,
    '*': lambda x, y: x*y,
    '/': lambda x, y: x/y
}

done = False

for op in ops:
    if ops[op](a, b) == c:
        print(f'{a}{op}{b}={c}')
        done = True
    elif ops[op](b, c) == a:
        print(f'{a}={b}{op}{c}')
        done = True
    if done:
        break
