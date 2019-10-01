import math

inp = list(map(float, input().split()))

print(math.ceil(inp[0] / math.sin(math.radians(inp[1])))) 