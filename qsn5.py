text = input("Enter a string: ").lower()
freq = {}
for ch in text:
    if ch != " ":
        if ch in freq:
            freq[ch] = freq[ch] + 1
        else:
            freq[ch] = 1
for ch in freq:
    print(ch, "→", freq[ch])
