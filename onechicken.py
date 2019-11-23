n, m = list(map(int, input().split()))

if m - n > 1: print(f"Dr. Chaz will have {m - n} pieces of chicken left over!")
elif m - n == 1: print(f"Dr. Chaz will have {m - n} piece of chicken left over!")
elif n - m == 1: print(f"Dr. Chaz needs {n - m} more piece of chicken!")
else: print(f"Dr. Chaz needs {n - m} more pieces of chicken!")