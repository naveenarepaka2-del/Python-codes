s = input().strip()
vowels = set('aeiouAEIOU')
count = sum(1 for char in s if char in vowels)
print(count)
