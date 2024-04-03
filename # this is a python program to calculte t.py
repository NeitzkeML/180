# this is a python program to calculte the fibonacci sequence. Create the python code below to do this
def fibonacci(n):
    sequence = [0, 1]  # Initialize the sequence with the first two numbers
    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]  # Calculate the next number
        sequence.append(next_number)  # Add the next number to the sequence
    return sequence

n = 10  # Change this value to generate the Fibonacci sequence up to a different number
fib_sequence = fibonacci(n)
print(fib_sequence)
