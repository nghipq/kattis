n = int(input())
arr = []
sum = 0
for i in range(n):
    arr.append(list(map(float, input().split())))

for i in range(n):
    sum += arr[i][0]*arr[i][1]
print(sum)