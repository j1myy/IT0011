
def palindrome_ito(n):
    num2string = str(n)
    return num2string == num2string[::-1]  



with open("numbers.txt", "r") as file:
    lines = file.readlines()


for i, line in enumerate(lines, start=1):
    line = line.strip()
    nums = line.split(",")


    total = sum(int(num) for num in nums)


    if palindrome_ito(total):
        print(f"Line {i}: {line} (sum {total}) - Palindrome")
    else:
        print(f"Line {i}: {line} (sum {total}) - Not a palindrome")
