
input_stringbyuser = input("Enter a string: ")

vowel_counter = 0
consonant_counter = 0
space_counter = 0
other_counter = 0


for char in input_stringbyuser:

    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
        vowel_counter += 1


    elif char.isalpha():
        consonant_counter += 1



    elif char == ' ':
        space_counter += 1


    else:
        other_counter += 1


print("Counted")
print("Vowels:", vowel_counter)
print("Consonants:", consonant_counter)
print("Spaces:", space_counter)
print("Other characters:", other_counter)