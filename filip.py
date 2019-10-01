lst =  list(input().split())

if int(lst[0][::-1]) > int(lst[1][::-1]):
    print(lst[0][::-1])
else:
    print(lst[1][::-1]) 