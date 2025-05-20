#1- Implement Python Script to generate first N natural numbers.
n = int(input("Enter the value of N: "))
print("First", n, "natural numbers are:")
for i in range(1, n + 1):
    print(i, end=' ')
print("\n")

#2- Implement Python Script to check given number is palindrome or not.
num = input("Enter a number: ")
if num == num[::-1]:
    print("Palindrome number.")
else:
    print("Not a palindrome.")
print()

#3- Implement Python script to print factorial of a number.
num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} is {factorial}")
print()

#4- Implement Python Script to print sum of N natural numbers.
n = int(input("Enter the value of N: "))
total = n * (n + 1) // 2
print(f"Sum of first {n} natural numbers is {total}")
print()

#5- Implement Python Script to check given number is Armstrong or not.
num = int(input("Enter a number: "))
order = len(str(num))
sum_of_powers = sum(int(digit) ** order for digit in str(num))

if num == sum_of_powers:
    print("Armstrong number.")
else:
    print("Not an Armstrong number.")
print()

#6- Implement Python Script to generate prime numbers series up to N.
n = int(input("Enter the value of N: "))
print(f"Prime numbers up to {n} are:")
for num in range(2, n + 1):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=' ')
print()