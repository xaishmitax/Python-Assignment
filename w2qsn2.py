#Take a string input and then reverse every alternate word of the string.

sentence= input("Enter any sentence of your choice:")
words= sentence.split()
new_list= []
i = 0

for word in words:
    if i%2 == 1:
        rev = ""
        for ch in word:
            rev = ch + rev
        new_list.append(rev)
    else:
        new_list.append(word)
    i = i + 1
    result = " ".join(new_list)
print(result)
