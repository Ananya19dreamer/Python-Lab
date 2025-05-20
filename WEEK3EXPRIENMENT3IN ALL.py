#1write a program for checking the given number is een or odd.
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
    
    
    
    
#2Using a for loop, write a program that prints the decimal equivalents of 1/2, 1/3, 1/4 ,....... 1/10
for i in range(2, 11):
    print(f"1/{i} = {1/i}")
    
    
#3Write a program for displaying reversal of a number.
num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reversed number:", rev)

#4Write a program for finding biggest number among 3 numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

biggest = max(a, b, c)
print("The biggest number is:", biggest)


#5Write a program using a while loop that asks the user for a number, and prints a countdown from that number to zero.S
num = int(input("Enter a number: "))

while num >= 0:
    print(num)
    num -= 1