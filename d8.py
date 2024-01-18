# Part 1

# Catching exceptions can help prevent immature program termination and be used to simplify error messages or give suggestions to end users

# In the code below, I attempt to read from a non existing file, which will cause a runtime error

# I used the try: and except: blocks to handle the errors and decide the outcome after encountering an error

try:
	# Attempting to read the file
	file = "hello.txt"
	# Read the file "file"
	with open(file, "r") as f:
		print(f.read())
except FileNotFoundError:
	# Handle File not found error 
	# Print user friendly error message
	print(f"No such file : {file}")
	# Provide solution to fix error
	print(f"Hint: Create a file named '{file}' in this directory before running the program.")

#  Output: 
# No such file : hello.txt
# Hint: Create a file named 'hello.txt' in this directory before running the program.

# Part 2

# The two main ways I would handle file errors in a production program would be to handle exceptions explicitly and logging friendly error messages. Exception handling would be done using the try:, except: blocks and logging would be done in the except: blocks. That way, errors are handled explicitly and suitable error messages are logged without immature program termination.
