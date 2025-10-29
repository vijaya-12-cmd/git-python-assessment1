def generate_fibonacci_list(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]

    fib_list = [0, 1]
    while len(fib_list) < n:
        next_fib = fib_list[-1] + fib_list[-2]
        fib_list.append(next_fib)
    return fib_list
# Get user input
try:
    num_terms = int(input("Enter the number of Fibonacci terms to print: "))
    fib_numbers = generate_fibonacci_list(num_terms)
    print(" ".join(map(str, fib_numbers)))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    