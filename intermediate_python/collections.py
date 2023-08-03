from collections import defaultdict

input_strings = ['mat', 'tam', 'ram', 'mar', 'hay' ,'bat' ,'tab' ]

anagrams = defaultdict(list)

for words in input_strings:
    sorted_word = ''.join(sorted(words))
    anagrams[sorted_word].append(words)


print(list(anagrams.values()))
    
