
NumDigits = input("Enter a string of digits: ")


TotalofNumDigits = 0


for char in NumDigits:

    if char.isdigit():
        TotalofNumDigits += int(char)



print("Total:", TotalofNumDigits)