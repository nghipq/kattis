dic = {'T': 0, 'C': 0, 'G': 0}
item = input()

for i in item:
    dic.update({i: dic.get(i) + 1})

rs = dic.get(min(dic, key=lambda x: dic.get(x)))*7

for i in dic.values():
    rs += i**2
    
print(rs)