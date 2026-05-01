s = input().strip()
vowels = set("aeiouAEIOU")
words = s.split()
result = []
for word in words:
    count = sum(1 for ch in word if ch in vowels)
    result.append(str(count))
print(" ".join(result))
