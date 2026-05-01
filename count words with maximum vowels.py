s = input().strip()
vowels = set('aeiouAEIOU')
words = s.split()
vowel_counts = [sum(1 for char in word if char in vowels) for word in words]
max_vowels = max(vowel_counts) if vowel_counts else 0
max_count_words = vowel_counts.count(max_vowels) if vowel_counts else 0
print(max_count_words)
