s = input().strip()
vowels = set("aeiouAEIOU")
words = s.split()
max_vowels = 0
for word in words:
    count = sum(1 for ch in word if ch in vowels)
    if count > max_vowels:
        max_vowels = count
print(max_vowels)
