n = int(input())
arr = list()

for i in range(n):
    dic = dict()
    m = int(input())
    items = input().split()
    for i in items:
        dic[i] = dic.get(i, 0) + 1
    arr.append(dic)

for i in range(n):
    print(f'Case #{i+1}: {min(arr[i], key=lambda x: arr[i].get(x))}')