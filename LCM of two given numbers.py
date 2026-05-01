import math
M, N = map(int, input().split())
lcm = (M * N) // math.gcd(M, N)
print(lcm)
