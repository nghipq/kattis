n = int(input())

for i in range(n):
    m = input()
    lst = list(map(int, input().split()))
    print(2*(max(lst) - min(lst)))