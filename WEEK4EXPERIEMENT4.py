
#1
import sys
if len(sys.argv) != 3:
    print("Please provide two numbers as command line arguments.")
else:
    try:
        # Convert the arguments to numbers
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        # Calculate and print the sum
        print(f"The sum of {num1} and {num2} is: {num1 + num2}")
    except ValueError:
        print("Please provide valid numbers.")
        
#2Implement python script to show the usage of various operators available in python language.

a = 10
b = 5

# Arithmetic Operators
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Modulus: {a % b}")
print(f"Exponentiation: {a ** b}")
print(f"Floor Division: {a // b}")

# Comparison Operators
print(f"a > b: {a > b}")
print(f"a < b: {a < b}")
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")

# Logical Operators
print(f"a > 5 and b < 10: {a > 5 and b < 10}")
print(f"a < 5 or b > 2: {a < 5 or b > 2}")
print(f"not(a > b): {not (a > b)}")

# Bitwise Operators
print(f"a & b: {a & b}")
print(f"a | b: {a | b}")
print(f"a ^ b: {a ^ b}")
print(f"~a: {~a}")

# Assignment Operators
a += 2
print(f"a after a += 2: {a}")

#3 Implement python script to read person’s age from keyboard and display whether he is eligible for voting or not.


age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
    
#4Implement python script to check the given year is leap year or not.


year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")