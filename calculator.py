import math
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."
def square_root(x):
    return math.sqrt(x)
def power(x, y):
    return math.pow(x, y)

def main():
    print("Welcome to the Simple Calculator!")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)") 
    print("5. Square Root (√)")
    print("6. Power (^)")
    
    choice = input("Enter your choice (1-6): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The result is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The result is: {divide(num1, num2)}")
    
    elif choice == '5':
        num = float(input("Enter a number: "))
        print(f"The square root of {num} is: {square_root(num)}")
    
    elif choice == '6':
        num1 = float(input("Enter base: "))
        num2 = float(input("Enter exponent: "))
        print(f"{num1} raised to the power of {num2} is: {power(num1, num2)}")
    
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
