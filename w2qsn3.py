#find all words that appear more than once fro the list story them in dictionary with their frequency count.

words = ["aishmita", "aaska", "aishmita", "rita", "sita", "bird", "aaska"]
freq = {}
duplicates = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

for word in freq:
    if freq[word] > 1:
        duplicates[word] = freq[word]  # <-- use word, not words

print(duplicates)