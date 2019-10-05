lst = [['A', 'B', 'C'], ['B', 'A', 'B', 'C'], ['C', 'C', 'A', 'A', 'B', 'B']]
dic = dict()

n = int(input())
inp = input()
for i in range(3):
    temp = 0
    for j in range(len(inp)):
        if temp >= len(lst[i]):
            temp = 0
        if inp[j] == lst[i][temp]:
            dic[str(i+1)] = dic.get(str(i+1), 0) + 1
        temp += 1

maxP = dic[max(dic, key=lambda x: dic.get(x))]
print(maxP)

for k, v in dic.items():
    if v == maxP:
        if k == '1':
            print("Adrian")
        elif k == '2':
            print("Bruno")
        else:
            print("Goran")
