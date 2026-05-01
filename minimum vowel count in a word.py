s = input().strip()
vowels = set("aeiouAEIOU")
words = s.split()
min_vowels = None
for word in words:
    count = sum(1 for ch in word if ch in vowels)
    if min_vowels is None or count < min_vowels:
        min_vowels = count
print(min_vowels)
