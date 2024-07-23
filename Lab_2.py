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