n = int(input())
rs = 0

for i in range(n):
    item = int(input())
    num = item // 10
    power = item % 10
    rs += num**power

print(rs)