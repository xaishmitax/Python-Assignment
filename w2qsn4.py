#Create a dictionary called books where keys are book titles(strings) and the values are the numbner of copies available for each book.

books = {
    'tsitp': 3,
    'tatbilb': 6,
    'Bible': 5
}

book_name = input("Enter the book you want: ")
copies_input = input("Enter number of copies you want: ")

while not copies_input.isdigit():
    print("read qsn again.")
    copies_input = input("Enter number of copies you want: ")

copies_wanted = int(copies_input)

if book_name in books:
    if books[book_name] >= copies_wanted:
        print("Available")
    elif 0 < books[book_name] < copies_wanted:
        print("Partially Available")
    else:
        print("Unavailable")
else:
    print("Unavailable")
