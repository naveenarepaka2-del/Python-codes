s = input().strip()
words = s.split()
result = [word[::-1] for word in words[::-1]]
print(" ".join(result))
