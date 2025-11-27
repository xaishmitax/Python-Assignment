# Program whic takes lits as inpout and store the frequencyof each word in dictionary.

sentence = input("Enter a sentence: ")
words = sentence.split()
freq= {}
for word in words:
    word_lower= word.lower()
    if word_lower in freq:
        freq[word_lower] += 1
    else:
        freq[word_lower] = 1
print("Word Frequency:", freq)