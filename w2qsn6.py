#@funciton to print olargest word

def largest_word(sentence):
    words = sentence.split()
    largest = ""
    for word in words:
        if len(word) > len(largest):
            largest = word
    return largest

sentence = input("Enter a sentence: ")
print("The largest word is:", largest_word(sentence))