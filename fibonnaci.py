#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--l", dest='limit', type=int, help='specify upper limit for Fibonacci', default=1)
parser.add_argument('--f', dest='file', type=str, help='specify file name', default='fibonacci_100.txt')
args = parser.parse_args()
upper_limit = args.limit
file_name = args.file

"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""

def generate_fibonacci(upper_limit):
	fibs = [0, 1]
	if upper_limit == 1: 
		return [0]
	elif upper_limit == 2:
		return fibs
	
	new_fib = fibs[-1] + fibs[-2]

	while new_fib < upper_limit:
		fibs.append(new_fib)
		new_fib = fibs[-1] + fibs[-2]

	return fibs

if __name__ == "__main__":
    # Do stuff here
	fibs = generate_fibonacci(upper_limit)
	with open(file_name, 'w') as f:
		try:
			f.write(str(fibs))
		except:
			"cannot write to file"