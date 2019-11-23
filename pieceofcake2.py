n, h1, v1 = list(map(int, input().split()))

h2 = n - h1
v2 = n - v1

area = [(h1*v1)*4,(h1*v2)*4,(h2*v1)*4,(h2*v2)*4]

print(max(area))