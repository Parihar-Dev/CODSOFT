
# --------------------    TASK 01    --------------------

# Simple Calculator

# Prompt the user to input two numbers

num1 = int(input("Enter the First Number : "))
num2 = int(input("Enter the Second Number : "))

# Basic Arithmetic Operations

def Addition():
    print(f"\n ----------  The Sum of two numbers is {num1 + num2}  ----------")

def Subtraction():
    print(f"\n  ----------  The Difference of two numbers is {num1 - num2}  ----------")

def Multiplication():
    print(f"\n  ----------  The Product of two numbers is {num1 * num2}  ----------")

def Division():
    print(f"\n  ----------  The Quotient of these two numbers is {num1 / num2}  ----------")

# Operation Choice
# Menu

menu = 1
while menu == 1 :
    print("\n1. Perform Addition Operation")
    print("2. Perform Subtraction Operation")
    print("3. Perform Multiplication Operation")
    print("4. Perform Division Operation")
    print("5. Terminate Program")
    choice = int(input("\nSELECT ANY ONE OPERATION : "))

    match choice:
        case 1 :
            Addition()
        case 2 :
            Subtraction()
        case 3 :
            Multiplication()
        case 4 :
            Division()
        case 5 :
            menu = 0
