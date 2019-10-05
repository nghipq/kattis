inp = input().split()
dic = dict()

for item in inp:
    dic[item[0]] = dic.get(item[0], 0) + 1

print(dic[max(dic, key=lambda x: dic.get(x))])
