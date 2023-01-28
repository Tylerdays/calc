import addition
import subtraction
import multiplication
import division

print("Select an operation:")
print("1. Add two numbers")
print("2. Subtract two numbers")
print("3. Multiply two numbers")
print("4. Divide two numbers")

choice = int(input("Enter your choice (1-4): "))

num1 = float(input("Enter number one: "))
num2 = float(input("Enter number two: "))

if choice == 1:
    result = addition.add(num1, num2)
elif choice == 2:
    result = subtraction.subtract(num1, num2)
elif choice == 3:
    result = multiplication.multiply(num1, num2)
elif choice == 4:
    result = division.divide(num1, num2)
else:
    print("Invalid choice. Please enter a number between 1 and 4.")

print("Result:", result)