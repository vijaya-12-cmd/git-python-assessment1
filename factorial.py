def factorial(n):
    """
    Calculates the factorial of a non-negative integer using a loop.
    Factorial of 0 is 1. Factorial is not defined for negative numbers.
    """
    if n < 0:
        return "Factorial does not exist for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result = result * i
        return result

# Get user input
try:
    number = int(input("Enter a non-negative integer: "))
    print(f"The factorial of {number} is {factorial(number)}")
except ValueError:
    print("Invalid input. Please enter an integer.")