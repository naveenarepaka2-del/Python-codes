s = input().strip()
vowels = set('aeiou')
missing_vowels = sorted(vowels - set(s))
if missing_vowels:
    print(" ".join(missing_vowels))
else:
    print(0)
