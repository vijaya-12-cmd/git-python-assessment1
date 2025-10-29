# Get input from the user and convert it to an integer
number = int(input("Enter an integer: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")