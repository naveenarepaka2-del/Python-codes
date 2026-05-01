M, N =  map(int, input().split())
cAount = 0
for i in range(M, N + 1):
    if i % 6 == 0:
        count += 1
print(count)
