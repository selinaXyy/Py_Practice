from art import logo

#functions
def add(num1, num2):
    result = num1 + num2
    return result

def subtract(num1, num2):
    result = num1 - num2
    return result

def multiply(num1, num2):
    result = num1 * num2
    return result

def divide(num1, num2):
    result = num1 / num2
    return result

def perform_and_print_operation(operation, num1, num2):
    """Takes the operation, first number, and second number as parameters,
    performs the calculation, prints the final result, and returns the result."""

    result = 0 #initialize result

    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    else:
        print("You entered an invalid operation.")
        return
    
    print(f"{num1} {operation} {num2} = {result}")
    return result

#declarations && program
current_number = result = 0
first_calculation = True
continue_program = "y"
operation_sign = ""

print(logo)

while continue_program == "y":
    if first_calculation:
        first_number = float(input("What's the first number?: "))
        operation_sign = input("+\n-\n*\n/\nPick an operation: ").strip() #== .trim()
        second_number = float(input("What's the next number? "))

        result = perform_and_print_operation(operation_sign, first_number, second_number)
        if not result == None:
            first_calculation = False
            current_number = result
            continue_program = input(f"Type 'y' to continue calculating with {current_number}, or type 'n' to start a new calculation: ").strip().lower()
        else:
            continue_program = input("Try again? (y/n): ").strip().lower()

    else:
        operation_sign = input("Pick an operation: ").strip()
        second_number = float(input("What's the next number?: "))

        result = perform_and_print_operation(operation_sign, current_number, second_number)
        if not result == None:
            current_number = result

        continue_program = input(f"Type 'y' to continue calculating with {current_number}, or type 'n' to start a new calculation: ").strip().lower()
