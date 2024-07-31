# Write a funtion in python to read the content from a text file "ABC.txt" line by line and display the same on screen
filename = 'ABC.txt'
with open(filename, 'r') as file:
    for line in file:
        print(line.strip())



# write a function in python to count and display the total number of words in a text file "ABC.txt"
filename = 'ABC.txt'
with open(filename, 'r') as file:
    text = file.read()
    words = text.split()
    total_words = len(words)
    print(f"Total number of words: {total_words}")



# Write a function in python to  count uppercase character in a text file "ABC.txt"
filename = 'ABC.txt'
with open(filename, 'r') as file:
    text = file.read()
    uppercase_count = sum(1 for char in text if char.isupper())
print(f"Total number of uppercase characters: {uppercase_count}")




# write a function display_words() in python to read lines from a text file "story.txt",and display those words,which are less than 4 charcters
filename = 'story.txt'
with open(filename, 'r') as file:
    for line in file:
        words = line.split()
        short_words = [word for word in words if len(word) < 4]
        for word in short_words:
            print(word)



#write a python program to handle a zerodivision error exception when dividing a number by zero
numerator = 10
denominator = 0

try:
    result = numerator / denominator
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print("The result is:", result)




#Write a python program that prompts the user to input an integer and raises a valueError exception if the input an integer and raises a value Error exception if the inputs is not a valid integer
try:
    user_input = input("Please enter an integer: ")
    user_integer = int(user_input)
    print("You entered the integer:", user_integer)
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")




#Write a python program that opens a file and handles a FileNotFoundError exception if the file does not exist
file_name = "example.txt"

try:
    with open(file_name, 'r') as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")




#Write a python program that prompts the user to input two numbers and rases a TypeError exception if the inputs are not numerical
try:
    num1 = input("Please enter the first number: ")
    num2 = input("Please enter the second number: ")

    # Attempt to convert the inputs to floats
    num1 = float(num1)
    num2 = float(num2)

    print("The first number is:", num1)
    print("The second number is:", num2)

except ValueError:
    raise TypeError("Error: Both inputs must be numerical.")
