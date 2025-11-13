name = input("Please enter your full name:") 
first = name[0]
space = name.find(" ")
last = name[space + 1]
print("Your initials are:", first.upper() + "." + last.upper())
