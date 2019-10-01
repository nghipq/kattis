inp = list(map(int, input().split()))

if inp[0] > inp[1]:
    temp = inp[0]
    inp[0] = inp[1]
    inp[1] = temp

for i in range(inp[0]+1, inp[1] + 2):
    print(i)