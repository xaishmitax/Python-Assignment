#funtion to_title_case (sentence that takes sentences as input and returns sentence iinto title case, wherre first letter of each word is cpaitalized

def to_title_case(sentence):
    words = sentence.split()
    title_words = []
    for word in words:
        title_words.append(word[0].upper()+ word[1:])
    return " ".join(title_words)


sentence = input("Enter a sentence: ")
print ("Title Case:", to_title_case(sentence))