#task1
def add(x, y):
    """Addition function"""
    return x + y

def subtract(x, y):
    """Subtraction function"""
    return x - y

def multiply(x, y):
    """Multiplication function"""
    return x * y

def divide(x, y):
    """Division function"""
    if y == 0:
        return "Error: Cannot divide by zero"
    else:
        return x / y


#task2
def main():
    x, y, operation = get_user_input()
    result = perform_operation(x, y, operation)
    print("Result:", result)

# Call the main function to start the calculator
if __name__ == "__main__":
    main()




#task3
def add(x, y):
    """Addition function"""
    return x + y

def subtract(x, y):
    """Subtraction function"""
    return x - y

def multiply(x, y):
    """Multiplication function"""
    return x * y

def divide(x, y):
    """Division function"""
    if y == 0:
        return "Error: Cannot divide by zero"
    else:
        return x / y

# Function to get user input for numbers and operation choice
def get_user_input():
    try:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        return x, y, operation
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
        return get_user_input()

# Function to perform the selected operation
def perform_operation(x, y, operation):
    if operation == '+':
        return add(x, y)
    elif operation == '-':
        return subtract(x, y)
    elif operation == '*':
        return multiply(x, y)
    elif operation == '/':
        return divide(x, y)
    else:
        return "Error: Invalid operation"

# Main function to execute the calculator
def main():
    try:
        x, y, operation = get_user_input()
        result = perform_operation(x, y, operation)
        print("Result:", result)
    except Exception as e:
        print("An error occurred:", e)

# Call the main function to start the calculator
if __name__ == "__main__":
    main()