s = input().strip()
lower_vowels = set("aeiou")
upper_vowels = set('AEIOU')
chars = set(s)
if lower_vowels.issubset(chars) or upper_vowels.issubset(chars):
    print(True)
else:
    print(False)
