#7.	Write a python program that accepts 2 strings from the user. Perform the following tasks:
#i.	Concatenate the two string
#ii.	Reverse the concatenated string
#iii.	Replace every vowel (a, e, i, o, u) in reversed string with character $
#iv.	Check whether concatenated string starts with first string
#v.	Accept a character from the user and count its number of occurences in concatenated string

def string_manipulations(str1, str2):
                # Task i: Concatenate the two strings
    concatenated_string = str1 + str2
    print("Concatenated String:", concatenated_string)
                # Task ii: Reverse the concatenated string
    reversed_string = concatenated_string[::-1]
    print("Reversed String:", reversed_string)
                # Task iii: Replace every vowel with the character $
    vowels = "aeiouAEIOU"  # List of vowels (both lowercase and uppercase)
    replaced_string = ''.join(['$' if char in vowels else char for char in reversed_string])
    print("String with Vowels Replaced:", replaced_string)
                    # Task iv: Check whether the concatenated string starts with the first string
    starts_with_first_string = concatenated_string.startswith(str1)
    print("Does the concatenated string start with the first string?:", starts_with_first_string)
           # Task v: Accept a character from the user and count its occurrences in the concatenated string
    char_to_count = input("Enter a character to count in the concatenated string: ")
    char_count = concatenated_string.count(char_to_count)
    print(f"Number of occurrences of '{char_to_count}' in concatenated string:", char_count)
                # Input: Accept two strings from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
                # Call the function to perform string manipulations
string_manipulations(string1, string2)
