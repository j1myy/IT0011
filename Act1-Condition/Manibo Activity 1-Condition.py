# 1
num1 = float(input("Please input the first number: "))
num2 = float(input("Please input the second number: "))
num3 = float(input("Please input the third number: "))

if num1 > num2:
    if num1 > num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 > num3:
        largest = num2
    else:
        largest = num3

print("The largest number is", largest)

print()
print()

# 2
if num1 > num2:
    if num1 > num3:
        if num2 > num3:
            largest, middle, smallest = num1, num2, num3
        else:
            largest, middle, smallest = num1, num3, num2
    else:
        largest, middle, smallest = num3, num1, num2
else:
    if num2 > num3:
        if num1 > num3:
            largest, middle, smallest = num2, num1, num3
        else:
            largest, middle, smallest = num2, num3, num1
    else:
        largest, middle, smallest = num3, num2, num1

print("Numbers in descending order:", largest, middle, smallest)