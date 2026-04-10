# CLI Calculator
# A simple command-line calculator that performs basic arithmetic operations.


def add(a, b):
    # Return the sum of two numbers
    return a + b


def subtract(a, b):
    # Return the difference between two numbers
    return a - b


def multiply(a, b):
    # Return the product of two numbers
    return a * b


def divide(a, b):
    # Prevent division by zero
    if b == 0:
        raise ValueError("Cannot divide by zero")
    else:
        return a / b


def get_number(prompt):
    # Continuously ask the user for a valid number
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Please enter a number")


def show_menu():
    # Display calculator options
    print("\nCalculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


def calculate(choice, num1, num2):
    # Perform the selected operation
    if choice == "1":
        return add(num1, num2)
    if choice == "2":
        return subtract(num1, num2)
    if choice == "3":
        return multiply(num1, num2)
    if choice == "4":
        return divide(num1, num2)

    # Raise an error if the operation is invalid
    raise ValueError("Invalid operation")


def main():
    # Main program loop
    while True:
        show_menu()
        choice = input("Select an operation (1-5): ")

        # Exit the program
        if choice == "5":
            print("Goodbye!")
            break

        # Validate the user's choice
        if choice not in {"1", "2", "3", "4"}:
            print("Invalid choice. Try again.")
            continue

        # Get numbers from the user
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        try:
            result = calculate(choice, num1, num2)
            print(f"Result: {result}")
        except ValueError as error:
            print(error)


# Ensure the program runs only when executed directly
if __name__ == "__main__":
    main()
