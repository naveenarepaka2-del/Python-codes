s = input().strip()
words = s.split()
for i in range(len(words)):
    if i % 2 == 0:
        words[i] = words[i][::-1]
result = " ".join(words)
print(result)
