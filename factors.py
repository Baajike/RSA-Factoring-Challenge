import sys
import time
from math import isqrt

def factorize(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return i, n // i
    return n, 1

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            numbers = [int(line.strip()) for line in file]
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except ValueError:
        print(f"Error: Invalid content in file '{input_file}'. Please ensure all lines are valid natural numbers.")
        sys.exit(1)

    for number in numbers:
        factors = factorize(number)
        print(f"{number}={factors[0]}*{factors[1]}")

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nExecution time: {elapsed_time:.3f} seconds")

