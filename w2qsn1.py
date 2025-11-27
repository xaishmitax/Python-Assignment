#To print number and skip if it is divisible by 5 and also stop if the number is > 50.

numbers_input = input("Enter numbersand use space please ")
numbers = numbers_input.split()

for num_str in numbers:
    num = int(num_str)
    if num > 50:
        break
    if num % 5 == 0:
        continue
    print(num)