dic = dict()

inp = input().split()

for item in inp:
    dic[item] = dic.get(item, 0) + 1

rs = 'yes'

for key, value in dic.items():
    if value > 1:
        rs = 'no'
        break
    
print(rs)