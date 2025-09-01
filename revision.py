import math

# Simple calculator program

def add(a,b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b!=0:
        return a / b
    else: 
        return "Error Division by zero"
    
def modulus(a, b):
    if b!=0:
        return a % b
    else: 
        return "Error Division by zero"

def exponent(a, b):
    if b!=0:
        return a ** b

def squared(a):
    if a < 0:
        return "Error, cannot take square root of negavive numbers"
    else:
        return math.sqrt(a)


# Display operations of the calculator
print("\n----Basic Calculator")
print("1. Add")
print("2. Subrtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print("6. Exponent")
print("7. Square root")


# Take input from the user for operation choice
choice = input("please enter a choice (1/2/3/4/5): ")

def main():
    while True:
        try:
            choice = input("please enter a choice (1/2/3/4/5/6): ")
            if choice != (('1') or ('2') or ('3') or ('4') or ('5') or ('6') or (7)):
                print ("Please make a valid selection")
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if choice == '1':
                    print("Result:", add(num1, num2))
                elif choice == '2':
                    print("Result:", subtract(num1, num2))
                elif choice == '3':
                    print("Result:", multiply(num1, num2))
                elif choice == '4':
                    print("Result:", divide(num1, num2))
                elif choice == '5':
                    print("Result:", modulus(num1, num2))
                elif choice == '6':
                    print("Result:", exponent(num1, num2))
            else: 
                print("Please make a valid selection")
            if choice == '7':
                num = float(input("Pllease enter a number: "))
                print("Result:", squared(num))
            else:
                print("Please second ")
        except ValueError:
            print("Str cannot convert to float")


    else: 
        print("Invalid option")

