s = input().strip()
vowels = set('aeiouAEIOU')
words = s.split()
vowel_counts = [sum(1 for char in word if char in vowels) for word in words]
min_vowels = min(vowel_counts) if vowel_counts else 0
min_count_words = vowel_counts.count(min_vowels) if vowel_counts else 0
print(min_count_words)
