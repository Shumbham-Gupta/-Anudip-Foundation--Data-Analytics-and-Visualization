#problem 1
def is_leap_year(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


#problem 2
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print(f"The largest number among {num1}, {num2}, and {num3} is {largest}.")


#problem 3
number = float(input("Enter a number: "))
if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")
else:
    print(f"{number} is zero.")



#problem 4
def calculate_discounted_amount(product_code, order_amount):
    if product_code == 1:  
        if order_amount > 1000:
            discount = 0.10
        else:
            discount = 0
    elif product_code == 2: 
        if order_amount > 100:
            discount = 0.05
        else:
            discount = 0
    elif product_code == 3: 
        if order_amount > 500:
            discount = 0.10
        else:
            discount = 0
    else:
        print("Invalid product code")
        return None

    discounted_amount = order_amount * (1 - discount)
    return discounted_amount
product_code = int(input("Enter the product code (1 for Battery Based Toys, 2 for Key-Based Toys, 3 for Electrical Charging Based Toys): "))
order_amount = float(input("Enter the order amount: "))
net_amount = calculate_discounted_amount(product_code, order_amount)

if net_amount is not None:
    print(f"The net amount to be paid after discount is: Rs. {net_amount:.2f}")



#problem 5
def calculate_fare(distance):
    if 1 <= distance <= 50:
        rate_per_km = 8
    elif 51 <= distance <= 100:
        rate_per_km = 10
    elif distance > 100:
        rate_per_km = 12
    else:
        print("Invalid distance")
        return None

    fare = distance * rate_per_km
    return fare

distance = float(input("Enter the distance traveled (in kilometers): "))

fare = calculate_fare(distance)
if fare is not None:
    print(f"The total fare for {distance} km is: Rs. {fare:.2f}")


#problem 6
def reverse_number(number):
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = (reversed_number * 10) + digit
        number = number // 10
    return reversed_number
number = int(input("Enter a number to reverse: "))
reversed_number = reverse_number(number)
print(f"The reversed number is: {reversed_number}")


#problem 7
def is_palindrome(number):
    str_number = str(number)
    reversed_str_number = str_number[::-1]
    return str_number == reversed_str_number
number = int(input("Enter a number to check if it is a palindrome: "))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")


#problem 8
# Function to calculate the factorial of a number
def factorial(number):
    result = 1
    while number > 0:
        result *= number
        number -= 1
    return result
number = int(input("Enter a number to find its factorial: "))
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    fact = factorial(number)
    print(f"The factorial of {number} is {fact}.")


#problem 9
total_sum = 0

while True:
    number = float(input("Enter a number (enter 0 to stop): "))
    if number == 0:
        break  
    total_sum += number
print(f"The sum of all entered numbers is: {total_sum:.2f}")


#problem 10
for number in range(1, 11):
    print(number)


#problem 11
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
string = input("Enter a string to check if it is a palindrome: ")
if is_palindrome(string):
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')


#problem 12
def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == number
number = int(input("Enter a number to check if it is an Armstrong number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")


#problem 13
def fibonacci_series(limit):
    series = []
    a, b = 0, 1
    while a <= limit:
        series.append(a)
        a, b = b, a + b
    return series

limit = 50
fib_series = fibonacci_series(limit)
print(f"Fibonacci series between 0 and {limit}: {fib_series}")


#problem 14
import re
def is_valid_password(password):
    min_length = 8
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    return (len(password) >= min_length and 
            has_upper and 
            has_lower and 
            has_digit and 
            has_special)

password = input("Enter a password to check its validity: ")
if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid. Ensure it meets the criteria:")
    print("1. At least 8 characters long.")
    print("2. Contains at least one uppercase letter.")
    print("3. Contains at least one lowercase letter.")
    print("4. Contains at least one digit.")
    print("5. Contains at least one special character.")


