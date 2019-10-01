n = int(input())

inp = list(map(int, input().split()))

count = 0
for i in inp:
    if i < 0:
        count += 1
print(count)