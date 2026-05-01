n = int(input())
last = n % 10
first = n
while first >= 10:
    first //= 10
print(first + last)
