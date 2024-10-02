#!/usr/bin/env python3
from fibonnaci import generate_fibonacci

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--l", dest='limit', type=int, help='specify upper limit for Fibonacci', default=1)
args = parser.parse_args()
upper_limit = args.limit

"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""

# You're on your own for this one. Good luck!

def is_prime(n):
    if (n < 2):
        return False
    for factor in range(2,n):
        if (n % factor == 0):
            return False
    return True


if __name__ == "__main__":
    # Do stuff here
	fibs = generate_fibonacci(upper_limit)
	for fib in reversed(fibs):
		if is_prime(fib):
			print(fib)
			break
	print("Done!")
	# 28657
	