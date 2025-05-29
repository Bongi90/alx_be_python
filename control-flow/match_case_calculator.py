# Objective: Learn to use Match Case statements for handling multiple operations in a simple calculator program.
# File: match_case_calculator.py
# Directory: control-flow
# Repository: alx_be_python

def simple_calculator():
    """
    Prompts the user for two numbers and an operation, then performs the calculation
    using a match-case statement. Handles division by zero.
    """
    # Prompt for User Input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    operation = input("Choose the operation (+, -, *, /): ")

    # Perform the Calculation Using Match Case
    match operation:
        case '+':
            result = num1 + num2
            print(f"The result is {result}.")
        case '-':
            result = num1 - num2
            print(f"The result is {result}.")
        case '*':
            result = num1 * num2
            print(f"The result is {result}.")
        case '/':
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"The result is {result}.")
        case _: # Default case for invalid operation
            print("Invalid operation. Please choose from +, -, *, /.")

# Call the function to run the calculator
if __name__ == "__main__":
    simple_calculator()
