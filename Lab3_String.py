#problem 1
def div(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    else:
        return num1 / num2
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
result = div(number1, number2)
print(f"The result of dividing {number1} by {number2} is: {result}")


#problem 2
def square(num):
    return num ** 2
number = float(input("Enter a number to find its square: "))
result = square(number)
print(f"The square of {number} is: {result}")


#problem 3
import random

random_numbers = [random.randint(1, 100) for _ in range(5)]
max_value = max(random_numbers)
min_value = min(random_numbers)
print(f"Random numbers: {random_numbers}")
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")


#problem 4
name = input("Enter your name: ")
lowercase_name = name.lower()
print(f"Your name in lowercase is: {lowercase_name}")


#problem 5
from collections import Counter
import re
string = "To change the overall look of your document. To change the look available in the gallery"
string = string.lower()
words = re.findall(r'\b\w+\b', string)
word_count = Counter(words)
print("Word occurrences:")
for word, count in word_count.items():
    print(f"{word}: {count}")


#problem 6
string = "\nBest \nDeeptech \nPython \nTraining\n"
cleaned_string = string.replace('\n', '')
print("String without newlines:")
print(cleaned_string)


#problem 7
string = "Deeptech Python Training"
words = string.split()
reversed_words = words[::-1]
reversed_string = ' '.join(reversed_words)
print("String with reversed words:")
print(reversed_string)


#problem 8
string = "Welcome to python Training"
vowels = 'aeiouAEIOU'
vowel_count = {vowel: 0 for vowel in vowels}
for char in string:
    if char in vowels:
        vowel_count[char] += 1
print("Vowel counts:")
for vowel, count in vowel_count.items():
    if count > 0:
        print(f"{vowel}: {count}")


#problem 9
input_string = "P@#yn26at^&i5ve"
letters_count = 0
digits_count = 0
special_symbols_count = 0
for char in input_string:
    if char.isalpha():
        letters_count += 1
    elif char.isdigit():
        digits_count += 1
    elif not char.isspace():
        special_symbols_count += 1

print(f"Letters count: {letters_count}")
print(f"Digits count: {digits_count}")
print(f"Special symbols count: {special_symbols_count}")


#problem 10
input_string = "String and String Function"
seen = set()
result = []
for char in input_string:
    if char not in seen:
        seen.add(char)
        result.append(char)
unique_string = ''.join(result)

print("String with duplicate characters removed:")
print(unique_string)


#problem 11
input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
uppercase_count = 0
lowercase_count = 0
digits_count = 0
special_characters_count = 0
for char in input_string:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isdigit():
        digits_count += 1
    elif not char.isspace():
        special_characters_count += 1
print(f"Uppercase letters count: {uppercase_count}")
print(f"Lowercase letters count: {lowercase_count}")
print(f"Numeric values count: {digits_count}")
print(f"Special characters count: {special_characters_count}")


#problem 12
input_string = "Welcome to Python Assignment"
vowels = 'aeiouAEIOU'
vowel_count = 0
for char in input_string:
    if char in vowels:
        vowel_count += 1
print(f"Number of vowels in the string: {vowel_count}")
