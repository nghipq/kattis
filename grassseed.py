c = float(input())
l = int(input())
rs = 0

for i in range(l):
    item = list(map(float, input().split()))
    rs += c*item[0]*item[1]

print(rs)
