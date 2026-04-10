# CLI Calculator

A simple command-line calculator written in Python that performs basic arithmetic operations. This project is designed as a beginner-friendly application while following clean coding practices and a clear project structure.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Input validation for numbers
- Error handling for invalid operations
- Protection against division by zero
- Simple command-line interface (CLI)

## How It Works

The program displays a menu that allows the user to choose an arithmetic operation. After selecting an operation, the user is prompted to enter two numbers. The calculator then performs the selected operation and displays the result.

If the user enters invalid input (such as text instead of a number) or attempts to divide by zero, the program handles the error gracefully and asks the user to try again.

## Project Structure

```
cli-calculator/
│
├── main.py
├── README.md
├── .gitignore
└── requirements.txt
```

- **main.py** — contains the calculator logic and command-line interface
- **README.md** — project documentation
- **.gitignore** — prevents unnecessary files from being pushed to GitHub
- **requirements.txt** — lists project dependencies (empty for this project)

## Requirements

- Python 3.x

This project uses only the Python standard library and does not require external packages.

## How to Run

1. Clone the repository

```
git clone https://github.com/your-username/cli-calculator.git
```

2. Navigate to the project directory

```
cd cli-calculator
```

3. Run the program

```
python main.py
```

## Example Usage

```
Calculator
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit

Select an operation (1-5): 1
Enter first number: 5
Enter second number: 3
Result: 8
```

## Learning Goals

This project demonstrates fundamental Python concepts including:

- Functions
- Loops
- Conditional statements
- Error handling with try/except
- Input validation
- Clean code structure

## Future Improvements

Possible enhancements for future versions:

- Support floating-point numbers
- Add more mathematical operations
- Add unit tests
- Create a graphical interface
- Package the tool as an installable CLI utility
