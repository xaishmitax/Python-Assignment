# Q4: Check password strength (weak, moderate, strong)

password = input("Enter your password: ")

for ch in password:
    if ch.isalpha():
        has_letter = True
    elif ch.isdigit():
        has_number = True
    elif ch in "@#$%&":
        has_special = True

if len(password) < 6 or (has_letter and not has_number and not has_special):
    print("Weak password")
elif len(password) >= 6 and has_letter and has_number and not has_special:
    print("Moderate password")
elif len(password) >= 8 and has_letter and has_number and has_special:
    print("Strong password")
else:
    print("Weak password")
